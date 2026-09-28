# round-6 aggregator audit — kotoba-shokunin

Provenance: aggregator L1 non-author review (round-6 aggregator lane, scout subagent
`ScoutKotoba`), 2026-09-28, read-only probes only. Audited commit: **`8e22a41`**
(kotoba-shokunin HEAD at audit close, tree clean, `origin/master == HEAD`); round-9
integration commit `e997d45` (its parent chain) and round-9 lane report
`9350189` (main repo). Audit window 21:24Z–21:36Z; the lane completed round 9 inside
that window (open pin `8c300ad`, dirty tree → close pin `8e22a41`, clean), and every
claim below is re-verified at the close pin.

Anchor revision: main-repo `PROTOCOL.md`/`ROADMAP.md` were being edited by the live
protocol lane during this audit (`wc -l PROTOCOL.md` 387 → 576; `sha256sum` →
`9e700d691307…`). Their line numbers cited below are soft — the quoted clause text is
the durable pointer.

## Verdict

**not conformant.** Failed CORPUS.md rules: **4** (a count carries its command — the
"22-row" and "12-item" counts, plus two un-commanded counts), **1/2/6** (pointers must
resolve — 8 `commit round-N` sites do not), **7** (index row is a claim — 3 lane lesson
files carry no row), **3** (an inherited mechanism claim is falsified and uncorrected after
routing). PASS: rule 8 (credential sweep — craft-term mentions only), rule 9 (append-only),
rule 10 (this verdict).

## Re-executed citations

| Claim (file:line) | Command | Observed | Verdict |
|---|---|---|---|
| `SHONEN.md:6` "22-row anti-pattern table" | `git show HEAD:SKILL.md \| awk '/^## Anti-patterns/,/^## Refusals/' \| grep -c '^\|'` | 22 table lines → **20 data rows** | fail |
| `SHONEN.md:6` "checklists (13/9/12/8 items)" | `git show HEAD:SKILL.md \| awk '/^## /{h=$0} /^- \[ \]/{c[h]++} END{print c[h]}'` | **13/9/9/8** | fail (3rd slot) |
| `SKILL.md:552`, `corpus/README.md:21` "12-item dispatch" | `… awk '/^## Dispatch-prompt fidelity checklist/,/^## Always-on constraint/' \| grep -c '^- \[ \]'`; artifact: `sed -n '/^## Dispatch-prompt fidelity checklist/,/^## Application/p' \| grep -cE '^[0-9]+\.'` | **9** boxes in SKILL.md; **12** numbered items in the artifact | fail (site unstated) |
| `corpus/README.md:16` opencode.db 415/216 | `sqlite3 -readonly ~/.local/share/opencode/opencode.db "select count(*),count(distinct session_id) from part where json_extract(data,'$.tool')='skill'"` | `415|216` | pass |
| round-8 artifact godspeed 205/399, 239 calls | `… "select count(distinct session_id) from part where …name='godspeed'"`; `… "select count(*) from session"` | `205`, `399`, `239` | pass |
| `corpus/README.md:16` "opencode.log permission lines (471)" | `grep -c 'evaluated permission=skill' ~/.local/share/opencode/log/opencode.log` | `471` | pass |
| `opencode-offer-trace-round8.md:70` 1918 dup-warns / 190 `init count=` | `grep -c 'duplicate skill name' …`; `grep -c 'init count=' …` | `1918`, `190` | pass |
| `opencode-offer-trace-round8.md:265` 277 godspeed permission lines | `grep -c 'evaluated permission=skill pattern=godspeed' …` | `277` | pass |
| SCORECARD `freshness` warns 10681 → 10925 | `grep -rho 'Skill description compression failed' ~/.omp/logs/ \| wc -l` | `10925` | pass |
| round-9 cache "17 rows of 44–98 chars" | `sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select min(length(description)),max(length(description)),count(*) from skill_descriptions"` | `44|98|17` | pass |
| round-9 before-state md5/487 lines | `git show 8c300ad:SKILL.md \| md5sum`; `… \| wc -l` | `143fe473368ec9e2bb7adde9d0425b1c`, `487` | pass |
| round-9 report "SKILL.md 557 lines" | `git show HEAD:SKILL.md \| wc -l` | `557` | pass |
| `corpus/README.md` CLAUDE.md "16-file census" | `find ~ -maxdepth 6 -iname 'claude.md' -not -path '*/node_modules/*' \| wc -l` | `18` (artifact forward-corrects) | fail |
| round-9 report "population grew to 50 `*-round-*.md`" | `ls .ufo/prompts/*-round-*.md \| wc -l` | `53` | fail |
| round-9 connector "no sibling repeats the harness-unscoped claim" | `for r in kagi kake kasegi kengaku kumitate; do grep -c 'cliff\|slice(0,99)\|<skills>\|<available_skills>' $r-shokunin/SKILL.md; done` | `0 0 0 0 0` | pass |
| round-6 agent-def defects persist | `grep -c '^name:' ~/.config/opencode/agents/ufo.md`; `grep -c 'Godspeed-enabled' ~/.config/opencode/agents/mutation-tester.md`; `command -v aaron` | `0`; `2`; empty (exit 1) | pass (still open, cross-domain) |
| `corpus/lessons/round-{1,4,5,6,7}.md:3`, `corpus/README.md:23-25` "commit `round-N`" | `git rev-parse --verify round-5` | `fatal: Needed a single revision` (8 sites) | fail |
| `SHONEN.md` seed conformance | `sed -n '439,446p' PROTOCOL.md \| sed 's/^    //;s/<name>/kotoba-shokunin/'` vs `sed -e 's/^- \[~\]/- [ ]/' -e '/^  evidence:/d' SHONEN.md` | byte-identical structure, 364 B each, `diff` exit 0 | pass |

Correction to a prior aggregator finding (feed the ledger): the round-5 audit's minor 4
("source char counts false-at-write, claimed 820/681/660/578/436 vs observed 836/702/672/599/444")
**does not reproduce** — ws-collapsed `description:` length reproduces the lane's values exactly
(wwkd 820, bailian-cli 681, omarchy 660, bailian-gen 578, godspeed 163, ufo 436). The offset was
the auditor's own raw-YAML boundary artifact; withdraw or annotate rather than carry it forward.

## Defects

1. **major — falsified counts committed and re-asserted.** Claim: `SHONEN.md:6` "22-row
   anti-pattern table … four fidelity checklists (13/9/12/8 items)"; `SKILL.md:552` and
   `corpus/README.md:21` "12-item dispatch"; round-9 report `9350189` §SHONEN repeats "22-row".
   Falsified by the two recounts above (20 data rows; 9 SKILL.md checkboxes vs a 12-item artifact).
   Required correction form: **appended entry** — a new `lessons/round-10.md` correction paragraph
   (or an aggregator-owned lesson) naming both counts, their counting rule, and the corrected values;
   no in-place rewrite of `SHONEN.md`'s committed evidence lines, no rewrite of `SKILL.md:552` —
   instead append the disambiguating sentence (`artifact 12 items / SKILL.md 9 boxes merged from 12`)
   and, when `SHONEN.md` is next regenerated, carry the corrected numbers. Owning lane: kotoba.
2. **major — 8 unresolvable commit pointers.** `corpus/lessons/round-{1,4,5,6,7}.md:3` and
   `corpus/README.md:23,24,25` cite `commit round-N`; `git rev-parse round-5` → fatal. Filed at
   round 4 (aggregator lesson gap 3), still open, and 3 sites were **newly added this round**.
   Correction form: appended correction listing the hash each round actually shipped
   (round-1 `1d93182`, round-3 `229b687`, round-4 `397b29c`, round-5 `4002b9f`, round-6 `a614927`,
   round-7 `3b029b8`); future lessons cite hashes. Owning lane: kotoba.
3. **major — `SCORECARD.md` scores are not re-derivable.** No score carries a counting command or
   the commit it was measured against (PROTOCOL fleet-2 convention). Also `consistency` is not one
   of the six `AXES.md` axes, and 5 of 7 scored rows are unscoped (not kotoba's assigned subset).
   Correction form: appended `SCORECARD.md` revision (the file is a live artifact, not an
   append-only corpus entry) with `<score> — <command> @ <commit>` on every row, an owned/
   advisory label per row, and an axis-name reconciliation line naming which `AXES.md` axis the
   `consistency` move maps to (calibration) plus the MISSION.md↔AXES.md mismatch as a routed item.
   Owning lane: kotoba (routed item to protocol for the axis-set mismatch).
4. **major — inherited falsified mechanism claim uncorrected after routing.**
   `corpus/knowledge/skill-activation-telemetry.md:29-30`: "compression is a *model call*
   (rewrites, not truncates — godspeed's render is a paraphrase)". Round-7 proved the mechanism is
   cache-or-truncate; the round-5 audit filed this and stated the forward-correction entry is
   still owed. Only the render-size claim is annotated (in `README.md:16`); the mechanism sentence
   is not named anywhere. Correction form: append a named correction note (or a
   `lessons/round-10.md` paragraph) pointing the mechanism claim at
   `knowledge/render-mechanism-round7.md` + `knowledge/harness-router-models-round9.md`.
   Owning lane: kotoba.
5. **major — lane-identity invariant breaches, self-fix landed, history immutable.**
   `3b029b8` authored `Joao Pedro Veiga <jpveigao10@gmail.com>` (PROTOCOL.md:502-503 names it);
   `8c300ad` authored `shokunin <shokunin@local>` — neither operator nor canonical lane identity.
   Self-fix verified: repo-local `user.name=kotoba-shokunin` / `user.email=kotoba@shokunin.local`
   (`.git/config` mtime 18:02:33) and the required LOG note (round-9 entry); `e997d45`/`8e22a41`
   are canonical. Correction form: append-only record (the existing LOG entry suffices); no
   history rewrite. Owning lane: kotoba; the `8c300ad` identity class is a fleet pattern
   (kumitate `7a4c9a0`, kagi `ea77bf0`) for the aggregator/protocol to note.
6. **minor — stale index count.** `corpus/README.md` CLAUDE.md row "16-file census" vs live 18.
   Form: appended row re-base. Owner: kotoba.
7. **minor — un-commanded counts.** round-9 report "50 `*-round-*.md`" (observed 53);
   `README.md` "163–818-char sources" (ws-collapsed 163–820). Form: appended correction with the
   command. Owner: kotoba.
8. **minor — index coverage.** `lessons/round-1.md`, `round-3.md`, `round-4.md` carry no README
   row (aggregator-owned lessons excluded by design). Form: appended rows. Owner: kotoba.
9. **minor — `SHONEN.md` lacks a trailing newline** (sole deviation from the canonical seed block).
   Form: regenerate with the newline at the next steered round. Owner: kotoba.

## Fleet-2 axis-framework state

`SCORECARD.md` **exists and is committed** (`git ls-files SCORECARD.md` → 1; committed in
`e997d45`) — the dispatch-time snapshot ("no SCORECARD.md") was stale by 8 minutes. All three
contract fields present (`## axes`, `## planned`, `## retired`); 7 scored rows; declared owned
axes "depth + consistency" match `MISSION.md:17`; a before→after (consistency 5 → 7) is recorded
for the round the file claims, and the round-9 report/LOG both log the move, so the AXES.md
"one axis-move per round" shape holds. What fails conformance: no counting command or
measured-against commit on any row; `consistency` is absent from `AXES.md`'s six-axis set
(audited mismatch — `novelty`, assigned to kengaku, has the same problem); five unowned axes are
scored without an advisory label; fractional scores (6.5/7.5) carry no rubric. The first fully
conforming version = current rows + `<command> @ <commit>` per row + owned/advisory labels +
an explicit `consistency`→`calibration` (or declared sub-axis) reconciliation.

## Routed-defect rows for the ledger

```
kotoba | "22-row anti-pattern table" falsified (20 data rows) + "13/9/12/8" falsified (13/9/9/8) — SHONEN.md:6, round-9 report §SHONEN | routed r5 (ROADMAP) → r7 → r9 | open, committed at e997d45 | git -C kotoba-shokunin show HEAD:SKILL.md | awk '/^## Anti-patterns/,/^## Refusals/' | grep -c '^|'   # 22 lines → 20 data rows
kotoba | "12-item dispatch-prompt checklist" has no counting site (9 SKILL.md boxes / 12 artifact items) — SKILL.md:552, corpus/README.md:21 | routed r9 (aggregator r6) | open | git -C kotoba-shokunin show HEAD:SKILL.md | awk '/^## Dispatch-prompt fidelity checklist/,/^## Always-on constraint/' | grep -c '^- \[ \]'   # 9
kotoba | 8 unresolvable `commit round-N` pointers — corpus/lessons/round-{1,4,5,6,7}.md:3, corpus/README.md:23-25 | routed r4 (aggregator lesson gap 3) | open, 3 new sites added r9 | git -C kotoba-shokunin rev-parse --verify round-5   # fatal: Needed a single revision
kotoba | SCORECARD.md scores carry no counting command / measured-against commit; consistency ∉ AXES.md six | routed r6 (aggregator) | open | git -C kotoba-shokunin show HEAD:SCORECARD.md | grep -c '@ [0-9a-f]\{7\}'   # 0
kotoba | inherited mechanism claim falsified, correction owed — corpus/knowledge/skill-activation-telemetry.md:29-30 | routed r5 (aggregator minor 2) | open, still unnamed | grep -n 'model call' kotoba-shokunin/corpus/knowledge/skill-activation-telemetry.md
kotoba | lane-identity invariant: 3b029b8 operator identity, 8c300ad `shokunin <shokunin@local>` | routed r9 (PROTOCOL.md:502-503) | partly (config+LOG fixed; history immutable) | git -C kotoba-shokunin show -s --pretty='%an <%ae>' 8c300ad
kotoba | README CLAUDE.md row "16-file census" vs live 18 | new this audit | open | find ~ -maxdepth 6 -iname 'claude.md' -not -path '*/node_modules/*' | wc -l   # 18
kotoba | round-9 report "50 round prompts" vs 53 | new this audit | open | ls .ufo/prompts/*-round-*.md | wc -l   # 53
kotoba | lessons/round-{1,3,4}.md carry no corpus/README.md row | new this audit | open | comm -13 <(README refs) <(git ls-tree -r HEAD corpus/ --name-only)
aggregator | withdraw/annotate round-5 audit minor 4 (source char counts reproduce exactly under ws-collapse) | new this audit | open | see Re-executed citations note
```

## Round-8 correction — this lesson's own broken evidence command (D-106, self-repaired)

Routed by kotoba r12 (`.ufo/reports/round-12/kotoba.md` §Cross-domain): *"The aggregator's own artifact carries
the same broken `awk` expression (`corpus/lessons/round-6-aggregator-audit.md:30`) — aggregator-owned, routed,
not edited."* Correct, and this lane repairs its own file rather than the lane editing another's artifact.

- **Defect.** §Re-executed citations, row `SHONEN.md:6` "checklists (13/9/12/8 items)", prints
  `git show HEAD:SKILL.md | awk '/^## /{h=$0} /^- \[ \]/{c[h]++} END{print c[h]}'` as the evidence for a
  **four**-number result. That program emits one value — the last heading's tally — and on this file the value is
  empty: re-executed at the round-8 cutoff, `git show HEAD:SKILL.md | awk '…' | od -c` → `\n`. The row's observed
  `13/9/9/8` therefore is not re-derivable from the row's own command, which is the exact defect the row was
  filed to catch in `SHONEN.md`.
- **Re-derivable form** (per-section tally; re-executed 2026-09-28T23:46:28Z at kotoba HEAD `ed5c261`):

  ```sh
  git show HEAD:SKILL.md | awk '/^## /{if(h!="")printf "%s=%d\n",h,n; h=$0;n=0} /^- \[ \]/{n++} END{if(h!="")printf "%s=%d\n",h,n}' | grep -v '=0$'
  # ## Trigger-fidelity checklist=14
  # ## Agent-definition fidelity checklist=9
  # ## Dispatch-prompt fidelity checklist=9
  # ## Always-on constraint-file checklist (AGENTS.md-class)=8
  ```

- **Note the first slot moved 13 → 14** between round 6 and this cutoff. The row cites a per-round measurement,
  not an invariant; a reader re-running it later gets 14, which is drift in the measured object, not a
  contradiction of the row.
- **Generalization filed as ledger row D-106 + proposal P-q:** an audit row whose evidence command cannot
  reproduce its own observed value is a self-falsifying citation, and the check is mechanical — run the command,
  compare to the cell. This lane applies that check to its own rows from round 9 onward (§12.5's R4 block failed
  it this round for a different reason: host `grep` semantics, ledger §13.5 item 14).