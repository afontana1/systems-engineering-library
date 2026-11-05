/* v57: Fully offline, explainable engineering discovery. No network or external AI service. */
(function(root, factory){
  const api=factory();
  if(typeof module==='object' && module.exports)module.exports=api;
  if(root)root.SEDiscoveryV57=api;
})(typeof window!=='undefined'?window:null,function(){
  'use strict';
  const normalize=s=>String(s||'').normalize('NFKD').toLowerCase().replace(/[\u0300-\u036f]/g,'').replace(/[‐‑–—]/g,'-').replace(/&/g,' and ').replace(/[^a-z0-9]+/g,' ').replace(/\s+/g,' ').trim();
  const STOP=new Set('a an the and or of for to from in on at by with into through how do does did can could should would i we you my our your is are was were be been being what which why where when who about a as if it this that them their make prove build define find give show explain help using use need want know decide know between much more best me'.split(' '));
  const stem=w=>w.length>5&&w.endsWith('ies')?w.slice(0,-3)+'y':w.length>6&&w.endsWith('ments')?w.slice(0,-1):w.length>6&&w.endsWith('ing')?w.slice(0,-3):w.length>5&&w.endsWith('ed')?w.slice(0,-2):w.length>5&&w.endsWith('s')&&!w.endsWith('ss')?w.slice(0,-1):w;
  const words=s=>normalize(s).split(' ').filter(w=>w&&!STOP.has(w)).map(stem);
  // Abbreviations are pointers to methods, not assertions that unlike concepts are equivalent.
  const ALIASES=[
    {forms:['mbse','sysml','model based systems engineering'],words:['model','architecture'],slugs:['model-language-method-tool','views-and-viewpoints']},
    {forms:['v and v','vv','v v','verify','verifying','validation'],words:['verification','validation'],slugs:['v-and-v','verification-matrix']},
    {forms:['fmea','fmeca','fault tree','fta','hazop','hazard analysis'],words:['hazard','safety','failure'],slugs:['system-safety-and-hazards','assurance-cases-and-evidence']},
    {forms:['mtbf','mttf','mttr','ram','uptime','downtime'],words:['reliability','availability','repair'],slugs:['reliability-availability-maintainability']},
    {forms:['doe','factorial experiment','factorial design'],words:['experimental','design'],slugs:['design-of-experiments']},
    {forms:['conops','operational concept','concept of operation'],words:['operational','scenario'],slugs:['conops-and-scenarios']},
    {forms:['wip','work in progress','work in process','kanban'],words:['flow','bottleneck'],slugs:['flow-wip-and-queues']},
    {forms:['cicd','ci cd','devops','deployment pipeline'],words:['software','release','assurance'],slugs:['software-lifecycle-evidence']},
    {forms:['sos','system of systems','systems of systems'],words:['constituent','federated'],slugs:['sos-characteristics']},
    {forms:['voi','evpi','evsi','value of information'],words:['decision','uncertainty','information'],slugs:['bayesian-value-of-information']},
    {forms:['digital twin','digital thread','digital twins'],words:['digital','model'],slugs:['digital-thread-and-twin']},
    {forms:['trade space','tradeoff','tradeoffs','trade off','trade study','trade studies'],words:['trade','alternatives'],slugs:['engineering-trades','pareto-and-value']},
    {forms:['safety case','assurance case','gsa','gsn'],words:['assurance','evidence','claim'],slugs:['assurance-cases-and-evidence','system-safety-and-hazards']},
    {forms:['sbom','software bill of materials','counterfeit parts'],words:['supply','provenance'],slugs:['supply-chain-assurance-and-provenance']},
    {forms:['obsolescence','end of life','eol','dmsms'],words:['technology','refresh'],slugs:['obsolescence-and-technology-refresh']},
    {forms:['metrology','calibration','measurement uncertainty'],words:['measurement','traceability'],slugs:['measurement-traceability-and-calibration']},
    {forms:['monte carlo','stochastic simulation','random sampling'],words:['simulation','probability'],slugs:['probability-and-dependence','design-of-experiments']},
    {forms:['formal methods','temporal logic','model checker'],words:['formal','verification'],slugs:['formal-verification-and-temporal-logic']}
  ];
  // Curated learner questions: recommendations are editorial associations, not generated answers.
  const INTENTS=[
    {id:'safety',title:'Establish that a design is acceptably safe',description:'Begin with hazards and safety claims, then examine test evidence and residual risk.', triggers:['prove design safe','prove my design is safe','prove my design safe','design safe','ensure safety','is my system safe','safety critical','fault tree','fmea','hazard'],concepts:['system-safety-and-hazards','assurance-cases-and-evidence','v-and-v','reliability-availability-maintainability'],route:'evidence'},
    {id:'evidence',title:'Decide whether the evidence is sufficient',description:'Distinguish a requirement test, statistical acceptance, measurement quality, and the claim being made.',triggers:['enough evidence','test result enough','demonstrate compliance','prove requirement','verify requirement','verify a requirement','acceptance criteria','test evidence','requirements verification'],concepts:['v-and-v','statistical-acceptance-and-confidence','verification-matrix','assurance-cases-and-evidence'],route:'evidence'},
    {id:'model',title:'Check whether a model can support a decision',description:'Compare intended use, implementation checks, validation evidence, and experiment design.',triggers:['simulation real','simulation differ from reality','simulation differs from reality','simulator wrong','model credibility','validate simulation','trust my model','trust a simulation','predict reality','model verification','simulation accuracy'],concepts:['model-vv-and-credibility','conceptual-m-and-s','design-of-experiments','test-fidelity-and-similarity'],route:'modeling'},
    {id:'requirements',title:'Turn needs into verifiable requirements',description:'Start with stakeholder needs and scenarios, then refine requirements and traceability.',triggers:['write requirements','good requirement','requirements unclear','capture needs','define requirements','requirements traceability','trace requirements'],concepts:['good-requirements','stakeholders-and-needs','traceability-graph','conops-and-scenarios'],route:'foundations'},
    {id:'architect',title:'Develop and compare system architectures',description:'Separate functions from physical solutions and make interface contracts explicit.',triggers:['system architecture','design architecture','sysml','mbse','allocate functions','interface design','architecture viewpoints'],concepts:['functional-vs-physical','views-and-viewpoints','allocation-matrix','interface-control'],route:'architecture'},
    {id:'reliability',title:'Estimate reliability and availability',description:'Understand failure behavior, repair time, common-cause dependence, and operational availability.',triggers:['mtbf','mttr','reliability','availability','uptime','repairability','failure rate','system fails'],concepts:['reliability-availability-maintainability','probability-and-dependence','lifecycle-sustainment-economics','system-safety-and-hazards'],route:'delivery'},
    {id:'optimization',title:'Choose among uncertain alternatives',description:'Make objectives explicit and compare tradeoffs, robustness, and the value of more evidence.',triggers:['best design','trade study','tradeoff','trade off','choosing alternatives','choose design','robust optimization','multiple objectives','pareto'],concepts:['engineering-trades','pareto-and-value','robust-optimization-and-margins','bayesian-value-of-information'],route:'modeling'},
    {id:'security',title:'Assess mission-level security',description:'Start with trust boundaries and threat scenarios, then build evidence-backed protection claims.',triggers:['cybersecurity','security','attack surface','secure system','trust boundary','threat model','zero trust'],concepts:['systems-security-engineering','assurance-cases-and-evidence','interface-control','configuration-assurance-and-change-control'],route:'evidence'},
    {id:'testing',title:'Plan representative tests',description:'Connect tests to claims, operating envelopes, measurement accuracy, and acceptance decisions.',triggers:['test plan','test fidelity','lab test','test coverage','qualification test','environmental test','measurement bias','test realistic'],concepts:['test-fidelity-and-similarity','environmental-qualification-and-test-levels','measurement-traceability-and-calibration','statistical-acceptance-and-confidence'],route:'evidence'},
    {id:'team',title:'Improve engineering delivery and flow',description:'Analyze queues, work in process, organizational dependencies, and governing decisions.',triggers:['project late','team slow','engineering bottleneck','schedule slip','agile delivery','work in process','wip','project risk'],concepts:['flow-wip-and-queues','agile-tailoring','wbs-and-baselines','risk-vs-issue'],route:'delivery'},
    {id:'digital',title:'Connect evidence across a digital lifecycle',description:'Preserve model meaning, configuration identity, lineage, and reproducibility across tools.',triggers:['digital twin','digital thread','data lineage','data governance','configuration management','digital engineering'],concepts:['digital-thread-and-twin','technical-data-governance-and-lineage','configuration-assurance-and-change-control','model-language-method-tool'],route:'architecture'},
    {id:'sustainment',title:'Design for long-term support',description:'Account for lifetime costs, maintainability, obsolescence, and supply-chain exposure.',triggers:['lifecycle cost','life cycle cost','sustainment','spare parts','obsolete parts','obsolescence','supplier risk','supply chain','technology refresh'],concepts:['lifecycle-sustainment-economics','obsolescence-and-technology-refresh','supply-chain-assurance-and-provenance','reliability-availability-maintainability'],route:'delivery'},
    {id:'complexity',title:'Reason about interdependent organizations and systems',description:'Identify constituents, boundaries, feedback effects, and organizational authority.',triggers:['systems of systems','federation','enterprise transformation','complex adaptive','emergent behavior','policy resistance','governance','stakeholder conflict'],concepts:['sos-characteristics','enterprise-as-system','complexity-emergence','authority-and-governance'],route:'complex'},
    {id:'learn',title:'Learn systems engineering progressively',description:'Begin with systems, stakeholder needs, operating scenarios, and verifiable requirements.',triggers:['learn systems engineering','start learning','systems engineering beginner','begin systems engineering','start from scratch','new to engineering'],concepts:['system-of-interest','stakeholders-and-needs','conops-and-scenarios','good-requirements'],route:'foundations'}
  ];
  const CLASS_PRIORITY={concept:8,book:2,lab:0,other:0};
  function create(docs,catalog,classify){
    const catById=new Map(catalog.map(c=>[c.id,c]));
    const slugToId=new Map(catalog.map(c=>[c.slug,c.id]));
    const records=docs.map(d=>{
      const c=catById.get(d.id);
      const title=normalize(d.title),summary=normalize(c?.summary||d.excerpt||''),course=normalize(d.courseTitle||d.course||'');
      const body=normalize(d.text||d.searchText||d.excerpt||'');
      return {d,c,title,summary,course,body,kind:classify(d)};
    });
    const lexicon=new Set();
    for(const c of catalog){for(const w of words(c.title+' '+c.summary))if(w.length>=4)lexicon.add(w);}
    for(const a of ALIASES)for(const w of a.words)lexicon.add(stem(w));
    function detect(q){
      const n=normalize(q);
      const matches=INTENTS.map(it=>{
        let s=0;
        for(const trigger of it.triggers){const tr=normalize(trigger);const tw=tr.split(' ');
          if(n.includes(tr))s+=tr.length>=12?12:9;
          else if(tw.length>1 && tw.filter(w=>n.split(' ').includes(w)).length===tw.length)s+=6;
        }
        return {it,score:s};
      }).filter(r=>r.score>0).sort((a,b)=>b.score-a.score);
      return matches[0]?.it||null;
    }
    function suggestion(term){
      if(term.length<5||lexicon.has(stem(term)))return null;
      let winner=null,best=3;
      for(const w of lexicon){if(Math.abs(w.length-term.length)>2)continue;
        const distance=edit(stem(term),w,best);
        if(distance<best){best=distance;winner=w;}
      }
      return winner;
    }
    function edit(a,b,limit){
      if(Math.abs(a.length-b.length)>limit)return limit+1;
      let row=Array.from({length:b.length+1},(_,i)=>i);
      for(let i=1;i<=a.length;i++){
        const next=[i];let min=i;
        for(let j=1;j<=b.length;j++){
          const v=Math.min(next[j-1]+1,row[j]+1,row[j-1]+(a[i-1]===b[j-1]?0:1));next.push(v);if(v<min)min=v;
        }
        if(min>limit)return limit+1;row=next;
      }
      return row[b.length];
    }
    const matchWord=(field,w)=>w.length<=3?(' '+field+' ').includes(' '+w+' '):field.includes(w);
    function query(q,scope='all'){
      const n=normalize(q);const raw=words(q).filter(t=>t.length>=2);
      const initial=[...new Set(raw)];
      const aliasMatches=ALIASES.filter(a=>a.forms.some(f=>n.includes(normalize(f))));
      const expansions=new Set(aliasMatches.flatMap(a=>a.words.map(stem)));
      const pinned=new Set(aliasMatches.flatMap(a=>a.slugs));
      const intent=detect(q);
      if(intent)intent.concepts.forEach(s=>pinned.add(s));
      const replacements=initial.map(w=>suggestion(w));
      const corrected=initial.map((w,i)=>replacements[i]||w);
      // Corrections are supplementary; a valid query never silently changes its terms.
      const core=initial.length?initial:[];
      const evalTokens=[...new Set([...core,...expansions])];
      const phrase=n;
      const ranked=[];
      for(const record of records){
        if(scope!=='all'&&scope!==record.kind)continue;
        const {d,c,title,summary,course,body,kind}=record;
        const pinnedHit=!!(c&&pinned.has(c.slug));
        let hits=0,score=CLASS_PRIORITY[kind]||0;
        let titleHits=0;
        for(const w of core){
          const t=matchWord(title,w),s=matchWord(summary,w),co=matchWord(course,w),b=matchWord(body,w);
          if(t||s||co||b){hits++;score+=t?46:s?20:co?7:3;if(t)titleHits++;}
        }
        const extra=[...expansions].filter(w=>!core.includes(w));
        const bonus=Math.min(22,extra.reduce((v,w)=>v+(matchWord(title,w)?9:matchWord(summary,w)?4:matchWord(body,w)?1:0),0));
        score+=bonus;
        if(phrase&&title===phrase)score+=210;
        else if(phrase.length>3&&title.includes(phrase))score+=85;
        if(core.length&&hits===core.length)score+=29;
        else if(core.length&&hits/core.length>=.60)score+=8;
        const pinPriority=intent&&c?intent.concepts.indexOf(c.slug):-1;
        if(pinPriority>=0)score+=185-pinPriority*16;
        else if(pinnedHit)score+=88;
        // Do not return documents based on the general concept boost alone.
        const threshold=core.length<=1?1:Math.max(1,Math.ceil(core.length*.62));
        if(!pinnedHit&&hits<threshold)continue;
        if(!core.length&&!pinnedHit)continue;
        const reason=pinPriority>=0?'Curated starting point':titleHits>=Math.max(1,Math.ceil(core.length*.6))?'Title matches your terms':hits===core.length?'Matches all key terms':'Related keyword match';
        ranked.push({doc:d,kind,score,hits,reason});
      }
      ranked.sort((a,b)=>b.score-a.score||a.doc.title.localeCompare(b.doc.title));
      const counts={concept:0,book:0,lab:0,other:0};for(const r of ranked)counts[r.kind]++;
      const didYouMean=replacements.some(Boolean)?corrected.join(' '):null;
      const picks=(intent?intent.concepts:aliasMatches.flatMap(a=>a.slugs)).map(slug=>slugToId.get(slug)).filter(Boolean);
      return {rows:ranked,counts,intent,picks:[...new Set(picks)],tokens:initial,expansions:[...expansions],didYouMean,normalized:n};
    }
    return {query,detect,normalize};
  }
  return {create,normalize,INTENTS,ALIASES};
});
