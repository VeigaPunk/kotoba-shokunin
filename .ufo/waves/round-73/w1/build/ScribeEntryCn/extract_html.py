import sys,re,html,unicodedata
from html.parser import HTMLParser
class T(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in ('script','style','noscript','svg'): s.skip+=1
        if t in ('p','div','li','tr','br','h1','h2','h3','h4','pre','table','section','article'): s.out.append('\n')
        if t in ('td','th'): s.out.append(' | ')
        if t=='code': s.out.append('`')
    def handle_endtag(s,t):
        if t in ('script','style','noscript','svg') and s.skip: s.skip-=1
        if t=='code': s.out.append('`')
        if t in ('p','div','li','tr','h1','h2','h3','h4','pre'): s.out.append('\n')
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
for name in sys.argv[1:]:
    src=open('raw/'+name,'rb').read().decode('utf-8','replace')
    if name.endswith('.md'): txt=src
    else:
        p=T(); p.feed(src); txt=''.join(p.out)
    txt=re.sub(r'[ \t]+',' ',txt)
    txt=re.sub(r'\n{3,}','\n\n',txt)
    open('txt/'+name+'.txt','w').write(txt)
    print(name, len(txt.encode()), txt.count('\n'))
