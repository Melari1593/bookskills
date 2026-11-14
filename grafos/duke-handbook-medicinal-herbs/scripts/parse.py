"""Parse Duke, Handbook of Medicinal Herbs 2nd ed. (raw pdftotext) into structured JSON."""
import re, json, sys
from collections import Counter
raw = open(sys.argv[1], encoding='utf-8').read()
pages = raw.split('\f')
# printed page per pdf page
printed = {}
for i, p in enumerate(pages):
    m = re.search(r'(?m)^\s*(\d{1,3})\s*$\n?\s*Handbook of Medicinal Herbs|Handbook of Medicinal Herbs\s*\n?\s*(\d{1,3})\s*$', p)
    nums = re.findall(r'(?m)^(\d{1,3})$', p)
    printed[i] = int(nums[0]) if nums else None
# build line list with pdf page index
lines = []
for i, p in enumerate(pages):
    for ln in p.split('\n'):
        lines.append((i, ln.rstrip()))
# stop before Reference Abbreviations section (catalog only)
end = next(k for k, (i, l) in enumerate(lines) if l.strip() == 'Reference Abbreviations' and i > 700)
start = next(k for k, (i, l) in enumerate(lines) if l.startswith('ABSCESS ROOT'))
lines = lines[start:end]
HDR_START = re.compile(r"^[A-ZÀ-Ý][A-ZÀ-Ý0-9’'\-\.,&/ ]{2,}(?:(?: or | etc\.| and )[A-ZÀ-Ý0-9’'\-\.,&/ ]*)*\s\(")
HDR_END = re.compile(r"\)\s*(X|\+{1,3})(\s*\+)?\s*$")
NAME_LINE = re.compile(r"^[A-ZÀ-Ý][A-ZÀ-Ý0-9’'\-\.,&/ ]{2,}(?:(?: or | etc\.| and )[A-ZÀ-Ý0-9’'\-\.,&/ ]*)*(\s\(|$)")
SCORE_TAIL = re.compile(r"\)\s*\+?\s*(X{1,3}|\+{1,3}).*$")
def parse_header(joined):
    i = joined.find(' (')
    if i < 2: return None
    name = joined[:i].strip()
    if re.sub(r' or | etc\.| and ', ' ', name).upper() != re.sub(r' or | etc\.| and ', ' ', name): return None
    rest = joined[i + 1:]
    groups = []; pos = 0
    while pos < len(rest) and rest[pos] == '(':
        depth = 0
        for k2 in range(pos, len(rest)):
            if rest[k2] == '(': depth += 1
            elif rest[k2] == ')':
                depth -= 1
                if depth == 0: break
        else:
            return None
        groups.append(rest[pos + 1:k2]); pos = k2 + 1
        while pos < len(rest) and rest[pos] == ' ': pos += 1
    if not groups: return None
    tail = rest[pos:].strip()
    sci = next((g for g in groups if re.match(r"^[A-Z][a-z]+ (\(?[a-z×]|x )", g)), None)
    if not sci: return None
    quals = [g for g in groups if g is not sci]
    m = re.search(r"(X{1,3}|\+{1,3})", tail) or next((re.search(r"(X{1,3}|\+{1,3})", q) for q in quals if re.search(r"(X{1,3}|\+{1,3})", q)), None)
    if not m: return None
    first = m.group(1)
    safety = 'X' if first.startswith('X') else first
    return {'common': name, 'scientific': sci.strip(), 'qualifier': '; '.join(quals), 'safety': safety, 'safety_raw': (' '.join('(' + q + ')' for q in quals) + ' ' + tail).strip()}

SEC = re.compile(r"^(Activities|Indications|Dosages?|Contraindications, Interactions, and Side Effects|Contraindications, Indications, and Side Effects|Extracts|Synonyms?|Clinical|Synergy Quote|Translation)\b(?: \(([^)]*)\))?\s*—\s*(.*)$")
herbs = []
k = 0
cur = None; cursec = None
while k < len(lines):
    pi, l = lines[k]
    s = l.strip()
    hdr = None
    if NAME_LINE.match(s) and not SEC.match(s):
        joined = s; j = k
        while j < k + 3 and j + 1 < len(lines) and not SCORE_TAIL.search(joined):
            j += 1; joined += ' ' + lines[j][1].strip()
        hdr = parse_header(joined)
    if hdr:
        cur = dict(hdr, pdf_page=pi + 1, notes=[], sections={})
        herbs.append(cur); cursec = 'notes'; k = j + 1; continue
    if cur is None or not s or re.fullmatch(r'\d{1,3}|Handbook of Medicinal Herbs|[A-Z]', s) or s.startswith('1284_frame'):
        k += 1; continue
    if re.fullmatch(r'(\d{1,3}\s+)?Handbook of Medicinal Herbs(\s+\d{1,3})?', s):
        k += 1; continue
    m = SEC.match(s)
    if m:
        name = m.group(1)
        name = {'Dosage': 'Dosages', 'Synonym': 'Synonyms', 'Contraindications, Indications, and Side Effects': 'Contraindications, Interactions, and Side Effects'}.get(name, name)
        cursec = name
        cur['sections'].setdefault(name, '')
        cur['sections'][name] += (' ' if cur['sections'][name] else '') + m.group(3)
        cur.setdefault('sec_page', {}).setdefault(name, pi + 1)
    else:
        if cursec == 'notes':
            cur['notes'].append(s)
        else:
            t = cur['sections'][cursec]
            cur['sections'][cursec] = (t[:-1] + s) if t.endswith('-') else (t + ' ' + s)
    k += 1
# parse activity/indication items
ITEM = re.compile(r"([^;()]+?)\s*\((1|2|3|f)((?:;\s*[^;()]+)*)\)")
def items(txt):
    out = []
    for m in ITEM.finditer(txt or ''):
        name = m.group(1).strip(' ;.,')
        srcs = [x.strip() for x in m.group(3).split(';') if x.strip()]
        out.append({'name': name, 'score': m.group(2), 'sources': srcs})
    return out
for h in herbs:
    h['activities'] = items(h['sections'].get('Activities'))
    h['indications'] = items(h['sections'].get('Indications'))
    h['printed_page'] = printed.get(h['pdf_page'] - 1)
    h['notes'] = ' '.join(h['notes'])
json.dump({'pdf_pages': len(pages), 'printed_page_map': printed, 'herbs': herbs}, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
c = Counter(h['safety'] for h in herbs)
print('herbs', len(herbs), c)
print('with activities', sum(1 for h in herbs if h['activities']), 'with indications', sum(1 for h in herbs if h['indications']))
print('items', sum(len(h['activities'])+len(h['indications']) for h in herbs))
print(Counter(i['score'] for h in herbs for i in h['activities']+h['indications']))
