/* v56 offline learning atlas: all concepts in learning pathways with advisory prerequisites. */
(() => {
  'use strict';
  const parsed = document.getElementById('corpus');
  if (!parsed) return;
  const DB = JSON.parse(parsed.textContent);
  const docs = DB.docs || [];
  const catalog = DB.referenceCatalog || [];
  const byId = new Map(docs.map(d => [d.id,d]));
  const bySlug = new Map(catalog.map(c => [c.slug,c]));
  const conceptIds = new Set(catalog.map(c => c.id));
  const $ = s => document.querySelector(s);
  const el = (tag,cls,value) => { const n=document.createElement(tag);if(cls)n.className=cls;if(value!==undefined&&value!==null)n.textContent=String(value);return n; };
  const normal = s => String(s||'').normalize('NFKD').toLowerCase().replace(/[\u0300-\u036f]/g,'');
  const terms = s => normal(s).trim().split(/\s+/).filter(Boolean);
  const hrefDoc = (id,from) => '#doc='+encodeURIComponent(id)+(from?'&from='+encodeURIComponent(from):'');
  const sourceHref = d => d.fileHref || ('../'+String(d.source||'').replace(/^K\//,''));
  const markdownHref = d => '../'+String(d.source||'').replace(/^K\//,'');
  const PATHS = window.SE_LEARNING_ROUTES_V56?.routes || [];
  const stages = ['Beginner','Intermediate','Advanced'];
  const routeOf = slug => PATHS.find(p=>p.steps.includes(slug));
  const atlasUrl = id => 'K/U/OPEN-ENCYCLOPEDIA.html#doc='+encodeURIComponent(id);
  // Reflect both the v54 atlas state and the v55 shared study desk where available.
  const studied = id => !!(progress.done[id] || window.SEStudyV55?.load()?.done?.[atlasUrl(id)]);
  function setStudied(id,value){
    if(value) progress.done[id]=true;else delete progress.done[id];
    const shared=window.SEStudyV55;
    if(shared){const url=atlasUrl(id),old=!!shared.load()?.done?.[url];
      if(old!==value)shared.toggle('done',url,byId.get(id)?.title||'Reference concept','Concept reference');
    }
    persist();
  }
  function setSaved(id,value){
    if(value) progress.saved[id]=true;else delete progress.saved[id];
    const shared=window.SEStudyV55;
    if(shared){const url=atlasUrl(id),old=!!shared.load()?.saved?.[url];
      if(old!==value)shared.toggle('saved',url,byId.get(id)?.title||'Reference concept','Concept reference');
    }
    persist();
  }
  const badPaths = PATHS.flatMap(p=>p.steps.filter(s=>!bySlug.has(s)));
  if (badPaths.length) console.warn('Invalid path slugs:',badPaths);
  let subject='all',letter='all',searchLimit=10,current=null,previous='#discover',activePath=null;
  let progress={done:{},saved:{},recent:[]};
  try {const old=JSON.parse(localStorage.getItem('se_atlas_done_v8')||'{}');progress.done=old||{};}catch(e){}
  try {const now=JSON.parse(localStorage.getItem('se_atlas_study_v54')||'null');if(now&&typeof now==='object')progress={done:now.done||progress.done,saved:now.saved||{},recent:now.recent||[]};}catch(e){}
  const persist=()=>{try {localStorage.setItem('se_atlas_study_v54',JSON.stringify(progress));localStorage.setItem('se_atlas_done_v8',JSON.stringify(progress.done));}catch(e) {}};
  $('#docsN').textContent=docs.length.toLocaleString();
  $('#expandedN').textContent=catalog.length;
  const knownSubjects=[...new Set(catalog.map(c=>c.subject))];

  function classify(d) {
    if(conceptIds.has(d.id))return 'concept';
    const k=normal(d.kind);
    if(k.includes('chapter')||k.includes('textbook'))return 'book';
    if(k.includes('lab')||k.includes('practice'))return 'lab';
    return 'other';
  }
  function kindLabel(d) {const k=classify(d);return k==='concept'?'Concept reference':k==='book'?'Textbook chapter':k==='lab'?'Practice / lab':'Supporting resource';}
  function show(mode) {
    for(const id of ['discover','paths','pathview','browse','results','reading','saved']) {
      const x=document.getElementById(id);if(x)x.hidden=(id!==mode);
    }
    document.querySelectorAll('.toplinks a[href^="#"],.side-menu a[href^="#"]').forEach(a=> {
      const active=a.getAttribute('href')==='#'+mode;
      a.classList.toggle('nav-current',active);
      if(active)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');
    });
    $('#announce').textContent=mode==='reading'?'Reading document':mode==='results'?'Search results':mode==='pathview'?'Learning route':mode+' view';
  }
  function pathCard(p){
    const a=el('a','route-card');a.href='#path='+p.id;
    const n=p.steps.filter(s=>studied(bySlug.get(s)?.id)).length;
    a.append(el('span','route-level',p.level),el('h3',null,p.title),el('p',null,p.subtitle));
    const stageTags=el('div','route-stage-tags');
    stages.forEach(level=>stageTags.append(el('span',null,level)));
    a.append(stageTags);
    const footer=el('div','route-bottom');footer.append(el('span',null,p.steps.length+' reference concepts · 3 levels'),el('span',null,n+' / '+p.steps.length+' studied'));
    a.append(footer);return a;
  }
  function renderPaths(){const h=$('#pathCards');h.replaceChildren();for(const p of PATHS)h.append(pathCard(p));}
  function readingMini(d,sub){
    const a=el('a','mini-link');a.href=hrefDoc(d.id);
    a.append(el('strong',null,d.title),el('span',null,sub||kindLabel(d)));return a;
  }
  function starterAndRecent(){
    const starters=$('#starterConcepts');starters.replaceChildren();
    for(const s of ['system-of-interest','stakeholders-and-needs','good-requirements','v-and-v']){
      const c=bySlug.get(s);if(c)starters.append(readingMini(byId.get(c.id),'Concept reference · '+c.subject));
    }
    const recent=$('#continuePanel');recent.replaceChildren();
    const ids=progress.recent.filter(id=>byId.has(id)).slice(0,4);
    if(ids.length)ids.forEach(id=>recent.append(readingMini(byId.get(id))));
    else recent.append(el('p','micro','Open a concept or chapter and it will appear here for quick return.'));
  }
  function renderPath(p) {
    activePath=p.id;
    $('#pathTitle').textContent=p.title;$('#pathIntro').textContent=p.subtitle;
    const n=p.steps.filter(s=>studied(bySlug.get(s)?.id)).length;
    $('#pathProgress').textContent=n+' of '+p.steps.length+' studied · 3 stages';
    const host=$('#pathSteps'),jumps=$('#pathStageNav'),continueHost=$('#pathContinue');
    host.replaceChildren();jumps.replaceChildren();continueHost.replaceChildren();
    const firstOutstanding=p.steps.find(s=>!studied(bySlug.get(s)?.id))||p.steps[0];
    const firstC=bySlug.get(firstOutstanding);
    const start=el('a','route-continue-link',(n===p.steps.length?'Review':'Continue')+' route: '+firstC.title);
    start.href=hrefDoc(firstC.id,p.id);continueHost.append(start);
    continueHost.append(el('span','route-progress-note', n===p.steps.length?'All concepts marked studied; revisit for retention.':'Study markers reflect reading, not graded mastery.'));
    let position=0;
    for(const [stageIndex,stage] of p.stages.entries()){
      const group=el('li','path-stage');group.id='route-stage-'+stageIndex;
      const completed=stage.steps.filter(slug=>studied(bySlug.get(slug)?.id)).length;
      const jump=el('button','stage-jump',stage.level+' · '+completed+'/'+stage.steps.length);
      jump.type='button';jump.addEventListener('click',()=>document.getElementById(group.id)?.scrollIntoView({behavior:'smooth',block:'start'}));
      jumps.append(jump);
      const header=el('div','stage-header');const left=el('div');left.append(el('span','stage-eyebrow',stage.level+' · '+(stageIndex+1)+' of 3'),el('h3',null,stage.title),el('p',null,stage.goal));
      header.append(left,el('span','stage-progress',completed+' / '+stage.steps.length+' studied'));group.append(header);
      const stepList=el('ol','path-stage-steps');
      for(const slug of stage.steps){
        const c=bySlug.get(slug);if(!c)continue;
        const li=el('li','path-step'),num=++position;
        const unmet=(c.prerequisites||[]).filter(s=>bySlug.has(s)&&!studied(bySlug.get(s).id));
        const top=el('div','step-top');top.append(el('span','step-number',String(num).padStart(2,'0')),
          el('span','step-state',studied(c.id)?'✓ Studied':unmet.length?'Suggested preparation available':'Ready to explore'));
        const link=el('a','step-main');link.href=hrefDoc(c.id,p.id);link.append(el('h4',null,c.title),el('p',null,c.summary));
        li.append(top,link);
        if(c.prerequisites?.length){
          const details=el('details','step-prereqs');const count=unmet.length;
          details.append(el('summary',null,'Recommended prerequisites · '+(c.prerequisites.length-count)+' of '+c.prerequisites.length+' studied'));
          const links=el('div','step-prereq-links');
          c.prerequisites.forEach(s=>{const pre=bySlug.get(s);if(!pre)return;
            const preRoute=routeOf(s);const a=el('a',null,(studied(pre.id)?'✓ ':'○ ')+pre.title+(preRoute?.id!==p.id?' · another route':''));
            a.href=hrefDoc(pre.id,preRoute?.id);links.append(a);
          });details.append(links);li.append(details);
        }
        if(c.books?.length){const div=el('div','step-depth');div.append(el('span',null,'Go deeper: '));
          const b=c.books[0],d=byId.get(b.id);if(d){const a=el('a',null,'Book '+b.book+' · Chapter '+b.chapter);
            a.href=hrefDoc(b.id,p.id);div.append(a);}li.append(div);
        }
        stepList.append(li);
      }
      group.append(stepList);
      const practice=byId.get(stage.practiceId);
      const footer=el('aside','stage-practice');footer.append(el('h4',null,'Apply what you learned'));
      if(practice){const a=el('a',null,practice.title);a.href=hrefDoc(practice.id,p.id);footer.append(a);
        footer.append(el('p','micro','Existing practice resource. Completing it is optional and is not automatically graded.'));
      }
      footer.append(el('p','stage-check','Self-check: '+stage.check));group.append(footer);host.append(group);
    }
    show('pathview');
  }
  function subjectButtons(){const h=$('#subjects');h.replaceChildren();
    for(const name of ['all',...knownSubjects]){
      const b=el('button','subject-chip',name==='all'?'All subjects':name);b.type='button';b.dataset.subject=name;
      b.addEventListener('click',()=>{subject=name;letter='all';refreshFilters();location.hash='browse';renderBrowse();show('browse');});h.append(b);
    }
    const host=$('#az');host.replaceChildren();
    for(const l of ['all',...'ABCDEFGHIJKLMNOPQRSTUVWXYZ']){
      const b=el('button','azbtn',l==='all'?'All':l);b.type='button';b.dataset.letter=l;
      b.addEventListener('click',()=>{letter=l;refreshFilters();renderBrowse();});host.append(b);
    }
    refreshFilters();
  }
  function refreshFilters(){
    document.querySelectorAll('[data-subject]').forEach(b=>{
      const active=b.dataset.subject===subject;b.classList.toggle('chosen',active);b.setAttribute('aria-pressed',String(active));
    });
    document.querySelectorAll('[data-letter]').forEach(b=>{
      const active=b.dataset.letter===letter;b.classList.toggle('chosen',active);b.setAttribute('aria-pressed',String(active));
    });
  }
  function topicCard(c){
    const a=el('a','topiccard');a.href=hrefDoc(c.id);
    const top=el('div','topic-top');top.append(el('span','tag tag-deep','Reference concept'));
    if(studied(c.id))top.append(el('span','tag tag-studied','Studied'));
    a.append(top,el('h3',null,c.title),el('p',null,c.summary),el('span','topic-subject',c.subject));
    return a;
  }
  function renderBrowse(){
    const rows=catalog.filter(c=>(subject==='all'||c.subject===subject)&&(letter==='all'||normal(c.title).startsWith(normal(letter)))).sort((a,b)=>a.title.localeCompare(b.title));
    $('#topicCount').textContent=rows.length+' of '+catalog.length+' concepts shown';
    const h=$('#topicCards');h.replaceChildren();
    rows.forEach(c=>h.append(topicCard(c)));
    if(!rows.length){const p=el('p','empty','Nothing starts with this letter in the selected subject. Reset the filters to browse all concepts.');h.append(p);}
  }
  // v57: search uses a dedicated offline engine, with transparent editorial topic associations.
  const discovery = window.SEDiscoveryV57?.create(docs,catalog,classify);
  if(!discovery)console.error('v57 discovery engine unavailable; search enhancements are missing.');
  function matchText(node,s,ts){
    const tokens=[...new Set(ts.filter(t=>t.length>=3))].sort((a,b)=>b.length-a.length).slice(0,8);
    if(!tokens.length){node.textContent=s;return;}
    const safe=t=>t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
    const regex=new RegExp('('+tokens.map(safe).join('|')+')','gi');
    const splits=String(s).split(regex);
    const keys=new Set(tokens.map(t=>t.toLowerCase()));
    for(const p of splits){if(!p)continue;
      if(keys.has(p.toLowerCase()))node.append(el('mark','hit',p));else node.append(document.createTextNode(p));
    }
  }
  function snippet(d,tokens){
    const body=String(d.text||d.searchText||d.excerpt||'').replace(/\s+/g,' ');
    const lower=normal(body);
    const matches=tokens.map(t=>lower.indexOf(t)).filter(i=>i>=0).sort((a,b)=>a-b);
    if(!matches.length)return String(d.excerpt||body).slice(0,200);
    const pos=matches[0],start=Math.max(0,pos-57),end=Math.min(body.length,pos+180);
    return (start?'…':'')+body.slice(start,end)+(end<body.length?'…':'');
  }
  function resultCard(r,ts){
    const d=r.doc,a=el('a','resultcard');a.href=hrefDoc(d.id);
    a.append(el('div','resultkind',kindLabel(d)+(d.course?' · '+d.course:'')+' · '+r.reason));
    const h=el('h3');matchText(h,d.title,ts);a.append(h);
    const p=el('p');matchText(p,snippet(d,ts),ts);a.append(p);
    return a;
  }
  function queryButton(text,cls){const b=el('button',cls||'search-query',text);b.type='button';
    b.addEventListener('click',()=>{$('#search').value=text;location.hash='q='+encodeURIComponent(text);renderSearch(text);});return b;
  }
  function renderOverview(r,q,scope){
    const host=$('#searchOverview');host.replaceChildren();
    if(r.intent){
      const panel=el('div','search-intent');
      panel.append(el('div','intent-eyebrow','CURATED ENGINEERING TOPIC MATCH'),el('h3',null,r.intent.title),el('p',null,r.intent.description));
      const conceptHost=el('div','search-picks');
      if(scope==='all'||scope==='concept')for(const id of r.picks.slice(0,4)){
        const d=byId.get(id);if(!d)continue;
        const a=el('a','search-pick');a.href=hrefDoc(id,r.intent.route);
        a.append(el('strong',null,d.title),el('span',null,'Read the reference →'));conceptHost.append(a);
      }
      panel.append(conceptHost);
      const path=PATHS.find(p=>p.id===r.intent.route);
      if(path){const a=el('a','search-route-link','Follow the '+path.title+' learning route →');a.href='#path='+path.id;panel.append(a);}
      host.append(panel);
    }
    if(r.didYouMean && !r.rows.length){const wrap=el('div','search-correction');
      wrap.append(document.createTextNode('Possible spelling correction: '),queryButton(r.didYouMean,'correction-button'));host.append(wrap);
    }
    const guidance=el('p','search-method','Results are ranked locally using title, terminology, and content matches. Curated topic matches are suggestions, not proof that a resource answers every part of your question.');
    host.append(guidance);
  }
  function renderSearch(q){
    const scope=$('#scope').value;
    const res=discovery?discovery.query(q,scope):{rows:[],counts:{concept:0,book:0,lab:0,other:0},tokens:terms(q),expansions:[],picks:[],intent:null};
    $('#resultTitle').textContent='Results for “'+q+'”';
    const count=res.counts;
    $('#resultCount').textContent=res.rows.length+' matching resources · '+count.concept+' concepts · '+count.book+' textbooks · '+count.lab+' labs · '+count.other+' other';
    const ts=[...res.tokens,...res.expansions];
    const host=$('#searchResults');host.replaceChildren();renderOverview(res,q,scope);
    if(!res.rows.length){
      host.append(el('p','empty','No matching resources in this filter. Try a shorter question, another term, or All sources.'));
      const sample=el('div','search-retry');sample.append(el('strong',null,'Try a practical engineering question:'));
      ['How do I verify a requirement?','How do I prove my design is safe?','How can I trust a simulation?'].forEach(x=>sample.append(queryButton(x)));
      host.append(sample);$('#more').hidden=true;show('results');return;
    }
    let displayed=0;
    for(const [kind,label] of [['concept','Concept references · Start here'],['book','Textbook chapters · Learn in depth'],['lab','Labs and practice · Apply it'],['other','Supporting learning resources']]){
      const group=res.rows.filter(x=>x.kind===kind);
      if(!group.length)continue;
      host.append(el('h3','group-title',label+' · '+group.length));
      const cap=searchLimit;
      for(const row of group.slice(0,cap))host.append(resultCard(row,ts));
      displayed+=Math.min(group.length,cap);
    }
    const more=$('#more');more.hidden=displayed>=res.rows.length;
    if(!more.hidden)more.textContent='Show more of each resource type ('+(res.rows.length-displayed)+' more matching resources)';
    $('#announce').textContent=res.rows.length+' ranked search results found';show('results');
  }
  function sideLink(title,href,meta){const a=el('a','side-doc');a.href=href;a.append(el('strong',null,title));if(meta)a.append(el('span',null,meta));return a;}
  function buildOutline(paper){
    const host=$('#articleOutline');host.replaceChildren();
    const headings=[...paper.querySelectorAll('h2,h3')].slice(0,conceptIds.has(current)?18:12);
    if(headings.length<2){host.hidden=true;return;}
    host.hidden=false;host.append(el('strong',null,'On this page'));
    for(const [i,h] of headings.entries()){
      if(!h.id)h.id='atlas-section-'+i;
      const a=el('a',h.tagName.toLowerCase()==='h3'?'outline-sub':'',h.textContent.trim());
      a.href=hrefDoc(current)+'&section='+encodeURIComponent(h.id);host.append(a);
    }
  }
  function isSaved(id){return !!(progress.saved[id] || window.SEStudyV55?.load()?.saved?.[atlasUrl(id)]);}
  function addRecent(id){progress.recent=[id,...progress.recent.filter(x=>x!==id)].slice(0,25);persist();}
  function readingActions(d){
    const host=$('#readerActions');host.replaceChildren();
    host.append(sideLink('Open standalone HTML',sourceHref(d)),sideLink('Markdown source',markdownHref(d)));
    const mark=el('label','mark-read'),cb=el('input');cb.type='checkbox';cb.checked=studied(d.id);
    cb.addEventListener('change',()=>{setStudied(d.id,cb.checked);renderPaths();starterAndRecent();if(activePath){const p=PATHS.find(x=>x.id===activePath);if(p)renderPathContentOnly(p);} });
    mark.append(cb,document.createTextNode(' Mark studied'));host.append(mark);
    const b=el('button','bookmark-btn',isSaved(d.id)?'★ Saved':'☆ Save for later');b.type='button';b.setAttribute('aria-pressed',String(isSaved(d.id)));
    b.addEventListener('click',()=>{setSaved(d.id,!isSaved(d.id));b.textContent=isSaved(d.id)?'★ Saved':'☆ Save for later';b.setAttribute('aria-pressed',String(isSaved(d.id)));});host.append(b);
  }
  function renderPathContentOnly(p){const id=current;renderPath(p); if(id&&byId.has(id)) show('reading');}
  function articleRelations(d,c){
    const side=$('#related');side.replaceChildren();
    if(!c){side.append(el('h2',null,'Continue learning'));
      side.append(el('p','micro','Open the related reference subjects to connect this resource with the wider curriculum.'));
      side.append(sideLink('Browse the concept encyclopedia','#browse'));
      side.append(sideLink('Choose a learning route','#paths'));return;
    }
    side.append(el('h2',null,'Learning connections'));
    side.append(el('p','micro','Reference topic · '+c.subject));
    if(c.prerequisites?.length){side.append(el('h3',null,'Read first'));
      c.prerequisites.forEach(s=>{const x=bySlug.get(s);if(x)side.append(sideLink(x.title,hrefDoc(x.id),'Prerequisite concept'));});}
    if(c.related?.length){side.append(el('h3',null,'Explore next'));
      c.related.forEach(s=>{const x=bySlug.get(s);if(x)side.append(sideLink(x.title,hrefDoc(x.id),'Connected concept'));});}
    if(c.books?.length){side.append(el('h3',null,'Go deeper in a textbook'));
      c.books.forEach(b=>{const x=byId.get(b.id);if(x)side.append(sideLink(x.title,hrefDoc(x.id),'Book '+b.book+' · Chapter '+b.chapter));});}
    const path=PATHS.find(p=>p.id===activePath&&p.steps.includes(c.slug))||routeOf(c.slug);
    if(path){side.append(el('h3',null,'Learn in a sequence'));side.append(sideLink(path.title,'#path='+path.id,'Ordered concept pathway'));}
    side.append(el('p','micro','Sources and internal numerical checks do not constitute independent peer review or qualification.'));
  }
  function nextSteps(d,c){
    const host=$('#articleNext');host.replaceChildren();
    if(!c)return;
    const path=PATHS.find(p=>p.id===activePath&&p.steps.includes(c.slug))||routeOf(c.slug);
    const ix=path?path.steps.indexOf(c.slug):-1;
    const next=path&&ix<path.steps.length-1?bySlug.get(path.steps[ix+1]):null;
    const prev=path&&ix>0?bySlug.get(path.steps[ix-1]):null;
    host.append(el('h2',null,'Your next learning step'));
    if(path){host.append(sideLink('↩ Return to '+path.title,'#path='+path.id,'Your current guided pathway'));}
    if(prev)host.append(sideLink('Previous concept: '+prev.title,hrefDoc(prev.id,path.id),'Review the earlier step'));
    if(next)host.append(sideLink('Next concept: '+next.title,hrefDoc(next.id,path.id),'Continue the '+path.title+' route'));
    else if(c.related?.length){const r=bySlug.get(c.related[0]);if(r)host.append(sideLink('Related concept: '+r.title,hrefDoc(r.id,routeOf(r.slug)?.id),'Continue exploring'));}
    if(c.books?.length){const b=c.books[0];host.append(sideLink('Read deeper: Book '+b.book+' · Chapter '+b.chapter,hrefDoc(b.id,path?.id),b.title));}
  }
  function readDoc(id,section,from){
    const d=byId.get(id);if(!d){location.hash='discover';return;}
    if(current!==id){const hash=location.hash;if(!hash.startsWith('#doc='))previous=(!$('#results').hidden&&$('#search').value.trim())?'#q='+encodeURIComponent($('#search').value.trim()):(hash||'#browse');}
    const concept=catalog.find(x=>x.id===id);
    if(from&&PATHS.some(p=>p.id===from&&p.steps.includes(concept?.slug)))activePath=from;
    else if(concept&&!PATHS.some(p=>p.id===activePath&&p.steps.includes(concept.slug)))activePath=routeOf(concept.slug)?.id||null;
    current=id;addRecent(id);
    if(window.SEStudyV55)window.SEStudyV55.record(atlasUrl(id),d.title,kindLabel(d));
    const c=catalog.find(x=>x.id===id);
    $('#readingMeta').textContent=kindLabel(d)+(d.course?' · '+d.course:'');
    readingActions(d);
    const paper=$('#reader');paper.replaceChildren();
    const content=el('div','article-body');content.innerHTML=d.html||'<p>Open the original source for the complete document.</p>';
    paper.append(content);buildOutline(content);articleRelations(d,c);nextSteps(d,c);
    show('reading');
    requestAnimationFrame(()=>{
      const safe=String(section||'').replace(/[^A-Za-z0-9_-]/g,'');
      const target=safe?document.getElementById(safe):null;
      if(target)target.scrollIntoView();else $('#reading').scrollIntoView({block:'start'});
      if(window.MathJax?.typesetPromise)window.MathJax.typesetPromise([paper]).catch(()=>{});
    });
  }
  function savedList(){
    const blocks=[['#savedList',Object.keys(progress.saved)],['#recentList',progress.recent],['#studiedList',Object.keys(progress.done)]];
    for(const [id,ids] of blocks){const host=$(id);host.replaceChildren();
      const valid=ids.filter(i=>byId.has(i)).slice(0,30);
      if(!valid.length)host.append(el('p','micro','No resources here yet. Open an article and use Save or Mark studied.'));
      else valid.forEach(i=>host.append(readingMini(byId.get(i))));
    }
  }
  function route(){
    const frag=decodeURIComponent(location.hash.substring(1)||'discover');
    let args;try{args=new URLSearchParams(frag);}catch(e){args=new URLSearchParams('');}
    if(args.has('doc')){const id=args.get('doc');if(byId.has(id)){readDoc(id,args.get('section'),args.get('from'));return;}}
    if(args.has('q')){const q=args.get('q');$('#search').value=q;renderSearch(q);return;}
    if(args.has('path')){const p=PATHS.find(p=>p.id===args.get('path'));if(p){renderPath(p);requestAnimationFrame(()=>$('#pathview').scrollIntoView({block:'start'}));return;}}
    const viewName=['browse','paths','saved','discover'].includes(frag)?frag:'discover';
    current=null;
    if(viewName==='browse')renderBrowse();
    if(viewName==='paths')renderPaths();
    if(viewName==='saved')savedList();
    if(viewName==='discover')starterAndRecent();
    show(viewName);window.scrollTo(0,0);
  }
  function searchNow(){const q=$('#search').value.trim();searchLimit=10;
    if(q){renderSearch(q);}else{location.hash='discover';route();}
  }
  subjectButtons();renderBrowse();renderPaths();starterAndRecent();
  let searchTimer=null;
  $('#search').addEventListener('input',()=>{if(searchTimer)clearTimeout(searchTimer);searchTimer=setTimeout(searchNow,175);});
  $('#search').addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();const q=$('#search').value.trim();if(q)location.hash='q='+encodeURIComponent(q);}});
  $('#scope').addEventListener('change',()=>{if($('#search').value.trim())renderSearch($('#search').value.trim());});
  $('#clear').addEventListener('click',()=>{$('#search').value='';$('#scope').value='all';subject='all';letter='all';refreshFilters();location.hash='discover';route();$('#search').focus();});
  document.querySelectorAll('[data-example]').forEach(b=>b.addEventListener('click',()=>{const q=b.dataset.example;$('#search').value=q;location.hash='q='+encodeURIComponent(q);route();}));
  $('#more').addEventListener('click',()=>{searchLimit+=10;renderSearch($('#search').value.trim());});
  $('#back').addEventListener('click',()=>{location.hash=previous.startsWith('#doc=')?'browse':previous.slice(1);route();});
  $('#resetProgress').addEventListener('click',()=>{
    if(!window.confirm('Clear saved, studied, and recently opened resources on this browser?'))return;
    progress={done:{},saved:{},recent:[]};persist();savedList();starterAndRecent();renderPaths();
    $('#progressMessage').textContent='Encyclopedia-only markers cleared. Shared study desk markers can be cleared separately on the Study Desk.';
  });
  document.addEventListener('click', e=>{const a=e.target.closest?.('a[href^="#doc="]');if(!a||!$('#reading').hidden)return;if(!$('#results').hidden&&$('#search').value.trim()){previous='#q='+encodeURIComponent($('#search').value.trim());return;}previous=location.hash&&!location.hash.startsWith('#doc=')?location.hash:'#browse';});
  // Changing a hash view is equivalent to navigating to a new page for keyboard users.
  // Do not move focus on incremental search updates or internal article-outline jumps.
  function focusRoutedHeading(){
    if(location.hash.includes('&section='))return;
    const visible=['discover','paths','pathview','browse','results','reading','saved']
      .map(id=>document.getElementById(id)).find(x=>x&&!x.hidden);
    if(!visible)return;
    const heading=visible.querySelector('h1,h2');
    if(heading){heading.setAttribute('tabindex','-1');heading.focus({preventScroll:true});}
  }
  window.addEventListener('hashchange',()=>{route();requestAnimationFrame(focusRoutedHeading);});
  route();
})();
