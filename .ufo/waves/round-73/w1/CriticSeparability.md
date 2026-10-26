# CriticSeparability — plan attack, round 73 wave 1

**Verdict: REJECT the plan + addendum 1 as frozen.** Two defects are fatal to admission as declared
(one breaks causal separability through a gate that is inside another claim's predicate; one puts a
battery-health reading on the lane's calibration sub-axis). Four are major and fixable before data.
C1's and C2's core constructions survive with the replacements given. All findings are pre-data, so
every correction below is an erratum, not a post-hoc rule change (prompt `:425-435`).

Base state re-verified by me, not taken from the plan: lane tip `072048f` (branch `master`),
`git status --porcelain` shows only `.ufo/waves/round-73/` untracked entries; 142 registry rows;
lane max id `S216`; `verifiers/check_gate_registry.py --rev 072048f…` → `56 of 56`, exit 0.

| # | Claim | Defect class | Severity | Axis harmed if unfixed |
|---|---|---|---|---|
| V1 | C1/C2 → C3 | separability + protocol registry | **fatal** | consistency (C3 unreachable) |
| V2 | C3 | calibration rule / axis label | **fatal** | calibration (mislabeled) |
| V3 | C3 | predicate does not measure the M127 class; no guard count | major | consistency |
| V4 | C3 | guard cap re-set would weaken the gate | major | consistency |
| V5 | C1 | sourced-claim provenance unmeasured (rows already `mined`, 2026-10-23) | major | coverage (evidence predates round) |
| V6 | C1 | coverage map (`PROVINCE.md`) never moves | major | coverage |
| V7 | C1 | frozen-predicate path/column ambiguity | minor | — (non-determinism) |
| V8 | C2 | a listed shortcut world meets the predicate (3 of 3) | major | depth |
| V9 | C2 | line-count guard printed, not counted | major | consistency (SKILL.md:<line>) |
| V10 | C2 | axis name ≠ surface changed; re-score of a held rule | major | depth (lowest-axis duty) |
| V11 | C2 | R1 fallback auto-passes a boundary-less description | minor | — |
| V12 | C2 | R2 case policy unspecified (score flips 2↔3) | minor | — |

---

## V1 — `check_gate_registry.py` is inside C3's six, and C1/C2 add unregistered verifiers

**Plan sentence.** C1: “python3 -B verifiers/check_cn_vendor_surfaces.py --rev <rev> → prints "vendor
skill surfaces backed N of 4"” (C1 predicate); addendum C2: “check_own_description.py --rev <rev> →
prints "own-description rules held N of 3"”. C3 counts `check_gate_registry.py --rev <rev>` among its
six: “the six frozen commands are the r72 set”.

**Rule.** AXES.md:29-31 — “Claims must be **causally separable** — each verifiable without the others
having landed”; PROTOCOL.md:398 — “a child lane's *registry home* is its own `SKILL.md`”;
PROTOCOL.md:418-421 — “closure grades no gate conformant until its registry row exists at the lane's
*registry home*”.

**Counterexample (run).** The registry gate's universe is *every blob directly under `verifiers/`
ending in `.py` or `.sh`* (`verifiers/check_gate_registry.py:19-22`), and it exits 0 only when
`K == M` (`:377-378`). A `--shared` clone at the base, plus one unregistered verifier:

```
$ python3 -B verifiers/check_gate_registry.py --rev 072048f…      # base
gate registry rows conformant 56 of 56 lane verifiers; phantom 0
base exit=0
$ printf '#!/usr/bin/env python3\nimport sys\nsys.exit(0)\n' > verifiers/check_new_counter.py && commit
$ python3 -B verifiers/check_gate_registry.py --rev <new tip>
verifiers/check_new_counter.py               no registry rows naming it: 0 (need 1)
gate registry rows conformant 56 of 57 lane verifiers; phantom 0
tip exit=1
```

Therefore, at the r73 tip (C1 + addendum-C2 landed), that gate is **red** unless both new counters
carry conformant rows — so C3's `N == 6` is a function of C1's and C2's delivery. The addendum
deleted the only instrument that counted those rows (old C2's counted `R`, “registry rows R of R
conformant”, plan C2 predicate), and addendum C2 has no registry clause at all. So the round ships
two gates with no counted registry home and puts the failure inside C3's number. C3 cannot verify
without C1/C2's rows, and a wave-2 seat re-running C3 on a rev with C1's counter but not its row reads
`5 of 6` for a reason the claim does not name.

**Smallest safe correction.** Add the gate's own protocol conformance to each new counter's predicate
and land each row in the counter's own commit:

> C1 adds clause (f): “the tip's `python3 -B verifiers/check_gate_registry.py --rev <rev>` reports
> `verifiers/check_cn_vendor_surfaces.py` conformant (one row, the eight protocol fields); the counter
> prints `registry home ok`”.
>
> C2 adds R4: “`check_gate_registry.py --rev <rev>` reports `verifiers/check_own_description.py`
> conformant”, counted in the printed `own-description rules held N of 4`.

**Commit order that proves separability** (each claim's counter green at its own commit):

1. **C3 commit** — counter fix + addendum + baseline re-record, no new `verifiers/*.py`. C3 measured
   here proves it *without C1 and C2 landed*: `N == 6`, both invocation forms.
2. **C1 commit** — entry, six renumbered rows, snapshots + manifest, `check_cn_vendor_surfaces.py`
   **and its registry row**. C1 measured here proves it without C2 (C2's description edit and
   `check_own_description.py` are absent).
3. **C2 commit** — description + `check_own_description.py` + its registry row, `R3`'s
   `check_sibling_census.py` green either way (`git show` at pinned sibling commits,
   `verifiers/check_sibling_census.py:46,313-320` — a frozen read, not a live one).
   Re-run the battery as no-harm evidence (not claim data).

## V2 — C3 is a battery-health reading wearing the calibration label

**Plan sentence.** “C3 — consistency (calibration sub-axis, owned, 10): the tip battery counter agrees
with the hand run”, predicate “prints "tip battery exit 0: N of 6", exit 0 when N == 6”.

**Rule.** Prompt `:422-423` — “A calibration claim must count mismatches between the lane's
self-assessment (SCORECARD/SHONEN) and observed repo state. It cannot be an assertion.” The lane maps
consistency *onto* calibration in the same row: SCORECARD.md:8-11 — “This lane declares
`consistency` a sub-axis of `calibration` (claim-scope coherence: a claim is scored on whether it says
what it can support, which is self-assessment)”; row text (SCORECARD.md:29) “consistency (calibration
sub-axis)”; PROTOCOL.md:514-516 requires that mapping in the row, so the row is the binding.

**Counterexample.** C3's predicate reads only the six gate exit codes and a guard set. It never opens
SCORECARD.md or SHONEN.md, and its target can be met while both are wrong. Meanwhile the mismatch the
claim is *about* (M127: the r72 receipt's `4 of 6` against the gates' by-hand exits) is exactly a
self-assessment-versus-state mismatch that the predicate does not count. `grep -o 'tip battery[^.|]*'
SCORECARD.md SHONEN.md` → **no match**: the lane records no battery number in its self-assessment at
all, so the calibration framing needs one line added before it can be counted.

**Smallest safe correction.** Keep the mechanism, change the claim object:

> C3 predicate: “`python3 -B verifiers/check_tip_battery.py --rev <rev>` prints `self-assessment
> rows matching M of 2; tip battery exit 0: N of 6; guards G of 5; fleet root <realpath>`, exit 0
> when M == 0, N == 6 and G == 5”, where the two rows are SCORECARD.md's consistency row and
> SHONEN.md's battery box, each of which this round first writes with the measured
> `tip battery exit 0: N of 6` at `<rev>`; M counts any recorded number that differs from the run.

Alternative (also admissible, cheaper): relabel C3 `operability (advisory)` and keep the predicate as
frozen. Then the round's axes are coverage / depth / operability — three distinct — and depth still
carries the lowest-axis duty (C2, subject to V10). Either way the `consistency` row's 10 is not moved
by a gate-health number, which is what the current label implies.

**Third-claim cost.** Prompt `:424` — “Prefer 2 claims. Add a 3rd only if it is independent and cheap
to verify.” C3 is neither independent (V1) nor cheap (V3). Dropping C3 to a routed repair (it is
already “Inherited routed defects” item 1 in the plan) and running 2 claims is the smallest
admissible shape.

## V3 — C3's predicate does not measure the M127 class; `every guard` has no counting line; the two-run form is unpriced

**Plan sentence.** “python3 -B verifiers/check_tip_battery.py --rev <rev> -> prints "tip battery exit
0: N of 6", exit 0 when N == 6 and every guard passes, in each of two consecutive runs on fresh
sandboxes”.

**Evidence (independently re-derived).** The disagreement is *between invocation forms*, not between
two runs of one form:

- `verifiers/check_tip_battery.py:608-610`: `repo = Path(args.repo)`; `fleet = Path(args.fleet) if
  args.fleet else repo.parent`.
- `python3 -c 'from pathlib import Path; print(repr(Path(".").parent))'` → `PosixPath('.')`
  (and `.resolve()` → the lane itself). With `--repo .`, `fleet` is the **lane**, so
  `build_sandbox` (`:181-187`, `for entry in fleet.iterdir()`) symlinks the lane's own entries beside
  the clone instead of the fleet root; every `../` citation dies.
- Receipt `.ufo/waves/round-73/receipts/m127-l1-repro.txt`: run A (`--repo .`) `2 of 6`; run B
  (absolute `--repo`) `4 of 6`. So the class is “two forms disagree”, and a predicate that runs one
  unnamed form twice cannot see a fix that repairs only one.
- Guards are five, and the printed line carries only the gate tally: the base receipt lists
  `no-deletions PASS`, `floors PASS`, `FAIL instrument-size`, `instrument-pin PASS`,
  `spotcheck-identity PASS` — “every guard passes” has no enumerating command in the frozen sentence
  (prompt `:421`: universal clauses need one).
- Cost: base run `wall 153.5s` (receipt). Two runs inside one invocation ≈ 307 s, above the wave
  contract's 300 s per-command bound; two external runs need two receipts, which the predicate's
  “the same sentence in … the receipt” does not allow for.

**Smallest safe correction.**

> “`python3 -B verifiers/check_tip_battery.py --rev <rev>` prints `fleet root <realpath>; guards G of
> 5; tip battery exit 0: N of 6`, exit 0 when G == 5 and N == 6, in **both** invocation forms — `--repo
> .` from the lane and `--repo <absolute lane path>` — one run per form, each with its wall time in
> its own receipt; the printed fleet root must equal the fleet root in both.”

That measures the class, prices each command under the cap, and gives `every guard` a count.

## V4 — re-setting the `instrument-size` cap removes the guard's discrimination; rebase instead

**Plan sentence.** “the `instrument-size` guard, whose cap measured against the r72 base punishes an
honest repair, is re-set by a committed addendum before any C3 data with the arithmetic stated”.

**Evidence.** `verifiers/check_tip_battery.py:102` `BASE = "c69711ee…"  # round-72 base (pinned)`;
`:105` `LINE_CAP = 40`; the guard sums added+deleted lines of the six `BATTERY` scripts only
(`:279-306`). Base receipt: “instruments added 76 / deleted 24 lines (cap 40)” → FAIL. The 76 lines
are **r72's** growth, not this round's; the cap is being asked to absorb history.

**Rule.** PROTOCOL.md:377-379 — “A **gate** is a committed, re-runnable verdict script … A tool that
cannot fail is not [a gate]”; the plan itself promises “weakening-resistance stays in the
`instrument-pin`, `floors`, `no-deletions` and `spotcheck-identity` guards”, and a cap ≥ 76 lets an
instrument be rewritten by 76 lines this round without a verdict.

**Smallest safe correction.** Replace the cap raise with a rebase:

> “the guard's base revision moves to the r73 base `072048f` (the cap stays 40), so `instrument-size`
> measures this round's delta; `floors` is read from the same base and `spotcheck-identity` now treats
> `corpus/lessons/round-72-verifier-spotcheck.md` as a base file (it is compared, not merely
> reported)”.

Arithmetic to state in the addendum: base delta 76+24 lines drops out; the round's fix is one line at
`:610` plus the guard's own base constant = 2 inserted lines ≤ 40.

## V5 — C1's sourced claim can be met by rows opened 2026-10-23; the predicate reads no date

**Plan sentence.** “Every cited page is re-opened this round; the entry's Gate block carries the lane's
own access date and located quotes”, predicate (a)-(d).

**Counterexample (local bytes, no network needed).** The staged package already carries exactly the
shape the predicate accepts, two days old:

```
$ awk 'NR>=18 && NR<=25 {n=split($0,a,"|"); printf "%s cells=%d status=%s opened=%s\n", a[2], n-2, a[9], a[10]}' \
    /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
 S214  cells=11 status= mined  opened= 2026-10-23
 S216  cells=11 status= mined  opened= 2026-10-23
 S218  cells=11 status= mined  opened= 2026-10-23
 S221  cells=11 status= mined  opened= 2026-10-23          (S220 queued; S215/S217/S219 mined)
$ sed -n '1,12p' …/chinese-client-skill-surfaces.md
source: S214 — https://docs.trae.cn/ide_skills — … retrieved 2026-10-23
verified-at: 2026-10-23
recheck: 60d — re-fetch all six pages … (ran 2026-10-23)
```

Predicate (b) checks 11 cells, `status mined`, tier A/B, `used-by`, host — all already true of the
staged rows; (a) checks only that `verified-at:` and `recheck:` *exist*; (c) checks a snapshot pin;
(d) checks a quote in the snapshot. **No conjunct reads the `opened` column** (`corpus/SOURCES.md:12`
has it) or any fetch receipt. So: copy the staged entry, renumber, append the staged rows unchanged,
fetch six snapshots, and the counter reads `4 of 4` with `opened: 2026-10-23` — the round would report
coverage whose evidence was read before the round began. The lane's own row convention already records
provenance in the anchor cell (“fetched 2026-10-23T09:35:04Z, HTTP 200, 15,152 B, sha256 …; exact bytes
`.ufo/waves/round-59/snapshots/S098.page`”, `corpus/SOURCES.md:110`); the predicate ignores it.

**Smallest safe correction.** Add:

> “(e) each cited row's `opened` cell equals the entry's `verified-at:` cell and equals the round's
> capture date `2026-10-25`; each cited row's anchor cell records `fetched <ISO8601>Z, HTTP 200,
> <bytes> B, sha256 <hex>` whose sha256 is the snapshot's; the counter prints `opened this round 6 of
> 6` and any row whose date is not the capture date is exit 2 (could-not-evaluate), never a backed
> vendor.”

## V6 — C1 never moves the coverage map

**Plan sentence.** “**Axis:** `coverage` (8.5). **Surface:** client skill surfaces the lane's maps
(`PROVINCE.md` § Core: …) do not hold”.

**Rule.** Prompt `:436-439` — “A coverage claim names the surface it moves (frontier → core, a new
tool, operation or edge class) and the command that would show it unmoved”; AXES.md:11-12 — coverage
signal: “PROVINCE.md lists every surface; none unexplored without reason”.

**Counterexample.** The predicate's four conjuncts read the entry, `corpus/SOURCES.md` rows,
`.ufo/waves/round-73/snapshots/` and the entry's quotes. `PROVINCE.md` is not read at all. So C1 can
score `4 of 4` with `PROVINCE.md` byte-identical to base — the map that defines the axis stays
unmoved, and there is no command that shows it unmoved. Base state: `grep -rniE
'trae|codebuddy|kimi code|kimi-code|zhipu|bigmodel|moonshot' corpus SKILL.md PROVINCE.md` → **1** hit,
`corpus/knowledge/opencode-offer-trace-round8.md:84` (a host config path, not a skill-surface row);
`grep -cE '^\| \`' SKILL.md` registry rows naming those hosts: 0. `PROVINCE.md` Core rows
(`:10-30`) each name their surfaces **and** their counter — that is the convention the claim must
join.

**Smallest safe correction.** Add clause (e):

> “`PROVINCE.md` § Core carries one bullet that names all four vendors and
> `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`; the counter prints `province surfaces
> named N of 4` over a parse of that section, and exit 0 requires both `N == 4` and the vendor tally.”

## V7 — frozen-predicate ambiguity (path root; vendor column)

**Plan sentence.** “a snapshot under `.ufo/waves/round-73/snapshots/` whose sha256 equals the pin in
the committed manifest `snapshots/MANIFEST.sha256`”; and “has exactly one row for `V` in its vendor
table”.

**Evidence.** The lane has no `snapshots/` at its root (`ls` at base: absent; the staging root is
`.ufo/waves/round-73/assimilation/`), so `snapshots/MANIFEST.sha256` resolves to two different paths.
The staged vendor table's first column is the **company** (`| ByteDance | TRAE IDE (S214) | …`), while
the plan's vendor set is the product (TRAE, CodeBuddy, Kimi Code, Zhipu): “exactly one row for `V`”
has no defined cell. Also “a URL whose host is one of V's hosts (… `github.com/moonshotai/kimi-cli` …)”
mixes a host with a path.

**Smallest safe correction.** “a snapshot under `.ufo/waves/round-73/snapshots/` whose sha256 equals
the pin in `.ufo/waves/round-73/snapshots/MANIFEST.sha256`”; “exactly one row whose `product` cell
names `V` (case-insensitive, backticks stripped)”; “whose URL matches: prefix `https://docs.trae.cn/`
… or `https://github.com/moonshotai/kimi-cli/` …”.

## V8 — C2 ships a shortcut world that meets its own predicate (3 of 3)

**Plan sentence.** Shortcut controls: “the first sentence made short by inserting a period mid-phrase
while the old 151-character sentence continues after it (R1 reads the new first sentence only — judged
by the non-author reviewer for hollowness; the counter prints the first sentence)”.

**Rule.** The addendum's own kill rule: “any shortcut world scoring 3 means the counter is wrong; fixed
before data”; prompt `:426-431`: “if it meets the target, the counter or target is wrong — fix it
before data”. Deferring one shortcut world to a reviewer is exactly the exception the rule does not
grant (kumitate r42 in the same bullet).

**Counterexample (run, scratch).** I rebuilt that world on the real description (a 57-char first
sentence, old sentence's tail continuing after it, everything else kept, total 1,017 chars), and
scored it with the addendum's R1/R2/R3 as written:

```
first sentence 57 'Prompt & skill craft: audits "skill file" in prompt text.'
head99 'Prompt & skill craft: audits "skill file" in prompt text. And rewrites SKILL.md / AGENTS.md / dispa'
R1 True R2 True R3 True N 3
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md \
      --province PROVINCE.md --skill SKILL.md
skill description names 9 of 9 non-none lanes
exit=0
```

**Smallest safe correction.** Remove this world from the shortcut list and record it as in-bounds: the
render the claim pays for (first 99 chars carrying `skill`, `prompt` and a quoted trigger) is
genuinely present, so this is not a bypass and needs no reviewer. Keeping it as a “must read below 3”
control while accepting it at 3 makes the claim's own kill rule false on its first run.

## V9 — the frontmatter line-count guard must be counted, not printed

**Plan sentence.** “Guard the counter prints but the predicate does not count: the frontmatter keeps
its line count, so every `SKILL.md:<line>` citation after it stays valid”.

**Rule.** AXES.md:34-36 — a round is admitted “only if every claim verifies **and no axis is harmed**”.
`SKILL.md:<line>` citations are the consistency surface the lane's own gates read
(`verify_corpus_integrity.py` resolves lane-tree citations — plan, Inherited defect 4 and the M127
receipt's `trigger.citation_resolves` failure both show the class). A world that adds one frontmatter
line scores `1 of 3… 3 of 3` by the predicate while shifting every body citation by one — harm with a
green counter.

**Smallest safe correction.** Make it a rule:

> “R4 the frontmatter keeps its line count: `git diff --numstat <base> <rev> -- SKILL.md` reports 0
> inserted and 0 deleted lines before the byte offset where the frontmatter's `---` closes; prints
> `own-description rules held N of 4`, exit 0 when N == 4 (a violation is exit 1, never a printed
> note).”

## V10 — C2's surface is the artifact-versus-own-rule agreement, and it re-scores a held rule

**Plan sentence.** “C2 (replacement) — depth (owned, 9): SKILL.md's own description obeys the lane's
own trigger rule”.

**Rule.** Prompt `:436-438` — “Re-scoring a rule the lane already holds on new inputs … is quality
work, never coverage or depth”; AXES.md:9 — depth is “Verifiable technical detail — decision tables
with real thresholds, named error signatures, cited sources”, signal “A reader can act on SKILL.md
alone”. The lowest-axis duty is depth (AXES.md:33; SCORECARD depth 9), so it rests on this claim.

**Counterexample.** The rule C2 applies is already held and already instrumented: the truncator facts
sit in `corpus/knowledge/frontmatter-trigger-surface.md:62-69` (“deterministic truncator keeps at most
99 chars — first sentence wins if ≥40 chars, else last-space cut + `…`”) and `:116-120` (“Put the
capability clause + the most match-critical WHEN material in the first ≤99 chars”), and
`verifiers/check_description_thresholds.py` (round-54 depth claim) already scores descriptions. C2's
new input is **one string in the lane's own file** — the smallest possible input, not new ground — and
its property is artifact-versus-own-teaching agreement, i.e. the lane's `consistency` sub-axis, not
technical detail a reader acts on. As labeled, the round's depth move is quality work; relabeled, the
round has no claim on its lowest axis. Both branches fail admission as frozen.

**Smallest safe correction (keeps depth honest, cheapest edit).**

> “C2 — depth: `SKILL.md` § Describing a skill's own description gains a three-row decision table
> (render length ≤99; first sentence 40–99 chars; a quoted trigger plus `skill` and `prompt` inside
> the first 99; total ≤1024), each row carrying its threshold and its `S###`/entry source, **and** the
> lane's own description is the worked instance at `len(D) ≤ 1024`. Counter prints `own-description
> rules held N of 4`: three table rows backed by a cited source, plus the description conformant to
> them.”

That is technical detail with thresholds and citations (depth), and it keeps the self-audit as the
worked instance rather than the whole claim.

## V11/V12 — minor predicate determinism

**V11.** “R1 the first sentence of `D` (… else the first 99 characters) is between 40 and 99
characters long”. A description with **no** `. `/`: `+uppercase boundary in its first 99 chars takes
the fallback, and `len(D[:99]) == 99 ∈ [40,99]` → R1 true regardless of the render; the source's real
fallback is the last-space cut (`frontmatter-trigger-surface.md:68-69`), not a raw 99-char prefix.
Replacement: “R1 holds iff `D`'s first 99 characters contain a `. ` or `: ` boundary followed by an
uppercase letter, and the text before that boundary is 40–99 characters; otherwise R1 fails (the
counter prints the boundary offset).”

**V12.** R2's “whole words `skill` and `prompt`” does not state case. In the V8 world, a case-sensitive
read scores R2 false and a case-insensitive read true (`\bPrompt\b` vs `\bprompt\b`) — the same world
is 2 or 3 depending on an unstated policy. Replacement: “case-insensitive whole-word match on the
folded description”.

---

## Checked and clean (no defect found)

- **Do-nothing controls reach every target** (item 4). C1 base: no registry row names any of the four
  vendor hosts (`grep -rniE` → the single unrelated hit above; registry rows 0) → `0 of 4`, exit 1
  ✓. C2 base re-derived from bytes: first sentence 151 chars → R1 false; head99 has no double-quoted
  string → R2 false; `check_sibling_census.py …` exit 0 → R3 true → `1 of 3` ✓ (commands above).
  C3 base `2 of 6`, exit 1 from the committed receipt (five guards: four PASS, `instrument-size`
  FAIL) ✓. No do-nothing control reaches any target.
- **C1's axis label is right by surface.** The surface it moves is client skill surfaces the maps do
  not hold (AXES.md:11-12) and the four vendors are absent from `PROVINCE.md`/`SKILL.md` (grep above).
  Once V6 is added, C1 is a coverage claim by the sizing rule's own test. Not a rename.
- **Universal clauses that are enumerated.** C2 R3's “all 9 adjacent lanes” is enumerated by the gate
  itself (`skill description names 9 of 9 non-none lanes`, run above); C1's “every cited id / every
  cited `S###`” is enumerable from the entry's `source:` lines by the counter; C1's “at least three
  tokens … each occur” enumerates a named token list. Only C3's “every guard passes” lacks a counting
  line (V3).
- **Single-exploratory rule.** No claim is exploratory, and C1's “owned reading: advisory” attaches
  advisory status to the axis reading, not to an exploratory declaration; each claim ships a counting
  command. The max-one-exploratory rule (PROTOCOL-APPENDIX.md:50) is not triggered, and no claim
  needs the reviewer route.
- **M127's cause, re-derived independently** (not accepted from the L1 receipt): `Path(".").parent`
  is `PosixPath('.')`, so `fleet` at `verifiers/check_tip_battery.py:610` is the lane, and
  `build_sandbox` (`:181-187`) then symlinks the lane's own entries beside the clone. The L1's cause
  statement is correct; the *claim's* use of it is what V3 replaces.
- **Base-table spot re-measurements** (Q19): 142 registry rows; max id `S216`; gate registry
  `56 of 56`, exit 0; `check_sibling_census.py` exit 0 with `1019 of 1024`; `SKILL.md` description
  1,019 chars. The plan's base row for the C1 vendor grep and the C3 battery tally holds.

## Not observed

- No C1/C2 counter exists yet (`verifiers/check_cn_vendor_surfaces.py`, `check_own_description.py`
  absent at base), so V5/V6/V7 are predicate-level proofs, not counter runs. The V8 world was scored
  with a 20-line implementation of the addendum's R1/R2/R3 plus the real gate, not with a counter.
- I did not fetch any vendor page; source viability is the wave-1 scouts' item, not mine.
- Tool installs: none. Scratch dirs (`/tmp/k73w1-CriticSeparability.*`) removed; the fixture repo was
  a `--shared` clone with a throwaway identity, verified `rev-parse --show-toplevel` before the first
  commit, and deleted.
