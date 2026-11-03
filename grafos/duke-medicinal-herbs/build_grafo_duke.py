import json,re,collections
E_=json.load(open('trabajo/ents.json'))
def clean(n):
    n=re.sub(r'Handbook of Medicinal Herbs\s+\d+','',n)
    n=re.sub(r'\s+\d+\s+Handbook of Medicinal Herbs','',n)
    n=re.sub(r'^\s*[A-Z]\s*\n','',n)
    n=re.sub(r'\s+',' ',n).strip()
    return n
ents=[]
seen=set()
for x in E_:
    x['act']=[(clean(a),c) for a,c in x['act']]; x['ind']=[(clean(a),c) for a,c in x['ind']]
    x['act']=[(a,c) for a,c in x['act'] if 2<len(a)<35]
    x['ind']=[(a,c) for a,c in x['ind'] if 2<len(a)<35]
    key=(x['common'],x['latin'])
    if key in seen: continue
    seen.add(key); ents.append(x)
print(len(ents))
G={ # chapter key: (title, block, activities, resumen)
 'inf':('Antiinflamatorio y analgésico','dolor',{'Antiinflammatory','Analgesic','Antiedemic','Antirheumatic','Anodyne','Antiarthritic','Antineuralgic','Antiarthritic'},'Hierbas con uso registrado contra la inflamación, el dolor y el reumatismo.'),
 'mic':('Antimicrobiano y antiséptico','infec',{'Antibacterial','Antiseptic','Fungicide','Antiviral','Antimicrobial','Bacteriostat','Antifungal','Virucide'},'Hierbas con actividad antibacteriana, antifúngica, antiviral o antiséptica.'),
 'par':('Antiparasitario e insecticida','infec',{'Vermifuge','Insecticide','Antimalarial','Pesticide','Amebicide','Anthelmintic','Taenicide','Larvicide','Pediculicide','Protisticide'},'Hierbas usadas contra lombrices, protozoos, malaria o insectos.'),
 'dig':('Digestivo','dig',{'Stomachic','Carminative','Laxative','Bitter','Digestive','Aperitif','Cholagogue','Antiemetic','Purgative'},'Hierbas para apetito, gases, estreñimiento y malestar gástrico.'),
 'hep':('Hepático y depurativo','dig',{'Hepatoprotective','Hepatotonic','Depurative','Alterative','Choleretic','Antihepatotoxic'},'Hierbas "depurativas" y de apoyo al hígado y la vesícula.'),
 'res':('Respiratorio','resp',{'Expectorant','Antitussive','Bronchodilator','Demulcent','Decongestant','Antiasthmatic'},'Hierbas para tos, bronquios, asma y catarro.'),
 'cardio':('Cardiovascular y metabólico','card',{'Hypotensive','Cardiotonic','Hypoglycemic','Antiaggregant','Hypocholesterolemic','Vasodilator','Antiarrhythmic','Antihyperlipidemic','Cardioprotective'},'Hierbas con efecto sobre presión, corazón, glucosa y lípidos.'),
 'sn':('Sistema nervioso','nerv',{'Sedative','Narcotic','Anxiolytic','Anticonvulsant','Antidepressant','Nervine','Hypnotic','Stimulant','CNS-Stimulant','Antispasmodic'},'Hierbas sedantes, estimulantes y antiespasmódicas.'),
 'gin':('Ginecológico y reproductivo','gin',{'Emmenagogue','Abortifacient','Aphrodisiac','Lactagogue','Estrogenic','Oxytocic','Uterotonic','Antispermatogenic','Contraceptive','Galactagogue','Uterocontractant','Uterosedative','Antifertility'},'Hierbas con uso menstrual, uterino, de lactancia o de fertilidad.'),
 'uri':('Urinario y diurético','gin',{'Diuretic','Lithontryptic','Antilithic'},'Hierbas que aumentan la diuresis o se usan en vías urinarias.'),
 'piel':('Piel, heridas y hemostasia','piel',{'Vulnerary','Emollient','Astringent','Hemostat','Rubefacient','Counterirritant','Styptic','Antipruritic','Cicatrizant'},'Hierbas para heridas, sangrado y afecciones de la piel.'),
 'onc':('Antitumoral e inmunomodulador','inm',{'Antitumor','Anticancer','Immunostimulant','Antioxidant','Antimutagenic','Cytotoxic','Cancer'},'Hierbas con actividad antitumoral, inmunoestimulante o antioxidante registrada.'),
 'feb':('Febrífugo y tónico general','inm',{'Antipyretic','Diaphoretic','Tonic','Adaptogen','Febrifuge','Refrigerant'},'Hierbas para fiebre, sudoración y fortalecimiento general.'),
 'tox':('Emético y tóxico','tox',{'Emetic','Poison','Toxic'},'Hierbas cuyo rasgo principal es provocar vómito o su toxicidad.'),
}
BL={'dolor':('Dolor e inflamación','#B0622A'),'infec':('Infecciones y parásitos','#2F4FA8'),'dig':('Digestivo e hígado','#6F7C24'),'resp':('Respiratorio','#16808A'),'card':('Cardio-metabólico','#A83A4F'),'nerv':('Sistema nervioso','#7A5BA6'),'gin':('Ginecológico y urinario','#C2549A'),'piel':('Piel y heridas','#8A6D3B'),'inm':('Inmunidad y tonificantes','#3F7F4F'),'tox':('Tóxicas','#5B6770')}
w=lambda c:2 if c=='1' or c.isdigit() else 1
chap=collections.defaultdict(list)
order=list(G)
for x in ents:
    sc=collections.Counter()
    for a,c in x['act']:
        for k,(t,b,acts,s) in G.items():
            if a in acts: sc[k]+=w(c)
    if not sc:
        # fallback by indications
        k='inf' if any(a in('Pain','Inflammation','Rheumatism') for a,_ in x['ind']) else 'feb'
    else:
        top=max(sc.values()); k=[o for o in order if sc.get(o)==top][0]
    chap[k].append(x)
# indication items
FEM=['Dysmenorrhea','Amenorrhea','Menorrhagia','Uterosis','Childbirth','Leukorrhea','Infertility','Menopause','PMS']
ci=collections.Counter(a for x in ents for a,_ in x['ind'])
top=[a for a,_ in ci.most_common(30)]
sel=list(dict.fromkeys(top+[f for f in FEM if ci.get(f)]))
ES={'Fever':'Fiebre','Cancer':'Cáncer','Pain':'Dolor','Inflammation':'Inflamación','Rheumatism':'Reumatismo','Dermatosis':'Dermatosis','Gastrosis':'Afecciones gástricas','Diarrhea':'Diarrea','Sore':'Llagas','Water Retention':'Retención de líquidos','Infection':'Infección','Cough':'Tos','Enterosis':'Afecciones intestinales','Wound':'Heridas','Hepatosis':'Afecciones hepáticas','Cramp':'Calambres','Constipation':'Estreñimiento','Bronchosis':'Afecciones bronquiales','Bacteria':'Bacterias','Cold':'Resfriado','Worm':'Lombrices','Dyspepsia':'Dispepsia','Asthma':'Asma','Bleeding':'Sangrado','Dysentery':'Disentería','Swelling':'Hinchazón','Headache':'Cefalea','Dysmenorrhea':'Dismenorrea','Arthrosis':'Artrosis','Nephrosis':'Afecciones renales','Amenorrhea':'Amenorrea','Menorrhagia':'Menorragia','Uterosis':'Afecciones uterinas','Childbirth':'Parto','Leukorrhea':'Leucorrea','Infertility':'Infertilidad','Menopause':'Menopausia','PMS':'Síndrome premenstrual','Tumor':'Tumores','Insomnia':'Insomnio','Catarrh':'Catarro','Ophthalmia':'Oftalmía','Hemorrhoid':'Hemorroides','Nervousness':'Nerviosismo','VD':'Enfermedad venérea'}
# section numbering
sec={}   # id -> (num, chapter idx)
chapters=[]
page_off=23
for ci_,k in enumerate(order,1):
    lst=sorted(chap[k],key=lambda x:x['common'])
    t,b,_,s=G[k]
    secs=[]
    for n,x in enumerate(lst,1):
        num=f'{ci_}.{n}'
        x['num']=num; x['ch']=ci_
        good=[a for a,c in x['act'] if w(c)==2][:4] or [a for a,_ in x['act']][:4]
        inds=[a for a,_ in x['ind']][:4]
        summ='Actividades mejor respaldadas: '+', '.join(good)+'.' if good else ''
        if inds: summ+=' Indicaciones registradas: '+', '.join(inds)+'.'
        if x['mark'] and x['mark'].startswith('X'): summ+=' Marcada como de uso no recomendado/tóxica en el libro.'
        secs.append({'num':num,'title':f"{x['common']} ({x['latin'].split(' ')[0]} {x['latin'].split(' ')[1] if len(x['latin'].split(' '))>1 else ''})".replace('  ',' ').strip(),'page':max(1,x['phys']-page_off),'summary':summ,'items':[]})
        x['sec']=secs[-1]
    chapters.append({'num':ci_,'title':t,'block':b,'summary':s+f' ({len(lst)} hierbas, agrupadas por su actividad predominante).','sections':secs})
# anchors
items={}
anchor={}
for a in sel:
    cand=[x for x in ents if any(n==a and w(c)==2 for n,c in x['ind'])]
    if not cand: continue
    best=max(cand,key=lambda x:sum(1 for _,c in x['ind'] if w(c)==2))
    key='i_'+re.sub(r'\W+','_',a.lower())
    anchor[a]=best
    items[key]={'title':ES.get(a,a),'summary':f'Indicación registrada en {ci[a]} hierbas del catálogo. Hierba con más respaldo experimental aquí: {best["common"].title()}.'}
    best['sec']['items'].append(key)
anchors_ids={x['num'] for x in anchor.values()}
req={}
for x in ents:
    if x['num'] in anchors_ids: continue
    c=[a for a,cc in x['ind'] if a in anchor and w(cc)==2 and anchor[a]['num']!=x['num']]
    c=sorted(c,key=lambda a:ci[a])[:2]
    tgt=list(dict.fromkeys(anchor[a]['num'] for a in c))
    if tgt: req[x['num']]=tgt
for c in chapters:
    for s in c['sections']:
        if not s['items']: s.pop('items')
        if not s['summary']: s.pop('summary')
g={'meta':{'title':'Handbook of Medicinal Herbs como grafo','subtitle':'James A. Duke, CRC Press, 2002 (vol. 1): hierbas agrupadas por actividad. Los enlaces unen hierbas que comparten una indicación con respaldo experimental; no son prerrequisitos de lectura.','language':'es','itemLabel':'Indicación ancla','itemLabelPlural':'Indicaciones ancla','chapterLabel':'Grupo','sectionLabel':'Hierba','searchHint':'Buscar: ginger, Dysmenorrhea, 3.12…'},
 'blocks':{k:{'name':v[0],'color':v[1]} for k,v in BL.items()},'chapters':chapters,'items':items,'requires':{'chapters':{},'sections':req,'items':{}}}
json.dump(g,open('grafo.json','w'),ensure_ascii=False,indent=1)
print(len(ents),len(items),len(req),[ (c['title'],len(c['sections'])) for c in chapters])
