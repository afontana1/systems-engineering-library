/* Optional offline v57 smoke tests. Requires Node.js; no packages or internet. */
'use strict';
const fs=require('fs');
const path=require('path');
const assert=require('assert');
const source=path.join(__dirname,'..','SE','K','U');
const html=fs.readFileSync(path.join(source,'OPEN-ENCYCLOPEDIA.html'),'utf8');
const match=html.match(/<script\s+type="application\/json"\s+id="corpus"[^>]*>(.*?)<\/script>/s);
assert(match,'the embedded offline search collection exists');
const db=JSON.parse(match[1]);
assert.equal(db.docs.length,1076);
assert.equal(db.referenceCatalog.length,56);
const {create}=require(path.join(source,'discovery-v57.js'));
const conceptIds=new Set(db.referenceCatalog.map(c=>c.id));
const classify=d=>conceptIds.has(d.id)?'concept':/chapter|textbook/i.test(d.kind)?'book':/lab|practice/i.test(d.kind)?'lab':'other';
const engine=create(db.docs,db.referenceCatalog,classify);
const slugById=new Map(db.referenceCatalog.map(c=>[c.id,c.slug]));
const scenarios=[
  ['How do I prove my design is safe?','safety','system-safety-and-hazards'],
  ['How do I verify a requirement?','evidence','v-and-v'],
  ['Why does my simulation differ from reality?','model','model-vv-and-credibility'],
  ['MTBF','reliability','reliability-availability-maintainability'],
  ['What is MBSE?','architect','model-language-method-tool'],
  ['digital twin','digital','digital-thread-and-twin'],
  ['How do I make a robust trade study?','optimization','engineering-trades'],
  ['test fidelity','testing','test-fidelity-and-similarity'],
  ['supply chain risk','sustainment','supply-chain-assurance-and-provenance'],
  ['FMEA','safety','system-safety-and-hazards'],
  ['How to learn systems engineering from scratch','learn','system-of-interest']
];
for(const [q,intent,target] of scenarios){
  const r=engine.query(q);
  assert.equal(r.intent?.id,intent,'incorrect intent for '+q);
  const topConcepts=r.rows.filter(x=>x.kind==='concept').slice(0,8).map(x=>slugById.get(x.doc.id));
  assert(topConcepts.includes(target),'missing top-8 canonical concept for '+q);
}
const typo=engine.query('reliablity');
assert(typo.didYouMean?.includes('reliability'),'no spelling suggestion');
const lab=engine.query('simulation test','lab');
assert(lab.rows.length>0&&lab.rows.every(r=>r.kind==='lab'),'lab filter failed');
const book=engine.query('requirements','book');
assert(book.rows.length>0&&book.rows.every(r=>r.kind==='book'),'textbook filter failed');
const all=engine.query('digital thread');
assert.equal(Object.values(all.counts).reduce((a,b)=>a+b,0),all.rows.length);
console.log('PASS: 11 curated questions, 1 typo correction, 2 filters, index/count assertions.');
console.log(`Offline corpus preserved: ${db.docs.length} resources and ${db.referenceCatalog.length} canonical concepts.`);
