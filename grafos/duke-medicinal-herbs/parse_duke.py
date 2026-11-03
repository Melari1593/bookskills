import re, json
t=open('trabajo/texto.txt').read()
pages=t.split('\x0c')
# flat lines with page
L=[]
for pi,pg in enumerate(pages):
    for l in pg.split('\n'): L.append((pi+1,l))
starts=[]
for i,(p,l) in enumerate(L):
    m=re.match(r'^Activities \((.+?)\) — ',l)
    if m:
        # walk back to header
        j=i-1
        while j>0 and (not L[j][1].strip() or re.match(r'^(Synonym|Synonyms|Other|Variet|Syn)',L[j][1].strip()) or L[j][1].startswith((' ','\t'))==False and not re.search(r'\(.*\)',L[j][1])): j-=1
        starts.append((i,j))
print(len(starts))
for i,j in starts[:8]+starts[300:306]: print(L[j][0],repr(L[j][1][:90]))

# build entries
ents=[]
for k,(i,j) in enumerate(starts):
    end=starts[k+1][1] if k+1<len(starts) else len(L)
    hl=L[j][1].strip()
    # header may be continuation line (name on previous line): if starts with '(' take previous
    if hl.startswith('('):
        hl=L[j-1][1].strip()+' '+hl
    m=re.match(r'^(.+?) \((.+)\)\s*(.*)$',hl)
    if not m: 
        print('SKIP',repr(hl)); continue
    seg=[x[1] for x in L[i:end]]
    txt='\n'.join(seg)
    txt=re.sub(r'-\n','',txt)
    txt=re.sub(r'\n(?![A-Z][a-z, ]+\(| ?\n)',' ',txt)
    def field(name):
        mm=re.search(r'^'+name+r' \(.*?\) — (.*?)(?=^(?:Activities|Indications|Dosages|Contraindications|Synonym|Extracts)[ ,\w]*\(|\Z)',txt,re.M|re.S)
        return mm.group(1).strip() if mm else ''
    def parse_list(s):
        out=[]
        for part in re.split(r';\s+(?=[A-Z])|\.\s*$',s):
            pass
        for mm in re.finditer(r'([A-Z][^;()]*?(?:, [a-z]+)?) \((1|2|f|[0-9]+)(?:;[^)]*)\)',s):
            out.append((mm.group(1).strip(),mm.group(2)))
        return out
    ents.append({'common':m.group(1).strip().title(),'latin':m.group(2).strip(),'mark':m.group(3).strip(),
      'phys':L[j][0],'act':parse_list(field('Activities')),'ind':parse_list(field('Indications')),
      'dose':field('Dosages')[:200]})
print(len(ents))
import collections
ca=collections.Counter(a for e in ents for a,_ in e['act'])
ci=collections.Counter(a for e in ents for a,_ in e['ind'])
print(ca.most_common(60)); print(ci.most_common(60))
print(sum(1 for e in ents if not e['act']), sum(1 for e in ents if not e['ind']))
json.dump(ents,open('trabajo/ents.json','w'),ensure_ascii=False)
