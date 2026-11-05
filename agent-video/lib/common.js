// Outils communs aux formats LexyLab (chargé par formats/*.html)
const U = {
  clamp:(x,a,b)=>Math.max(a,Math.min(b,x)),
  ease:x=>{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3);},
  easeIO:x=>{x=Math.max(0,Math.min(1,x));return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;},
  pop:x=>{x=Math.max(0,Math.min(1,x));const c=1.70158*1.3;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);},
  esc:s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'),
  // *mot* -> vert ; _mot_ -> surligné ; \n -> retour ligne
  md:s=>U.esc(s).replace(/\*([^*]+)\*/g,'<span class="g">$1</span>').replace(/_([^_]+)_/g,'<span class="hl">$1</span>').replace(/\n/g,'<br>'),
  // "Je vous [envoi|envoie] le ..." -> [{t:'Je vous '},{e:'envoi',f:'envoie'},...]
  parseErr:s=>{const out=[];const re=/\[([^|\]]+)\|([^\]]+)\]/g;let last=0,m;
    while((m=re.exec(s))){if(m.index>last)out.push({t:s.slice(last,m.index)});out.push({e:m[1],f:m[2]});last=re.lastIndex;}
    if(last<s.length)out.push({t:s.slice(last)});return out;},
  wrongLen:segs=>segs.reduce((a,s)=>a+(s.t!==undefined?s.t.length:s.e.length),0),
  inW:(t,w)=>t>=w[0]&&t<w[1],
  boil:t=>{const el=document.getElementById('turb'); if(el) el.setAttribute('seed',1+Math.floor(t*8)%6);},
};
// Carte de fin commune : <div id="end"> ... </div> fournie par endHTML()
U.endHTML = (tag)=>`<div id="end"><img src="../lib/logo.png"><div class="name">LexyLab</div>
  <div class="tag">${U.md(tag||'Le correcteur pensé\npour la dyslexie')}</div><div class="btn" id="endbtn">Lien en bio 👆</div></div>`;
U.renderEnd = (t,t0)=>{
  const e=document.getElementById('end'); if(!e) return;
  e.style.opacity=U.ease((t-t0)/0.5);
  const b=document.getElementById('endbtn'); b.style.transform=`scale(${t>t0+0.5?U.pop((t-t0-0.5)/0.3):0})`;
};
U.ROUGH_SVG = `<svg width="0" height="0" style="position:absolute"><defs><filter id="r" x="-5%" y="-5%" width="110%" height="110%">
  <feTurbulence id="turb" type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="1"/><feDisplacementMap in="SourceGraphic" scale="7"/></filter></defs></svg>`;
U.HEADER = `<div class="hdr"><img src="../lib/logo.png"><span>Lexy<span class="lab">Lab</span></span></div>`;
