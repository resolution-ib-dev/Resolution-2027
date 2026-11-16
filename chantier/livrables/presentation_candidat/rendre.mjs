import {createRequire} from 'module'; const {chromium}=createRequire(import.meta.url)('playwright'); import fs from 'fs';
const d=new URL('.',import.meta.url).pathname;
fs.writeFileSync(d+'presentation_candidat.html',fs.readFileSync(d+'gabarit.html','utf8').replace('__SANKEY__',fs.readFileSync(d+'sankey.svg','utf8')));
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:794,height:1123},deviceScaleFactor:2});
await p.goto('file://'+d+'presentation_candidat.html',{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready);
const ok=await p.evaluate(()=>['Archivo','Source Serif 4'].map(f=>[f,document.fonts.check(`16px "${f}"`)]));
console.log(ok); if(ok.some(x=>!x[1])){console.error('police de repli');process.exit(1)}
console.log(await p.evaluate(()=>[...document.querySelectorAll('.page')].map(s=>{const pied=(s.querySelector('.bas')||s.querySelector('.pied')).getBoundingClientRect().top;
 const bas=Math.max(...[...s.children].filter(e=>!e.classList.contains('pied')&&!e.classList.contains('bas')).map(e=>e.getBoundingClientRect().bottom));return Math.round(pied-bas)})));
await p.pdf({path:d+'presentation_candidat.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});
const ps=await p.$$('.page'); for(let i=0;i<ps.length;i++) await ps[i].screenshot({path:`${d}p${i+1}.png`});
await b.close();
