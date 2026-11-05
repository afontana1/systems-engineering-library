/* v55: Accessible shared navigation and study continuity. Local-only; no network, fetch, cookies, or tracking. */
(()=>{'use strict';
 const script=document.currentScript;
 if(!script)return;
 const page=script.getAttribute('data-se-page')||'';
 const root=script.getAttribute('data-se-root')||'';
 const shellMode=script.getAttribute('data-se-mode')||'standard';
 const index=window.SELearningMapV55||{};
 const info=index[page]||{title:document.title||page,kind:'Resource',parent:'START-HERE.html'};
 const DBKEY='se_library_study_v55';
 const MAXRECENT=35;
 const E=(t,c,txt)=>{const x=document.createElement(t);if(c)x.className=c;if(txt!==undefined)x.textContent=txt;return x;};
 const fileHref=k=>root+k;
 const title=k=>index[k]?.title||k.split('/').pop().replace(/\.html$/,'').replace(/[-_]/g,' ');
 const normalize=x=>x&&typeof x==='object'?x:{};
 const initial=()=>({recent:[],saved:{},done:{}});
 function load(){try{const data=normalize(JSON.parse(localStorage.getItem(DBKEY)||'null'));return {recent:Array.isArray(data.recent)?data.recent.filter(x=>x&&typeof x.url==='string').slice(0,MAXRECENT):[],saved:normalize(data.saved),done:normalize(data.done)};}catch(e){return initial();}}
 let db=load();
 function save(){try{localStorage.setItem(DBKEY,JSON.stringify(db));}catch(e){} }
 function entry(url,name,kind){return {url,title:String(name||url).slice(0,180),kind:String(kind||'Reading').slice(0,60)}};
 function record(url,name,kind){
  if(!url)return;
  let key=String(url);
  if(!key.startsWith('K/')&&!key.startsWith('C/')&&!key.startsWith('START-HERE'))return;
  const v=entry(key,name,kind);
  db.recent=[v,...db.recent.filter(x=>x.url!==key)].slice(0,MAXRECENT);save();updateUI();
 }
 const isSaved=url=>!!db.saved[url],isDone=url=>!!db.done[url];
 function toggle(prop,url,name,kind){
  const was=!!db[prop][url];if(was)delete db[prop][url];else db[prop][url]=entry(url,name,kind);
  save();updateUI();
  if(status)status.textContent=(prop==='saved'?(was?'Removed from saved items: ':'Saved for later: '):(was?'Unmarked studied: ':'Marked studied: '))+String(name||url);
 }
 // Shared API: encyclopedia records the specific #doc= item rather than only the atlas landing page.
 window.SEStudyV55={record,toggle,reset:()=>{db=initial();save();updateUI();},load:()=>load(),url:fileHref};
 function link(key,lab){const a=E('a','',lab===undefined?title(key):lab);a.href=fileHref(key);return a;}
 function displayItems(host,items,empty){host.replaceChildren();if(!items.length){host.append(E('p','',empty));return;}
  const ul=E('ul');items.slice(0,7).forEach(it=>{const li=E('li');li.append(link(it.url,it.title),E('span','',it.kind));ul.append(li);});host.append(ul);
 }
 let bar=null,bookmark=null,studied=null,studyButton=null,drawer=null,status=null;
 function updateUI(){if(bookmark){bookmark.textContent=isSaved(page)?'★ Saved':'☆ Save';bookmark.setAttribute('aria-pressed',String(isSaved(page)));}
  if(studied){studied.textContent=isDone(page)?'✓ Studied':'Mark studied';studied.setAttribute('aria-pressed',String(isDone(page)));}
  if(studyButton){studyButton.textContent='Study list ('+Object.keys(db.saved).length+')';}
  if(drawer&&!drawer.hidden)refreshDrawer();
  if(page==='START-HERE.html')mountHome();
 }
 function refreshDrawer(){if(!drawer)return;drawer.replaceChildren();drawer.append(E('h2','', 'Continue learning'));
  const recent=E('div');displayItems(recent,db.recent.filter(it=>it.url!==page), 'No previously opened resources yet.');drawer.append(recent);
  drawer.append(E('h2','', 'Saved for later'));
  const saved=E('div');displayItems(saved,Object.values(db.saved),'No saved pages yet. Use ☆ Save while reading.');drawer.append(saved);
  const bottom=E('div','se55-drawer-bottom');bottom.append(link('K/STUDY-DESK.html','Open study desk'),link('K/U/OPEN-ENCYCLOPEDIA.html#saved','Encyclopedia study list'),link('K/ACCESSIBILITY-HELP.html','Keyboard and accessibility help'));drawer.append(bottom);
  drawer.append(E('p','se55-badge','Progress is stored only in this browser, when local storage is available.'));
 }
 function mountHome(){const anchor=document.querySelector('#find-learning')||document.querySelector('main');if(!anchor)return;
  let panel=document.querySelector('#se55-home-resume');if(!panel){panel=E('section','se55-home-resume');panel.id='se55-home-resume';anchor.insertAdjacentElement('afterend',panel);}
  panel.replaceChildren();panel.append(E('h2','', 'Continue where you left off'));
  if(db.recent.length){let first=db.recent.find(x=>x.url!=='START-HERE.html');if(first){const p=E('p');p.append(link(first.url,first.title));panel.append(p);}}
  else panel.append(E('p','','Your recent reading will appear here after you open a chapter, lesson, lab, or encyclopedia concept.'));
  let foot=E('p');foot.append(link('K/STUDY-DESK.html','Open your study desk'),document.createTextNode(' · '+Object.keys(db.saved).length+' saved · '+Object.keys(db.done).length+' marked studied'));panel.append(foot);
 }
 if(shellMode==='home'){
  const main=document.querySelector('main');
  if(main&&!main.id)main.id='se58-home-content';
  if(main&&!document.querySelector('.se58-home-skip')){
   const s=E('a','se58-home-skip','Skip to learning choices');s.href='#'+main.id;
   document.body.insertBefore(s,document.body.firstChild);
  }
  mountHome();return;
 }
 if(shellMode==='atlas'){
  const recordDeepLink=()=>{const match=location.hash.match(/^#doc=([^&]+)/);if(!match)return;
   let id='';try{id=decodeURIComponent(match[1]);}catch(e){return;}
   const display=document.querySelector('#reader h1')?.textContent?.trim()||'Encyclopedia reference';
   record('K/U/OPEN-ENCYCLOPEDIA.html#doc='+encodeURIComponent(id),display,'Concept / resource');};
  recordDeepLink();window.addEventListener('hashchange',()=>setTimeout(recordDeepLink,80));return;
 }
 if(page==='K/STUDY-DESK.html'){/* the study desk populates itself after the shell is ready */}
 const nav=E('nav');nav.id='se55-shell';nav.setAttribute('aria-label','Unified learning library navigation');bar=nav;
 const skip=E('a','se55-skip','Skip to learning content');skip.href='#se55-content';nav.append(skip);
 const top=E('div','se55-row');
 const brand=link('START-HERE.html','');brand.className='se55-brand';const brandmark=E('span','', 'SE');brand.append(brandmark,document.createTextNode('Learning library'));top.append(brand);
 const links=E('div','se55-primary');[['K/U/OPEN-ENCYCLOPEDIA.html','Encyclopedia'],['K/OPEN-BOOKS.html','Textbooks'],['C/PROGRAM.html','Courses'],['K/LAB-LIBRARY.html','Labs']].forEach(([k,v])=>links.append(link(k,v)));top.append(links);
 const form=E('form','se55-global-search'),input=E('input');input.setAttribute('aria-label','Search all library resources');input.type='search';input.placeholder='Find a topic…';input.maxLength=180;form.append(input);const go=E('button','', 'Search');go.type='submit';form.append(go);
 form.addEventListener('submit',ev=>{ev.preventDefault();if(input.value.trim())location.href=fileHref('K/U/OPEN-ENCYCLOPEDIA.html#q='+encodeURIComponent(input.value.trim()));});top.append(form);
 studyButton=E('button','se55-study');studyButton.type='button';studyButton.setAttribute('aria-expanded','false');studyButton.setAttribute('aria-controls','se55-study-drawer');studyButton.setAttribute('aria-haspopup','true');top.append(studyButton);nav.append(top);
 const context=E('div','se55-row se55-context'),where=E('div','se55-where');
 if(info.parent&&info.parent!==page){where.append(link(info.parent,title(info.parent)),document.createTextNode(' / '));}
 where.append(E('span','',info.title.length>85?info.title.slice(0,85)+'…':info.title));context.append(where);
 const actions=E('div','se55-actions');
 if(info.prev)actions.append(link(info.prev,'← Previous'));
 if(info.next){const l=link(info.next,'Next →');l.className='se55-prevnext';actions.append(l);}
 if(info.related?.length){const l=link(info.related[0],info.kind==='Concept reference'?'Related concept':'Companion resource');l.className='se55-secondary-link';actions.append(l);}
 if(info.kind==='Textbook chapter'&&info.book){const l=link('K/B'+info.book+'/OPEN-BOOK.html','Full book');l.className='se55-secondary-link';actions.append(l);}
 if(!['Study desk','Textbook catalog','Lab catalog','Program guide','Phase guide'].includes(info.kind)){
 bookmark=E('button','se55-smallbutton');bookmark.type='button';bookmark.addEventListener('click',()=>toggle('saved',page,info.title,info.kind));actions.append(bookmark);
 studied=E('button','se55-smallbutton');studied.type='button';studied.addEventListener('click',()=>toggle('done',page,info.title,info.kind));actions.append(studied);
 }
 context.append(actions);nav.append(context);
 drawer=E('section','se55-drawer');drawer.id='se55-study-drawer';drawer.hidden=true;drawer.setAttribute('aria-label','Recent and saved study items');drawer.setAttribute('role','region');drawer.setAttribute('tabindex','-1');nav.append(drawer);
 studyButton.addEventListener('click',()=>{
  const opening=drawer.hidden;drawer.hidden=!opening;
  studyButton.setAttribute('aria-expanded',String(opening));
  if(opening){refreshDrawer();drawer.focus({preventScroll:true});}
  else studyButton.focus();
 });
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!drawer.hidden){drawer.hidden=true;studyButton.setAttribute('aria-expanded','false');studyButton.focus();}
  if(e.key==='/'&&!e.ctrlKey&&!e.altKey&&!e.metaKey&&!e.shiftKey&&!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement?.tagName)&&!document.activeElement?.isContentEditable){e.preventDefault();input.focus();}
 });
 document.addEventListener('click',e=>{if(!drawer.hidden&&!nav.contains(e.target)){drawer.hidden=true;studyButton.setAttribute('aria-expanded','false');}});
 const contentTarget=document.querySelector('main')||document.querySelector('#article')||document.querySelector('article')||document.querySelector('.layout')||document.querySelector('header');
 if(contentTarget&&!contentTarget.id)contentTarget.id='se55-content';else if(contentTarget)skip.href='#'+contentTarget.id;else skip.href='#se55-shell';
 status=E('div','se58-status');status.setAttribute('role','status');status.setAttribute('aria-live','polite');status.setAttribute('aria-atomic','true');nav.append(status);
 document.body.insertBefore(nav,document.body.firstChild);
 if(page!=='K/STUDY-DESK.html')record(page,info.title,info.kind);
 updateUI();
 // For book readers, the native reader's chapter selection is separate from the standalone-page study state.
 if(info.kind==='Textbook reader'){
  const note=E('a','se55-badge','Want to resume an individual chapter? Open its standalone chapter page.');
  note.href=fileHref('K/B'+info.book+'/README.html');note.style.display='none';
 }
})();


/* v59: Optional learner-journey context, shared by encyclopedia, chapter, lab, and study-desk pages. */
(()=>{'use strict';
 const source=document.currentScript; if(!source)return;
 const root=source.getAttribute('data-se-root')||'';
 const page=source.getAttribute('data-se-page')||'';
 const journeys=[{"id":"needs","title":"From stakeholder need to testable requirements","steps":[{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=d8e1de722acc0","label":"Define the system and its boundaries"},{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=da9595994eeb3","label":"Separate stakeholder claims from measurable needs"},{"path":"K/B1/chapters/03-needs-and-conops.html","label":"Read the operational-concept chapter"},{"path":"K/B1/labs/lab-03-stakeholder-hearing.html","label":"Apply it in the Stakeholder Hearing"}]},{"id":"safety","title":"From hazard to defensible assurance claim","steps":[{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=d829e15a0d4cb","label":"Understand hazards and required controls"},{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=de50b71ae3099","label":"Build a claim–argument–evidence chain"},{"path":"K/B8/chapters/10-analyze-results-determine-evidence-sufficiency-and-reco.html","label":"Read about evidence sufficiency"},{"path":"K/B8/labs/lab-10-analyze-results-determine-evidence-sufficiency-and-reco.html","label":"Test an evidence-sufficiency decision"}]},{"id":"simulation","title":"From simulation results to credible decisions","steps":[{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=db8eae7a8e3ee","label":"Define the modeling purpose and assumptions"},{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=d4b5e67dcb0f2","label":"Separate implementation verification from validation"},{"path":"K/B11/chapters/09-apply-simulation-in-design-and-development-using-selection-ranking-a.html","label":"Read about using simulation for design decisions"},{"path":"K/B11/labs/lab-09-apply-simulation-in-design-and-development-using-selection-ranking-a.html","label":"Challenge the simulation evidence"}]},{"id":"trade","title":"From trade study to robust choice","steps":[{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=d39ba99b7db20","label":"Frame objectives and constrained alternatives"},{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=ddd706e06cd3d","label":"Challenge the choice under uncertainty"},{"path":"K/B14/chapters/11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.html","label":"Read robustness, regret and information value"},{"path":"K/B14/labs/lab-11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.html","label":"Stress-test a decision"}]},{"id":"interfaces","title":"From interface definition to integration evidence","steps":[{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=dda682f83cc9d","label":"Define a testable interface contract"},{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=d922e041d8ca8","label":"Preserve configuration and test provenance"},{"path":"K/B7/chapters/04-mature-the-physical-architecture-interfaces-and-perform.html","label":"Read the physical-interface design chapter"},{"path":"K/B7/labs/lab-04-mature-the-physical-architecture-interfaces-and-perform.html","label":"Practice contract review"}]},{"id":"mbse","title":"From architecture views to allocation evidence","steps":[{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=db3032ecc2404","label":"Choose the model semantics"},{"path":"K/U/OPEN-ENCYCLOPEDIA.html#doc=d7c6c77e3a16d","label":"Trace engineering claims across models"},{"path":"K/B3/chapters/07-logical-architecture-functional-allocation-de.html","label":"Read functional allocation in MBSE"},{"path":"K/B3/labs/lab-07-logical-architecture-functional-allocation-de.html","label":"Critique an architecture allocation"}]}];
 const key='se_active_learning_journey_v59';
 const read=()=>{try{const x=JSON.parse(localStorage.getItem(key)||'null');return x&&journeys.some(j=>j.id===x.id)?x:null;}catch(e){return null;}};
 const activate=(id,step)=>{try{localStorage.setItem(key,JSON.stringify({id,step:Number(step)||0}));}catch(e){}};
 const E=(t,c,v)=>{const e=document.createElement(t);if(c)e.className=c;if(v)e.textContent=v;return e;};
 const base=x=>x.split('#')[0];
 // Journeys are opt-in. Only clicking a numbered step activates the reading companion.
 document.addEventListener('click',e=>{const a=e.target.closest?.('a[data-v59-journey]');if(a)activate(a.dataset.v59Journey,a.dataset.v59Step);});
 function currentPath(){
  if(page==='K/U/OPEN-ENCYCLOPEDIA.html')return page+location.hash;
  return page;
 }
 function render(){
  const prior=document.getElementById('se59-journey-companion');if(prior)prior.remove();
  const state=read();if(!state)return;
  const j=journeys.find(x=>x.id===state.id);if(!j)return;
  const url=currentPath();const step=j.steps.findIndex(s=>s.path===url||base(s.path)===url&&url!=='K/U/OPEN-ENCYCLOPEDIA.html');
  // Atlas #doc links are checked exactly, so an unrelated search is not mistaken for a journey step.
  if(step<0)return;
  if(step!==state.step)activate(j.id,step);
  const next=j.steps[step+1],panel=E('aside','se59-journey-companion');panel.id='se59-journey-companion';panel.setAttribute('aria-label','Current learning journey');
  panel.append(E('span','se59-journey-step','LEARNING JOURNEY · '+(step+1)+' OF '+j.steps.length));
  const copy=E('span','se59-journey-copy',j.title);panel.append(copy);
  const links=E('span','se59-journey-links');const back=E('a','', 'All journey steps');back.href=root+'K/LEARNER-JOURNEYS.html#journey-'+j.id;links.append(back);
  if(next){const go=E('a','', 'Next: '+next.label);go.href=root+next.path;go.addEventListener('click',()=>activate(j.id,step+1));links.append(go);}
  else {const desk=E('a','','Review on study desk');desk.href=root+'K/STUDY-DESK.html';links.append(desk);}
  panel.append(links);
  const nav=document.getElementById('se55-shell');
  if(nav)nav.insertAdjacentElement('afterend',panel);
  else{const main=document.querySelector('#workspace')||document.querySelector('main');if(main)main.insertAdjacentElement('afterbegin',panel);}
 }
 function insertStyle(){if(document.querySelector('#se59-journey-style'))return;
  const style=E('style');style.id='se59-journey-style';style.textContent='.se59-journey-companion{max-width:1200px;margin:12px auto;padding:11px 17px;border:1px solid #bdd9d4;background:#eff8f5;color:#194a50;border-radius:10px;display:flex;align-items:center;gap:10px 18px;flex-wrap:wrap;font:14px/1.45 system-ui,Segoe UI,sans-serif}.se59-journey-step{font-size:11px;letter-spacing:.07em;font-weight:800;color:#2e7471}.se59-journey-copy{font-weight:750}.se59-journey-links{margin-left:auto;display:flex;gap:15px;flex-wrap:wrap}.se59-journey-links a{color:#116a71;text-decoration:underline;font-weight:700}.se59-journey-links a:focus-visible{outline:3px solid #ba7828;outline-offset:3px}@media(max-width:650px){.se59-journey-companion{margin:8px 10px}.se59-journey-links{margin-left:0}}';document.head.append(style);}
 insertStyle();render();if(page==='K/U/OPEN-ENCYCLOPEDIA.html')window.addEventListener('hashchange',render);
 if(page==='K/STUDY-DESK.html'){const active=read();if(active){const j=journeys.find(x=>x.id===active.id),host=document.querySelector('main .actions');if(j&&host){const a=E('a','','Resume journey: '+j.title);a.href=root+'K/LEARNER-JOURNEYS.html#journey-'+j.id;host.prepend(a);}}}
})();
