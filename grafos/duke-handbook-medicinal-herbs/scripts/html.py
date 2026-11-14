"""Build the self-contained interactive HTML of the Duke graph.
Usage: python3 scripts/html.py out/compact.json out/duke-grafo.html
Embeds compact.json and the verification badges (VERIF below, summary of out/VERIFICACION.md)."""
import json, sys

data = json.load(open(sys.argv[1], encoding='utf-8'))

# Verification badges (source: out/VERIFICACION.md, 2026-11-14). Keys = Duke common name.
V = {
 'BILBERRY': {'eff': {'Constipation': 'sin', 'Diarrhea': 'sin'}},
 'FEVERFEW': {'eff': {'Migraine': 'mat'}, 'seg': 'Retirada: cefalea de rebote; suspender 2 semanas antes de cirugía (EMA).'},
 'GARLIC': {'eff': {'High Cholesterol': 'mat', 'Hyperlipidemia': 'mat', 'High Triglyceride': 'mat', 'Atherosclerosis': 'mat',
                    'Cardiopathy': 'sin', 'Antiaggregant': 'inc', 'Fibrinolytic': 'inc', 'Antiseptic': 'sin'},
            'seg': 'Sangrado: suspender 7 días antes de cirugía; baja saquinavir (EMA/HMPC/7685/2013).'},
 'GINGER': {'eff': {'Vomiting': 'mat', 'Antiemetic': 'mat'}, 'seg': 'Más sangrado autorreferido con warfarina (observacional); la EMA prefiere evitarlo en embarazo.'},
 'MUGWORT': {'eff': {'Breech Birth': 'mat'}, 'nota': 'La evidencia es moxibustión en BL67, no ingestión.'},
 'SAW PALMETTO': {'eff': {'BPH': 'con'}},
 'VALERIAN': {'eff': {'Insomnia': 'con', 'Hypnotic': 'con', 'Sedative': 'inc', 'Nervousness': 'inc', 'Nervous Tension': 'inc'}},
 'WATERCRESS': {'eff': {'Scurvy': 'sin'}},
 'WITCH HAZEL': {'eff': {'Bleeding': 'sin', 'Antihemorrhagic': 'sin'}},
 'KAVA': {'seg': 'Hepatotoxicidad; extractos prohibidos en Alemania en 2002.'},
 'ST. JOHN’S-WORT': {'seg': 'Induce CYP3A4 y P-gp: baja anticonceptivos, ciclosporina, tacrolimus, warfarina, antirretrovirales. Riesgo serotoninérgico con ISRS. Duke no lo menciona.'},
 'FO-TI': {'seg': 'Causa principal de lesión hepática por hierbas en series publicadas.'},
 'TURMERIC': {'seg': 'Hepatitis con suplementos concentrados (sobre todo con piperina); HLA-B*35:01.'},
 'GREEN or BLACK TEA': {'seg': 'Extractos concentrados (EGCG ≥ 800 mg/día): lesión hepática (EFSA 2018). La infusión no tiene esa alerta.'},
 'CASSIA': {'seg': 'Cumarina hasta 1 %: IDT 0,1 mg/kg/día; un adulto de 60 kg la alcanza con ~2 g/día. Usa canela de Ceilán.'},
 'LICORICE': {'seg': 'Pseudohiperaldosteronismo: hipopotasemia e hipertensión.'},
 'STAR ANISE': {'seg': 'Adulteración con anís japonés neurotóxico. No lo des a lactantes.'},
 'TANSY': {'seg': 'Tuyona neurotóxica. El propio texto dice que el té ha sido fatal: la calificación ++ es incoherente.'},
 'SKULLCAP': {'seg': 'Lesión hepática, a menudo por adulteración con germandrina.'},
 'BAICAL SKULLCAP': {'seg': 'Riesgo hepático (adulteración); posible suma con warfarina.'},
 'SAGE': {'seg': 'El aceite esencial (tuyona) causó convulsiones en niños. La EMA la limita a 1 semana.'},
 'GINSENG, ORIENTAL GINSENG': {'seg': 'Interacción con warfarina.'},
 'FENNEL': {'seg': 'Estragol: la EMA no lo recomienda en menores de 4 años, embarazo ni lactancia.'},
 'NONI, INDIAN MULBERRY': {'seg': 'Casos de hepatitis publicados (no verificados en esta sesión).'},
 'COMFREY': {'seg': 'Alcaloides pirrolizidínicos: nunca por vía oral (EMA).'},
 'ROSELLE': {'skill': 'Jamaica: PAS −7,10 mmHg (metaanálisis). Duke la puntúa 1: subestima.'},
 'CACAO': {'skill': 'Cacao rico en flavanoles: PAS −1,76 mmHg (Cochrane). Duke: f.'},
 'POMEGRANATE': {'skill': 'Jugo: PAS −4,96 mmHg. Duke no lista la presión arterial.'},
 'OATS': {'skill': 'Betaglucano: LDL −0,19 mmol/L. Coincide con Duke (2).'},
 'CRANBERRY': {'skill': 'ITU recurrente: RR 0,74 (Cochrane). Coincide con Duke (2).'},
 'PSYLLIUM, BLONDE ISPAGHULA': {'skill': 'Estreñimiento: RR 1,48. Coincide con Duke (2).'},
 'CHAMOMILE': {'skill': 'Sueño posparto: mejora a 2 semanas, certeza baja.'},
 'LEMONBALM': {'skill': 'Té casero: sin evidencia suficiente. Duke sobrestima (Insomnia 2).'},
 'LEMONGRASS': {'skill': 'ECA doble ciego: sin efecto en sueño ni ansiedad. Duke: 1.'},
 'ECHINACEA, PURPLE CONEFLOWER': {'skill': 'Cochrane: sin beneficio en el tratamiento del resfriado. Duke sobrestima (Cold 2).'},
 'PEPPERMINT': {'skill': 'SII: solo cápsulas entéricas de aceite; no aplica al té.'},
 'NETTLE': {'skill': 'EMA: hoja 8–12 g/día, máximo 4 semanas.'},
}
for k in ('GREEN or BLACK TEA',): V[k]['skill'] = 'Té verde: LDL −0,64 mmol/L; PAS −3,18 mmHg. Duke: 1 y f.'

html = r'''<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Grafo de Duke</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<style>
:root{--bg:#f7f6f2;--panel:#fff;--ink:#1d2321;--mute:#5f6a66;--line:#dfe3df;--acc:#2f6f4f;--acc2:#a4532b;
--sx:#b3261e;--s1:#c77700;--s2:#3f7d5a;--s3:#1f5f8b;--act:#7a5ea8;--ind:#2f6f4f;--chip:#eef1ec}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#141816;--panel:#1c2220;--ink:#e6ebe8;--mute:#9aa6a1;--line:#2c3532;--acc:#7cc39b;--acc2:#e09a72;--chip:#232b28;--act:#b39ce0;--ind:#7cc39b}}
:root[data-theme="dark"]{--bg:#141816;--panel:#1c2220;--ink:#e6ebe8;--mute:#9aa6a1;--line:#2c3532;--acc:#7cc39b;--acc2:#e09a72;--chip:#232b28;--act:#b39ce0;--ind:#7cc39b}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 system-ui,-apple-system,Segoe UI,sans-serif}
header{padding:16px;border-bottom:1px solid var(--line);display:flex;flex-wrap:wrap;gap:8px 20px;align-items:baseline}
h1{font-size:19px;margin:0}header .m{color:var(--mute);font-size:13px}
a{color:var(--acc)}
.wrap{display:grid;grid-template-columns:340px 1fr;min-height:calc(100vh - 60px)}
@media(max-width:820px){.wrap{grid-template-columns:1fr}}
aside{border-right:1px solid var(--line);padding:16px;display:flex;flex-direction:column;gap:10px;min-width:0}
input,select{width:100%;padding:9px 10px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--ink);font:inherit}
.row{display:flex;gap:6px;flex-wrap:wrap}.chip{border:1px solid var(--line);background:var(--chip);color:var(--ink);border-radius:999px;padding:4px 10px;font-size:13px;cursor:pointer}
.chip[aria-pressed="true"]{background:var(--acc);color:var(--panel);border-color:var(--acc)}
#list{overflow:auto;flex:1;min-height:200px;max-height:70vh;border:1px solid var(--line);border-radius:8px;background:var(--panel)}
#list div{padding:7px 10px;border-bottom:1px solid var(--line);cursor:pointer}#list div:hover,#list div.on{background:var(--chip)}
#list small{color:var(--mute)}
main{padding:16px;min-width:0}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px;margin-bottom:14px}
.b{display:inline-block;border-radius:6px;padding:1px 7px;font-size:12px;font-weight:600;color:#fff;margin-right:4px}
.zX{background:var(--sx)}.z1{background:var(--s1)}.z2{background:var(--s2)}.z3{background:var(--s3)}
.v{display:inline-block;border-radius:6px;padding:1px 6px;font-size:11px;font-weight:600;border:1px solid}
.vmat{color:var(--s2);border-color:var(--s2)}.vinc{color:var(--s1);border-color:var(--s1)}.vsin{color:var(--mute);border-color:var(--mute)}.vcon{color:var(--sx);border-color:var(--sx)}
.alert{border-left:4px solid var(--sx);padding:8px 12px;background:var(--chip);border-radius:6px;margin:8px 0}
.skill{border-left:4px solid var(--acc);padding:8px 12px;background:var(--chip);border-radius:6px;margin:8px 0}
details{margin-top:8px}summary{cursor:pointer;font-weight:600}
.txt{white-space:pre-wrap;color:var(--ink);font-size:14px;margin:6px 0 0}
.items span{display:inline-block;margin:2px 4px 2px 0;padding:1px 7px;border-radius:6px;background:var(--chip);font-size:13px;cursor:pointer}
.items span.s3{outline:2px solid var(--s3)}
svg{width:100%;height:420px;background:var(--panel);border:1px solid var(--line);border-radius:12px}
.lg{font-size:12px;color:var(--mute)}
table{border-collapse:collapse;width:100%;font-size:14px}td,th{border-bottom:1px solid var(--line);padding:5px 6px;text-align:left}
.warn{font-size:13px;color:var(--mute)}
</style></head><body>
<header><h1>Handbook of Medicinal Herbs — grafo</h1><span class="m" id="stats"></span>
<span class="m">Duke et al., 2.ª ed., CRC 2002 · <a href="GRAPH_REPORT.md">Reporte</a> · <a href="VERIFICACION.md">Verificación 2026</a></span></header>
<div class="wrap"><aside>
<div class="row"><button class="chip" id="mH" aria-pressed="true">Hierbas</button><button class="chip" id="mI" aria-pressed="false">Indicaciones → hierbas</button></div>
<input id="q" placeholder="Busca: nombre común, científico o indicación" aria-label="Buscar">
<div class="lg">Seguridad (Duke)</div>
<div class="row" id="zf"></div>
<label class="lg">Eficacia mínima de los ítems <select id="sc"><option value="0">f (folclor) o más</option><option value="1">1 (experimental) o más</option><option value="2" selected>2 (estudios/Comisión E) o más</option><option value="3">3 (ensayos clínicos)</option></select></label>
<label class="lg"><input type="checkbox" id="onlyV" style="width:auto"> Solo con verificación 2026</label>
<div id="list" role="listbox"></div>
<p class="warn">Libro de 2002. Los puntajes son de Duke. No es una guía clínica.</p>
</aside><main id="main"></main></div>
<script>
const D=__DATA__, V=__VERIF__;
const ZL={'X':'X: no tomar sin guía experta','+':'+: menos segura que el café','++':'++: tan segura como el café','+++':'+++: más segura que el café'};
const ZC={'X':'zX','+':'z1','++':'z2','+++':'z3'};
const SR={'f':0,'1':1,'2':2,'3':3};
const VL={mat:'respaldado con matices',inc:'incierto',sin:'sin evidencia clínica',con:'contradicho'};
const T=D.terms, H=D.herbs, byId={}; H.forEach(h=>byId[h.id]=h);
const inv={}; H.forEach(h=>h.i.forEach(([k,t,s])=>{(inv[t]=inv[t]||[]).push([h.id,s])}));
const nT=Object.keys(T).length, nE=H.reduce((a,h)=>a+h.i.length+1,0);
document.getElementById('stats').textContent=`${H.length} hierbas · ${nT} actividades e indicaciones · ${nE.toLocaleString('es')} aristas`;
let mode='H', zOn=new Set(['X','+','++','+++']), cur=null;
const zf=document.getElementById('zf');
['X','+','++','+++'].forEach(z=>{const b=document.createElement('button');b.className='chip';b.textContent=z;b.setAttribute('aria-pressed','true');b.onclick=()=>{zOn.has(z)?zOn.delete(z):zOn.add(z);b.setAttribute('aria-pressed',zOn.has(z));render()};zf.appendChild(b)});
const $=s=>document.getElementById(s), esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const norm=s=>s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();
$('mH').onclick=()=>{mode='H';$('mH').setAttribute('aria-pressed',true);$('mI').setAttribute('aria-pressed',false);render()};
$('mI').onclick=()=>{mode='I';$('mI').setAttribute('aria-pressed',true);$('mH').setAttribute('aria-pressed',false);render()};
['q','sc','onlyV'].forEach(i=>$(i).addEventListener('input',render));
function minS(){return +$('sc').value}
function render(){
 const q=norm($('q').value.trim()), L=$('list'); L.innerHTML='';
 if(mode==='H'){
  let r=H.filter(h=>zOn.has(h.z)&&(!$('onlyV').checked||V[h.c])&&(!q||norm(h.c+' '+h.s+' '+h.y).includes(q)));
  $('list').setAttribute('aria-label',r.length+' hierbas');
  r.slice(0,400).forEach(h=>{const d=document.createElement('div');d.innerHTML=`<span class="b ${ZC[h.z]}">${esc(h.z)}</span>${esc(h.c)} ${V[h.c]?'✓':''}<br><small><i>${esc(h.s)}</i> · p. ${h.p}</small>`;d.onclick=()=>showH(h.id);L.appendChild(d)});
  if(r.length>400)L.insertAdjacentHTML('beforeend',`<div><small>${r.length-400} más: afina la búsqueda</small></div>`);
 }else{
  let r=Object.entries(T).filter(([t,[l]])=>(!q||norm(l).includes(q))).map(([t,[l,k]])=>[t,l,k,(inv[t]||[]).filter(([h,s])=>SR[s]>=minS()&&zOn.has(byId[h].z)).length]).filter(x=>x[3]>0).sort((a,b)=>b[3]-a[3]);
  r.slice(0,400).forEach(([t,l,k,n])=>{const d=document.createElement('div');d.innerHTML=`${esc(l)} <small>· ${k?'indicación':'actividad'} · ${n} hierbas</small>`;d.onclick=()=>showT(t);L.appendChild(d)});
 }
 if(cur)(cur[0]==='h'?showH(cur[1],1):showT(cur[1],1));
}
function vBadge(h,label){const v=V[h.c]&&V[h.c].eff&&V[h.c].eff[label];return v?` <span class="v v${v}" title="Verificación 2026">${VL[v]}</span>`:''}
function showH(id,keep){
 const h=byId[id];cur=['h',id];const v=V[h.c]||{};
 const its=h.i.filter(([k,t,s])=>SR[s]>=minS());
 const grp=k=>its.filter(x=>x[0]===k).sort((a,b)=>SR[b[2]]-SR[a[2]]).map(([k,t,s,r])=>`<span class="s${s}" data-t="${t}" title="Fuentes: ${esc(r.join(', '))}">${esc(T[t][0])} (${s})${vBadge(h,T[t][0])}</span>`).join('');
 $('main').innerHTML=`<div class="card"><h2 style="margin:0 0 4px">${esc(h.c)}</h2><div><i>${esc(h.s)}</i>${h.q?' · '+esc(h.q):''}</div>
 <p><span class="b ${ZC[h.z]}">${esc(h.zr||h.z)}</span> ${esc(ZL[h.z])} · página impresa ${h.p}</p>
 ${v.seg?`<div class="alert"><b>Alerta 2026:</b> ${esc(v.seg)}</div>`:''}${v.nota?`<div class="alert">${esc(v.nota)}</div>`:''}
 ${v.skill?`<div class="skill"><b>Mis skills:</b> ${esc(v.skill)}</div>`:''}
 <details open><summary>Indicaciones (${its.filter(x=>x[0]==1).length})</summary><div class="items">${grp(1)||'<i>Ninguna con este puntaje</i>'}</div></details>
 <details><summary>Actividades (${its.filter(x=>x[0]==0).length})</summary><div class="items">${grp(0)||'<i>Ninguna con este puntaje</i>'}</div></details>
 ${h.d?`<details><summary>Dosis (Duke)</summary><p class="txt">${esc(h.d)}</p></details>`:''}
 ${h.k?`<details><summary>Contraindicaciones, interacciones y efectos adversos (Duke)</summary><p class="txt">${esc(h.k)}</p></details>`:''}
 ${h.e?`<details><summary>Extractos</summary><p class="txt">${esc(h.e)}</p></details>`:''}
 ${h.y?`<details><summary>Sinónimos</summary><p class="txt">${esc(h.y)}</p></details>`:''}</div>
 <div class="card"><b>Red de la hierba</b> <span class="lg">· morado: actividad · verde: indicación · grosor: puntaje · máx. 70 nodos</span><svg id="g"></svg></div>`;
 $('main').querySelectorAll('.items span').forEach(s=>s.onclick=()=>showT(s.dataset.t));
 ego({id:h.id,label:h.c,kind:'h',z:h.z},its.slice().sort((a,b)=>SR[b[2]]-SR[a[2]]).slice(0,70).map(([k,t,s])=>({id:t,label:T[t][0],kind:k?'i':'a',s})));
 if(!keep)window.scrollTo(0,0);
}
function showT(t,keep){
 cur=['t',t];const [l,k]=T[t];
 const hs=(inv[t]||[]).filter(([h,s])=>SR[s]>=minS()&&zOn.has(byId[h].z)).sort((a,b)=>SR[b[1]]-SR[a[1]]);
 $('main').innerHTML=`<div class="card"><h2 style="margin:0">${esc(l)}</h2><p class="lg">${k?'Indicación':'Actividad'} · ${hs.length} hierbas con puntaje ≥ ${$('sc').selectedOptions[0].text.split(' ')[0]} y seguridad filtrada</p>
 <table><thead><tr><th>Hierba</th><th>Puntaje</th><th>Seguridad</th><th>Pág.</th></tr></thead><tbody>${hs.map(([h,s])=>{const x=byId[h];return `<tr data-h="${h}" style="cursor:pointer"><td>${esc(x.c)} <i class="lg">${esc(x.s)}</i>${vBadge(x,l)}${V[x.c]&&V[x.c].seg?' ⚠️':''}</td><td>${s}</td><td><span class="b ${ZC[x.z]}">${esc(x.z)}</span></td><td>${x.p}</td></tr>`}).join('')}</tbody></table></div>
 <div class="card"><b>Red de la indicación</b> <span class="lg">· color: seguridad · máx. 70 hierbas</span><svg id="g"></svg></div>`;
 $('main').querySelectorAll('tr[data-h]').forEach(r=>r.onclick=()=>showH(r.dataset.h));
 ego({id:t,label:l,kind:k?'i':'a'},hs.slice(0,70).map(([h,s])=>({id:h,label:byId[h].c,kind:'h',z:byId[h].z,s})));
 if(!keep)window.scrollTo(0,0);
}
function col(n){const cs=getComputedStyle(document.documentElement);if(n.kind==='h')return cs.getPropertyValue({'X':'--sx','+':'--s1','++':'--s2','+++':'--s3'}[n.z]);return cs.getPropertyValue(n.kind==='a'?'--act':'--ind')}
function ego(c,ns){
 const svg=d3.select('#g'),W=svg.node().clientWidth,Hh=420;svg.selectAll('*').remove();
 const nodes=[{...c,fx:W/2,fy:Hh/2}].concat(ns.map(n=>({...n})));const links=ns.map(n=>({source:c.id,target:n.id,s:n.s}));
 const sim=d3.forceSimulation(nodes).force('l',d3.forceLink(links).id(d=>d.id).distance(d=>150-SR[d.s]*25)).force('c',d3.forceManyBody().strength(-90)).force('x',d3.forceCollide(16));
 const ink=getComputedStyle(document.documentElement).getPropertyValue('--mute');
 const L=svg.append('g').selectAll('line').data(links).join('line').attr('stroke',ink).attr('stroke-opacity',.5).attr('stroke-width',d=>0.6+SR[d.s]);
 const G=svg.append('g').selectAll('g').data(nodes).join('g').style('cursor','pointer').on('click',(e,d)=>{if(d.id===c.id)return;d.kind==='h'?showH(d.id):showT(d.id)});
 G.append('circle').attr('r',(d,i)=>i?6:11).attr('fill',col);
 G.append('text').text(d=>d.label.length>22?d.label.slice(0,21)+'…':d.label).attr('x',9).attr('y',4).attr('font-size',(d,i)=>i?11:13).attr('fill',getComputedStyle(document.documentElement).getPropertyValue('--ink'));
 G.append('title').text(d=>d.label+(d.s?' ('+d.s+')':''));
 sim.on('tick',()=>{nodes.forEach(n=>{n.x=Math.max(8,Math.min(W-90,n.x));n.y=Math.max(10,Math.min(Hh-10,n.y))});L.attr('x1',d=>d.source.x).attr('y1',d=>d.source.y).attr('x2',d=>d.target.x).attr('y2',d=>d.target.y);G.attr('transform',d=>`translate(${d.x},${d.y})`)});
}
render();
const g=H.find(h=>h.c==='GARLIC');if(g)showH(g.id);
</script></body></html>'''
html = html.replace('__DATA__', json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')).replace('__VERIF__', json.dumps(V, ensure_ascii=False))
open(sys.argv[2], 'w', encoding='utf-8').write(html)
missing = [k for k in V if k not in {h['c'] for h in data['herbs']}]
print('bytes', len(html.encode()), 'verif keys missing:', missing)
