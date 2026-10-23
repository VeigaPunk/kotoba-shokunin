Result: MIXED — the candidate line rule (LEADING, five clauses) is quote-blind on U+2192 and therefore fails the v2 H8 class 8 of 8 per seed, can turn a base PASS into a FAIL when it skips a heredoc opener, and repairs only 34 of the 119 unresolved subjects in the three lanes that actually carry decoration: every one of those lanes still FAILs afterwards.

# C2 redesign input — attack on the candidate per-line skip rule

Seat: KotobaR57.CriticC2Rule. C2 is withdrawn before data (plans/round-57.md Erratum 1); nothing here
proposes a fix to ship this round. All runs are in my own sandbox clone
`/fast/scratch/hyaku/kotoba-r57/CriticC2Rule` checked out at `01312a77e36317feb6e961aba77841ddab1225ca`
(`git rev-parse HEAD` printed that hash). No lane file was written; sibling SKILL.md files were read only.

## 0. The rule under test, exactly as implemented

The only implementation of the five clauses is the control's `LEADING` variant,
sandbox `f5505ff` in `/fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC2CharShortcuts`
(instrument `sha256 104ce911e12c09b54b2dfb215183408ab26468bc999d42c0a483c692029520ec`, printed by both counters):

```
1092  LEAD_STRUCTURAL = "|\u2502\u250c\u2510\u2514\u2518\u251c\u2524+"
1119  return (bool(s) and s[0] in LEAD_STRUCTURAL) or "\u2192" in line \
1120      or first.endswith(":")
1143  if infoless and shortcut_skip(line):   # s = line.strip(); first = first whitespace token
```

Three things the rule text does not say but the code does:

1. the box-drawing clause is **seven characters** (`│┌┐└┘├┤`), not U+2500–U+257F;
2. the arrow clause is **`"\u2192" in line`** — anywhere, with no quote state at all;
3. the skip runs **before** heredoc tracking (`heredoc_delimiter` is consulted at `:1153`, after the `:1143`
   skip; the `heredoc_end is not None` body guard at `:1144` too), so a skipped opener loses its heredoc suppression.

Harness (mine, sandbox only): `probe/run_probes.py` (per-line verdict matrix, base vs LEADING),
`probe/freq.py` (info-less fence census over the sibling SKILL.md files, using the instrument's own
`fenced_regions`), `probe/residual.py` (exact unresolved-subject sets). Each probe case is a fresh
directory with an info-less fence holding one resolvable line (`ls -la`) plus the probe line, run as
`python3 -B <tree>/verifiers/verify_skill_checklist.py --repo <case> --skill <case>/SKILL.md
--check trigger.command_binary_resolves --json`. Base tree = the clone's unmodified `verifiers/`;
LEADING tree = the same tree with `git show f5505ff:verifiers/verify_skill_checklist.py`.

## 1. Real shell lines the rule wrongly skips (all measured, base vs rule)

| probe line (info-less fence, one real `ls -la` also present) | base | LEADING | truthful verdict |
|---|---|---|---|
| `: "${DEPLOY_ENV:?}" && cardlog-deploy --prod` | FAIL | **N/A** | FAIL — colon clause eats the whole line, the missing command is never seen |
| `cardlog-render "step → done"` (U+2192 inside double quotes) | FAIL | **PASS** | FAIL — quote-blind arrow clause (this is v2's H8) |
| `cardlog-render 'step → done'` (single quotes) | FAIL | **PASS** | FAIL — same |
| `cardlog-map old→new notes/` (arrow in an unquoted argument) | FAIL | **PASS** | FAIL — same |
| `ls -la \|` + `\| cardlog-parse --json` (leading `\|`, previous line has no `\`) | FAIL | **PASS** | FAIL — leading-`\|` clause |
| `ls -la` + `\|\| cardlog-cleanup --force` (`\|\|` at line start) | FAIL | **PASS** | FAIL — leading-`\|` clause |

Corrections to the brief's hypotheses, measured:

- `\|&` at line start does **not** need the rule: the base instrument already misses it (`|&` splits into a
  segment whose head is `&`, a metachar) — base PASS, LEADING PASS. Pre-existing hole, not rule-induced.
- `logical_lines` joins `\`-continuations **before** the skip, so the usual doc style
  `cmd \` + `  | jq .` is immune: the merged line starts with `cmd`. The leading-`\|` clause only bites on
  a leading `|` with no backslash before it. Real today: 0 lines (see §3).
- `ssh host:path`, `docker run -v a:b`, `scp a:b`, `case` arms `deploy)` and `$(...)` are **not** broken by
  this rule (first token is `ssh`/`docker`/`scp`; `)` is already a `SHELL_METACHAR`; `[` `(` are too).
  Probes A1/A3/A4/A5 are PASS on both trees. (`scp a:b ./` is FAIL on both trees only because `scp` is not
  installed on this host — the rule changes nothing there.)
- Heredoc regression (base PASS → rule FAIL): fence `cat <<'EOF' > notes.md   # step → ship` /
  `this line is prose, not a command` / `EOF`. Base PASS (heredoc suppressed), LEADING **FAIL**
  (`2 segments; line 10: 'this' … does not resolve; line 11: 'EOF'`). Same defect with the real
  `: <<'EOF'` comment idiom (base FAIL for its own reason; the rule still exposes the body).
- A skipped line whose only content is a resolvable command plus an arrow comment (`ls -la  # a → b`)
  drops the check to N/A instead of PASS: harmless for the false-FAIL goal, but it shows the clause
  removes *checkable* content, not just decoration.

## 2. Non-shell lines that still FAIL under the rule (measured)

| probe line (with `ls -la` in the same fence) | base | LEADING | truthful verdict |
|---|---|---|---|
| `╭──────────────╮` / `│ cardlog │` / `╰──────────────╯` | FAIL | **FAIL** | PASS — rounded corners not in the 7-char set |
| `┏━━━━━━━━━━━━━━┓` / `┃ cardlog ┃` / `┗━━━━━━━━━━━━━━┛` | FAIL | **FAIL** | PASS — heavy/double box not in the set |
| `  ┬──────────┬` / `  │ cardlog  │` / `  ┴──────────┴` | FAIL | **FAIL** | PASS — `┬`/`┴` not in the set |
| `Total size: 4.2 GB` (two-word key) | FAIL | **FAIL** | PASS — `first.endswith(":")` only sees one-word keys |
| `Step 1: extract the archive` | FAIL | **FAIL** | PASS — first token `Step` |
| `PASS healthy: all planes pass (exit 0, HEALTHY)` (real tsukuroi line) | FAIL | **FAIL** | PASS — two-word key, the dominant residual |
| `exit map: 0 HEALTHY \| 1 DEGRADED \| 2 BLOCKED` (real tsukuroi line) | FAIL | **FAIL** | PASS — the base splits on mid-line `\|`; heads `1`, `2` survive |
| `js-kimi-census   175de6ba   current` (real tameshi row) | FAIL | **FAIL** | PASS — space-aligned table, no pipes |
| `p_success    = p_in_scope × p_accepted` (real kasegi line) | FAIL | **FAIL** | PASS — non-ASCII dropped from the rule |
| `draft -> review -> ship` | FAIL | **FAIL** | PASS — `->` is not U+2192 |
| `build => deploy` | FAIL | **FAIL** | PASS — same |
| `draft --> review` | FAIL | **FAIL** | PASS — same |
| `draft ⇒ review` (U+21D2) | FAIL | **FAIL** | PASS — only U+2192 is tested |
| `1. extract the archive` | FAIL | **FAIL** | PASS — numbered output |
| `NAME      READY   STATUS` | FAIL | **FAIL** | PASS — aligned header |
| `http://localhost:8080/health` (bare URL output) | FAIL | **FAIL** | PASS — token has `/`, `://` is not special here |
| `● cardlog   ● kv` | FAIL | **FAIL** | PASS — bullets |
| `\|-- src` / `\|-- tests` (ascii tree) | FAIL | **PASS** | PASS — repaired by the leading-`\|` clause (brief's "tree `\|--` still fails" is wrong) |
| `  \| Name \| Value \|` (indented table) | FAIL | **PASS** | PASS — `strip()` makes it leading `\|` (brief's "indented tables still fail" is wrong) |
| `TSUKUROI_CENSUS: HEALTHY\|DEGRADED\|BLOCKED` (real tsukuroi:263) | FAIL | **PASS** | PASS — repaired (first token ends `:`; whole line skipped) |

Commands (all from my sandbox; every one exited 0 where a score is reported):

```
python3 -B probe/run_probes.py
python3 -B probe/freq.py
python3 -B probe/residual.py
python3 -B verifiers/check_infoless_fences.py --repo /fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC2CharShortcuts \
    --rev f5505ffd00c222737955e485a4b85ed9be9225da          # v1: 120 of 120, exit 0
python3 -B .ufo/waves/round-57/w0/check_infoless_fences_v2.py --repo …/KotobaR57.CtlC2CharShortcuts \
    --rev f5505ffd00c222737955e485a4b85ed9be9225da --seed 11  # v2: 80 of 88, 8 wrong H8
```

The v1 counter and the v2 counter were read from the lane (read-only); `--repo` pointed at the control's
scratch clone, which the counters only `git archive`.

## 3. Real-corpus census and the residual (decisive)

18 `*-shokunin/SKILL.md` exist (21 lane dirs; `audio-`, `game-dev-2d-`, `revenger-shokunin` have no
SKILL.md, so 18 is the whole population, not 20). Info-less fences are rare: **14 fences, 83 lines, in 3
lanes** — kasegi 14, tameshi 28, tsukuroi 41. Every other fence is tagged (`sh` 12, `bash` 5; the rest are
outside `FENCED_INFO` entirely and the rule never sees them).

| shape in the 83 info-less lines | lines | files | rule verdict | truthful |
|---|---|---|---|---|
| `→` mapping line (`policy read (…)  → evidence/…json`) | 9 | kasegi | skip | correct |
| `key:` first token (`id:`, `class:`, `site:`, …) | 14 | tameshi | skip | correct |
| `+ expected_risk_cost` (formula continuation) | 1 | kasegi | skip | correct |
| mid-line colon after a multi-word key / `PASS healthy: …` | 31 | tsukuroi | keep | **still FAILs** |
| leading `\|` (table, tree, `\|\|`) | 0 | — | skip | latent only |
| leading box-drawing char | 0 | — | skip | latent only |
| aligned no-pipe table rows | 18 | tameshi | keep | **still FAILs** |
| non-ASCII formula (`×`, `−`) | 4 | kasegi | keep | **still FAILs** |

No false skip was observed in the real corpus; all 24 skips are decorative. The failure is the other side.

Unresolved subjects per lane, base → LEADING (`probe/residual.py`, `command_subjects` + `safe_resolve`):

| lane | base | LEADING | repaired lines | residual lines |
|---|---|---|---|---|
| kasegi | 21 | 5 | 39-47, 831 | 828, 829, 830, 832, 897 |
| tameshi | 37 | 28 | 255-261 | 545, 589, 613, 627, 664, 831, 1044-1049, 1056, 1173-1178, 1404-1409, 1720, 1767, 1768 |
| tsukuroi | 61 | 52 | 263, 292, 304, 583, 611, 885, 1216 | 264, 275-291, 300-303, 880-884, 1041, 1210-1215, 1416, 1587, 1592 |

The three lines the plan names as the live false FAILs are repaired line-for-line (kasegi:39, tameshi:255,
tsukuroi:263), but the rule repairs 34 of 119 unresolved subjects (21+37+61 base, 5+28+52 after) and **no lane changes status**: all 10
FAIL lanes before the rule are FAIL after it, all 8 PASS lanes stay PASS
(`--check trigger.command_binary_resolves --json`, both trees). tsukuroi's residual is dominated by the 17
`PASS healthy: …` output lines and the two mid-line-pipe segments of the very `exit map:` line that follows
the repaired `TSUKUROI_CENSUS:` line.

## 4. Counter face

- Frozen v1 (`verifiers/check_infoless_fences.py`, sha `b3dbe72f…`) scores LEADING **120 of 120, exit 0**
  (`--repo …/KotobaR57.CtlC2CharShortcuts --rev f5505ff…`). v1 has classes P1–P5/H1–H5 only
  (`verifiers/check_infoless_fences.py:28-57`) — it never puts U+2192 in a command line, so it cannot see
  the rule's arrow hole. The control receipt's 120/120 is true and uninformative.
- v2 (`w0/check_infoless_fences_v2.py`, sha `8e388382…`) with `--seed 11`: **80 of 88**, and all 8 wrong
  cases are H8 (`wrong 11 H8 … status=PASS`, 4 classes × 2 twins). H8 exists exactly because the rule text
  says "outside quotes" and the code does not implement it.
- v2's diff guard flags the control's patch itself: `instrument diff guard: 3 suspicious added line(s)`
  (`infoless = not info.strip()`, the skip call, the fallback). Any natural implementation naming a local
  `infoless` trips K>0 — a false positive a v3 guard should scope to behaviour, not identifier text.

## 5. Frequency ranking (what a later round should key on first)

Ranked by real incidence in the 83 info-less lines and the 119 unresolved subjects, not by the counter's
classes:

1. **Multi-word `key: value` / `PASS healthy: …` output and mid-line `|` segments** — 31 lines, 52 residual
   subjects in tsukuroi alone. No clause catches it. This is the shape the claim exists to fix.
2. **Space-aligned tables with no pipes** — 18 rows in tameshi (1044-1049, 1173-1178, 1404-1409).
3. **Non-ASCII formula/output lines** (`×`, `−`) — 4 lines in kasegi (828-832); LEADING dropped the
   NONASCII clause that would have caught them, and the `+` clause skips only line 831 of the block.
4. **U+2192 inside quotes in a command line** — 0 in the corpus, 8 of 8 v2-H8 cases per seed wrong. Latent
   in the corpus, fatal to the counter.
5. **First token ending `:` followed by a real command** (`: … && cmd`) — 0 in the corpus; 1 probe.
6. **Leading `|` / `||`** — 0 in the corpus; 2 probes. Merged continuations make it mostly inert.
7. **Leading `+`** — 1 corpus line, correctly skipped.
8. **Leading box-drawing** — 0 in the corpus, and the 7-char set is wrong for the drawing styles that
   actually appear in boxes elsewhere (`╭ ╰ ┬ ┴ ┼ ━ ┃ ┏ ┗ ╔ ╝`): 3 probes still FAIL.

## 6. Impacted axes

- **operability (primary)**: the rule meets the synthetic predicate and leaves every decorated lane red;
  the counter's PASS classes always inject a resolvable command, so a rule can score 120/120 while the real
  check still FAILs 52 subjects. The predicate as frozen cannot certify the claim's own purpose.
- **calibration**: the five clauses fire 24 times on real text and 0 of those are shell lines — the family
  is keyed to the counter's synthetic classes (tables, boxes, arrows) that the lane corpus barely contains,
  and blind to the shape it contains most (`PASS <word>: …`).
- **regression surface**: skipping before heredoc tracking converts base PASS to FAIL (one probe); the
  quote-blind arrow converts a true FAIL to a false PASS (v2 H8, 8/8 per seed).
- consistency/adjacency/depth: untouched (no C1 content, no counter/fixture edits by this seat).

## 7. Smallest safe correction (redesign inputs, in order)

1. Make the arrow clause quote-aware (single and double quotes, backslash escapes) and skip only outside
   quotes. Without this the rule cannot pass v2's H8 at all.
2. Evaluate the skip after heredoc state is established, or still call `heredoc_delimiter` on a line the
   rule skips, so a skipped opener keeps suppressing its body.
3. Replace `LEAD_STRUCTURAL` with the full U+2500–U+257F range plus U+2550–U+256C (heavy/double), or a
   `unicodedata`-style "box drawing" test; the 7-char set is a silent hole.
4. Add real shapes to the counter before re-freezing — a class for `<KEY>: <A>|<B>|<C>` (mid-line pipes,
   tsukuroi:263-264), a class for `PASS <word>: <text>` two-word keys (tsukuroi:275-291), a class for
   space-aligned no-pipe tables (tameshi:1044-1049), a class for `×`/`−` formula lines (kasegi:828-832),
   and a twins/hard-negative arm that puts a *decorative* line next to a *missing* command in the same
   fence (`ls -la` + `: "${X:?}" && <bogus>`; `ls -la` + `<bogus> "<tok> → <tok>"`), which is the only way
   to see both failure modes at once.
5. Score the rule on the three live lanes, not only on generated cases: an exit-0 predicate that leaves
   kasegi, tameshi and tsukuroi FAILing does not measure the claim.

## 8. Not run / limits

- No fix was written and no counter or fixture edited; the LEADING tree is a byte copy of the control's
  sandbox blob, used read-only for probes.
- I did not re-run the counter's `--self-test` for the LEADING variant (the control reports 0 failures over
  1852 assertions).
- The census counts only fences whose info string is in `FENCED_INFO`; `text`/`json`/`yaml` fences are
  invisible to the instrument and therefore to this rule, by design.
- Three lane dirs have no SKILL.md (`audio-`, `game-dev-2d-`, `revenger-shokunin`), so the "20 sibling
  files" in the brief is 18 here; the scan covered all 18.
- No tool installs were needed; no pacman transaction was attempted.
