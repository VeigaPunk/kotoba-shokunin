import sys, importlib.util, re
L="/home/vgpnk/Projects/shokunin/kotoba-shokunin"
spec=importlib.util.spec_from_file_location("cat", L+"/.ufo/waves/round-79/build/check_allowed_tools.py")
m=importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(m)
except SystemExit as e:
    print("import SystemExit", e)
tv=m.text_view
snapdir=L+"/.ufo/waves/round-79/snapshots/"
rows=[
 ("S226","S226-spec.md","The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental."),
 ("S227","S227-claude.md","allowed-tools field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval."),
 ("S228","S228-factory.md","allowed-tools records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces"),
 ("S229","S229-msaf.html","allowed-tools No Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations."),
 ("S230","S230-pi.md","allowed-tools | Experimental pre-approved tool list"),
 ("S231","S231-vibe.md","user-invocable: true allowed-tools: read grep ask_user_question"),
]
for sid,fn,q in rows:
    raw=open(snapdir+fn,encoding="utf-8").read()
    view=tv(fn,raw)
    hits=sum(1 for line in view if q in line)
    joined=" ".join(view)
    total=joined.count(q)
    print(f"{sid} {fn} bytes={len(raw.encode())} words={len(q.split())} view_line_hits={hits} view_span_count={total} raw_count={raw.count(q)} pipes={'|' in q}")
