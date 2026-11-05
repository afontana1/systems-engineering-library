"""v58 offline structural/link smoke audit. Run: python SE/INTERNAL/ACCESSIBILITY-STATIC-CHECKS-v58.py
Uses only the Python standard library. This is not a WCAG conformance test.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from collections import Counter
import json, sys
ROOT = Path(__file__).resolve().parents[1]
class AuditHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=[]; self.links=[]; self.inputs=[];self.labels=set()
        self.has_main=False;self.has_h1=False;self.has_lang=False;self.has_title=False;self.label_depth=0
    def handle_starttag(self, tag, attributes):
        a=dict(attributes)
        if tag=='html' and a.get('lang'):self.has_lang=True
        if tag=='main':self.has_main=True
        if tag=='h1':self.has_h1=True
        if tag=='title':self.has_title=True
        if tag=='label':
            self.label_depth+=1
            if a.get('for'):self.labels.add(a['for'])
        if a.get('id'):self.ids.append(a['id'])
        if tag=='input' and a.get('type','text').lower() not in {'hidden','submit','button'}:
            self.inputs.append((a.get('id'),bool(a.get('aria-label') or a.get('aria-labelledby') or self.label_depth)))
        if tag in {'a','link','script','img','source','iframe','video','audio'}:
            href=a.get('href') if tag in {'a','link'} else a.get('src')
            if href:self.links.append(href)
    def handle_endtag(self,tag):
        if tag=='label':self.label_depth=max(0,self.label_depth-1)

def audit():
    pages=list(ROOT.rglob('*.html'));total=Counter();issues={key:[] for key in ['missing_main','missing_h1','missing_lang','missing_title','duplicate_ids','unlabeled_inputs','broken_links','folder_only_links']}
    for path in pages:
        rel=path.relative_to(ROOT).as_posix();parser=AuditHTML()
        try:parser.feed(path.read_text(encoding='utf8'))
        except Exception as ex:issues['broken_links'].append(f'{rel}:parse:{ex}');continue
        total['pages']+=1
        for prop,key in [('has_main','missing_main'),('has_h1','missing_h1'),('has_lang','missing_lang'),('has_title','missing_title')]:
            if not getattr(parser,prop):issues[key].append(rel)
        if len(parser.ids)!=len(set(parser.ids)):issues['duplicate_ids'].append(rel)
        unnamed=[id or '(no id)' for id,named in parser.inputs if not named and id not in parser.labels]
        if unnamed:issues['unlabeled_inputs'].append(rel+': '+','.join(unnamed))
        for link in parser.links:
            u=urlsplit(link)
            if u.scheme or u.netloc or not u.path:continue
            target=(path.parent/unquote(u.path)).resolve()
            if not target.is_relative_to(ROOT):continue
            total['local_file_links']+=1
            if not target.exists():issues['broken_links'].append(f'{rel} => {link}')
            elif target.is_dir():issues['folder_only_links'].append(f'{rel} => {link}')
    return {'pages':len(pages),'checked_local_links':total['local_file_links'],'issue_counts':{k:len(v) for k,v in issues.items()},'examples':{k:v[:10] for k,v in issues.items() if v}}
if __name__=='__main__':
    result=audit();print(json.dumps(result,indent=2));sys.exit(int(any(result['issue_counts'].values())))
