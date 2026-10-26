import re,subprocess,sys,textwrap
P=open('/tmp/k73-scd-P.txt').read().strip()+'/kotoba-shokunin'
src=open(P+'/SKILL.md').read().split('\n')
front=src[:19]  # lines 1-19
assert front[0]=='---' and front[18]=='---'
body=src[19:]
D0=re.sub(r'\s+',' ',' '.join(front[3:18])).strip()
print(len(D0))
OLD1="Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts for trigger fidelity and decision density."
assert D0.startswith(OLD1)
REST=D0[len(OLD1):].strip()
cands={
 'c1':('Prompt and skill craft: "write a skill", "audit this skill", "prompt craft".',
       'Audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts for trigger fidelity and decision density.'),
 'c2':('Audit or write a skill or prompt: "skill file", "write a skill".',
       'Audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts for trigger fidelity and decision density.'),
 'c3':('Write and audit skill and prompt files: "SKILL.md", dispatch prompts, AGENTS.md.',
       'Audits and rewrites them for trigger fidelity and decision density.'),
}
def first_sentence(D):
    m=re.search(r'(\. |: )(?=[A-Z])',D)
    return D[:m.start()+ (1 if m.group(1)=='. ' else 0)] if m and m.start()+1<=99 else D[:99]
def mk(c):
    a,b=cands[c]; D=(a+' '+b+' '+REST)
    return D
def wrap(D,width=78):
    # fold greedily into exactly 15 lines when possible: lines 4..18
    return textwrap.wrap(D,width=width-2,break_long_words=False,break_on_hyphens=False)
for c in cands:
    D=mk(c); print(c,'len D',len(D),'first',repr(first_sentence(D)),len(first_sentence(D)))

cands['c1']=('Skill and prompt craft: "write a skill", "audit this skill".','Audits and rewrites SKILL.md, AGENTS.md and dispatch prompts for trigger fidelity.')
cands['c2']=(cands['c2'][0],'Audits and rewrites SKILL.md, AGENTS.md, dispatch and system prompts for trigger fidelity.')
import os,json
res={}
for c in cands:
    D=mk(c)
    lines=None
    for w in range(60,92):
        L=textwrap.wrap(D,width=w,break_long_words=False,break_on_hyphens=False)
        if len(L)==15: lines=L;wd=w;break
    assert lines, (c,len(D))
    fm=['---','name: kotoba-shokunin','description: >']+['  '+l for l in lines]+['---']
    assert len(fm)==19
    new=fm+body
    out=P+'/SKILL.md'
    open('/tmp/k73-scd-%s.SKILL.md'%c,'w').write('\n'.join(new))
    res[c]=dict(len=len(D),first=first_sentence(D),flen=len(first_sentence(D)),width=wd,maxline=max(len(x) for x in fm))
    print(c,res[c])
json.dump(res,open('/tmp/k73-scd-res.json','w'))
