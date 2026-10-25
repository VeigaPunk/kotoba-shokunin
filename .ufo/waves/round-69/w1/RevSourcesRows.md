# RevSourcesRows — the six appended `corpus/SOURCES.md` rows (S203–S208)

Seat: `L1Kotoba69-2.RevSourcesRows`, leaf, round-69 wave 1 (build+attack), judged on consistency.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, working tree (rows uncommitted; lane tip
`a238989`, base `a5f7459f99bb27bf697e9438362e75ac5833eca8`). Read-only: no file outside this report
was written; the census was run from the fleet-root script (a parser that writes only to stdout).

## Verdict

**Schema: PASS for all six rows. Census: PASS (`exit 0`, `W04` notices only).**
No row-level schema defect — every assigned structural check holds. Three content/consistency
findings follow, all below schema severity; the strongest touches S203's evidence fit.

## 1. Structural check (assigned items)

Parse: `python3` split of lines `corpus/SOURCES.md:144-149`; separator count on the raw line.
`NF=13` in the census (two edge pipes + 11 cells) is met by all six.

| id | cells | literal `\|` | escaped `\|` | status | opened | recheck | used-by (exact cell) | target exists | cited by target |
|---|---|---|---|---|---|---|---|---|---|
| S203 | 11 | no | no | mined | 2026-10-25 | 90d | corpus/knowledge/skill-name-precedence-round69.md | yes | yes (`:1`, `:21`) |
| S204 | 11 | no | no | mined | 2026-10-25 | 90d | corpus/knowledge/skill-name-precedence-round69.md | yes | yes (`:2`, `:22`) |
| S205 | 11 | no | no | mined | 2026-10-25 | 90d | corpus/knowledge/skill-name-precedence-round69.md | yes | yes (`:3`, `:23`) |
| S206 | 11 | no | no | mined | 2026-10-25 | 90d | corpus/knowledge/skill-name-precedence-round69.md | yes | yes (`:4`, `:24`) |
| S207 | 11 | no | no | mined | 2026-10-25 | 90d | corpus/knowledge/skill-name-precedence-round69.md | yes | yes (`:5`, `:25`) |
| S208 | 11 | no | no | mined | 2026-10-25 | 90d | corpus/knowledge/client-trust-gates-round68.md | yes | yes (`:79-82`) |

- `recheck` is a bare cadence (`90d`) in every row; no stripped prose leaked back in.
- `used-by` is a single bare path in every row (no comma list, no trailing text), and each path is
  the entry that names the id. `corpus/README.md:130` and `corpus/lessons/round-69.md` also mention
  S203–S208, but the registry convention excludes the coverage map and the Gate: `corpus/README.md:128`
  cites S198–S202 while those rows' `used-by` is the entry alone.
- Append-only, not a rewrite: `git diff --numstat corpus/SOURCES.md` → `6 0`, one hunk
  `@@ -143,0 +144,6 @@`; `git diff` shows zero removed lines. Nothing above S202 was touched.
- No id collision, no E01–E12: the census run below prints only `W04` and the `ok` line.

### Census re-run (assigned command)

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
    --root /home/vgpnk/Projects/shokunin kotoba
… 18 × kotoba	W04	<id> duplicate url <host/path> across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
EXIT=0
```

Run twice (identical output). 16 of the 18 `W04` are inherited, byte-matching
`.ufo/waves/round-69/controls/census-before.txt`; the two new ones are inherent to the frozen
design, not defects:

- `S207 duplicate url opencode.ai/docs/skills` — S024 holds the same page for a different scope
  (tie-break between two skills whose *descriptions* both match vs. same-*name* precedence).
- `S208 duplicate url …/agent-framework/agents/skills` — D5 deliberately adds a supersede row on
  S201's page; `teaches` carries `supersedes S201`, so the E04 within-scope test stays quiet.

## 2. Findings

### F1 — MEDIUM (S203): the located quote does not carry the same-name condition the row's scope claims; the page has an unshaped, on-point quote, and the page's own ordering qualifies the `mode`/`generic` clause

Evidence, all from the page fetched this round (`/tmp/k69-fetch/roo.html`, 71,129 B, opened
2026-10-25):

- Row `:144` scope: "Roo Code's own documented resolution of **same-named** skills"; `teaches`:
  "a **same-named** project skill beats a global one and a mode-specific skill beats a generic one".
- The anchor's located quote — `"Project skills override global skills, mode-specific override
  generic"` — is verbatim, unshaped (plain inside `<li><strong>Override Control</strong>: …</li>`),
  and inside `What Skills Let You Do`. It says nothing about names.
- The page's `Override Priority` section holds the name condition in **plain, unshaped text**
  (no inline markup in that sentence): "When skills with the same name exist in multiple locations,
  this priority applies (highest to lowest)." (16 words), then
  "A <strong>project</strong> skill always overrides a <strong>global</strong> skill of the same name."
  (the second sentence is shaped; the first is not).
- The same section orders: Project `.roo` mode-specific > Project `.roo` generic > Project `.agents`
  mode-specific > … So "mode-specific beats generic" holds **within a root only**; a Project
  `.roo` *generic* skill outranks a Project `.agents` *mode-specific* one. The row's `teaches`
  states the clause unqualified, and the entry repeats it at
  `corpus/knowledge/skill-name-precedence-round69.md:21` ("a mode-specific skill beats a generic
  one").
- The entry's Limits paragraph justifies the anchor as the "unshaped Override Control bullet
  instead (QUALITY Q42)" — Q42 is indeed satisfied (the chosen quote needs no shaping), but the
  disclosure leaves the reader believing the same-name statement is only available shaped. It is
  not: the 16-word lead sentence of `Override Priority` is unshaped and directly on-scope.

Impact: the row/entry claim is true (the page does state same-name precedence, and the entry is
right that Roo orders by scope), but the *cited* quote does not evidence the scope word, and the
`mode`/`generic` clause as written overstates the page's ordering. Not a schema failure: the
assigned checks (11 cells, quote ≤25 words and present on the page) all pass. Fix if a seat may
touch content: anchor on the unshaped 16-word sentence (or add it), and qualify
`mode`/`generic` as "within one root, mode-specific over generic". The seat cannot edit; this is a
recommendation for the L1/Gate.

### F2 — LOW (S206): declared word count is 12; the quote is 11 words

- Row `:147` (and the same cell in `.ufo/waves/round-69/assimilation/append-block.md:4`,
  `.ufo/waves/round-69/assimilation/validate/corpus/SOURCES.md:147`): `(12 words)`.
- The quote — "the project-level skill takes precedence and the user-level skill is ignored." — is
  verbatim on the page (checked in `/tmp/k69-fetch/junie.html`, context: "If a project-level
  (`<projectRoot>/.junie/skills/<skill-name>/`) and a user-level (…) skills share the same name,
  the project-level skill takes precedence and the user-level skill is ignored.") and is
  **11 words** by both `wc -w` and `split()`. No convention gives 12 (hyphen-splitting gives 13).
- The wrong count is propagated to `corpus/lessons/round-69.md:49` (`(12 words)`).
- Calibration: the registry already carries three off-by-one counts from earlier rounds —
  S199 `(12)` vs 11, S200 `(16)` vs 15, S201 `(13)` vs 14 (audit over all 11 `(N words)`
  annotations in the registry: 7 match, 4 miss). S206 repeats the drift rather than introducing a
  new class, but it is in scope and wrong; the other five new rows' counts are exact
  (S203 8, S204 9, S205 6, S207 8, S208 8).

### F3 — LOW (S208): `scope`/`teaches` describe the repair, not the source; and the `used-by` entry cites S208 only inside its amendment while its body still attributes the approval claim to S201

- Row `:149` `scope`: "the English page's approval-by-default statement …, **quoted to fix the
  S201 row's anchor**". Every other row in the block states a trust scope and ends with
  "one client's implementation, no claim about any other client" (S203–S207); S208 omits the
  limiter and spends the cell on repair bookkeeping. `teaches` likewise ("supersedes S201 — the
  approval sentence is verbatim on the page …") reports the supersede action instead of what the
  page teaches. The census does not test this (E04 only wants `supersedes S###` present when a
  within-scope URL repeats), so it passes cleanly, but it is a template deviation the Gate should
  either adopt for all supersede rows or normalise.
- Traceability: `corpus/knowledge/client-trust-gates-round68.md` cites S208 in the appended
  amendment only (`:79-82`). Its table (`:25`) still attaches "the skill tools require approval by
  default" to **S201** with S201's security-best-practices quote, and its "three shapes" list
  still says "**Approval and review (S201)**" (`:36`). The entry's provenance trio lists five ids
  and its `recheck:` line says "re-fetch each of the five URLs" (`:5`, `:6`), while the entry now
  cites six. So S208's `used-by` is literally satisfied (the path does name the id) but the use is
  an annotation, not a source line — a reader following the body lands on S201. This is the C2/D5
  seam (CritC2Repairs owns the verdict); recorded here because it is what S208's `used-by` rests
  on.

## 3. Quote verification (independent, all six)

Five pages from the round's 07:10 cache under `/tmp/k69-fetch/`; the Microsoft page re-fetched
live (HTTP 200, 156,438 B).

| id | quote verbatim | named section present | words |
|---|---|---|---|
| S203 | yes (`Override Control` bullet) | `What Skills Let You Do`; `Choose a location` lists carry "Roo-specific (higher priority)" | 8 |
| S204 | yes | `Skill Sources and Precedence` | 9 |
| S205 | yes ("If multiple skills resolve to the same name, only the highest-priority one is kept.") | `Scan Locations` | 6 |
| S206 | yes | `Skill location` | **11 declared 12** |
| S207 | yes (third troubleshooting check) | `Troubleshoot loading`; page has no `precedence`/`priority`/`override` rule for names | 8 |
| S208 | yes (live page, twice) | tool-approval section | 8 |

S207's negative claim ("states no precedence") survives an independent scan of the page for
`precedence`, `priority`, `duplicate`, `collision`, `same name`: zero hits; `unique` once (the
quoted troubleshooting check). `Override per agent` on that page is a permissions feature, not a
name rule. No contradiction found.

## 4. Residual risk and verification gaps

1. **No after-census receipt.** `.ufo/waves/round-69/controls/` holds `census-before.txt` (16 W04
   at `a5f7459`) and no `census-after.txt`; rounds 61–65 committed one and their spot-checks read
   it (`corpus/lessons/round-61-verifier-spotcheck.md:120`, `round-63.md:24`, `round-64.md:52`).
   My run above supplies the number the Gate needs (exit 0, **18** W04 = 16 + S207 + S208), and
   the +2 delta is real movement, not noise. Without the file the round's "census before … and
   after" step is asserted rather than recorded.
2. **The recorded pre-append scratch validates a different document.** The lesson says the append
   block was "normalized to the lane's 11-column schema" and validated (`corpus/lessons/round-69.md`
   § "Scratch transformation and validation"), and `assimilation/validate-census.txt` records
   `exit=0`. But that mirror's S203–S207 rows are **tier A** and keep a "page as served 2026-10-25"
   anchor tail, and it has **no S208**; the shipped rows are **tier B** with that tail removed and
   six rows. So the `--file` receipt covers neither S208 nor the shipped tiers. The shipped bytes
   are still clean (my live census, exit 0); the gap is evidence hygiene, and it is the kind of
   stale-scratch divergence the r68 spot-check routed defects were about.
3. **S208 is not in the coverage map.** `corpus/README.md:128` (client trust gates) names S198–S202;
   the new round-69 coverage row (`:130`) names S203–S207. No map row names S208. Consistent with
   "coverage map mentions are not `used-by`", but it means the correction row is invisible to the
   index a reader browses.
4. **Not re-derived here (out of slice):** the campaign staged rows' re-pointing (ConnectorSiblingScan
   / ScoutQuarantine), the C1 counter's own semantics (`RevC1Counter` / `CritC1Semantics`), and the
   C2/D5 verdict (`CritC2Repairs`). I did not run `check_skill_precedence.py`; F1 is about evidence
   fit, not the counter's exit code, and the counter reads the same quote the row carries.

## 5. Tooling

No install or update. Bash, coreutils (`wc`, `diff`, `grep`), `curl`, python3 only.
