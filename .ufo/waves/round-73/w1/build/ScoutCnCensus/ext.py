import sys,re,html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.o=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style'): s.skip+=1
        if t in('p','div','li','br','tr','h1','h2','h3','h4','pre','code','td','th'): s.o.append('\n') if t!='code' else None
    def handle_endtag(s,t):
        if t in('script','style'): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.o.append(d)
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
p=P(); p.feed(t); print(html.unescape(''.join(p.o)))
