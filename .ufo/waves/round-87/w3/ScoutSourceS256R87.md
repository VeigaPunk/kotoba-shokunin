# ScoutSourceS256R87 — re-open S256 and re-verify its bytes (round-87 w3)

Seat: scout, leaf member (no subagent dispatch). Lane:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`. Read-only on the lane;
every byte this seat wrote is under `.ufo/waves/round-87/w3/ScoutSourceS256R87/` plus this
report file.

**Scope note.** The item asks for two things: (a) re-open `corpus/SOURCES.md` row `S256` and
re-verify its bytes against the live upstream, and (b) run the lane's sources census. Both are
done below. The milestone additionally asks for the C2 D5 drift to be measured, so that
measurement is included as supporting evidence for the round's known state — it is a
*measurement*, not a repair. No counter, ledger, plan, corpus, LOG or SCORECARD byte was
touched.

---

## 1. The S256 row, as printed (nothing taken from this seat's summary)

```
$ grep -n '^| S256' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
197:| S256 | omp 18.15.0 plugin skill-root reader — the module embedded in the installed bun ELF
/home/vgpnk/.local/bin/omp (sha256 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f)
and upstream https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/omp-plugins.ts
(tag v18.15.0, HTTP 200, 15362 B) | code | A | what code reads the omp plugin skills root
~/.omp/plugins/node_modules/*/skills — the terminal <pkg>/skills join and the provider it
registers — rather than the provider's description string | `packages/coding-agent/src/discovery/omp-plugins.ts`
§ the skills provider at tag v18.15.0 (upstream line 70, leading tabs trimmed; ELF module header
`// packages/coding-agent/src/discovery/omp-plugins.ts` @173914407, reader @173914936); upstream
bytes sha256 4e66819cf706b81c6f31bd71e6de8892083a284525ab151948642faea00cb1b4 (15362 B, 430 lines);
located quote: "dir: path.join(root.path, "skills")," (3 words, 2026-11-04); byte-identical anchor in
both files: "Sub-discovery (skills, hooks, tools, commands, rules, prompts, .mcp.json) inside
extension packages" (line 46; ELF @114492956) | the plugin root's reader is a <pkg>/skills join
performed per extension-package root, so a root can be grounded on the code line that reads it even
where the ELF carries no literal for the root's own path | mined | 2026-11-04 | on-release |
corpus/knowledge/omp-root-semantics-round87.md, verifiers/omp-skill-roots-semantics.tsv |
```

Extracted fields (11 cells, NF=13 as the census wants):

| cell | value |
|---|---|
| id | `S256` |
| source | ELF `/home/vgpnk/.local/bin/omp` sha256 `6737ee24…b7b0f` **and** upstream `https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/omp-plugins.ts` (tag v18.15.0, HTTP 200, 15362 B) |
| kind / tier | `code` / `A` |
| scope | what code reads the omp plugin skills root `~/.omp/plugins/node_modules/*/skills` — the terminal `<pkg>/skills` join and the provider it registers — rather than the provider's description string |
| anchor | `packages/coding-agent/src/discovery/omp-plugins.ts` § the skills provider at tag v18.15.0 (upstream line 70, leading tabs trimmed; ELF module header `// packages/coding-agent/src/discovery/omp-plugins.ts` @173914407, reader @173914936); upstream bytes sha256 `4e66819cf706b81c6f31bd71e6de8892083a284525ab151948642faea00cb1b4` (15362 B, 430 lines); located quote: `dir: path.join(root.path, "skills"),` (3 words, 2026-11-04); byte-identical anchor in both files: `Sub-discovery (skills, hooks, tools, commands, rules, prompts, .mcp.json) inside extension packages` (line 46; ELF @114492956) |
| teaches | the plugin root's reader is a `<pkg>/skills` join performed per extension-package root, so a root can be grounded on the code line that reads it even where the ELF carries no literal for the root's own path |
| status | `mined` |
| opened / recheck | `2026-11-04` / `on-release` |
| used-by | `corpus/knowledge/omp-root-semantics-round87.md`, `verifiers/omp-skill-roots-semantics.tsv` (both exist on disk) |

**Access date.** `2026-11-04` (row cell `opened`; also the quote's own date stamp, "3 words,
2026-11-04"). This seat re-opened the URL on **2026-11-05** and got byte-identical bytes, so the
row's pin is reproducible a day later.

---

## 2. Independent re-fetch of the row's URL

```
$ curl -sS -o "$S/body" -w '%{http_code} %{size_download}\n' \
    'https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/omp-plugins.ts'
200 15362
$ sha256sum "$S/body"
4e66819cf706b81c6f31bd71e6de8892083a284525ab151948642faea00cb1b4  $S/body
$ wc -lc "$S/body"
  430 15362 $S/body
```

* **HTTP code 200, bytes 15362, sha256 `4e66819cf706b81c6f31bd71e6de8892083a284525ab151948642faea00cb1b4`, 430 lines.**
  Every one of these equals what the row's `source`/`anchor` cells state. **The pin holds.**
* Extra cross-check the row does not make, so the pin is not just self-consistent: the fetched
  bytes' git blob id equals the blob GitHub serves at `ref=v18.15.0`.

```
$ git hash-object "$S/body"
c4cee136d81b6878aeb466f6be3b253e96dc8a11
$ curl -sS 'https://api.github.com/repos/can1357/oh-my-pi/contents/packages/coding-agent/src/discovery/omp-plugins.ts?ref=v18.15.0'
{"sha": "c4cee136d81b6878aeb466f6be3b253e96dc8a11", "size": 15362, ...}
```

  The tag is immutable, so the row's byte pin is stable, not a moving branch.
* The fetch was repeated after an unrelated scratch-tree deletion (another lane's cleanup removed
  `/fast/scratch/hyaku/kotoba-r87/` mid-run); the second fetch returned the same code, byte count
  and sha256. Re-fetch is deterministic.

### The located quote, at the line the row names

```
$ grep -n 'dir: path.join(root.path, "skills"),' "$S/body"
70:				dir: path.join(root.path, "skills"),
```

The row says "upstream line 70, leading tabs trimmed". Confirmed: line 70 is
`\t\t\t\tdir: path.join(root.path, "skills"),`, and `line.lstrip('\t ')` equals the row's quote
byte for byte. The quote occurs exactly once in the fetched body. **The row's quote is present
verbatim at the line the row names.**

### Reader, not a doc/string-table line

This is the substantive question the item asks, and it is the one the round-86 closure's CF1
finding turned on. The row's *scope* cell promises "the terminal `<pkg>/skills` join and the
provider it registers — **rather than the provider's description string**". The fetched file
contains both candidates, and they are distinguishable:

```
 43  const PROVIDER_ID = "omp-plugins";
 44  const DISPLAY_NAME = "OMP Extension Packages";
 45  const DESCRIPTION =
 46  	"Sub-discovery (skills, hooks, tools, commands, rules, prompts, .mcp.json) inside extension packages";
 ...
 65  async function loadSkills(ctx: LoadContext): Promise<LoadResult<Skill>> {
 66  	const roots = await allowedRoots(ctx, "skills");
 67  	const results = await Promise.all(
 68  		roots.map(root =>
 69  			scanSkillsFromDir(ctx, {
 70  				dir: path.join(root.path, "skills"),
 71  				providerId: PROVIDER_ID,
 72  				level: root.level,
 73  				requireDescription: true,
 74  				pluginName: root.name,
 75  			}),
 76  		),
 77  	);
```

* Line 70 is an **executed statement**: the `dir:` field of the object literal passed to
  `scanSkillsFromDir`, i.e. the code that builds the per-package skills root and hands it to the
  scanner. It carries the path-join token `path.join(` — it is a **reader**.
* Line 46 is the `DESCRIPTION` **string constant**: a doc/description line with no join token. It
  is the very thing the row says it is *not* using.
* The provider registration the row also names is at lines 376–382
  (`registerProvider<Skill>(skillCapability.id, { id: PROVIDER_ID, …, load: loadSkills })`).

So the row's located quote is the reader and the row's byte-identical anchor
(`Sub-discovery (…) inside extension packages`, upstream line 46) is the description string —
used by the row only as a *cross-check* anchor ("byte-identical anchor in both files"), not as the
reader. The two roles are not confused. **The reader claim holds on the page's own text.**

### The ELF side, re-derived from the bytes

```
$ sha256sum /home/vgpnk/.local/bin/omp
6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f        # == the row's ELF pin
ELF @173914407  // packages/coding-agent/src/discovery/omp-plugins.ts
ELF @173914936      dir: Zo.join(R.path, "skills"),
ELF occurrences of 'dir: path.join(root.path, "skills"),' : 0
ELF occurrences of 'dir: Zo.join(R.path, "skills"),'    : 1
ELF occurrences of 'Sub-discovery (…) inside extension packages' : 2
ELF occurrences of '// packages/coding-agent/src/discovery/omp-plugins.ts' : 1
```

Both ELF offsets the row names are exact: the module header at **173914407** and the reader at
**173914936**. The upstream quote does **not** occur verbatim in the ELF — the bun bundle
minifies identifiers (`path`→`Zo`, `root`→`R`) — and the row does not claim it does: it claims the
upstream quote for the *source* and separately names the ELF's reader offset, with the
description string as the byte-identical cross-check between the two files. That is the honest
description of the situation.

The ELF module body also shows the reader is reached from the plugin-root enumeration
(`vd(u, "skills")` → `X9(u)` = `listOmpExtensionRoots`), i.e. the join is *per extension-package
root*, exactly as the row's `teaches` cell says.

### Supporting upstream chain (not required by the row, but it closes the root pattern)

The row's scope names `~/.omp/plugins/node_modules/*/skills`. The quoted file alone does not carry
that literal — the ELF has **no** `.omp/plugins` string at all (the round-86 CF1 finding). Two
sibling modules at the same tag supply the prefix; both fetch 200 and their sha256 match the
wave-1 record `.ufo/waves/round-87/w1/ScoutPlugin/SOURCE_RECORD.txt`:

```
https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/extensibility/plugins/loader.ts
  200 17785  d759c4661cdd13b7081d2005463e8ab0bbeb28a745992b998f986ebe971e5a1d   (matches SOURCE_RECORD)
  loader.ts:110   const nodeModulesPath = path.join(root, "node_modules");
https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/omp-extension-roots.ts
  200 15648  9f673afe2f2925826e41a9adfc8bc985de331404f80bce53a0c443c915d4fce3   (matches SOURCE_RECORD)
https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/utils/src/dirs.ts
  200 52434  2d423f4f18e5ed0c25cd4887c68cf2fea704f1615ad4c85846ae5c10d3207f24
  dirs.ts:691-704  getPluginsDir(home) -> path.join(home, getConfigDirName(), "plugins") | dirs.rootSubdir("plugins","data")
  dirs.ts:707      "Where npm installs packages (~/.omp/plugins/node_modules)."
```

and the ELF carries the same constant: `c.rootSubdir("plugins", "data")` at **166892431**
(the row's wave-1 note says 166892424; the *call* sits at 166892431, the `return` keyword at
166892424 — a 7-byte offset difference inside the same statement, not a disagreement about
content).

**Nothing in this chain contradicts the row.** The row does not claim the quoted file contains the
root literal; it claims the quoted file grounds *the reader* for that root. That is exactly what
the fetched bytes show.

---

## 3. The census for this lane

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
…
kotoba	W04	S249 duplicate url code.claude.com/docs/en/hooks.md across scopes
…
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
$ echo $?
0
```

* **Exit code: 0.** Last line: `kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`.
* 0 E-codes; 33 W-codes, all `W04 duplicate url across scopes`, all on rows **other than S256**
  (S256's URL appears exactly once in the registry). Warnings do not change the exit code.
* Hand-checked S256 against the contract's per-row rules, because the census prints no per-row OK
  line: `NF=13` (E01 ok), id `S256` unique (E03 ok), URL unique (E04 ok), kind `code` (E05 ok),
  tier `A` (E06 ok), status `mined` (E07 ok), opened `2026-11-04` (E08 ok), recheck `on-release`
  (E09 ok), not `community` so E10 n/a, both `used-by` paths exist on disk (E11 ok), row sits
  inside `## Registry` so E12 ok. Registry rows: **181 at base `223ae62` → 182 now** (S256 is the
  one added row).

---

## 4. The two frozen counters and the C2 D5 drift (measured, not repaired)

### Tip note — the lane tip moved during this seat's run

The brief names tip `760e1c5edfdefb4767420f711d08f669952de013`. That was the tip when the seat
started. **It is now `d1c031833c37af99196f72f84a6643f84eec129a`** ("round-87 attempt 2: the C2
D5(iii) drift measured at the tip …", committed 2026-11-05 00:09:30 -0300 by another actor).
`corpus/SOURCES.md` is byte-identical across the two tips (`git diff 760e1c5… d1c0318… --
corpus/SOURCES.md` is empty), so S256 is unaffected by the move. Both counters were measured at
**both** revisions; the readings are the same.

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse master
d1c031833c37af99196f72f84a6643f84eec129a

$ python3 -B verifiers/check_omp_root_semantics.py --rev d1c031833c37af99196f72f84a6643f84eec129a
…
row  9 GROUND '~/.omp/plugins/node_modules/*/skills' module='coding-agent/src/discovery/omp-plugins.ts' @173914936
…
guard S3 pattern-set PASS
omp root semantics grounded 12 of 12
exit=0                                                  # C1 = 12/12, exit 0 — as claimed

$ python3 -B verifiers/check_r86_routed_repairs.py --rev d1c031833c37af99196f72f84a6643f84eec129a
PASS d1  two receipts carry exit=0; instruments equal 04647b0f..d1c03183
PASS d2  carried by plans/round-87.md; validator sentence present, 10 roles, no planner
PASS d3  5 reject row(s), longest reason 52 words
PASS d4  plans/round-87.md names the boundary 'after the first candidate score'
FAIL d5  verifiers/verify_corpus_integrity.py red set ['corpus.pointers.commit_unresolvable'],
        want exactly ['corpus.pointers.commit_unresolvable', 'corpus.pointers.report_dead']
r86 routed defects closed 4 of 5
exit=1                                                  # C2 = 4/5, exit 1 — as the brief states
```

C1's row 9 — the row S256 grounds — is GROUND, at exactly the ELF offset S256 names
(173914936), by the counter's own bytes.

### The D5 drift, and its causal variable (measured independently)

The frozen D5(iii) demands the corpus gate's red set be **exactly**
`{report_dead, commit_unresolvable}` and the tally be exactly `7/9 checks pass`
(`verifiers/check_r86_routed_repairs.py:114,417-418,462`). Three readings, all measured:

| reading | report_dead | commit_unresolvable | tally | d5 verdict |
|---|---|---|---|---|
| lane worktree (the environment the counter measures in) | **0** | 1 | `8/9 checks pass` | FAIL — red set `['corpus.pointers.commit_unresolvable']` |
| fresh `--shared` clone of the lane, scratch cwd | 1 | 1 | `7/9 checks pass` | FAIL — but on the *detail site*: `report_dead detail ['corpus/lessons/round-81.md:29: ../../.ufo/reports/round-76/kotoba.md'] does not name corpus/lessons/round-86-verifier-spotcheck.md:33` |
| same clone **after** copying the fleet's `round-76/kotoba.md` into the clone's own resolution root | 0 | 1 | `8/9 checks pass` | FAIL — identical to the lane reading |

So the lane's red set lost `report_dead` because the fleet-root report
`.ufo/reports/round-84/kama.md` — cited at `corpus/lessons/round-86-verifier-spotcheck.md:33` —
landed on the fleet repo (fleet commit `5b052020a13b37340c1054286d85b2514c7133d5`,
2026-11-04 12:16:01 -0300; file mtime 22:47:40) and now carries the `## SHONEN` marker and
8 128 bytes, so the pointer resolves and `report_dead` heals to 0. The third row of the table is
the causal pin: putting the external file back into the clone's resolution root reproduces the
lane's reading exactly. **The drift is caused by an external file in the fleet root, not by any
lane corpus byte.** D5(i)+(ii) are intact — both non-author records are byte-identical from the
base to the tip (`ae3f49a3…` and `315c0ec6…`), and the lesson's disclosure text still names both
sites and the `left red and disclosed` disposition.

**This is a finding for the wave, not a repair.** The frozen D5 predicate is *environment-
sensitive*: it asserts a red set that an external actor can change. Measured consequence: the
same committed lane bytes read 5 of 5 before the fleet report landed, 4 of 5 after, and a third
state (4 of 5 on a different sub-check) in a checkout whose resolution root differs. The
candidate C2 score of 5 of 5 is therefore not reproducible from the lane's committed bytes alone.

---

## 5. Check table

| check | command | observed | verdict |
|---|---|---|---|
| S256 row exists and is unique | `grep -n '^| S256' corpus/SOURCES.md` | line 197; 1 occurrence | PASS |
| row shape (contract E01) | `awk -F'|' '/^\| S256 \|/ {print NF}'` | `13` | PASS |
| row kind/tier/status/opened/recheck enums (E05–E09) | per-cell `awk` | `code` / `A` / `mined` / `2026-11-04` / `on-release` | PASS |
| row used-by paths exist (E11) | `ls corpus/knowledge/omp-root-semantics-round87.md verifiers/omp-skill-roots-semantics.tsv` | both present | PASS |
| row is inside `## Registry` (E12) | file layout | yes | PASS |
| URL re-fetch: HTTP code | `curl -sS -o "$S/body" -w '%{http_code} %{size_download}' <url>` | `200 15362` | PASS (matches the row's "HTTP 200, 15362 B") |
| URL re-fetch: sha256 == row's pin | `sha256sum "$S/body"` | `4e66819cf706b81c6f31bd71e6de8892083a284525ab151948642faea00cb1b4` | PASS (equal to the row's anchor cell) |
| URL re-fetch: line count | `wc -lc "$S/body"` | 430 lines / 15362 B | PASS (matches the row's "15362 B, 430 lines") |
| pin is the tag's blob, not a branch | `git hash-object` vs GitHub API `?ref=v18.15.0` | both `c4cee136d81b6878aeb466f6be3b253e96dc8a11` | PASS (stronger than the row claims) |
| quote present verbatim at the named line | `grep -n 'dir: path.join(root.path, "skills"),' "$S/body"` | line 70, leading tabs trimmed == quote | PASS |
| quote is a **reader**, not doc/string-table | fetch lines 43–48 vs 65–77 | line 70 = `dir:` field of the `scanSkillsFromDir` call, carries `path.join(`; line 46 = `DESCRIPTION` constant, no join token; row uses the latter only as the byte-identical anchor | PASS |
| ELF pin | `sha256sum /home/vgpnk/.local/bin/omp` | `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f` | PASS |
| ELF module header @173914407 | byte probe | `// packages/coding-agent/src/discovery/omp-plugins.ts` | PASS |
| ELF reader @173914936 | byte probe | `dir: Zo.join(R.path, "skills"),` (minified counterpart; upstream form occurs 0× in the ELF, as the row does not claim otherwise) | PASS |
| ELF carries no `.omp/plugins` literal (round-86 CF1) | byte probe | 0 occurrences — consistent with the row's `teaches` cell | PASS (consistent) |
| root-pattern prefix chain | fetch `loader.ts`, `omp-extension-roots.ts`, `utils/src/dirs.ts` at v18.15.0 | 200/200/200; sha256 match the wave-1 record for the first two; `dirs.ts` documents `~/.omp/plugins` and `~/.omp/plugins/node_modules`; ELF `c.rootSubdir("plugins","data")` @166892431 | PASS (supports the scope cell) |
| lane census | `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | **exit 0**; last line `kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`; 0 E-codes; 33 W04 on other rows; no line mentions S256 | PASS |
| C1 at the tip | `python3 -B verifiers/check_omp_root_semantics.py --rev <tip>` | `omp root semantics grounded 12 of 12`, exit 0; row 9 GROUND @173914936 | PASS (12/12 as claimed) |
| C2 at the tip | `python3 -B verifiers/check_r86_routed_repairs.py --rev <tip>` | `r86 routed defects closed 4 of 5`, exit 1; D5(iii) FAIL on the red set | FINDING (known drift; caused by an external fleet file) |
| D5 drift causal variable | lane worktree vs fresh `--shared` clone vs clone with the fleet report copied in | 8/9 (red={commit_unresolvable}) / 7/9 (red={report_dead,commit_unresolvable}, wrong detail site) / 8/9 — the third reproduces the lane exactly | FINDING: D5 is environment-sensitive; the 5-of-5 score is not reproducible from committed lane bytes alone |
| D5(i)+(ii) non-author records unchanged | `git rev-parse <base>:<f>` vs `<tip>:<f>` | `ae3f49a3…` = `ae3f49a3…`; `315c0ec6…` = `315c0ec6…` | PASS |

---

## 6. Findings

1. **S256 re-opens byte-identically and its pin is correct.** HTTP 200, 15362 B, 430 lines,
   sha256 `4e66819cf706b81c6f31bd71e6de8892083a284525ab151948642faea00cb1b4` — equal to the
   row's pin, re-fetched on 2026-11-05, a day after the row's `2026-11-04` access date. The
   located quote is present verbatim at upstream line 70 (leading tabs trimmed), exactly as the
   row states, and the row's byte-identical cross-check anchor is present at upstream line 46.
   Independently, the fetched bytes' git blob id equals the blob GitHub serves at the immutable
   tag `v18.15.0`, so the pin cannot drift with a moving branch.
2. **The quote is a reader, not a doc string — the round's substantive claim survives
   re-opening.** The quoted line is the `dir:` field of the object literal passed to
   `scanSkillsFromDir`, and carries `path.join(`. The provider's *description string* is a
   different line (46) and the row uses it only as the cross-check anchor, exactly as its scope
   cell promises ("rather than the provider's description string"). The ELF's counterpart is the
   minified `dir: Zo.join(R.path, "skills"),` at the exact offset the row names (173914936),
   preceded by the module header at 173914407.
3. **The census is clean for this lane and for this row: exit 0, last line
   `kotoba	ok	…/corpus/SOURCES.md`**, 0 E-codes, and no line of the output mentions S256.
4. **C1 re-verifies at the tip: `omp root semantics grounded 12 of 12`, exit 0**, and the row
   S256 grounds (row 9, `~/.omp/plugins/node_modules/*/skills`) is GROUND at the ELF offset S256
   names. Both the brief's tip and the tip that superseded it mid-run give the same reading.
5. **FINDING — the frozen C2 predicate D5(iii) is environment-sensitive, so the round's 5-of-5
   C2 score is not reproducible from the lane's committed bytes.** D5 asserts the corpus gate's
   red set is exactly `{report_dead, commit_unresolvable}` and its tally exactly `7/9 checks
   pass`; both are properties of files *outside* the lane's corpus (the fleet root's
   `.ufo/reports/**`). Measured: the fleet's `round-84/kama.md` landed at 22:47 in fleet commit
   `5b052020` with the `## SHONEN` marker, `report_dead` healed 3 → 0, the lane now reads
   `8/9 checks pass` and the red set `{commit_unresolvable}`; a fresh `--shared` clone reads
   `7/9` with the red set right but the *detail site* wrong
   (`corpus/lessons/round-81.md:29`, a `../../` pointer that dangles outside the lane);
   copying the fleet's `round-76/kotoba.md` into the clone's resolution root reproduces the lane's
   reading exactly. Same committed lane bytes, three readings. D5(i)/(ii) are intact (both
   non-author records byte-identical from base to tip) and the disclosure text is intact — only
   the environmental conjunct moved. This is a counter/predicate defect to be recorded by the
   wave; per the wave's rules it is a **finding, not an edit**.
6. **The lane tip moved during this seat's run** (`760e1c5…` → `d1c03183…`, committed
   2026-11-05 00:09:30 -0300 by another actor). `corpus/SOURCES.md` is byte-identical across the
   two tips, so S256 is unaffected; both counters were measured at both revisions with identical
   readings.

## 7. Risks / caveats

* The row's `scope` cell names the root `~/.omp/plugins/node_modules/*/skills`, but the quoted
  file carries **no** `node_modules` and no `.omp/plugins` literal (nor does the ELF). The prefix
  is supplied by two sibling modules at the same tag (`extensibility/plugins/loader.ts`,
  `utils/src/dirs.ts`), both re-fetched 200 here with matching pins, plus the ELF constant
  `c.rootSubdir("plugins","data")`. The row does not claim otherwise — its `teaches` cell says the
  grounding is "the code line that reads it even where the ELF carries no literal for the root's
  own path" — so this is not a defect, but a reader of the row alone would not see the prefix's
  provenance. The wave-1 record `.ufo/waves/round-87/w1/ScoutPlugin/SOURCE_RECORD.txt` does record
  it.
* The quote's word count ("3 words") counts `dir:` / `path.join(root.path,` / `"skills"),` — the
  ≤25-word contract limit holds either way.
* `omp` was not re-run as a live client for this item; the ELF bytes and the upstream sources are
  the evidence, and the row's own scope (ELF + upstream module) is what was re-verified. No
  client-run claim is made or refuted here.
* Worktree note: `git status` shows `corpus/lessons/round-87.md` **modified** in the lane worktree.
  That edit is **not this seat's** — this seat wrote only the two paths named above and never
  touched `corpus/`, `verifiers/`, `plans/`, `LOG.md`, `SCORECARD.md` or `SKILL.md`. The D5
  measurements above are therefore read against a worktree that another actor is editing; the
  counter itself reads the lesson from the *committed* bytes at `<rev>` (S1-style guard) and the
  corpus gate from the worktree, which is the sensitivity finding #5.
* The lane's `## Gate` in `corpus/lessons/round-87.md:37` records S256's admission with the URL's
  module, tag, HTTP code, byte count, sha256 and the located quote at line 70 — consistent with
  the row and with this re-opening.

**S256: admit-as-grounded**

---

### Receipts (all under `.ufo/waves/round-87/w3/ScoutSourceS256R87/`)

| file | content |
|---|---|
| `01-s256-row.txt` | the row as printed + its 11 cells split |
| `02-fetch.txt` | the re-fetch: code, bytes, sha256, blob-id cross-check, quote/anchor line numbers |
| `03-reader-vs-doc.txt` | upstream lines 43–48 / 60–82 / 374–383 and the ELF reader/header probes — the reader-vs-doc test |
| `04-census.txt` | the census command, its full output, exit code, last line, "no line mentions S256" |
| `05-counters-at-tip.txt` | C1 and C2 at both tips, with the tip-move note |
| `06-d5-drift.txt` | the D5 drift: lane vs fresh clone vs clone-with-fleet-report, plus the fleet-commit evidence and the D5(i)/(ii) blob check |
| `07-census-summary.txt` | census exit code / last line, E- and W-code counts, per-row S256 checks, registry row counts |

Scratch (`/fast/scratch/hyaku/kotoba-r87/ScoutSourceS256R87/`, including the `--shared` clone and
the fetched bodies) was removed after the receipts were copied into the lane.
