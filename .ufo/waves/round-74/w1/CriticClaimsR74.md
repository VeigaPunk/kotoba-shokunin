# CriticClaimsR74 — attack on both frozen predicates (kotoba round 74, wave 1)

**Verdict: both predicates are attackable, and C2's two conjuncts contradict each other.**
Five cheap worlds built from real page bytes score **3 of 3** under the frozen C1 predicate
`spec craft pages backed N of 3` while the lane's guidance gains nothing a reader can act on, and
one of them is a world the plan itself names as a must-fail control ("a token-stuffed row"). The
pure carry-forward world scores **20 of 20** under the frozen C2 predicate
`sibling rows re-pinned and re-read N of 20`, and the factual premise the plan's own C2 control
rests on — "quotes die at moved lines for the changed lanes" — is **false for this lane set: 20 of
20 r49 quotes still locate at the freeze heads at the same line numbers**. Separately, C2 (a)
demands the 9-cell r49 row shape and C2 (c) reads "the row's `delta` cell"; the 10th cell is
refused by the pinned base checker ("expected 9 cells, found 10"), so **20 of 20 is unreachable as
frozen** until the counter projects the row. Everything else in both predicates was re-run and
holds; a strengthened C1 predicate is implemented in this seat's probe and it scores an honest
entry 3 of 3 while dropping every cheap world to 0. Two smaller calibration defects: the base
do-nothing control cannot produce the exit code the plan promises (C1-7), and "word-bounded" is
undefined where it decides the honest tokens (C1-5).

Base: lane tip `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`; measured plan commit
`329e7d91d7d750031c35d264f0e34af1d0ce8385` (`git rev-parse HEAD`). Freeze receipt
`.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`, committed at `329e7d9`, sha256
`6e6012fc800d0f8da9666a2c1ad42934c6de4c0225d97391ae72c97ecdee195d` (working tree and
`git show 329e7d9:…` give the same hash).

## Axes

| axis | claim | cheap world's effect | correction's effect |
|---|---|---|---|
| `depth` (C1) | the Agent Skills `skill-creation/` body-craft rules reach `SKILL.md` | the counter goes green, the `SKILL.md` guidance gains a row that restates chrome: a reader cannot act on it | requires one page-unique token and real content words per row, so the row must say what to do |
| `freshness` (C2) | the sibling census is re-pinned **and re-read** at the frozen heads | pins go current; nothing about the siblings' changed ground is looked at | forces the deciding line to be re-located at the new head, and prints the pin's live distance |

The words attacked are the plan's own: C1 "the specification's own authoring guides … reach
`SKILL.md`'s guidance", C2 "re-pinned **and re-read**". A counter that measures only form cannot
earn those words; the corrections either earn them or force the receipt to say less.

## Method (reproducible)

Sources were fetched by this seat (`curl -sL --max-time 60 -A 'Mozilla/5.0'`, 2026-10-25):

| URL | HTTP | bytes | sha256 |
|---|---|---|---|
| `https://agentskills.io/skill-creation/best-practices.md` | 200 | 15 060 | `ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41` |
| `https://agentskills.io/skill-creation/using-scripts.md` | 200 | 12 078 | `2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f` |
| `https://agentskills.io/skill-creation/quickstart.md` | 200 | 4 080 | `7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb` |
| `https://agentskills.io/skill-creation/best-practices-does-not-exist.md` | **404** | 705 | `5694925680c9842fc9631f25ba7cf2a881ddf1503173d5237e16455144dfebad` |

The byte counts and hashes match the wave-1 scout's figures for the three pages
(scout: 15 060 / 12 078 / 4 080). Worlds and the predicate model live in
`.ufo/waves/round-74/w1/build/CriticClaimsR74/`:

```
python3 -B probe_c1_predicate.py build c1worlds snapshots     # 9 worlds + FETCH.tsv + manifest
python3 -B probe_c1_predicate.py check c1worlds               # the frozen C1 predicate, literal
python3 -B probe_c1_predicate.py strict c1worlds              # the proposed C1' (see § C1 fix)
python3 -B build_c2_worlds.py c2worlds                        # the C2 worlds from the r49 entry
```

`probe_c1_predicate.py` is **this seat's reading**, not the lane's counter and not a proposal for
`verifiers/`. Its open choices are listed in its docstring; each finding below says what survives
a different reasonable choice. The C2 worlds are checked with the **lane's own base checker**, not
a model: `verifiers/check_sibling_census.py` (sha256
`2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7` at both `1e03d19` and
`329e7d9`, so the "base copy" of C2 (a) is the live file today).

---

## C1 — findings

### C1-1 (kill rule fires) the frozen (e) admits the "token-stuffed row" the plan names as a must-fail control

World `c1worlds/W4_token_stuff`: honest page-unique tokens and an honest page sentence (so (a) and
(d) pass for the right reason), and each `SKILL.md` action cell is `Use <token> as the guide says.`

```
$ python3 -B probe_c1_predicate.py check c1worlds | grep W4
W4_token_stuff                 3/3  best=YYYYYY usin=YYYYYY quic=YYYYYY
```

Conjunct walk: (a) passes (the row carries 2 real tokens, each located); (b) passes (S232/S236/S237
are 11-cell, `mined`, `A`, host `agentskills.io`, `opened 2026-10-25`, `used-by` names the entry);
(c) passes (snapshot hash = manifest pin); (d) passes (the quote is a real body sentence, 12/16/14
words); (e) passes because it requires only "an action cell of at least five words and at least one
rule token that occurs in `P`'s snapshot" — `Use \`--dry-run\` as the guide says.` is six words and
carries a token, and it says nothing; (f) passes. So the plan's kill rule — "any shortcut world
scoring 3 means the counter is wrong" — fires on the plan's own control list before any data.

**Smallest safe correction (e'):** the action cell must carry **≥1 page-unique token of P** and
**≥5 words that are neither tokens nor drawn from a pinned generic-filler list** (`use, see, page,
guide, says, the, as, for, this, …`; pinned in the counter, named as a lexical approximation like
the base checker's G1). Measured: W4 → 0 of 3, honest world → 3 of 3 (§ C1 matrix).

### C1-2 ((a)+(d)) the site's own chrome backs all three pages; the page-title probe is refused only by accident

The snapshots' first three lines are the site's documentation-index banner, **sha256-identical on
all three pages** (`sed -n '1,4p' <page>.md | sha256sum` → `16a68f9c0e0a8bda…` for each):

```
$ sed -n '2p' snapshots/best-practices.md
> Fetch the complete documentation index at: https://agentskills.io/llms.txt
```
(`> ` dropped; 7 words, identical in `using-scripts.md` and `quickstart.md`, measured
`{p: (s in pages[p])}` → all `True`.)

That single sentence satisfies (a)'s "double-quoted rule sentences of at least five words" and
(d)'s 5–25-word located quote for **every** page. World `c1worlds/W2_chrome_banner` uses it as the
only token and the quote for all three rows:

```
$ python3 -B probe_c1_predicate.py check c1worlds | grep W2
W2_chrome_banner               3/3  best=YYYYYY usin=YYYYYY quic=YYYYYY
```

The same hole in the shape this seat's brief names ("a quote cell that is a page title"): each
page's **subtitle** is a blockquote, ≥5 words, and is not a rule —

```
$ sed -n '7p' snapshots/best-practices.md
> How to write skills that are well-scoped and calibrated to the task.
```

World `W5_page_subtitle` (subtitle + the backticked field name `description`, which occurs on all
three pages, as the second token) → **3 of 3**. The title variant is refused only
accidentally: best-practices' H1 is 5 words ("Best practices for skill creators") but
using-scripts' is 4 ("Using scripts in skills") and quickstart's is 1 ("Quickstart"), so the
5-word floor kills the title world for 2 of 3 pages; **no conjunct refuses a heading, a blockquote
or a chrome line**, so the subtitle world is the portable version of the same cheat.

**Smallest safe correction (a')+(d'):** (a') at least one of the row's ≥2 tokens must be
**page-unique** — located in `P`'s snapshot and in neither of the other two; (d') the quote's
located line must be after the page's first `# ` heading, must not be a heading, must not be in the
blockquote block between that heading and the first `## ` heading (the subtitle), and must not be a
markdown link to another `skill-creation/` page. Measured: W2 → 0, W5 → 0, honest → 3 of 3.

### C1-3 ((b)) no conjunct binds the registry id to page P

(b) enumerates: 11 cells, `mined`, `A`, host `agentskills.io`, `opened` = round-74 date, `used-by`
names the entry, census-conformant. It never compares the row's URL with `P`. World
`W3_wrong_id` cites the lane's existing **S212** (`…/skill-creation/evaluating-skills.md`) in all
three rows (with S212's `used-by` cell carrying the entry, a one-string registry edit), honest
tokens and honest cells:

```
$ python3 -B probe_c1_predicate.py check c1worlds | grep W3
W3_wrong_id                    3/3  best=YYYYYY usin=YYYYYY quic=YYYYYY
```

**Smallest safe correction (b'):** the cited row's URL path must end
`/skill-creation/<P>.md`. Measured: W3 → 0 of 3 (message: `id S212 URL does not name
best-practices`).

### C1-4 ((c)) the snapshot pin is self-attestation, and the predicate never asks what the snapshot is

(c) compares the snapshot file with a manifest the same seat commits. It does not compare either
with the byte hash in the registry row, and nothing records the HTTP status. Measured consequences:

* World `W6_404_snapshot` — every snapshot is the **HTTP 404** body above (705 B), which contains
  the banner sentence at line 3 (`> Use this file to discover all available pages before exploring
  further.`, `> ` dropped) — scores **3 of 3** under the frozen predicate.
* World `W7_one_snapshot_three_pages` — one page's bytes stored under three names with a manifest
  that agrees with the file — passes (c) for the page whose bytes they are (the other two die on
  (a)/(d), so this world is 1 of 3, not 3 of 3; it is reported as partial credit, not a cheat).
* The lane's own precedent records no byte hash in a row's anchor cell: S212's anchor cell carries
  the section, a byte count (13 403 B), the upstream commit and the access date —
  `grep -o 'sha256'` on the cell returns nothing.

**Smallest safe correction (c'):** the snapshot's sha256 must equal the sha256 in the **cited
row's anchor cell**, and a per-page fetch record (`page, url, status, bytes, sha256`) must record
`200`; the manifest stays as the third copy. Measured: W6 → 0 (sha mismatch), W7 → 0 for the two
pages it does not hold.

### C1-5 "word-bounded" is undefined and load-bearing; `\b` breaks the honest tokens

Measured on the fetched bytes (`\b` vs `(?<![\w-])…(?![\w-])`):

```
.agents/skills/          best-practices \b=False lookaround=False
.agents/skills/          quickstart     \b=False lookaround=True
--dry-run                using-scripts  \b=False lookaround=True
uvx ruff@0.8.0 check .   using-scripts  \b=False lookaround=True
theme={null}             (all three)    \b=False lookaround=True
```

With `\b`, using-scripts loses its central command and quickstart loses its discovery root: the
honest target **drops**, while every chrome token that a lookaround form accepts stays available.
Define the lookaround form in the counter's docstring before data (Q28), and say that ≥1 location
is enough (`stdout`, `stderr` and `Pin versions` occur many times).

### C1-6 reachability of 3 of 3 holds without chrome

The honest target is not the problem. Page-unique candidates exist on every page (measured, each
located in exactly one snapshot): best-practices `"Match the specificity of your instructions to
the fragility of the task."` (12 words, line 96); using-scripts `` `uvx ruff@0.8.0 check .` ``,
`` `--dry-run` ``, and the 16-word sentence at line 9; quickstart `` `.agents/skills/` ``,
`` `roll-dice` ``, and the 14-word sentence at line 17. World `W8_honest` uses exactly those and
scores 3 of 3 under the frozen predicate **and** 3 of 3 under C1' — so the corrections do not lower
the bar, they only refuse the chrome. (Quickstart's honest sentence sits on a blockquote line 17
*inside* `## Prerequisites`; the (d') rule refuses only the subtitle block, so it stays legal —
verified by W8 passing strict.)


### C1-7 (exit ladder) at base the do-nothing control cannot produce the exit code the plan promises

The plan fixes two things that collide: "**Do-nothing control:** base scores `0 of 3`, exit 1
(receipt committed before data)" and (c) "(missing or tampered snapshot is exit 2)". At the plan
commit both are true — the entry does not exist and neither does the snapshot directory:

```
$ git cat-file -e 329e7d9:corpus/knowledge/spec-skill-creation-craft-round74.md ; echo $?
fatal: path 'corpus/knowledge/spec-skill-creation-craft-round74.md' does not exist in '329e7d9'
128
$ git cat-file -e 329e7d9:.ufo/waves/round-74/snapshots/best-practices.md ; echo $?
fatal: path '.ufo/waves/round-74/snapshots/best-practices.md' does not exist in '329e7d9'
128
```

So a literal (c) makes the base control exit **2**, not 1, and the committed do-nothing receipt
cannot read `0 of 3 / exit 1`. **Smallest correction:** fix the ladder — the counter prints
`spec craft pages backed N of 3` and exits 1 whenever `N < 3`; exit 2 is reserved for a usage error
and for a snapshot that is **present but does not match** its manifest pin ("tampered"), with the
missing-snapshot case scored as a failed page (the page is not backed) rather than as a crash.
State the ladder in the docstring the same way the base checker states its family contract.

---

## C2 — findings

### C2-1 (hard blocker) (a) and (c) are mutually unsatisfiable: 9 cells vs a `delta` cell

(a) says the entry has "exactly one row for `L` in the round-49 row shape and that row passes the
**base's** `check_sibling_census.py` row checks"; the base checker's own code is
`if len(cells) != CENSUS_COLUMNS: failures.append("expected %d cells, found %d")` with
`CENSUS_COLUMNS = 9`. (c) reads "the row's `delta` cell". A row cannot be 9 and 10 cells.

```
$ python3 verifiers/check_sibling_census.py c2worlds/W8_ten_cell_delta.md --fleet /home/vgpnk/Projects/shokunin
FAIL row 1 (census line 5): expected 9 cells, found 10
rows 20 verified 0          exit=1
```

The frozen world `W2_carry_forward` (9 cells) verifies 20 of 20, so the whole deficit is the extra
cell. **Smallest safe correction:** the counter builds the 9-cell projection of each row and runs
the pinned base checker on that projection, reading the 10th `delta` cell itself. Measured:

```
$ python3 verifiers/check_sibling_census.py c2worlds/W8_projection_nine_cells.md --fleet /home/vgpnk/Projects/shokunin
rows 20 verified 20         exit=0
```

Without this, the target `20 of 20` is unreachable by construction and the round's C2 cannot exit 0.

### C2-2 "re-read" is not measured, and the plan's control premise is false

World `c2worlds/W2_carry_forward`: the r49 entry with every commit cell bumped to the freeze head,
the mechanical cells (skill file / names / arbitration) recomputed from the pinned `SKILL.md`, and
every quote re-located by script.

```
$ python3 verifiers/check_sibling_census.py c2worlds/W2_carry_forward.md --fleet /home/vgpnk/Projects/shokunin
rows 20 verified 20         exit=0
```

World `W1_commit_bump_only` (commits bumped, nothing else) scores **19 of 20**; its only failure is
not a quote but revenger's skill cells:

```
FAIL row 16 … (lane revenger): SKILL.md exists at the pin but the skill cell says NONE
FAIL row 16 …: names-kotoba cell 'no SKILL.md' but the pinned description gives 'no'
FAIL row 16 …: arbitration cell 'no SKILL.md' but the pinned description gives 'no'
rows 20 verified 19
```

The plan says this world must score below 20 because "quotes die at moved lines for the changed
lanes". They do not. Measured for all 20 rows: quote still present at the freeze head **20 of 20**,
and at the **same line numbers** (`PROVINCE.md:3` for 15 rows, `SKILL.md:3` for
2, `SKILL.md:8` for 3). The 15 changed lanes changed *around* the quoted scope sentence (kake `2 files changed, 955
insertions(+), 5 deletions(-)`, tsukuroi `872 insertions(+)`, revenger `618 insertions(+)`), not
through it. So the cheapest world is not the plan's second control (the carry-forward): it is the
first — 19 of 20 for a `sed` over the commit column and 20 of 20 after revenger's three cells, with
no quote relocation at all.

Consequence: (a)–(e) contain **no conjunct that distinguishes a carry-forward from a re-read**, so
the claim's phrase "re-pinned and **re-read**" is unsupported by its own predicate. Two honest
options: (i) restate the claim and the receipt as "re-pinned, re-located and re-diffed", or (ii)
add the strongest mechanical conjunct that at least forces the changed ground to be touched again.

**Proposed (f, mechanical, reachable):** each row carries an `evidence` cell
`<path>:<line> <changed|unchanged> "<≤25-word quote of the deciding sentence>"`, and the counter
re-checks: the line exists at the freeze head and contains the quote; the quote's line is not a
heading; the declared flag equals `git diff --quiet <r49 pin> <freeze head> -- <path>` recomputed
by the counter; for a `none` row the evidence is the absence sweep `SKILL.md+PROVINCE.md kotoba=0`
with the counter recomputing the whole-word count; for `adjacent`/`contested` the evidence line
carries a routing marker from the base checker's pinned `OWNERSHIP_MARKERS`. This kills the
bump-only world and the carry-forward world as frozen. It does **not** prove a human read them —
no counter can — which is why (ii) must be paired with the receipt sentence, not sold as more.

### C2-3 the freeze pin's authority is left to the implementer

The freeze table is committed at the plan commit (sha `6e6012fc…`, above), so it *can* be bound to
`--rev`. But (b) says only "equals `L`'s head in the freeze file", and the only sha256-pinned
*code/authority input* in the two predicates is C2 (a)'s "run from the base copy of that checker
(sha256-pinned in the counter)" — the freeze table, which decides every pin, gets no pin of its
own. If the counter reads the working-tree receipt (the natural way, because the sibling
repos are read live via `--fleet`), then the pin can be re-edited in the very commit that lands the
entry, and `--rev` shows the edited file. **Smallest correction:** (b) reads the receipt from the
measured revision (`git show <rev>:<path>`) *and* compares it with the pinned sha, or reads the
plan commit by name; either way the pin's provenance is as strong as the checker's.

### C2-4 ancestry is the only rewrite guard, and (a) cannot see a rewrite at all

Fixture (own repo, `mktemp -d`, `git -C "$D"` everywhere, deleted after):

```
frozen A=9e7a05f5…  rewritten-head=32cc6e17…
ancestor: exit=1 (NOT an ancestor)
git show A:f.md -> original line
cat-file -e A exit=0
```

`git show <frozen>:path` keeps serving the dangling commit, so (a) — quote located, cells
recomputed — passes on a commit no branch reaches. (b) is therefore load-bearing and must fail
closed: `git rev-parse refs/heads/<branch>` must resolve, `git merge-base --is-ancestor` must exit 0,
and a missing object must be exit 2 with the lane named, not a silent skip.

Live drift also belongs in the output: at measurement, **6 of 20** sibling heads have already moved
since the freeze (kake 1, kasegi 4, kengaku 3, kotodama 6, mori 1, souji 3 commits ahead; all still
descendants), and 5 of those lanes' `pin→live` shortstat already differs from `pin→freeze`
(kama 417→393 insertions, kengaku 30→77, kotodama 85→89, mori 462→499, souji
`1 file, 2 insertions` → `2 files, 27 insertions`). (b) passes them all, by
design; printing `rev-list --count <frozen>..<branch>` per row (and the plan's own "rows are valid
at their pins, not at the round end" sentence in the entry) is what lets a reader see the pin's age.

### C2-5 (d) compares only commit and classification, so the boundary prose can go false

The base checker's province arm checks lane set, classification and commit — its docstring says
"the boundary text is not checked". Live counterexample: revenger's `## Adjacent` row at base says

```
PROVINCE.md:67: | revenger | none | 876630db… | reverse engineering of shipped artifacts; no skill file at the pin; overlaps kaidoku …
```

At the r49 pin that is true (`git -C revenger-shokunin show 876630d:SKILL.md` → exit 128); at the
freeze head it is false (`cat-file -t 6da884c:SKILL.md` → `blob`; the freeze file itself records
`skill_md_blob 082af19c…`). A carried-forward boundary cell passes (d) while stating a falsehood at
the new pin. **Smallest correction:** the evidence cell of C2-2 is quoted *from the freeze head*, so
the prose that (d) does not read becomes a cell the counter does read (it must contain the located
quote and the recomputed `changed` flag).

### C2-6 reachability of 20 of 20 (apart from C2-1): yes

* 21 `*-shokunin` directories under the fleet root minus kotoba = **20 lanes**, equal to the freeze
  table's 20 lanes and to `PROVINCE.md` § Adjacent's 20 rows (no new or removed lane).
* All 20 frozen heads resolve and are ancestors of their branch heads (`merge-base --is-ancestor`
  exit 0 for 20 of 20).
* `audio` and `game-dev-2d` have no `SKILL.md` at their heads (freeze `skill_md_blob -`), and the
  base checker already accepts exactly that shape: `mechanical_findings` requires the row to read
  `NONE / no SKILL.md / no SKILL.md`; `W2_carry_forward` verifies both rows. So `audio` does not
  block the target.
* `revenger` is the one lane whose cells must change: r49 `NONE/no SKILL.md/no SKILL.md` →
  `SKILL.md/no/no` at `6da884c` (it gained a `SKILL.md`). Measured as the only failing row of W1.
* `kumitate`'s `PROVINCE.md` names `kotoba` at its freeze head, but its class is `adjacent`; the
  `none` rule only bars `none` rows, so it passes.

The target is reachable in content and structure; C2-1 is the only thing that makes it unreachable.

---

## Hand-walk of the C2 conjuncts on the carry-forward world

`c2worlds/W2_carry_forward` (the world that must be "measured and reported", per the plan). Each
conjunct, the command, and what the bytes say:

| conjunct | result | evidence |
|---|---|---|
| (a) base row checks | **pass** | `check_sibling_census.py W2_carry_forward.md --fleet /home/vgpnk/Projects/shokunin` → `rows 20 verified 20`, exit 0. Includes the quote located at the freeze head (±2 lines), the recomputed skill/names/arbitration cells, and the `none` recomputation. |
| (b) commit = freeze head, ancestor | **pass** | every commit cell was written from `receipts/sibling-heads-freeze.tsv` (20/20 equal); `git -C <lane> merge-base --is-ancestor <frozen> <branch>` exit 0 for 20 of 20. |
| (c) `delta` cell | **unsatisfiable as frozen** | the row is 9 cells by (a); adding the 10th gives `expected 9 cells, found 10` and `rows 20 verified 0`. Needs the projection fix (C2-1). |
| (d) PROVINCE carries the same commit/classification | **pass** | `check_sibling_census.py W2_carry_forward.md --fleet … --province c2worlds/W2_province.md` → `rows 20 verified 20` + `province rows 20 matched 20`, exit 0 — with the r49 boundary prose copied verbatim (which is false for revenger, § C2-5). |
| (e) no `none` row whose pinned bytes name kotoba | **pass** | recomputed inside (a): the 11 `none`-classified lanes at their freeze heads have a whole-word `kotoba` count of 0 in `SKILL.md`+`PROVINCE.md` (table in § C2-6). |

So four of the five measured conjuncts are satisfied by a script that moves the commit column,
recomputes three cells and copies the boundary text; the fifth is unsatisfiable. That is the whole
gap between the predicate and the word "re-read".

## C1 conjunct walk for the chrome worlds

* `W2_chrome_banner`: (a) **pass** — the row's two tokens are two banner sentences, each ≥5 words
  and located in all three snapshots; (b) **pass** — the three rows are 11-cell, `mined`, `A`,
  `agentskills.io`, `opened 2026-10-25`, `used-by` names the entry; (c) **pass** — file hash =
  manifest pin; (d) **pass** — the 7-word banner sentence is located after whitespace collapse;
  (e) **pass** — the `SKILL.md` row's action cell carries the 11-word banner sentence (a token) and
  is ≥5 words; (f) **pass** — `PROVINCE.md` § Core names the entry. Nothing in the six asks whether
  the token is *about* the page.
* `W5_page_subtitle`: same walk with each page's line-7 blockquote; the only difference from W2 is
  that the subtitle is page-unique — which the frozen (a) does not ask for.
* `W6_404_snapshot`: same walk with the 404 body; (c) passes because the manifest agrees with the
  stored bytes, and (d) passes because the 404 body repeats the banner sentence at line 3. HTTP
  status is not a conjunct anywhere.

## Matrices (observed)

C1, frozen predicate (literal reading), raw output of `probe_c1_predicate.py check c1worlds`:

```
W0_base                        0/3  best=...... usin=...... quic=......
W1_staged_verbatim             0/3  best=...... usin=...... quic=......
W2_chrome_banner               3/3  best=YYYYYY usin=YYYYYY quic=YYYYYY
W3_wrong_id                    3/3  best=YYYYYY usin=YYYYYY quic=YYYYYY
W4_token_stuff                 3/3  best=YYYYYY usin=YYYYYY quic=YYYYYY
W5_page_subtitle               3/3  best=YYYYYY usin=YYYYYY quic=YYYYYY
W6_404_snapshot                3/3  best=YYYYYY usin=YYYYYY quic=YYYYYY
W7_one_snapshot_three_pages    1/3  best=.YY..Y usin=YYYYYY quic=.YY..Y
W8_honest                      3/3  best=YYYYYY usin=YYYYYY quic=YYYYYY
```

C1, proposed predicate (a')(b')(c')(d')(e') + (f), same worlds (compressed from the run: one
representative reason per world, all pages behave alike except W7):

```
W0_base                        0/3   (no entry)
W1_staged_verbatim             0/3   (no rule table)
W2_chrome_banner               0/3   (a') no page-unique token; (d') line 2 precedes the H1 (site chrome);
                                     (e') 0 action cells carry a page-unique token and >= 5 content words
W3_wrong_id                    0/3   (b') id S212 URL does not name <page>;
                                     (c') snapshot sha256 not recorded in the row anchor
W4_token_stuff                 0/3   (e') 0 action cells carry a page-unique token and >= 5 content words
W5_page_subtitle               0/3   (d') page-subtitle blockquote; (e')
W6_404_snapshot                0/3   (a') no page-unique token; (d') line 3 precedes the H1 (site chrome);
                                     (c') snapshot sha256 not recorded in the row anchor
W7_one_snapshot_three_pages    0/3   (a') (c') (d')
W8_honest                      3/3   all six
```

C2, the lane's own base checker on the world files:

```
W1_commit_bump_only            exit=1  rows 20 verified 19   (only revenger's three skill cells)
W2_carry_forward               exit=0  rows 20 verified 20
W3_msing_row (audio dropped)   exit=1  rows 19 verified 19   FAIL lane set: 1 sibling lane(s) never surveyed: audio
W2d_carry_forward_delta_cell   exit=1  rows 20 verified 0    expected 9 cells, found 10
W8_projection_nine_cells       exit=0  rows 20 verified 20   (the 9-cell projection fix)
```

Per-row quote survival (script `build_c2_worlds.py`, output `quotes still present at the freeze
head: 20 of 20`; every relocated line equals the r49 line: `PROVINCE.md:3`, `SKILL.md:3`,
`SKILL.md:8`).

## Proposed amendments (exact text, minimal)

C1, replace (a), (b), (d) and (e) and tighten (c):

```
(a') ... at least one of the row's >= 2 rule tokens is PAGE-UNIQUE: located word-bounded
     (lookarounds (?<![\w-])... (?![\w-]), never \b) in the committed snapshot of P's source and
     in neither of the other two pages' snapshots.
(b') ... and the cited row's URL path ends with /skill-creation/<P>.md.
(c') ... the snapshot's sha256 equals the sha256 recorded in the cited row's anchor cell and in
     the committed fetch record (page, url, HTTP status, bytes, sha256); a status other than 200
     is a failure, not a missing snapshot (exit 2 stays for a missing/tampered snapshot).
(d') ... the quote's located line lies after P's first `# ` heading, is not a heading, is not in
     the blockquote block between that heading and the first `## ` heading, and is not a markdown
     link to another skill-creation page.
(e') ... each action cell has >= 1 PAGE-UNIQUE rule token of P and >= 5 words that are neither
     tokens nor members of the pinned generic-filler list (named as a lexical approximation).
```

C2, add (and keep the existing (a)–(e)):

```
(a) read the row through a 9-cell projection for the pinned base checker; the row itself may be
    10 cells.                                    [fixes the (a)/(c) contradiction]
(b) the freeze table is read from the measured revision and its sha256 must equal
    6e6012fc800d0f8da9666a2c1ad42934c6de4c0225d97391ae72c97ecdee195d (the plan commit's copy);
    the branch ref must resolve; merge-base --is-ancestor must exit 0; a missing ref/object is
    exit 2 with the lane named.  Print per row: rev-list --count <frozen>..<branch>.
(f) evidence cell `<path>:<line> <changed|unchanged> "<quote>"` at the freeze head, re-checked by
    the counter as in C2-2; a `none` row's evidence is the recomputed absence sweep.
```

## Bounds (Q26/Q51 honest)

* C1' does not measure whether a rule sentence is *true of the page* or whether the action is the
  right action; it measures page-uniqueness, line shape, content-word mass and token presence. A
  determined faker can still write a page-unique sentence that says the wrong thing — that is the
  reviewer judgement the plan already assigns to named wave-2 seats, and the counter must keep
  saying so in its docstring.
* C2 (f) does not prove reading. It forces the changed ground to be re-located at the new head and
  the pin distance to be visible; the classification (adjacent/contested/none) stays a judgement.
* My C1 probe's open choices (any backticked span counts as a token; the first double-quoted span
  is the quote; a rule table is a markdown table with a page cell) are documented in its docstring.
  Findings C1-1, C1-2, C1-3 and C1-4 do not depend on them: each cheat lives in bytes the plan
  itself names, and each correction is stated as a conjunct, not as an implementation.

## Unobserved

* I did not run `scripts/sources-census.sh validate` on a staged-row world, so C1 (b)'s last clause
  ("the registry is census-conformant at `--rev`") is not modelled; that clause is the only guard
  the predicate has against the campaign-schema staged rows, and it belongs to the census gate, not
  to `check_spec_craft.py`. The staged rows are 11 cells with `opened 2026-10-23`, so as-is they
  fail (b) on the date and on `used-by`; a date/used-by sed makes them pass (b) otherwise.
* The lane's id space starts at `S223` (`assimilation/reg-ids` ends at S222, measured), and the
  assimilation scratch pipeline assigns the three pages `S232→S223`, `S237→S224`, `S236→S225`
  (`ExecIdsR74` § 1, re-derived there, not re-derived here). My worlds use the staged ids
  `S232`/`S236`/`S237`; the predicate is id-agnostic and the id values change nothing measured.
* I did not diff the S019 page (the scout's 14-byte drift note); out of scope for this seat.

## Hygiene

No lane file was modified: `git status --porcelain | grep -v '^??'` is empty. Everything I wrote is
under `.ufo/waves/round-74/w1/`: this report, `build/CriticClaimsR74/{probe_c1_predicate.py,
build_c2_worlds.py,c1worlds/,c2worlds/,snapshots/}` (snapshots ≤15 060 B each). Scratch dirs were
`mktemp -d /tmp/k74w1-CriticClaimsR74.*` and are deleted (`ls -d /tmp/k74w1-CriticClaimsR74.*` →
none). Tools installed: none. The fleet repos were read with read-only git only
(`show/cat-file/merge-base/rev-parse/rev-list/diff/ls-tree`).
