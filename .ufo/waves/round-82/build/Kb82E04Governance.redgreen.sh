#!/bin/bash
# Kb82E04Governance red/green driver — reproduces the seat's evidence from the
# patch alone.  Builds a fleet-layout scratch world (the lane's `..`-hop
# citations resolve against a synthetic fleet root symlinked to the real one,
# read-only) and runs RED (base) and GREEN (base+patch) checklists plus the
# mutation arms.  Usage: Kb82E04Governance.redgreen.sh <patch> <outdir>
set -u
PATCH=${1:?patch path}
OUT=${2:?output dir}
BASE=47dbe8781657de563ff867caca6244d28e3db504
W=$OUT/world
mkdir -p "$W/fleet-root" "$OUT"
for p in /home/vgpnk/Projects/shokunin/* /home/vgpnk/Projects/shokunin/.ufo; do
  n=$(basename "$p"); [ "$n" = kotoba-shokunin ] || ln -sfn "$p" "$W/fleet-root/$n"
done
git clone -q --shared --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin "$W/fleet-root/kotoba-shokunin"
git -C "$W/fleet-root/kotoba-shokunin" checkout -q --detach "$BASE"
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
T=$W/fleet-root/kotoba-shokunin
for r in 70 72 73; do
  mkdir -p "$T/.ufo/waves/round-$r"
  ln -sfn "$L/.ufo/waves/round-$r/snapshots" "$T/.ufo/waves/round-$r/snapshots"
done
cd "$T"
echo "== RED: base =="
python3 -B verifiers/verify_skill_checklist.py --check governance.citation_resolves --repo "$T"
echo "exit=$?"
echo "== GREEN: base + patch =="
git -C "$T" apply "$PATCH"
python3 -B verifiers/verify_skill_checklist.py --check governance.citation_resolves --repo "$T"
echo "exit=$?"
echo "== M1 stale-restored =="
echo probe > .ufo/wapes
python3 -B verifiers/verify_skill_checklist.py --check governance.citation_resolves --repo "$T"
echo "exit=$?"; rm -f .ufo/wapes
echo "== M5 unrelated dead subject =="
printf -- '- `corpus/knowledge/kb82e04-probe-gone.md` probe citation.\n' >> SCORECARD.md
python3 -B verifiers/verify_skill_checklist.py --check governance.citation_resolves --repo "$T"
echo "exit=$?"
