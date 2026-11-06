#!/usr/bin/env python3
"""Round-100 C2 pre-data control worlds (L1 KotobaR100). Builds one scratch commit per control on
the round base in a scratch repo D (never the lane), writes each control's diff to
receipts/ctl-worlds/<name>.patch and prints `<name>:<commit>` for predata.sh."""
import re, subprocess, sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
BASE = "7b449a637c03d9b4c43a81b4df37cb38c2ea89ee"
D = Path(sys.argv[1])
OUT = LANE / ".ufo/waves/round-100/receipts/ctl-worlds"
CK = "verifiers/verify_skill_checklist.py"
BT = "verifiers/check_tip_battery.py"
BASE_LINE = '    m = re.match(r"^(.+\\.\\w+):\\d+(-\\d+)?$", tok)\n'
FIX_LINE = '    m = re.match(r"^(.+\\.\\w+):\\d+(-\\d+)?(,\\d+(-\\d+)?)*$", tok)\n'
SLOPPY = '    m = re.match(r"^(.+\\.\\w+):.*$", tok)\n'
ROW = ('    (3598,\n'
       '     "49419804caef1b49e64d9586134f8d3cc05fcdce2d113023796e2a4fc0057077",\n'
       '     "SCORECARD.md", 529, "corpus/lessons/round-80-verifier-spotcheck.md:30,37",\n'
       '     "corpus/lessons/round-80-verifier-spotcheck.md"),\n')
END = '    for f in failures:\n        print("self-test FAIL: %s" % f)\n'
ARM = ('    rec("r100 control: a comma-list anchor is a line anchor",\n'
       '        strip_token_dressing("corpus/a.md:30,37") == "corpus/a.md",\n'
       '        strip_token_dressing("corpus/a.md:30,37"))\n\n')
GOV = '    repo = repo.resolve()\n    subjects: list[dict] = []\n'
GOV_PASS = '    return "PASS", 1, "forced"\n'


def g(*a, check=True):
    p = subprocess.run(["git", "-C", str(D), *a], capture_output=True, text=True)
    if check and p.returncode:
        sys.exit("git %s: %s" % (a, p.stderr))
    return p.stdout.strip()


def sub(text, old, new):
    assert text.count(old) == 1, old[:60]
    return text.replace(old, new)


def build(name, line=None, drop_row=False, arm=False, gov_pass=False, pin=True):
    g("checkout", "-q", "--detach", BASE)
    ck = (D / CK).read_text(encoding="utf-8")
    if line:
        ck = sub(ck, BASE_LINE, line)
    if drop_row:
        ck = sub(ck, ROW, "")
    if arm:
        ck = sub(ck, END, ARM + END)
    if gov_pass:
        ck = sub(ck, GOV, GOV_PASS + GOV)
    (D / CK).write_text(ck, encoding="utf-8")
    if pin:
        blob = g("hash-object", CK)
        bt = (D / BT).read_text(encoding="utf-8")
        bt = sub(bt, '        "b6280c684b300ba313f1fc6a06655471e1c7142e"),\n',
                 '        "b6280c684b300ba313f1fc6a06655471e1c7142e",\n'
                 '        "%s"),\n' % blob)
        (D / BT).write_text(bt, encoding="utf-8")
    g("-c", "user.name=scratch", "-c", "user.email=scratch@invalid", "commit", "-qam", "ctl " + name)
    rev = g("rev-parse", "HEAD")
    (OUT / (name + ".patch")).write_text(g("diff", BASE, rev) + "\n", encoding="utf-8")
    print("%s:%s" % (name, rev))


assert g("rev-parse", "--show-toplevel") == str(D.resolve()), "scratch toplevel mismatch"
OUT.mkdir(parents=True, exist_ok=True)
build("p1-fixline-only", line=FIX_LINE, pin=False)
build("f1-sloppy-regex", line=SLOPPY, drop_row=True)
build("f2-no-arm", line=FIX_LINE, drop_row=True)
build("f3-row-kept", line=FIX_LINE, arm=True)
build("f4-data-only-removal", drop_row=True)
build("f5-gov-forced-pass", line=FIX_LINE, drop_row=True, arm=True, gov_pass=True)
