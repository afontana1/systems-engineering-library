#!/usr/bin/env python3
"""Systems Engineering Library v59 offline learning-journey checks.

Run: python SE/INTERNAL/LEARNER-JOURNEY-CHECKS-v59.py
Stdlib only; checks static references and generated navigation, not native browser behavior.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, parse_qs
from collections import Counter
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=set(); self.links=[]; self.main=0; self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.add(a['id'])
        if tag=='a' and a.get('name'):self.ids.add(a['name'])
        if tag=='main':self.main+=1
        if tag=='h1':self.h1+=1
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if tag in ('script','link','img'):
            u=a.get('src') or (a.get('href') if tag=='link' else '')
            if u:self.links.append(u)

def fail(msg):
    print('FAIL:',msg)
    return msg

def main():
    errors=[]
    pages={}
    links=[]
    for file in ROOT.rglob('*.html'):
        name=file.relative_to(ROOT).as_posix()
        p=Page();p.feed(file.read_text(encoding='utf-8',errors='replace'))
        pages[name]=p
        for h in p.links:links.append((name,h))
    if not (ROOT/'K/LEARNER-JOURNEYS.html').exists():errors.append(fail('Journey guide missing'))
    if not (ROOT/'K/LEARNER-JOURNEYS-v59.json').exists():errors.append(fail('Journey manifest missing'))

    labpage=(ROOT/'K/LAB-LIBRARY.html').read_text(encoding='utf-8')
    labmatch=re.search(r'<script\b[^>]*\bid="file-data"[^>]*>(.*?)</script>',labpage,re.I|re.S)
    if not labmatch:errors.append(fail('Lab catalog data missing'));labpaths=set()
    else:labpaths={x['path'] for x in json.loads(labmatch.group(1))}
    corpus=(ROOT/'K/U/OPEN-ENCYCLOPEDIA.html').read_text(encoding='utf-8')
    m=re.search(r'<script\b[^>]*\bid="corpus"[^>]*>(.*?)</script>',corpus,re.I|re.S)
    if not m:errors.append(fail('Encyclopedia corpus missing'));docids=set()
    else:docids={x['id'] for x in json.loads(m.group(1))['docs']}

    valid=0; dynamic_lab=0; dynamic_atlas=0; missing_targets=[];missing_anchors=[]
    for source,h in links:
        if not h or h.startswith(('mailto:','data:','javascript:','tel:','//')):continue
        parts=urlsplit(h)
        if parts.scheme or parts.netloc:continue
        dest=(ROOT/source).parent.joinpath(unquote(parts.path)).resolve() if parts.path else (ROOT/source).resolve()
        if not dest.is_relative_to(ROOT):continue
        dest_name=dest.relative_to(ROOT).as_posix()
        if not dest.is_file():
            missing_targets.append((source,h));continue
        valid+=1
        fragment=unquote(parts.fragment)
        if not fragment or dest_name not in pages:continue
        if dest_name=='K/LAB-LIBRARY.html' and fragment in labpaths:
            dynamic_lab+=1;continue
        if dest_name=='K/U/OPEN-ENCYCLOPEDIA.html':
            if fragment in ('discover','saved','paths','browse'):
                dynamic_atlas+=1;continue
            args=parse_qs(fragment)
            if 'q' in args or 'path' in args:
                dynamic_atlas+=1;continue
            if 'doc' in args and args['doc'][0] in docids:
                dynamic_atlas+=1;continue
        if fragment not in pages[dest_name].ids:
            missing_anchors.append((source,h))
    if missing_targets:errors.append(fail(f'{len(missing_targets)} missing local targets: {missing_targets[:5]}'))
    if missing_anchors:errors.append(fail(f'{len(missing_anchors)} broken local fragment links: {missing_anchors[:5]}'))

    guide=json.loads((ROOT/'K/LEARNER-JOURNEYS-v59.json').read_text())
    journeys=guide['journeys']
    if len(journeys)!=6 or len({x['id'] for x in journeys})!=6:errors.append(fail('Journey cardinality/ID mismatch'))
    missing_steps=[]
    for j in journeys:
        if len(j['steps'])!=4:errors.append(fail('Journey '+j['id']+' does not have four learning steps'))
        if [x['kind'] for x in j['steps']]!=['Concept','Concept','Textbook','Practice']:
            errors.append(fail('Unexpected concept → chapter → lab sequence in '+j['id']))
        for st in j['steps']:
            parts=urlsplit(st['path']);dest=ROOT/parts.path
            if not dest.is_file():missing_steps.append((j['id'],st['path']))
            if parts.fragment and parse_qs(parts.fragment).get('doc',[''])[0] not in docids:
                errors.append(fail('Journey concept ID missing: '+st['path']))
    if missing_steps:errors.append(fail('Broken journey steps '+str(missing_steps[:5])))
    if len([p for p in pages.values() if not p.h1])!=0:errors.append(fail('New missing h1 document'))
    if len([p for p in pages.values() if not p.main])!=0:errors.append(fail('New missing main document'))
    result={'release':'v59','html_pages_checked':len(pages),'relative_targets_resolved':valid,
            'dynamic_lab_fragments_verified':dynamic_lab,'dynamic_atlas_fragments_verified':dynamic_atlas,
            'broken_local_targets':len(missing_targets),'broken_local_fragments':len(missing_anchors),
            'journeys':len(journeys),'steps':sum(len(j['steps']) for j in journeys),
            'main_landmark_missing':sum(not p.main for p in pages.values()),
            'h1_missing':sum(not p.h1 for p in pages.values()),'errors':errors}
    print(json.dumps(result,indent=2))
    return 1 if errors else 0

if __name__=='__main__':sys.exit(main())
