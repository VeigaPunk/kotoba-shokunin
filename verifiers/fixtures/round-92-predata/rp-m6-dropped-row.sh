#!/usr/bin/env bash
# rp-m6-dropped-row (round 92 pre-data): the m6-class dropped-kill-row world at the round-92 base
# bytes. Removes one `kill` row from the committed manifest in a scratch clone, then runs the
# battery's self-test. Round-91 routed defect 2 says this world stays GREEN (the bound lives only
# in the printed count) — this probe commits that red-before observable.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
BASE="5031a78215778525a7c777116ad6f6b89acac817"
ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r92/l1-predata/rp-m6"
mkdir -p "$ROOT" && W="$(mktemp -d "$ROOT/w.XXXX")" || { echo "rp-m6 could-not-evaluate: scratch unavailable"; exit 1; }
trap 'rm -rf -- "$W"' EXIT
S="$W/lane"; git clone -q --shared "$LANE" "$S" && git -C "$S" checkout -q "$BASE" || { echo "rp-m6 could-not-evaluate: clone failed"; exit 1; }
before="$(grep -cP '\tkill\t' "$S/verifiers/fixtures/mutation-battery/manifest.tsv")"
grep -P '\tkill\t' "$S/verifiers/fixtures/mutation-battery/manifest.tsv" | head -1 > "$W/dropline" || { echo "rp-m6 could-not-evaluate: no kill row"; exit 1; }
grep -vFx -f "$W/dropline" "$S/verifiers/fixtures/mutation-battery/manifest.tsv" > "$W/m" && cp "$W/m" "$S/verifiers/fixtures/mutation-battery/manifest.tsv"
after="$(grep -cP '\tkill\t' "$S/verifiers/fixtures/mutation-battery/manifest.tsv")"
echo "kill rows before=$before after=$after"
python3 -B "$S/verifiers/check_mutation_battery.py" --self-test 2>&1 | tail -1
rc="${PIPESTATUS[0]}"
if [ "$rc" = 0 ] && [ "$after" = "$((before-1))" ]; then echo "rp-m6 self-test GREEN on a dropped kill row (bound defect observable)"; exit 0; fi
echo "rp-m6 self-test not green or row not dropped (rc=$rc)"; exit 1
