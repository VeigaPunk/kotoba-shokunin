#!/usr/bin/env bash
# check_receipt_revs.sh — Q36/Q50 receipt revision-naming check (kotoba round 76, seat B27).
#
# PURPOSE
#   For every receipt file under .ufo/waves/round-7{3,4,5,6}/receipts/ , decide whether the
#   receipt names the revision it measured.
#     Q36 (corpus/QUALITY.md:47): "A no-harm or tip receipt cited in a report names the revision
#     it measured in the receipt itself (a printed `git rev-parse HEAD` or `--rev`/`--head` value)".
#     Q50 (corpus/QUALITY.md:61): "Every gate result a report states for the lane tip has a
#     committed receipt that names that exact tip revision and the observed result".
#
# THE CHECK (one verdict per file)
#   A receipt PASSES when it names a revision by one of:
#     (A) a full 40-hex revision token standing alone (a maximal hex run of exactly 40 chars, so
#         a 64-hex sha256 or a 12-hex abbreviation does NOT count), or
#     (B) an explicitly marked '<rev>' placeholder (the literal angle-bracket token).
#   Verdicts are graded so a reader can see *how* the revision was named:
#     MEASURED     — a 40-hex token appears on a line that also names a revision
#                   (measured-rev / base / rev / head / revision / --rev / --head / at …).
#     TOKEN        — a 40-hex token is present, but no line carrying it names a revision.
#                   Passes the literal rule; flagged WEAK, because the 40-hex may be a sha256, a
#                   blob id or a sibling-lane head rather than the revision the receipt measured.
#     PLACEHOLDER  — no 40-hex token, but an explicitly marked '<rev>' placeholder is present.
#     ABBREV       — no 40-hex token, but a revision-naming line carries an abbreviated hex rev
#                   (7-39 chars).  The receipt names *a* revision but not in the full 40-hex form
#                   Q36 asks for; reported separately from FAIL because it is a weaker defect.
#     FAIL         — none of the above: the receipt names no revision at all (a Q36/Q50 failure).
#   Exit status: 0 when no receipt FAILs, 1 when at least one receipt FAILs.
#
# USAGE
#   build/check_receipt_revs.sh [--repo <lane-root>] [--exclude <lane-relative-path> ...]
#   Default lane root is derived from this script's own location
#   (<lane>/.ufo/waves/round-76/build/check_receipt_revs.sh).
#
# READ-ONLY: this script writes nothing; it only reads the lane tree and prints a report on
# stdout.  It performs no git/jj write of any kind.
set -u
LC_ALL=C
export LC_ALL

SELF="$(readlink -f "$0")"
REPO="$(cd "$(dirname "$SELF")/../../../.." && pwd)"
EXCLUDES=(".ufo/waves/round-76/receipts/receipt-revs.txt")   # this check's own output

while [ "$#" -gt 0 ]; do
  case "$1" in
    --repo) REPO="$2"; shift 2 ;;
    --exclude) EXCLUDES+=("$2"); shift 2 ;;
    -h|--help) sed -n '2,42p' "$SELF"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

ROUNDS=(73 74 75 76)
WAVE_DIR=".ufo/waves"

# A line that names a revision.  Used only to grade HOW a 40-hex token is presented.
# Matched case-insensitively (the awk side lowercases the line), so `git rev-parse HEAD`,
# `tip:` and `--rev` all count.
REVCFG_RE='measured[- _]?rev|receipt_rev|base[- _]?rev|(^|[^a-z])base([^a-z]|$)|(^|[^a-z])rev([^a-z]|$)|--rev|--head|rev-parse|revision|(^|[^a-z])head([^a-z]|$)|(^|[^a-z])tip([^a-z]|$)|(^|[^a-z])at([^a-z]|$)'

# Print every maximal hex run of exactly 40 characters, one per line.
# $1 = file, $2 = "ctx" to restrict to lines matching REVCFG_RE.
hex_runs() {
  awk -v ctx="$2" -v RE="$REVCFG_RE" '
    {
      line = $0
      if (ctx == "ctx" && tolower(line) !~ RE) next
      n = length(line); i = 1
      while (i <= n) {
        c = substr(line, i, 1)
        if (c ~ /[0-9a-fA-F]/) {
          j = i
          while (j <= n && substr(line, j, 1) ~ /[0-9a-fA-F]/) j++
          if (j - i == 40) print substr(line, i, 40)
          i = j
        } else i++
      }
    }' "$1" 2>/dev/null | sort -u
}

# Print abbreviated hex revs (7-39 chars) that sit on a revision-naming line.
abbrev_revs() {
  awk -v RE="$REVCFG_RE" '
    {
      line = $0
      if (tolower(line) !~ RE) next
      n = length(line); i = 1
      while (i <= n) {
        c = substr(line, i, 1)
        if (c ~ /[0-9a-fA-F]/) {
          j = i
          while (j <= n && substr(line, j, 1) ~ /[0-9a-fA-F]/) j++
          len = j - i
          if (len >= 7 && len <= 39) print substr(line, i, len)
          i = j
        } else i++
      }
    }' "$1" 2>/dev/null | sort -u
}

is_excluded() {
  local p="$1" e
  for e in "${EXCLUDES[@]}"; do
    [ "$p" = "$e" ] && return 0
  done
  return 1
}

class_of() {  # receipt | code | data
  case "$1" in
    *.txt|*.md|*.log|*.out) echo receipt ;;
    *.py|*.sh) echo code ;;
    *.tsv|*.csv|*.json) echo data ;;
    *) echo other ;;
  esac
}

printf '# receipt revision check (Q36/Q50) — kotoba round 76, seat B27ReceiptVerifier\n'
printf '# generated: %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
printf '# repo: %s\n' "$REPO"
printf '# lane HEAD: %s\n' "$(git -C "$REPO" rev-parse HEAD 2>/dev/null || echo unknown)"
printf '# script: %s\n' "$SELF"
printf '# script sha256: %s\n' "$(sha256sum "$SELF" | cut -d" " -f1)"
printf '# rounds scanned: %s\n' "${ROUNDS[*]}"
printf '# rule: PASS iff a standalone 40-hex revision token OR an explicitly marked %s placeholder\n' "'<rev>'"
printf '# tiers: MEASURED (40-hex on a revision-naming line) / TOKEN (40-hex, no revision-naming line) / PLACEHOLDER (marked <rev>) / ABBREV (revision named only in abbreviated form) / FAIL (no revision named at all)\n'
printf '# file class: receipt = text receipt; code = source copy filed under receipts/; data = tabular artifact\n'
printf '#\n'

total=0; n_meas=0; n_tok=0; n_ph=0; n_abbrev=0; n_fail=0
fail_list=(); weak_list=(); uncommitted_list=(); abbrev_list=()

for r in "${ROUNDS[@]}"; do
  rdir="$REPO/$WAVE_DIR/round-$r/receipts"
  if [ ! -d "$rdir" ]; then
    printf '## round-%s: NO receipts directory (%s)\n' "$r" "$WAVE_DIR/round-$r/receipts"
    continue
  fi
  printf '## round-%s: %s\n' "$r" "$WAVE_DIR/round-$r/receipts"
  mapfile -t files < <(find "$rdir" -type f | LC_ALL=C sort)
  if [ "${#files[@]}" -eq 0 ]; then
    printf '   (directory present, no files)\n\n'
    continue
  fi
  for f in "${files[@]}"; do
    rel="${f#$REPO/}"
    if is_excluded "$rel"; then
      printf '   SKIP     %s (excluded)\n' "$rel"
      continue
    fi
    total=$((total + 1))
    bytes=$(wc -c < "$f" | tr -d ' ')
    fsha=$(sha256sum "$f" | cut -d" " -f1)
    cls=$(class_of "$f")
    if git -C "$REPO" ls-files --error-unmatch -- "$rel" >/dev/null 2>&1; then
      tracked="committed"
    else
      tracked="UNCOMMITTED"
      uncommitted_list+=("$rel")
    fi
    ctx=$(hex_runs "$f" ctx)
    alltoks=$(hex_runs "$f" all)
    nctx=$(printf '%s' "$ctx" | grep -c . || true)
    nall=$(printf '%s' "$alltoks" | grep -c . || true)
    nph=$(grep -aoF '<rev>' "$f" 2>/dev/null | wc -l | tr -d ' ')
    if [ "$nctx" -gt 0 ]; then
      first=$(printf '%s\n' "$ctx" | head -1)
      printf '   MEASURED  %8s  [%s]  [%s]  %s\n' "$bytes" "$cls" "$tracked" "$rel"
      printf '              sha256=%s\n' "$fsha"
      printf '              rev=%s  (%s revision-named line(s) carry %s distinct 40-hex token(s); %s total)\n' \
        "$first" "$nctx" "$nctx" "$nall"
      n_meas=$((n_meas + 1))
    elif [ "$nall" -gt 0 ]; then
      first=$(printf '%s\n' "$alltoks" | head -1)
      printf '   TOKEN     %8s  [%s]  [%s]  %s\n' "$bytes" "$cls" "$tracked" "$rel"
      printf '              sha256=%s\n' "$fsha"
      printf '              rev=%s  (40-hex token present, but no line carrying it names a revision)\n' "$first"
      n_tok=$((n_tok + 1))
      weak_list+=("$rel")
    elif [ "$nph" -gt 0 ]; then
      printf '   PLACEHOLDER %5s  [%s]  [%s]  %s\n' "$bytes" "$cls" "$tracked" "$rel"
      printf '              sha256=%s\n' "$fsha"
      printf '              marked %s placeholder(s); no 40-hex revision token\n' "$nph"
      n_ph=$((n_ph + 1))
    else
      abv=$(abbrev_revs "$f")
      if printf '%s' "$abv" | grep -q .; then
        nav=$(printf '%s\n' "$abv" | wc -l | tr -d ' ')
        first=$(printf '%s\n' "$abv" | head -1)
        printf '   ABBREV   %8s  [%s]  [%s]  %s\n' "$bytes" "$cls" "$tracked" "$rel"
        printf '              sha256=%s\n' "$fsha"
        printf '              rev=%s  (abbreviated rev on a revision-naming line; %s abbreviated token(s), no full 40-hex)\n' \
          "$first" "$nav"
        n_abbrev=$((n_abbrev + 1))
        abbrev_list+=("$rel")
      else
      printf '   FAIL      %8s  [%s]  [%s]  %s\n' "$bytes" "$cls" "$tracked" "$rel"
      printf '              sha256=%s\n' "$fsha"
      printf "              no 40-hex revision token and no marked '<rev>' placeholder\n"
      case "$rel" in
        *.sh|*.py) : ;;   # a runner, not a receipt — not a Q36/Q50 receipt defect
        *) n_fail=$((n_fail + 1)); fail_list+=("$rel") ;;
      esac
      fi
    fi
  done
  printf '\n'
done

printf '## summary\n'
printf '   receipts scanned: %s\n' "$total"
printf '   MEASURED %s / TOKEN %s / PLACEHOLDER %s / ABBREV %s / FAIL %s\n' \
  "$n_meas" "$n_tok" "$n_ph" "$n_abbrev" "$n_fail"
printf '   PASS (full 40-hex or marked <rev>) %s of %s ; FAIL %s of %s\n' \
  "$((n_meas + n_tok + n_ph))" "$total" "$n_fail" "$total"
printf '\n'

printf '## ABBREV list (a revision is named, but only in abbreviated form — weaker than a 40-hex rev)\n'
if [ "${#abbrev_list[@]}" -eq 0 ]; then
  printf '   (none)\n'
else
  for f in "${abbrev_list[@]}"; do printf '   ABBREV  %s\n' "$f"; done
fi
printf '\n'

printf '## FAIL list (receipts that name no revision — Q36/Q50 defects)\n'
printf '#   A runner filed under receipts/ (a .sh/.py script) is not itself a receipt: the revision\n'
printf '#   appears in the OUTPUT it writes, not in the script text.  Such files are listed\n'
printf '#   separately and are NOT counted as Q36/Q50 receipt defects.\n'
if [ "${#fail_list[@]}" -eq 0 ]; then
  printf '   (none)\n'
else
  for f in "${fail_list[@]}"; do
    case "$f" in
      *.sh|*.py) printf '   RUNNER-NO-REV  %s\n' "$f" ;;
      *) printf '   FAIL           %s\n' "$f" ;;
    esac
  done
fi
printf '\n'

printf '## advisory: TOKEN-only files (rule-pass, but the 40-hex is not on a revision-naming line)\n'
if [ "${#weak_list[@]}" -eq 0 ]; then
  printf '   (none)\n'
else
  for f in "${weak_list[@]}"; do printf '   WEAK  %s\n' "$f"; done
fi
printf '\n'

printf '## advisory: UNCOMMITTED receipts (named a revision but not committed — Q50 "committed receipt")\n'
if [ "${#uncommitted_list[@]}" -eq 0 ]; then
  printf '   (none)\n'
else
  for f in "${uncommitted_list[@]}"; do printf '   UNCOMMITTED  %s\n' "$f"; done
fi
printf '\n'

if [ "${SELFTEST:-0}" = "1" ]; then
  printf '## self-test (arms run against synthetic fixtures; the checker must reject each bad shape)\n'
  ST="$(mktemp -d)"
  trap 'rm -rf -- "$ST"' EXIT
  st_fail=0
  arm() {  # arm <name> <expect PASS|FAIL|ABBREV> <content>
    local name="$1" expect="$2" content="$3"
    printf '%s\n' "$content" > "$ST/receipt.txt"
    local toks ctx nph verdict
    toks=$(hex_runs "$ST/receipt.txt" all)
    ctx=$(hex_runs "$ST/receipt.txt" ctx)
    nph=$(grep -aoF '<rev>' "$ST/receipt.txt" 2>/dev/null | wc -l | tr -d ' ')
    if printf '%s' "$ctx" | grep -q .; then verdict=PASS
    elif printf '%s' "$toks" | grep -q .; then verdict=PASS
    elif [ "$nph" -gt 0 ]; then verdict=PASS
    elif abbrev_revs "$ST/receipt.txt" | grep -q .; then verdict=ABBREV
    else verdict=FAIL; fi
    if [ "$verdict" = "$expect" ]; then
      printf '   PASS arm %-34s expected %s, got %s\n' "$name" "$expect" "$verdict"
    else
      printf '   FAIL arm %-34s expected %s, got %s\n' "$name" "$expect" "$verdict"
      st_fail=$((st_fail + 1))
    fi
  }
  arm "full-40-hex-named"        PASS   "measured-rev: 072048fa8e8a52c707d25f7079772fa317244eb7"
  arm "marked-placeholder"       PASS   "measured-rev: <rev>"
  arm "no-rev-at-all"             FAIL   "date: 2026-10-27
exit=0
nothing named"
  arm "abbrev-rev-only"           ABBREV "measured-rev: 072048fa"
  arm "sha256-not-a-rev"          FAIL   "counter sha256 bd34ec1bfded53706921fd7c0bb833712daa3d4f9f98812ee81dfc6765769d01"
  arm "40-hex-plus-rev-word"      PASS   "base 072048fa8e8a52c707d25f7079772fa317244eb7"
  arm "40-hex-no-rev-word"        PASS   "blob 072048fa8e8a52c707d25f7079772fa317244eb7"
  arm "39-hex-truncated"           ABBREV "measured-rev: 072048fa8e8a52c707d25f7079772fa317244eb"
  arm "41-hex-overlong"           FAIL   "measured-rev: 072048fa8e8a52c707d25f7079772fa317244eb7a"
  arm "unmarked-placeholder"      FAIL   "measured-rev: REV"
  arm "sha256-plus-abbrev-rev"    ABBREV "counter sha256 bd34ec1bfded53706921fd7c0bb833712daa3d4f9f98812ee81dfc6765769d01
base 1e03d1991bc0"
  printf '   self-test failures: %s\n' "$st_fail"
  printf '\n'
fi

printf '## coverage appendix (OUT OF SCOPE for the Q36/Q50 receipt check — reported for context only)\n'
printf '#   round-75 has no receipts/ directory; its round artifacts live in w1/ and w2/ as seat\n'
printf '#   REPORTS.  Q36/Q50 govern receipts, not reports, so the counts below are NOT Q36/Q50\n'
printf '#   defects and are not added to the PASS/FAIL totals above.  They are reported because the\n'
printf '#   same revision-naming discipline applies to a report that asserts a measured result.\n'
for d in "$REPO/$WAVE_DIR/round-75/w1" "$REPO/$WAVE_DIR/round-75/w2"; do
  if [ ! -d "$d" ]; then
    printf '   ## %s : absent\n' "${d#$REPO/}"
    continue
  fi
  a=0; b=0; c=0; e=0; g=0; f_n=0
  while IFS= read -r f; do
    rel="${f#$REPO/}"
    is_excluded "$rel" && continue
    a=$((a + 1))
    if hex_runs "$f" ctx | grep -q .; then b=$((b + 1))
    elif hex_runs "$f" all | grep -q .; then c=$((c + 1))
    elif [ "$(grep -aoF '<rev>' "$f" 2>/dev/null | wc -l | tr -d ' ')" -gt 0 ]; then e=$((e + 1))
    elif abbrev_revs "$f" | grep -q .; then g=$((g + 1))
    else f_n=$((f_n + 1)); fi
  done < <(find "$d" -type f | LC_ALL=C sort)
  printf '   ## %s : files %s | MEASURED %s | TOKEN %s | PLACEHOLDER %s | ABBREV %s | no-rev %s\n' \
    "${d#$REPO/}" "$a" "$b" "$c" "$e" "$g" "$f_n"
done

if [ "$n_fail" -gt 0 ]; then exit 1; fi
exit 0
