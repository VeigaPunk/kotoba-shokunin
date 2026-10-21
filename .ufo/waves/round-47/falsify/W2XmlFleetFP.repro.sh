#!/bin/sh
# W2XmlFleetFP repro: the tip's trigger.no_xml_tag, FP/FN edges, and the one live hit.
# usage: sh W2XmlFleetFP.repro.sh [clone-at-7ad7fad]
set -eu
CLONE=${1:-/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2XmlFleetFP-2/kotoba-shokunin}
python3 - "$CLONE" <<'PY'
import importlib.util, sys
from pathlib import Path
import yaml

clone = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("vsc", clone/"verifiers/verify_skill_checklist.py")
vsc = importlib.util.module_from_spec(spec); spec.loader.exec_module(vsc)

def run(label, desc_line):
    lines = ["---", "name: x", "description: " + desc_line, "---"]
    fm = vsc.parse_frontmatter(lines)
    st, _, det = vsc.check_no_xml_tag(fm)
    raw = desc_line
    val = yaml.safe_load("k: " + raw)["k"]
    print("%-18s checker=%-4s yaml_value=%-22r yaml_has_lt=%s"
          % (label, st, val, "<" in val))

print("== escaping FP: only the double-quoted shape decodes to '<' ==")
run("single-quoted", r"'use \u003c here'")
run("plain-scalar",  r"use \u003c here")
run("double-quoted", r'"use \u003c here"')
run("dq-escaped-bs", r'"use \\u003c here"')

print("== other shapes ==")
for label, d in [
    ("gt-escape-only", r"just \x3e"),
    ("prose-pair",     "if a<b then c>d"),
    ("entity",         "use &lt;skills&gt; here"),
    ("autolink",       "see <https://example.com/a>"),
    ("comparison",     "a < b and c > d"),
]:
    lines = ["---", "name: x", "description: " + d, "---"]
    print("%-18s checker=%s" % (label, vsc.check_no_xml_tag(vsc.parse_frontmatter(lines))[0]))

print("== when_to_use is not scanned (declared at verifiers/verify_skill_checklist.py:210-213) ==")
lines = ["---", "name: x", "description: fine", "when_to_use: use <skills> here", "---"]
print("when_to_use       checker=%s" % vsc.check_no_xml_tag(vsc.parse_frontmatter(lines))[0])
PY
echo "== live hit (user skill, not the fleet repo) =="
python3 "$CLONE/verifiers/verify_skill_checklist.py" \
  --skill "$HOME/.agents/skills/shokunin/SKILL.md" \
  --check trigger.no_xml_tag --json || echo "exit=$? (expected 1: '<id>' in description)"
