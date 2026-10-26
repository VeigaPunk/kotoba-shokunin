import re, json
entry = open('/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/chinese-client-skill-surfaces.md', encoding='utf-8').read().splitlines()
rows = {21:'S214', 22:'S216,S217', 23:'S218,S219', 24:'S221'}
snaps = {'S214':'S214.raw','S216':'S216.raw','S217':'S217.raw','S218':'S218.raw','S219':'S219.raw','S221':'S221.raw'}
bytes_ = {k:open(v,'rb').read().decode('utf-8','replace') for k,v in snaps.items()}
def occurs(tok, hay):
    # word-bounded: not flanked by ASCII word chars
    pat = r'(?<![A-Za-z0-9_])' + re.escape(tok) + r'(?![A-Za-z0-9_])'
    return re.search(pat, hay) is not None
for ln, ids in rows.items():
    line = entry[ln-1]
    toks = re.findall(r'`([^`]+)`', line)
    ids_l = ids.split(',')
    hay = '\n'.join(bytes_[i] for i in ids_l)
    miss = [t for t in toks if not occurs(t, hay)]
    paths = [t for t in toks if '/' in t]
    print(f"line {ln} [{ids}] tokens={len(toks)} paths={len(paths)} missing={miss}")
