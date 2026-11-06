#!/bin/bash
# Full matrix on the validated slim substrate + the new-control-world probes.
set +e
S=/fast/scratch/hyaku/kotoba-r97/MutTesterCounterV5
SLIM=$S/slim
export HYAKU_SCRATCH=$S/slimscratch
export HOME=$S/fakehome
REVS=$S/receipts/slim-revs.txt
rev() { awk -v n="$1" '$1==n{print $2}' "$REVS"; }
BASE=$(rev base97)
OUT=$S/receipts/matrix
mkdir -p "$OUT"
SUM=$OUT/summary.txt
: > "$SUM"

measure() { # label counter table rev outdir
  local label=$1 ctr=$2 table=$3 r=$4 out=$5
  { echo "# cmd: $ctr $table $r $SLIM"
    python3 -B "$ctr" "$table" "$r" "$SLIM" 2>&1
    echo "rc=$?"; } > "$out/$label.txt"
  local pred line rc rules
  pred=$(grep -E "PREDICATE|NOT-EVALUATED" "$out/$label.txt" | tail -1)
  line=$(grep -E "targets killed" "$out/$label.txt" | tail -1)
  rc=$(grep -E "^rc=" "$out/$label.txt" | tail -1)
  rules=$(grep -E "^rules " "$out/$label.txt" | tail -1)
  echo "$label | $pred | $line | $rc | $rules" >> "$SUM"
}

row() { # name counter
  local name=$1 ctr=$2 out=$S/receipts/matrix/$1
  mkdir -p "$out"
  local refused=0 held=0
  for world in g3-recompile-compare g7-stateful-fake g8-clone-marker g2b-guard-aware-sniff; do
    measure "world-$world" "$ctr" r96c1 "$(rev $world)" "$out"
    local pred
    pred=$(grep -E "PREDICATE|NOT-EVALUATED" "$out/world-$world.txt" | tail -1)
    case $world in
      g3-*|g7-*|g8-*) [ "$pred" = "R96C1-PREDICATE-MET" ] || refused=$((refused+1));;
    esac
  done
  measure "honest-h1" "$ctr" r96c1 "$(rev h1-r96-landing)" "$out"
  [ "$(grep -E 'PREDICATE|NOT-EVALUATED' "$out/honest-h1.txt" | tail -1)" = "R96C1-PREDICATE-MET" ] && held=$((held+1))
  local h2rev
  if [ "$name" = baseline ]; then h2rev=$BASE; else h2rev=$(rev "$name"); fi
  measure "honest-h2" "$ctr" r95c1 "$h2rev" "$out"
  [ "$(grep -E 'PREDICATE|NOT-EVALUATED' "$out/honest-h2.txt" | tail -1)" = "R95C1-PREDICATE-MET" ] && held=$((held+1))
  measure "base-c1" "$ctr" c1 "$BASE" "$out"
  echo "$name C2-equivalent: forgeries refused $refused of 3; honest held $held of 2" >> "$SUM"
  echo "done $name $(date -Is)"
}

row baseline "$S/counters/baseline.py"
for name in V1-mirror-dropped V2-bracket-first-only V3-isolation-dropped V4-home-not-reset \
            V5-no-shuffle V6-honest-any V7-unicode-uncaught V8-mirror-original \
            V9-decoy-runerror-held; do
  row "$name" "$S/counters/$name.py"
done

# --- new control worlds: baseline vs the mutant each is designed to expose ----
probe() { # world counter label
  local world=$1 ctr=$2 label=$3 out=$S/receipts/probes
  mkdir -p "$out"
  measure "$label" "$ctr" r96c1 "$(rev $world)" "$out"
}
probe g7p-tmpdir-marker "$S/counters/baseline.py" g7p-baseline
probe g7p-tmpdir-marker "$S/counters/V3-isolation-dropped.py" g7p-V3
probe g9-home-marker "$S/counters/baseline.py" g9-baseline
probe g9-home-marker "$S/counters/V4-home-not-reset.py" g9-V4
probe g10-workdir-marker "$S/counters/baseline.py" g10-baseline
probe g10-workdir-marker "$S/counters/V2-bracket-first-only.py" g10-V2
probe g10-workdir-marker "$S/counters/V6-honest-any.py" g10-V6
probe g11-blob-crash "$S/counters/baseline.py" g11-baseline
probe g11-blob-crash "$S/counters/V9-decoy-runerror-held.py" g11-V9
probe g12-blob-committed "$S/counters/baseline.py" g12-baseline
probe g12-blob-committed "$S/counters/V1-mirror-dropped.py" g12-V1
probe g12-blob-committed "$S/counters/V8-mirror-original.py" g12-V8
probe g12-blob-committed "$S/counters/V3-isolation-dropped.py" g12-V3

# --- exit-ladder probe: invalid UTF-8 instrument at a rev --------------------
for pair in "baseline:$S/counters/baseline.py" "V7:$S/counters/V7-unicode-uncaught.py"; do
  label=${pair%%:*}; ctr=${pair#*:}
  { echo "# cmd: $ctr c1 $(rev badutf8) $SLIM"
    python3 -B "$ctr" c1 "$(rev badutf8)" "$SLIM" 2>&1
    echo "rc=$?"; } > "$S/receipts/probes/badutf8-$label.txt"
  echo "badutf8-$label | $(grep -E 'NOT-EVALUATED|PREDICATE' "$S/receipts/probes/badutf8-$label.txt" | tail -1) | $(grep -E '^rc=' "$S/receipts/probes/badutf8-$label.txt" | tail -1) | $(grep -E 'Traceback|UnicodeDecodeError' "$S/receipts/probes/badutf8-$label.txt" | tail -1)" >> "$SUM"
done
echo "ALL DONE $(date -Is)" >> "$SUM"
echo "ALL DONE $(date -Is)"