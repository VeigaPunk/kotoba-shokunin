# RuleKengaku — D3 fact base, kengaku row (round 50 build)

**RULING: `adjacent` holds for kengaku under precedence (a) and under (b) as written; only a widened
reading of (b) ("any cwd-parameterised counter over a SKILL.md") flips it to `contested`, and that rests
on a wave report, which kotoba's census rule excludes as a scope surface. The premise "kengaku's script
counts trigger strings in other lanes' SKILL.md" is not supported by the pinned script.**

Subject: kengaku-shokunin at pin `1f3b0f1ec41ec297130e8944ff97968d32324632` and at the current tip
(identical, §4). No lane file was written; scratch copies only.

## 1. Kengaku's committed scope surfaces: no claim to write or audit other lanes' skill files

- "Sibling arbitration: kotoba owns prompt and skill craft (kengaku keeps only measured capability
  effects); kumitate owns OMP route resolution and fallback policy; kama owns local endpoint health and
  identity; chousa owns research method; tameshi owns verification-fixture craft." — `SKILL.md:3`
  (frontmatter description; kotoba named first, retained half is capability effects).
- "prompt- and skill-craft rules — measured capability effects of prompt format stay here; reusable craft
  implications route out (r7 tools-without-system, r11/r12 ack-intent findings)" — `PROVINCE.md:138`
  (§Adjacent, kotoba row).
- "**Refuses:** anything outside this domain; report cross-domain evidence back to the orchestrator rather
  than absorbing it." — `PROVINCE.md:6`.
- "Kotoba owns the craft rule and production render/trigger behavior. Kengaku owns experimental design,
  scoring, and claims about resulting capability." — `corpus/evidence/round9-fleet/sibling-overlap.md:12`.
- "kotoba's province and render artifacts define craft; kengaku's source probe and result summary define
  measured experimental outcomes. Attribution is deliberately split by claim type." — same file `:53`
  (confidence section, rated High).
- "Research-only survey. **Result: no sibling owns an exact replay of kengaku's committed round-8/round-9
  probe evidence.**" — `corpus/evidence/round10-fleet/r10-connector.md:3`; "kengaku's current
  evidence-only scope does not cross it" (shared kake/kotoba assets) — `:60`.
- "Work only within this repo and its PROVINCE.md scope." — `AGENTS.md:3`.

Inventory at the pin: `git ls-tree --name-only 1f3b0f1` → `.gitignore .ufo AGENTS.md LOG.md PROVINCE.md
README.md SCORECARD.md SHONEN.md SKILL.md considerthese corpus grader.py plans`; no `verifiers/`, no
`skills/`, one runnable root artifact (`grader.py`, own bytes). No committed `.sh`/`.py` outside `.ufo`
names a sibling lane root (exit 1, 0 files). Kengaku's only claim over sibling material is reading it as
evidence — connector surveys, `git grep` sweeps over sibling HEADs
(`corpus/evidence/round11-fleet/r11-connector.md:7-9`) — with ownership left in place: "… are
complementary and should remain their owners' scopes" (`:27`). Purpose stated there is eval/novelty
positioning of its own probe evidence: measurement, not craft, not fixture method, not endpoint
verification (endpoint rows route to kama, `PROVINCE.md:136`).

## 2. The instrument behind the row: what `plans/round25_census.sh` actually does

- The cited README row: "| `plans/round25_census.sh` | Round-25 counting script (SOURCES census, new
  rows, mistakes rows, SHONEN form, frontmatter triggers, both instruments' summaries) |" —
  `corpus/README.md:192`, inside the "## What's here" table (`:25-27`, columns `Entry | Covers | Primary
  source`): kengaku's index of its own files, saying "frontmatter triggers" with no sibling qualifier.
- Contract: "# kengaku round-25 census — run from the lane root: sh plans/round25_census.sh" (`:2`);
  "round25_census: cwd is not a lane root (needs SKILL.md and corpus/)" (`:38`). The trigger block
  (`:101-175`) reads the file `SKILL.md` in the cwd: 7 `SKILL.md` tokens, 0 tokens matching any sibling
  lane name or a `../` path.
- Committed receipt: `skill_frontmatter_triggers=6` after, `=0` at base `6180e4f`
  (`corpus/evidence/round25-calibration/round25-census-after.txt:11` and `...-before-6180e4f.txt:11`) —
  the only numbers it committed are kengaku's own description.
- Live parameterisation (scratch only): the script over a copy of kotoba's `SKILL.md` prints
  `skill_frontmatter_triggers=8`; over kengaku's own, `=6`.
- Origin of "other lanes": kengaku's round-25 seat predicted sibling readings — "chousa 5, mori 5,
  kotoba 8, lore 5, tameshi 0 (all five have SKILL.md + corpus/)" — and justified YAML awareness because
  "fleet descriptions use a `"…"` scalar … a `>` block holding `"…"` triggers (kotoba, lore) …"
  (`.ufo/waves/round-25/build/CensusScriptExec.md:44` and risks section). That is a wave report; kotoba's
  own rule excludes wave reports as scope surfaces
  (`corpus/knowledge/sibling-overlap-census-round49.md:54`).

So the bytes support: "counts quoted trigger strings in the frontmatter description of the lane-root
SKILL.md; takes the lane root from cwd, so it can be pointed at another lane (a seat predicted kotoba 8,
reproduced)" — not "counting other lanes' trigger strings"; no kengaku surface says it is for siblings.

## 3. Stated split on either side over the same artifact or function — yes, both sides

- Kotoba: "Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts /
  system prompts for trigger fidelity and decision density." — kotoba `SKILL.md:4-5`.
- Kotoba: "Sibling boundary: the five `*-shokunin` domain skills (kagi, kake, kasegi, kengaku, kumitate)
  own their own SKILL.md content — this skill audits and reports; fixes route to the owning lane." —
  kotoba `SKILL.md:10-12`.
- Kotoba: "kengaku keeps measured capability effects of prompt format, kotoba owns the craft rules
  (kengaku description, `SKILL.md:3`)" — kotoba `PROVINCE.md:46`, the row carrying the unruled census
  clause.
- Kengaku: `SKILL.md:3`, `PROVINCE.md:138`, `sibling-overlap.md:12,53` above.

The split covers who writes/owns each lane's SKILL.md, who audits it cross-lane, and where "production
render/trigger behavior" sits (kotoba); it never allocates trigger-string counting to kengaku, whose
retained half is capability effects.

Contradiction inside kotoba's round-49 record: the seat that produced the row says the opposite of its
open clause — "It does not write or audit another lane's `SKILL.md`, prompts, or `AGENTS.md`, and owns no
instrument over those surfaces" (`.ufo/waves/round-49/build/CensusKengaku.md`, finding 1) — while the
census note says "kengaku's round-25 census script counts trigger strings in other lanes' SKILL.md files,
kotoba's included … a possible `contested` element, recorded for the integrator; the row stays `adjacent`"
(`corpus/knowledge/sibling-overlap-census-round49.md:162-165`). The README row never says "other lanes";
the seat report never mentions the script.

## 4. Pin versus tip: nothing relevant changed

- `git rev-parse HEAD master origin/master` → the same hash three times; `git symbolic-ref -q HEAD` → exit
  1 (detached). `git status --porcelain | wc -l` → 0; `git diff --stat 1f3b0f1 HEAD | wc -l` → 0.
- `hyaku/s3-kengaku-containment` 6a2c2df and `round29/R29ExecCore` 31934e5 are both ancestors of the pin
  (`git merge-base --is-ancestor`, exit 0 each). Commits outside the pin touching these paths live only in
  jj keep refs, and the diff against one is empty. kotoba already pins this commit
  (`PROVINCE.md:46`; census row 78), so the row's commit is current.

## 5. Rulings under the two candidate precedences

**(a) A stated split covering the same function decides `adjacent` → `adjacent`.** Both sides state a
split over the artifact (lane SKILL.md content and description) and over the trigger/render function: the
owning lane writes its SKILL.md, kotoba audits and reports cross-lane, kengaku retains only measured
capability effects. A trigger-string census is not a capability effect and kengaku claims no such
function. Confidence: high.

**(b) Any claim over kotoba-core instruments decides `contested` → `adjacent` as written.** No claim over
a kotoba-core instrument exists: kengaku never names kotoba's `verifiers/` (census guard, dispatch-prompt
instrument, floors registry), has no path into a kotoba tree, and its script's object is the cwd's own
SKILL.md. Confidence: medium-high.

Boundary that flips it, so the integrator chooses deliberately: if (b) is implemented as "any committed
instrument whose input is a SKILL.md frontmatter description and which runs from a sibling root", then
kengaku's counter qualifies on cwd parameterisation plus the seat's predicted `kotoba 8`, and the row
becomes `contested`. I recommend against that reading: (i) the only evidence of sibling intent is a wave
report, excluded by `:54`; (ii) the committed receipt records only kengaku's count (0 → 6); (iii) the same
shape describes tameshi's and kama's open items, so the precedence flips more rows than D3 names; (iv)
kotoba's own guard reads all sibling `SKILL.md` files at their pins
(`verifiers/check_sibling_census.py`), so "reads a sibling SKILL.md" cannot itself be the discriminator —
a claimed function over the artifact must be, and kengaku claims none.

## 6. Remaining unknowns

- Whether kengaku's L1 wants the counter to become a standing cross-lane check: nothing committed says
  so; its seat framed sibling readings as a one-off post-integration check.
- Whether the open clause is kept. If kept, its wording should match the bytes (§2): the current "counts
  trigger strings in other lanes' SKILL.md files" asserts more than the pinned script does, and kotoba's
  own seat report already said the opposite.
- No semantic trace applies: subjects are Markdown and POSIX sh, so every quote is a pinned `git show`
  byte (literal fallback; no LSP server answers `.md`/`.sh`).

## Evidence (exit codes verbatim)

- `git -C kengaku-shokunin rev-parse HEAD master origin/master` → three identical hashes, exit 0;
  `git status --porcelain | wc -l` → 0; `git diff --stat 1f3b0f1 HEAD | wc -l` → 0.
- `git -C kengaku-shokunin ls-tree --name-only 1f3b0f1` → 11 entries, no `verifiers/`, no `skills/`.
- `git -C kengaku-shokunin grep -l -E 'Projects/shokunin/[a-z0-9]+-shokunin' 1f3b0f1 -- '*.sh' '*.py'
  ':!.ufo'` → exit 1, 0 files.
- `git -C kengaku-shokunin show 1f3b0f1:plans/round25_census.sh | grep -cE
  'shokunin|\.\./|kotoba|chousa|tameshi|kama|kagi|kumitate|kake|kasegi'` → 0, exit 1; `| grep -o
  'SKILL\.md' | wc -l` → 7. `show 1f3b0f1:SKILL.md | grep -c kotoba` → 1; over `PROVINCE.md` → 5.
- Scratch probe under `/fast/scratch/hyaku/kotoba-r50/build/RuleKengaku/`: kotoba `SKILL.md` copy →
  `skill_frontmatter_triggers=8`, exit 0; kengaku `SKILL.md` copy → `=6`, exit 0.
- `git -C kengaku-shokunin merge-base --is-ancestor 6a2c2df 1f3b0f1` → exit 0; same for `31934e5` → 0;
  `git diff --stat 1f3b0f1 4e5e6d8 -- corpus/README.md SKILL.md PROVINCE.md plans/round25_census.sh` →
  empty, exit 0.
- Tool installs: none. Web fetches: none.
