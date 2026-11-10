/* Global library navigation: ordinary links, optional menus, no stored state. */
(() => {
  'use strict';
  const source = document.currentScript;
  if (!source) return;
  const root = source.getAttribute('data-se-root') || '';
  const page = source.getAttribute('data-se-page') || '';
  const mode = source.getAttribute('data-se-mode') || 'standard';
  const make = (tag, cls, value) => {
    const node = document.createElement(tag);
    if (cls) node.className = cls;
    if (value !== undefined) node.textContent = value;
    return node;
  };
  const link = (path, label, cls = '') => {
    const a = make('a', cls, label);
    a.href = root + path;
    if (page === path) a.setAttribute('aria-current', 'page');
    return a;
  };
  const nav = make('nav', 'se-nav');
  nav.id = 'se55-shell';
  nav.setAttribute('aria-label', 'Main library navigation');
  const skip = link('#se55-content', 'Skip to main content', 'se-skip');
  skip.href = '#se55-content';
  nav.append(skip);
  const top = make('div', 'se-toprow');
  top.append(link('../index.html', 'SE Library', 'se-brand'));
  const primary = make('div', 'se-primary');
  const items = [
    { name:'Concepts', path:'K/CONCEPTS.html', children:[
      ['K/CONCEPTS.html','Concept directory'],
      ['K/T/INDEX.html','Cross-course core concepts']
    ]},
    { name:'Subject Guides', path:'K/LEARNING-PATHWAYS.html', children:[
      ['K/LEARNING-PATHWAYS.html','Subject learning pathways'],
      ['K/LEARNER-JOURNEYS.html','Applied learning journeys']
    ]},
    { name:'Courses', path:'C/PROGRAM.html', children:[
      ['C/PROGRAM.html','All courses'],
      ['C/P0/OVERVIEW.html','Phase 0 · Foundations'],
      ['C/P1/OVERVIEW.html','Phase 1 · Modeling and software'],
      ['C/P2/OVERVIEW.html','Phase 2 · Design and integration'],
      ['C/P3/OVERVIEW.html','Phase 3 · Analytics and simulation'],
      ['C/P4/OVERVIEW.html','Phase 4 · Digital engineering'],
      ['C/P5/OVERVIEW.html','Phase 5 · Systems of systems']
    ]},
    { name:'Textbooks', path:'K/OPEN-BOOKS.html', children:[
      ['K/OPEN-BOOKS.html','All textbooks'],
      ['K/A/INDEX.html','Architecture, Models & Assurance'],
      ['K/Q/INDEX.html','Quantitative Systems Engineering'],
      ['K/G/INDEX.html','Advanced Systems Engineering Studies'],
      ['K/V/INDEX.html','Graduate Engineering Methods'],
      ['K/GS/INDEX.html','Graduate Textbook Studies']
    ]},
    { name:'Labs', path:'K/LAB-LIBRARY.html' },
    { name:'Encyclopedia', path:'K/U/OPEN-ENCYCLOPEDIA.html' }
  ];
  // Pages under a book and the cross-course concepts collection belong to their parent sections.
  const parent = /^K\/T\//.test(page) ? ['K/CONCEPTS.html','Concepts'] :
    /^K\/(?:B\d+|A|G|GS|Q|V)\//.test(page) ? ['K/OPEN-BOOKS.html','Textbooks'] :
    /^C\//.test(page) ? ['C/PROGRAM.html','Courses'] :
    /^K\/encyclopedia\//.test(page) ? ['K/CONCEPTS.html','Concepts'] :
    /^K\/U\//.test(page) ? ['K/U/OPEN-ENCYCLOPEDIA.html','Encyclopedia'] :
    ['../index.html','Library'];
  const panels = [];
  const closeMenus = (except) => panels.forEach(({button,panel}) => {
    if (panel !== except) { panel.hidden = true; button.setAttribute('aria-expanded','false'); }
  });
  for (const item of items) {
    const group = make('div','se-menu');
    const current = page === item.path || (parent[0] === item.path && page !== 'index.html');
    group.append(link(item.path, item.name, current ? 'se-current' : ''));
    if (item.children) {
      const button = make('button','se-drop','▾');
      button.type='button';
      button.setAttribute('aria-label','Show '+item.name+' options');
      button.setAttribute('aria-expanded','false');
      const panel = make('div','se-submenu');
      panel.hidden = true;
      for (const [path,label] of item.children) panel.append(link(path,label));
      button.addEventListener('click',() => {
        const opening=panel.hidden;
        closeMenus();
        panel.hidden=!opening;
        if (opening && window.innerWidth <= 540) {
          const bottom = Math.max(0, nav.getBoundingClientRect().bottom);
          panel.style.top = Math.round(bottom + 4) + 'px';
          panel.style.maxHeight = 'calc(100vh - ' + Math.round(bottom + 12) + 'px)';
        } else {
          panel.style.removeProperty('top');
          panel.style.removeProperty('max-height');
        }
        button.setAttribute('aria-expanded', String(opening));
      });
      group.append(button,panel);
      panels.push({button,panel});
    }
    primary.append(group);
  }
  top.append(primary);
  nav.append(top);
  const landing = ['K/CONCEPTS.html','K/OPEN-BOOKS.html','K/LEARNING-PATHWAYS.html','K/LEARNER-JOURNEYS.html','K/LAB-LIBRARY.html','C/PROGRAM.html'];
  if (mode !== 'atlas' && mode !== 'home' && page !== 'index.html' && !landing.includes(page) && parent[0] !== page) {
    const context = make('div','se-context');
    const trail = make('div','se-trail');
    trail.append(link(parent[0],parent[1]),make('span','',' / '+(document.title||'Reading')));
    context.append(trail);
    nav.append(context);
  }
  document.addEventListener('click',e => { if(!nav.contains(e.target)) closeMenus(); });
  nav.addEventListener('keydown',e => {if(e.key==='Escape') { closeMenus(); e.target.closest('.se-menu')?.querySelector('.se-drop')?.focus(); }});
  const content = document.querySelector('main') || document.querySelector('#article') || document.querySelector('article') || document.querySelector('.layout');
  if (content && !content.id) content.id='se55-content';
  else if (content) skip.href='#'+content.id;
  else skip.href='#se55-shell';
  document.body.insertBefore(nav, document.body.firstChild);
})();
