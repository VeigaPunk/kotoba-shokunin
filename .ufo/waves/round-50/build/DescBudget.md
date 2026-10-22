# DescBudget — C1 no-harm map (kotoba round 50, build)

**Result: NO-HARM-BOUNDED.** At `f3046466` no instrument reads or pins kotoba's own
`SKILL.md` description bytes or frontmatter. Three pins touch `SKILL.md` bytes at all
(checklist box map, `PINNED_BOX_SHA`, the line-budget box); all three read body box text
only, and 0 of 3 move under a +150-char, +2–3-line description edit. The edit stales 10
prose sites (5 of them count claims), none machine-checked. Budgets: 537/600 lines
(63 spare) and 814/~1024 description chars (~210 spare). The round-50 Q25 guard is new
code — at base the census instrument has no `--skill` flag and exits 2.

## Map

| file:line | what it reads | effect of the edit | action |
|---|---|---|---|
| `verifiers/verify_skill_checklist.py:2322-2327`, `1222-1237` | whole `SKILL.md`; frontmatter needs non-empty `name:`/`description:`; prints `description N chars`; **no maximum** | PASS. Only the printed char count changes | none |
| `verifiers/verify_skill_checklist.py:1255-1273` | `Triggers:` literal or one quoted span in `description` | none while the `Triggers:` line survives; a quote split across folded lines stops matching (masked here) | keep each quoted trigger on one physical line |
| `verifiers/verify_skill_checklist.py:1276-1294` | exclusion vocabulary in `description` outside quoted spans (`Anti-triggers:` qualifies) | none | keep an exclusion marker |
| `verifiers/verify_skill_checklist.py:1502-1519`, `373` | repo-rooted backtick tokens across the whole file, frontmatter included (`corpus/`, `verifiers/`, `opencode/`, `.ufo/`, `../`) | new backticked paths become citation subjects that must resolve; globs (`*-shokunin`) and `$`/`<>` are skipped | prefer bare lane names; no backticked repo paths in the description unless they resolve |
| `verifiers/verify_skill_checklist.py:1322-1342` + `SKILL.md:252` | first integer in a box matching `file … <int> … line(s)` = 600 | 537+N ≤ 600 for N ≤ 63; +3 → 540 PASS. Quote `from box at line 252` becomes 255 (unpinned) | none |
| `verifiers/checklist-baseline.json:3-4,9…,253` | 41 checklist boxes' normalized text sha256, `box_total: 41`, `file: SKILL.md`, normalization rule | none — box text only, no line numbers, no frontmatter | none. **No re-record flag exists**; values are hand-recorded (mismatch prints live vs pinned) |
| `verifiers/verify_dispatch_prompts.py:64,236-243,758-763,782-790` + `PINNED_BOX_SHA:79-82` | repo `SKILL.md`, hashes only the 9 dispatch-prompt boxes (text normalization) | none for a frontmatter edit | only if a dispatch box's text changes: edit `PINNED_BOX_SHA` **and** the map together |
| `verifiers/check_sibling_census.py:340-346,358`, CLI `644-652` | *sibling* `SKILL.md` via `git show <pin>:SKILL.md`; re-derives the sibling's description | none — kotoba's own description is never read; **no `--skill` flag at base** | the plan's Q25 guard is round-50 new code; `--skill SKILL.md` exits 2 at base (evidence below) |
| `verifiers/check_assertion_floors.py:21-23` + `verifiers/floors-registry.json` | instrument self-test counts (10 rows; **no census entry**) | none | D3 registers the census guard; re-record = the registry row + floor (registry is the anchor, no `--record` flag) |
| `verifiers/baseline.json:47-61,129` | live-host omp/opencode pins: `omp.db.rows`, `omp.descriptions.{over_cliff,missing,unmodelled}`, catalogue match | none — kotoba has no copy in any omp/opencode discovery root (globs exit 2) | none; installing a copy would move `omp.db.rows` (named re-record) |
| `verifiers/surfaces-baseline.json:226` | prose mention only; `verify_surfaces.py` reads host surfaces | none | none |
| `verifiers/corpus-baseline.json:58-63` | corpus file/pointer counts | none — `SKILL.md` is outside `corpus/` and never scanned (`verify_corpus_integrity.py:72-73`) | round-50 corpus files get their own count re-record |
| `verifiers/fault_injection_corpus.sh:65` | sha256 of the corpus instrument, not `SKILL.md` | none | none |
| `verifiers/checklist-command-vocabulary.json:19` | command words in checklist boxes | none | none |
| `verifiers/verify_harness_claim*.py`, `harness-independent-scope.json` | live harness recomputation; `SKILL.md` named only as a file convention | none | none |

Prose anchors / claims that go stale (no verifier validates line numbers in kotoba's own files):

| file:line | content | effect | action |
|---|---|---|---|
| `corpus/knowledge/sibling-overlap-census-round49.md:39` | `../SKILL.md:12-15` (unpinned) for the "not in a discovery root" note | the note moves down by the inserted lines (12-15 → 14-18 at +2) | append a re-anchor in the round-50 section; do not rewrite round-49 text |
| `…-census-round49.md:51` | `SKILL.md:10-12` **at `a5adc146`** | stays true (commit-pinned) | none |
| `…-census-round49.md:117` | "names five siblings (kagi, kake, kasegi, kengaku, kumitate) and not kotodama" | count stale | appended section states 9 of 9 |
| `corpus/knowledge/frontmatter-rule-authorities-round48.md:49` | budget box cited as `SKILL.md:246` | **already stale**: box at 250 @ `c48793d`, 252 @ base (frontmatter unchanged since `887b6af`; body lines moved it) | pre-existing; usable as the round-50 mined instance, or re-anchor in the appended note |
| `corpus/knowledge/sibling-description-rewrites-round8.md:51` | "kotoba's own 814-char description" | measured 814 now; ~964 after the edit | record the new count in round-50 knowledge; keep the round-8 trail |
| `corpus/knowledge/render-mechanism-round7.md:22` | quotes the opening sentence only | survives if lines 4-5 stay byte-identical | keep the opening sentence untouched |
| `PROVINCE.md:17`, `:23` | "kotoba's own description names 5 of 20 siblings" (two live claims) | stale count | update with the claim; table rows `:43`/`:45` stay true (kake/kasegi still named) |
| `corpus/README.md:121` | same "names 5 of 20", inside a block labelled "Round 49 (append-only)" | stale; in-place rewrite breaks the block's own convention | append the round-50 correction |
| `SCORECARD.md:34`, `:118` | adjacency row; "Next: round 50" candidate (same 5-of-20 phrasing) | stale phrasing; nothing pins the text | D4's qualifier + claim landing |
| `.ufo/round-33/SKILL.md:4-15` | tracked fixture copy of the old `SKILL.md` | **already diverged** (`0404fdc…` vs current `f290e89…`); read only by round-47's falsify XML sweep, by no gate | leave; do not re-sync |

## Budgets measured

- Lines: `537` vs the box's `600` → `PASS trigger.line_budget: evaluated 537 — 537 lines within budget 600 (from box at line 252)`, exit 0. Headroom 63; +3 lines → 540.
- Description value: `814` chars whitespace-collapsed (matches the round-8 "814-char" record); folded block occupies lines 3-15, fences 1-16. +150 chars → ~964 against the documented 1,024-character maximum (`frontmatter-rule-authorities-round48.md:44`, agentskills `MAX_DESCRIPTION_LENGTH`). Kotoba's own instrument enforces **no** maximum (same row records "1025 characters pass").
- Every line added inside the fences shifts every body line anchor at or after line 16 by that amount. Frontmatter is byte-identical since `887b6af`.

## Traps

1. Do not copy the census's anchor form `../SKILL.md:12-15` into `SKILL.md` body or `SCORECARD.md`/`LOG.md`: `strip_token_dressing` reduces it to `../SKILL.md` and `citation_resolve` returns `False` from the lane root (no `/home/vgpnk/Projects/shokunin/SKILL.md`). In `corpus/` files it is unscanned.
2. Appended description lines must be indented two spaces: `description_of` (census `:340-346`) and the YAML flattened view both end the value at a column-0 line starting a new key.
3. No re-record command exists for description bytes anywhere. The only re-record paths nearby: `verifiers/floors-registry.json` (hand-edited, D3) and the `corpus-baseline.json` notes (measured numbers from `verify_corpus_integrity.py --json`).

## Evidence (read-only; no LSP server was started for this Python repo, so file reads are the literal fallback and no semantic claims rest on grep alone)

```
git -C . rev-parse HEAD                                  -> f3046466...5a8
wc -l SKILL.md                                           -> 537
python3 -B verifiers/verify_skill_checklist.py --check trigger.line_budget
  -> PASS ... 537 lines within budget 600 (from box at line 252)   exit 0
git show f3046466:SKILL.md | awk fm | grep -oiwE '<9 lanes>' | sort -u | wc -l  -> 5
  names: kagi kake kasegi kengaku kumitate
python3 -B verifiers/check_sibling_census.py ... --province PROVINCE.md --skill SKILL.md
  -> usage error (no --skill)                                     exit 2
python3 - <<EOF  # description value collapse        -> 814 chars
for r in 887b6af c48793d bfd5a58 f3046466: grep -n 'File ≤ 600 lines'  -> 246 250 252 252
diff <(git show 887b6af:SKILL.md | sed -n 1,16p) <(git show f3046466:SKILL.md | sed -n 1,16p) -> empty
sha256sum SKILL.md .ufo/round-33/SKILL.md  -> f290e89… / 0404fdc…   (already divergent)
ls -d ~/.agents/skills/kotoba* ~/.claude/skills/kotoba* ~/.omp/agent/managed-skills/kotoba* \
      ~/.config/opencode/skill*/kotoba* ~/.codex/skills/kotoba*      -> nothing, exit 2
citation_resolve('../SKILL.md', lane_root) -> False ; strip_token_dressing('../SKILL.md:12-15') -> '../SKILL.md'
```

## Remaining unknowns

- The round-50 guard's exact acceptance shape (token list from the census table vs. PROVINCE rows) is CensusGuard's item; my map only shows that nothing else reads the bytes, so a guard bug cannot be masked by an existing pin.
- Whether `SCORECARD.md:118`'s forward note is rewritten or superseded is the claim owner's call (Q19: re-measure, do not copy).
- No tool was installed or upgraded for this seat.
