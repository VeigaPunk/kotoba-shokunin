#!/usr/bin/env bash
# Build forgery worlds in the scratch clone and score them on the FROZEN C1 counter.
set -u
S=${S:?}
D=$S/repo
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_omp_root_semantics.py
LED=$D/verifiers/omp-skill-roots-semantics.tsv

top=$(git -C "$D" rev-parse --show-toplevel) || { echo "no repo"; exit 1; }
[ "$top" = "$D" ] || { echo "toplevel $top != $D"; exit 1; }
git -C "$D" checkout -q -B fixture d1c031833c37af99196f72f84a6643f84eec129a
echo "fixture base: $(git -C "$D" rev-parse HEAD)  toplevel=$top"

run_world() {  # $1 = label, $2 = python snippet mutating rows
  python3 - "$LED" "$2" <<'PY'
import sys
path, op = sys.argv[1], sys.argv[2]
lines = open(path, encoding="utf-8").read().splitlines()
hdr, rows = lines[0], lines[1:]
def setrow(i, quote, module=None):
    c = rows[i-1].split("\t")
    c[3] = quote
    if module is not None:
        c[2] = module
    rows[i-1] = "\t".join(c)
exec(op)
open(path, "w", encoding="utf-8").write("\n".join([hdr]+rows)+"\n")
PY
  git -C "$D" add verifiers/omp-skill-roots-semantics.tsv
  git -C "$D" -c user.name=critic -c user.email=critic@example.invalid commit -q -m "world $1"
  rev=$(git -C "$D" rev-parse HEAD)
  echo "=== world $1  rev=$rev ==="
  python3 -B "$L" --repo "$D" --rev "$rev" | sed -n '5,20p'
  echo "exit=${PIPESTATUS[0]}"
}

# W1: row 7 (.github) grounded by code whose only literal is .codex -- module cell untouched.
run_world w_cross_row7 'setrow(7, "return Xr.join(u.cwd, \".codex\");")'

# W2: the plugin skills root grounded by the SAME module's "commands" join (a different subdir).
run_world w_subdir_row9 'setrow(9, "Zo.join(R.path, \"commands\")")'

# W3: row 12 (managed-skills) grounded by a quote that lives in a different module chunk
#     merely because it occurs after managed-skills.ts's last header.
run_world w_misattr_row12 'setrow(12, "dir: Zo.join(R.path, \"skills\"),")'

# W4: conjunct 2's doc-exclusion is false as implemented: JOIN_TOKENS `.join(` also matches
#     Array#join inside a markdown-rendering template literal at ELF 188589625.
run_world w_renderline_row6 'setrow(6, "**Tags:** ${t.tags.join(\", \")}")'
