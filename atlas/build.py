"""Genera atlas-meridianos.html a partir de la skill acupuntura-puntos.

Uso (desde la raíz del repo):  python3 atlas/build.py
"""
import json, math, re, os

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, '..', '.claude', 'skills', 'acupuntura-puntos', 'references')
OUT = os.path.join(HERE, 'atlas-meridianos.html')

MER = ['LU','LI','ST','SP','HT','SI','BL','KI','PC','TE','GB','LR','CV','GV']
ELEM = {'LU':'metal','LI':'metal','ST':'tierra','SP':'tierra','HT':'fuego','SI':'fuego',
        'PC':'fuego','TE':'fuego','BL':'agua','KI':'agua','GB':'madera','LR':'madera',
        'CV':'vaso','GV':'vaso'}
YIN = {'LU','SP','HT','KI','PC','LR','CV'}

# ---------------------------------------------------------------- fichas
def parse_meridian(code):
    txt = open(f'{REF}/meridianos/{code}.md', encoding='utf-8').read()
    title = txt.split('\n', 1)[0].lstrip('# ').strip()
    name = title.split('—', 1)[1].strip() if '—' in title else title
    tray = re.search(r'\*\*Trayecto:\*\*\s*(.+)', txt)
    pts = []
    for block in re.split(r'\n(?=### )', txt):
        if not block.startswith('### '):
            continue
        head, *rest = block.split('\n')
        parts = [p.strip() for p in head[4:].split('·')]
        pcode = parts[0]
        pin_han = parts[1] if len(parts) > 1 else ''
        trad = re.sub(r'"\s*/\s*"', ' / ', parts[2]).strip('"“” ') if len(parts) > 2 else ''
        m = re.match(r'(.+?)\s+([㐀-鿿（）()一-鿿\s]+)$', pin_han)
        pinyin, hanzi = (m.group(1), m.group(2).strip()) if m else (pin_han, '')
        f = {}
        for line in rest:
            mm = re.match(r'- \*\*(.+?):\*\*\s*(.*)', line)
            if mm:
                f[mm.group(1)] = mm.group(2).strip()
        pts.append(dict(code=pcode, mer=code, pinyin=pinyin, hanzi=hanzi, trad=trad,
                        ubic=f.get('Ubicación', ''), cat=f.get('Categorías', ''),
                        acc=f.get('Acciones', ''), ind=f.get('Indicaciones', ''),
                        ins=f.get('Inserción', ''), prec=f.get('Precauciones', '')))
    return dict(code=code, name=name, trayecto=tray.group(1).strip() if tray else ''), pts

meridians, points = [], []
for c in MER:
    m, p = parse_meridian(c)
    meridians.append(m); points += p

# ---------------------------------------------------------------- extras
cat = open(f'{REF}/categorias.md', encoding='utf-8').read()
sec9 = cat.split('## 9.', 1)[1].split('## 10.', 1)[0]
extras = []
for line in sec9.split('\n'):
    if not line.startswith('| ') or line.startswith('| Código'):
        continue
    cols = [c.strip() for c in line.strip('|').split('|')]
    if len(cols) < 5:
        continue
    code, name, ubic, ind, ins = cols[:5]
    if 'Yintang' in name:
        continue  # ya está como GV29
    nm = re.sub(r'\s*\(.*?\)', '', name).split('/')[0].strip()
    extras.append(dict(code=('EX:' + nm), excode=code if code != '—' else '', mer='EX',
                       pinyin=name, hanzi='', trad='', ubic=ubic, cat='Punto extra' + (f' ({code})' if code != '—' else ''),
                       acc='', ind=ind, ins=ins, prec=''))

# ---------------------------------------------------------------- coordenadas
# Vistas: 'ant' y 'post' en viewBox 300x650 (cuerpo, dx desde la línea media x=150,
# se dibuja a ambos lados); 'lat' en viewBox 300x300 (cabeza de perfil, x absoluto).
def arm(y, s):
    if y <= 250:
        x = 77 + (y - 165) / 85 * 9; hw = 11
    else:
        x = 86 + (y - 250) / 90 * 12; hw = 12 - (y - 250) / 90 * 3.5
    return (round(x + s * hw, 1), round(y, 1))

W = lambda c: 340 - c * 7.5          # c cun por encima de la muñeca
U = lambda c: 165 + c * 85 / 9       # c cun por debajo del pliegue axilar
UE = lambda c: 250 - c * 85 / 9      # c cun por encima del codo
FE = lambda c: 250 + c * 7.5         # c cun por debajo del codo
HA = lambda c: 42 - 22 * math.sin(min(c, 5) / 5 * math.pi / 2)   # cabeza anterior
HP = lambda c: 98 - c * 11           # cabeza posterior (c cun sobre línea posterior del pelo)
T = lambda n: 126 + 11 * n + 5.5     # borde inferior de la apófisis de Tn (n=0 → C7)
L = lambda n: T(12 + n)
S = lambda n: 315 + 9 * n            # agujeros sacros
AB = lambda c: 300 - c * 9           # c cun por encima del ombligo (negativo = por debajo)
ICS = lambda n: 132 + 13 * n         # espacio intercostal n
LEG = lambda c: 480 + c * 7.5        # c cun por debajo de ST35/pliegue poplíteo
MAL = lambda c: 598 - c * 7.5        # c cun por encima del maléolo
PT = lambda c: 372 + c * 106 / 14    # c cun por debajo del pliegue glúteo

P = {}
def ant(code, dx, y): P[code] = ('ant', round(dx, 1), round(y, 1))
def post(code, dx, y): P[code] = ('post', round(dx, 1), round(y, 1))
def lat(code, x, y): P[code] = ('lat', x, y)
def armA(code, y, s):
    x, yy = arm(y, s); ant(code, x, yy)
def armP(code, y, s):
    x, yy = arm(y, s); post(code, x, yy)

# LU
ant('LU1', 54, ICS(1)); ant('LU2', 54, 140)
armA('LU3', U(3), .65); armA('LU4', U(4), .65); armA('LU5', 250, .35)
armA('LU6', W(5), .7); armA('LU7', W(1.5), .95); armA('LU8', W(1), .8); armA('LU9', W(0), .75)
ant('LU10', 107, 354); ant('LU11', 117, 374)
# LI (dorso → vista posterior; cuello y cara → anterior)
post('LI1', 105.5, 397); post('LI2', 105.5, 372); post('LI3', 105.5, 364); post('LI4', 104, 354); post('LI5', 106.5, 340)
armP('LI6', W(3), .9); armP('LI7', W(5), .9)
armP('LI8', FE(4), .95); armP('LI9', FE(3), .97); armP('LI10', FE(2), 1.0); armP('LI11', 250, 1.0)
armP('LI12', UE(1), 1.1); armP('LI13', UE(3), .95); armP('LI14', UE(7), .95)
post('LI15', 72, 140); post('LI16', 58, 134)
ant('LI17', 15, 119); ant('LI18', 15, 110); ant('LI19', 4, 83); ant('LI20', 8, 78)
# ST
ant('ST1', 11, 67.5); ant('ST2', 11, 71.5); ant('ST3', 11, 77); ant('ST4', 8.5, 88.5)
lat('ST5', 126, 206); lat('ST6', 140, 195); lat('ST7', 132, 150)
ant('ST8', 23, HA(.5))
ant('ST9', 10, 110); ant('ST10', 10, 118); ant('ST11', 6, 126); ant('ST12', 36, 131)
for i, n in zip(range(13, 19), [0, 1, 2, 3, 4, 5]):
    ant(f'ST{i}', 36, 138 if i == 13 else ICS(n))
for i, c in zip(range(19, 31), [6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]):
    ant(f'ST{i}', 18, AB(c))
ant('ST31', 41, 356); ant('ST32', 38, 415); ant('ST33', 37, 432.6); ant('ST34', 37, 438.4)
ant('ST35', 34, 480)
for i, c in [(36, 3), (37, 6), (38, 8), (39, 9)]:
    ant(f'ST{i}', 34, LEG(c))
ant('ST40', 38.5, LEG(8)); ant('ST41', 28, 600); ant('ST42', 28, 609); ant('ST43', 31, 618)
ant('ST44', 31, 626); ant('ST45', 32, 633)
# SP
ant('SP1', 17, 633); ant('SP2', 15.5, 627); ant('SP3', 14.5, 621); ant('SP4', 14.5, 614); ant('SP5', 16.5, 604)
ant('SP6', 18.5, MAL(3)); ant('SP7', 18.5, MAL(6)); ant('SP8', 18, LEG(4) + 7); ant('SP9', 17, 487)
ant('SP10', 18, 438.4); ant('SP11', 18.5, 392); ant('SP12', 31.5, 350)
ant('SP13', 36, AB(-4.3)); ant('SP14', 36, AB(-1.3)); ant('SP15', 36, AB(0)); ant('SP16', 36, AB(3))
for i, n in zip(range(17, 21), [5, 4, 3, 2]):
    ant(f'SP{i}', 54, ICS(n))
ant('SP21', 63, ICS(6))
# HT
ant('HT1', 66, 160); armA('HT2', UE(3), -.75); armA('HT3', 250, -.95)
armA('HT4', W(1.5), -.8); armA('HT5', W(1), -.8); armA('HT6', W(.5), -.8); armA('HT7', W(0), -.82)
ant('HT8', 91, 360); ant('HT9', 90, 391)
# SI
post('SI1', 87.5, 391); post('SI2', 87, 372); post('SI3', 86.5, 364); post('SI4', 87, 348); post('SI5', 88.5, 341)
armP('SI6', W(1), -.95); armP('SI7', W(5), -1.0); armP('SI8', 250, -.95)
post('SI9', 64, 172); post('SI10', 62, 158); post('SI11', 45, 182); post('SI12', 45, 150)
post('SI13', 31, 155); post('SI14', 27, T(1)); post('SI15', 18, T(0))
lat('SI16', 176, 238); lat('SI17', 160, 214); lat('SI18', 108, 150); lat('SI19', 145, 141)
# BL
ant('BL1', 4.5, 63); ant('BL2', 5.5, 57); ant('BL3', 5.5, HA(.5)); ant('BL4', 8, HA(.5))
ant('BL5', 8, HA(1)); ant('BL6', 8, HA(2.5)); ant('BL7', 8, HA(4))
post('BL8', 8, HP(5.5)); post('BL9', 8, HP(2.5)); post('BL10', 11, 103)
for i, n in zip(range(11, 22), [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]):
    post(f'BL{i}', 13.5, T(n))
for i, n in zip(range(22, 27), [1, 2, 3, 4, 5]):
    post(f'BL{i}', 13.5, L(n))
for i, n in zip(range(27, 31), [1, 2, 3, 4]):
    post(f'BL{i}', 13.5, S(n))
for i, n in zip(range(31, 35), [1, 2, 3, 4]):
    post(f'BL{i}', 6, S(n))
post('BL35', 4.5, 364); post('BL36', 28, 372); post('BL37', 28, PT(6)); post('BL38', 36, 470)
post('BL39', 37, 478); post('BL40', 28, 478)
for i, n in zip(range(41, 51), [2, 3, 4, 5, 6, 7, 9, 10, 11, 12]):
    post(f'BL{i}', 27, T(n))
post('BL51', 27, L(1)); post('BL52', 27, L(2)); post('BL53', 27, S(2)); post('BL54', 27, S(4))
post('BL55', 28, 493); post('BL56', 28, 515.5); post('BL57', 28, 538); post('BL58', 33, MAL(7))
post('BL59', 35, MAL(3)); post('BL60', 36.5, 598); post('BL61', 37, 610); post('BL62', 39, 605)
post('BL63', 41, 612); post('BL64', 42, 618); post('BL65', 43, 624); post('BL66', 43.5, 629); post('BL67', 44, 634)
# KI
post('KI1', 24, 630); ant('KI2', 12.5, 612); ant('KI3', 13.5, 599); ant('KI4', 13, 603.5)
ant('KI5', 13, 607.5); ant('KI6', 16.5, 606.5); ant('KI7', 13.5, MAL(2)); ant('KI8', 17, MAL(2))
ant('KI9', 14, MAL(5)); post('KI10', 19, 478)
for i, c in zip(range(11, 22), [-5, -4, -3, -2, -1, 0, 2, 3, 4, 5, 6]):
    ant(f'KI{i}', 4.5, AB(c))
for i, n in zip(range(22, 27), [5, 4, 3, 2, 1]):
    ant(f'KI{i}', 18, ICS(n))
ant('KI27', 18, 138)
# PC
ant('PC1', 45, ICS(4)); armA('PC2', U(2), .05); armA('PC3', 250, -.15)
armA('PC4', W(5), 0); armA('PC5', W(3), 0); armA('PC6', W(2), 0); armA('PC7', W(0), 0)
ant('PC8', 101, 360); ant('PC9', 99, 402.5)
# TE
post('TE1', 93, 398); post('TE2', 91.5, 370); post('TE3', 91.5, 362); post('TE4', 95.5, 340)
armP('TE5', W(2), 0); armP('TE6', W(3), 0); armP('TE7', W(3), -.35); armP('TE8', W(4), 0)
armP('TE9', FE(5), 0); armP('TE10', UE(1), -.25); armP('TE11', UE(2), -.2); armP('TE12', UE(5), -.1)
armP('TE13', 170, .15); post('TE14', 68, 143); post('TE15', 32, 147)
lat('TE16', 182, 212); lat('TE17', 170, 176); lat('TE18', 181, 156); lat('TE19', 178, 130)
lat('TE20', 160, 104); lat('TE21', 144, 131); lat('TE22', 136, 121); lat('TE23', 108, 104)
# GB
lat('GB1', 106, 121); lat('GB2', 145, 153); lat('GB3', 132, 133); lat('GB4', 120, 80)
lat('GB5', 125, 90); lat('GB6', 130, 100); lat('GB7', 139, 110); lat('GB8', 160, 88)
lat('GB9', 176, 86); lat('GB10', 190, 108); lat('GB11', 193, 140); lat('GB12', 194, 176)
ant('GB13', 18, HA(.5)); ant('GB14', 11, 50); ant('GB15', 11, HA(.5)); ant('GB16', 11, HA(1.5))
ant('GB17', 11, HA(2.5)); ant('GB18', 11, HA(4))
post('GB19', 17, 72); post('GB20', 17, 93); post('GB21', 35, 132)
ant('GB22', 62, ICS(4)); ant('GB23', 53, ICS(4)); ant('GB24', 36, ICS(7)); ant('GB25', 62, 286)
ant('GB26', 58, 300); ant('GB27', 40, AB(-3)); ant('GB28', 38, AB(-3.6)); ant('GB29', 48, 336)
post('GB30', 40, 345); ant('GB31', 50, 410); ant('GB32', 49, 425); ant('GB33', 44, 466)
ant('GB34', 40.5, 490); ant('GB35', 42, MAL(7)); ant('GB36', 39, MAL(7)); ant('GB37', 39, MAL(5))
ant('GB38', 39, MAL(4)); ant('GB39', 39, MAL(3)); ant('GB40', 38, 606); ant('GB41', 38, 616)
ant('GB42', 38.5, 621); ant('GB43', 37, 627); ant('GB44', 37.5, 633)
# LR
ant('LR1', 20, 633); ant('LR2', 22, 626); ant('LR3', 23.5, 617); ant('LR4', 21.5, 601.5)
ant('LR5', 21, MAL(5)); ant('LR6', 21, MAL(7)); ant('LR7', 13, 488); post('LR8', 15.5, 476)
ant('LR9', 16, 427); ant('LR10', 23.5, 363); ant('LR11', 22, 357); ant('LR12', 22.5, 345)
ant('LR13', 58, 275); ant('LR14', 36, ICS(6))
# CV
ant('CV1', 0, 358); ant('CV2', 0, AB(-5))
for i, c in zip(range(3, 16), [-4, -3, -2, -1.5, -1, 0, 1, 2, 3, 4, 5, 6, 7]):
    ant(f'CV{i}', 0, AB(c))
ant('CV16', 0, 228)
for i, n in zip(range(17, 21), [4, 3, 2, 1]):
    ant(f'CV{i}', 0, ICS(n))
ant('CV21', 0, 137); ant('CV22', 0, 127.5); ant('CV23', 0, 106); ant('CV24', 0, 94)
# GV
post('GV1', 0, 369); post('GV2', 0, 358)
for i, lv in [(3, L(4)), (4, L(2)), (5, L(1)), (6, T(11)), (7, T(10)), (8, T(9)), (9, T(7)),
              (10, T(6)), (11, T(5)), (12, T(3)), (13, T(1)), (14, T(0))]:
    post(f'GV{i}', 0, lv)
for i, c in [(15, .5), (16, 1), (17, 2.5), (18, 4), (19, 5.5), (20, 7)]:
    post(f'GV{i}', 0, HP(c))
ant('GV21', 0, HA(3.5)); ant('GV22', 0, HA(2)); ant('GV23', 0, HA(1)); ant('GV24', 0, HA(.5))
ant('GV25', 0, 78.5); ant('GV26', 0, 83); ant('GV27', 0, 86); ant('GV28', 0, 87.8); ant('GV29', 0, 57)

EXC = {
    'Sishencong': ('post', 7, 26), 'Yuyao': ('ant', 11, 56), 'Taiyang': ('lat', 114, 114),
    'Erjian': ('lat', 160, 113), 'Qiuhou': ('ant', 15.5, 68), 'Shangyingxiang': ('ant', 6, 73),
    'Haiquan': None, 'Jinjin': None, 'Yiming': ('lat', 186, 174), 'Jingbailao': ('post', 8, 112),
    'Anmian': ('lat', 200, 166), 'Qianzheng': ('lat', 146, 172), 'Zigong': ('ant', 27, AB(-4)),
    'Dingchuan': ('post', 4.5, T(0)), 'Huatuojiaji': ('post', 4.5, T(6)),
    'Weiwanxiashu': ('post', 13.5, T(8)), 'Pigen': ('post', 31.5, L(1)), 'Yaoyan': ('post', 31.5, L(4)),
    'Shiqizhui': ('post', 0, L(5)), 'Yaoqi': ('post', 0, 352), 'Erbai': ('ant',) + arm(W(4), .25),
    'Yaotongdian': ('post', 101, 356), 'Wailaogong': ('post', 101, 364.5), 'Baxie': ('post', 97, 373),
    'Sifeng': ('ant', 99.5, 386), 'Shixuan': ('ant', 99, 406), 'Jianqian': ('ant', 64, 158),
    'Heding': ('ant', 28, 447), 'Baichongwo': ('ant', 18.5, 426), 'Neixiyan': ('ant', 22, 480),
    'Xiyan': None, 'Dannang': ('ant', 41.5, 505), 'Lanwei': ('ant', 34, 517),
    'Bafeng': ('ant', 26, 629), 'Duyin': ('post', 31, 624),
}
kept = []
for e in extras:
    nm = e['code'][3:]
    key = next((k for k in EXC if nm.startswith(k)), None)
    if key and EXC[key]:
        v = EXC[key]; P[e['code']] = (v[0], round(v[1], 1), round(v[2], 1))
        kept.append(e)
extras = kept

allpts = points + extras
missing = [p['code'] for p in allpts if p['code'] not in P]
assert not missing, missing
for p in allpts:
    v, x, y = P[p['code']]
    p.update(view=v, x=x, y=y)

# ---------------------------------------------------------------- índice de síntomas
idx = open(f'{REF}/indice-sintomas.md', encoding='utf-8').read()
EXMAP = {'EX-HN3': 'GV29'}
for e in extras:
    if e['excode']:
        for c in re.split(r'\s*/\s*', e['excode']):
            EXMAP[c] = e['code']
names = {e['code'][3:]: e['code'] for e in extras}
names.update({'Yintang': 'GV29', 'Bitong': 'EX:Shangyingxiang', 'Luozhen': 'EX:Wailaogong',
              'Xiyan': 'EX:Neixiyan', 'Huatuojiaji': 'EX:Huatuojiaji', 'Jianneiling': 'EX:Jianqian'})
CODE_RE = re.compile(r'\b(?:LU|LI|ST|SP|HT|SI|BL|KI|PC|TE|GB|LR|CV|GV)\d{1,2}\b|EX-[A-Z]{2,3}\d+|' +
                     '|'.join(sorted(map(re.escape, names), key=len, reverse=True)))
valid = {p['code'] for p in allpts}

DESC_RE = re.compile(r'\((?:[^()]*\b(?:entre|punto extra|lateral a|hacia|por debajo|por encima)\b[^()]*)\)')
def codes_in(text):
    text = DESC_RE.sub('', text)
    out = []
    for m in CODE_RE.finditer(text):
        t = m.group(0)
        c = EXMAP.get(t) or names.get(t) or t
        if c in valid and c not in out:
            out.append(c)
    return out

systems, symptoms = [], []
for sec in re.split(r'\n(?=## )', idx):
    if not sec.startswith('## ') or 'Contenido' in sec[:20] or 'Principios' in sec[:40]:
        continue
    sysname = re.sub(r'^## \d+\.\s*', '', sec.split('\n', 1)[0]).strip()
    systems.append(sysname)
    for ent in re.split(r'\n(?=### )', sec)[1:]:
        lines = ent.strip().split('\n')
        name = lines[0][4:].strip()
        syn = ''
        body = []
        for l in lines[1:]:
            if l.startswith('*Sinónimos'):
                syn = l.strip('* ').replace('Sinónimos:', '').strip()
            elif l.strip():
                body.append(l.rstrip())
        principal = []
        for l in body:
            if l.startswith('- **Principales'):
                principal = codes_in(l)
        symptoms.append(dict(name=name, system=sysname, syn=syn, body=body,
                             principal=principal, all=codes_in('\n'.join(body))))

data = dict(meridians=meridians, points=allpts, systems=systems, symptoms=symptoms,
            elem=ELEM, yin=sorted(YIN))
tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
open(OUT, 'w', encoding='utf-8').write(tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False, separators=(',', ':'))))
print(len(points), 'puntos,', len(extras), 'extras,', len(symptoms), 'síntomas,',
      os.path.getsize(OUT) // 1024, 'KB')
