#!/usr/bin/env bash
# ExecKillPin: rp-m6 procedure against the patched battery (scratch only)
set -u
D="$1"; S="$2"
mkdir -p "$S" && W="$(mktemp -d "$S/w.XXXX")" || exit 1
trap 'rm -rf -- "$W"' EXIT
C="$W/lane"; git clone -q --shared "$D" "$C" && git -C "$C" checkout -q e073723ae667b64e534f8621bddb83ad12ad0e71 || exit 1
cp "$D/verifiers/check_mutation_battery.py" "$C/verifiers/check_mutation_battery.py"
M="$C/verifiers/fixtures/mutation-battery/manifest.tsv"
before="$(grep -cP '\tkill\t' "$M")"
grep -P '\tkill\t' "$M" | head -1 > "$W/dropline"
grep -vFx -f "$W/dropline" "$M" > "$W/m" && cp "$W/m" "$M"
after="$(grep -cP '\tkill\t' "$M")"
echo "kill rows before=$before after=$after"
python3 -B "$C/verifiers/check_mutation_battery.py" --self-test 2>&1 | tail -3
rc="${PIPESTATUS[0]}"
echo "self-test rc=$rc"
