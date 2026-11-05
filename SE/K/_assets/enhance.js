/* Offline math and code presentation. Mathematical expressions are converted only
   in visible reading content, never in code, scripts, or embedded document data. */
(()=>{'use strict';
 const skip='pre,code,script,style,textarea,kbd,samp,mjx-container,svg,.se-no-math';
 let inflight=false, pending=false;
 const roots=()=>{
   // One active reading surface. Do not typeset its ancestors as well.
   const active=document.querySelector('#workspace .doccontent');
   if(active)return [active];
   const single=document.querySelector('#article')||document.querySelector('#reader')||document.querySelector('.reader')||document.querySelector('#workspace')||document.querySelector('main');
   return single?[single]:[];
 };
 function mathCandidates(raw){
   if(!raw||(!raw.includes('$')&&!raw.includes('\\(')&&!raw.includes('\\[')))return raw;
   // Convert dollar-delimited TeX to MathJax's unambiguous delimiters.
   // Dollar amounts such as $7.2M are not mathematical delimiters.
   let s=raw;
   // Some Markdown renderers consumed the backslashes around display math,
   // leaving a paragraph containing [ newline TeX newline ]. Restore them.
   s=s.replace(/^\s*\[\s*\n([\s\S]*?)\n\s*\]\s*$/g,(full,tex)=>
     /\\[A-Za-z]+|[_^]\{?/.test(tex)?`\\[${tex.trim()}\\]`:full);
   s=s.replace(/\$\$([\s\S]*?)\$\$/g,(full,tex)=>tex.trim()?`\\[${tex.trim()}\\]`:full);
   s=s.replace(/(?<!\\)\$(?!\$)([^\n$]{1,700}?)\$(?!\$)/g,(full,tex)=>{
     if(/^\s*[0-9]/.test(tex)||!tex.trim()||/\$/.test(tex)) return full;
     if(/\b(?:USD|million|dollars)\b/i.test(tex))return full;
     return `\\(${tex.trim()}\\)`;
   });
   return s;
 }
 function prepare(root){
   // Unified encyclopedia stored block TeX as <div class=math-display><code>…</code></div>.
   // Replace that non-executable code wrapper with genuine MathJax delimiters.
   root.querySelectorAll('.math-display:not([data-se-equation])').forEach(el=>{
     const raw=el.textContent.trim();if(!raw)return;
     el.dataset.seEquation='1';el.textContent='\\['+raw+'\\]';
   });
   root.querySelectorAll('.math-inline:not([data-se-equation])').forEach(el=>{
     const raw=el.textContent.trim();if(!raw)return;
     el.dataset.seEquation='1';el.textContent='\\('+raw+'\\)';
   });
   const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);const changes=[];
   while(walker.nextNode()){
     const n=walker.currentNode,p=n.parentElement;
     if(!p||p.closest(skip))continue;
     const t=n.nodeValue;
     if(t&&(t.includes('$')||t.includes('\\(')||t.includes('\\['))){const next=mathCandidates(t);if(next!==t)changes.push([n,next]);}
   }
   for(const [n,s] of changes)n.nodeValue=s;
   return changes.length;
 }
 function code(root){
   if(!window.Prism)return;
   root.querySelectorAll('pre code:not([data-se-code])').forEach(c=>{
     c.dataset.seCode='1';
     if(!/language-\w+/.test(c.className)){
       if(/\b(def |import |from |class |if __name__)/.test(c.textContent))c.classList.add('language-python');
       else c.classList.add('language-none');
     }
     try{window.Prism.highlightElement(c)}catch(e){}
   });
 }
 async function enhance(){
   if(inflight){pending=true;return;}
   inflight=true;
   try{
     if(window.MathJax&&window.MathJax.startup)await window.MathJax.startup.promise;
     for(const root of roots()){
       prepare(root);code(root);
       if(window.MathJax?.typesetPromise){
         // Require an unrendered math delimiter in a non-code text node.
         let hasFormula=false;const scan=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
         while(scan.nextNode()){
           const node=scan.currentNode;
           if(node.parentElement?.closest(skip))continue;
           if(node.nodeValue?.includes('\\(')||node.nodeValue?.includes('\\[')){hasFormula=true;break;}
         }
         if(hasFormula){
           try{await window.MathJax.typesetPromise([root]);}catch(e){console.warn('Equation rendering issue',e)}
         }
       }
     }
   }finally{inflight=false;if(pending){pending=false;setTimeout(enhance,120)}}
 }
 function init(){
   window.SEEnhance=enhance;
   let timer;
   const target=document.querySelector('#article')||document.querySelector('#workspace')||document.querySelector('#reader')||document.querySelector('main')||document.body;
   const obs=new MutationObserver(muts=>{
     let changed=false;
     for(const m of muts){for(const n of m.addedNodes){
       if(n.nodeType===1){
         if(n.closest?.('mjx-container')||n.matches?.('mjx-container,svg,path,defs,use'))continue;
         if(n.querySelector?.('mjx-container')&&!n.textContent.includes('$')&&!n.textContent.includes('\\('))continue;
         if(n.matches?.('code,span.token'))continue;
         changed=true;break;
       }else if(n.nodeType===3&&/[\\$]/.test(n.textContent||'')){changed=true;break;}
     }if(changed)break;}
     if(changed){clearTimeout(timer);timer=setTimeout(enhance,140)}
   });
   obs.observe(target,{childList:true,subtree:true});
   enhance();
 }
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})();
