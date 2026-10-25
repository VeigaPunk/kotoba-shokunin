# ExecCollisionGuard — id-collision guard re-run + non-vacuity proof (round 69, wave 1)

Seat: `L1Kotoba69-2.ExecCollisionGuard`. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
All measurement ran in `/tmp/ecg69-scratch` (plus `/tmp/ecg69-scratch/run` for the final transcript).
No file inside the lane, the fleet repo, a sibling lane or `shokuknow` was written; only this report.
No tool installs, no package transactions, no subagent dispatch.

## Verdict

**The frozen pipeline reproduces `128 / 188 / 0` at the frozen revision `a5f7459f` (and at the plan
commit `a238989a`, whose `corpus/SOURCES.md` is byte-identical). It does *not* print `128` on the
live working tree: the L1's draft has already appended six rows there, so the live file measures
`134 / 188 / 6`.**

The guard is non-vacuous, re-proved two ways: on a controlled fixture and on the L1's own
`assimilation/guard-proof/` fixture (re-derived from the frozen bytes, byte-identical output).

So the ticket's expected triple holds exactly for the revision the plan froze it at. Read as a
statement about the live `corpus/SOURCES.md` it does not hold, and cannot: the six appended ids
`S203–S208` are the first six ids of the staged package, which is the arithmetic consequence of the
plan's own rule "adopted ids continue the lane registry from S203". Detail in §3–§4.

## 1. Pinned environment (read-only)

| Pin | Value |
|---|---|
| Lane HEAD (`master`) | `a238989a96cb0d2b939679126b832d75b861ca6e` (plan commit) |
| Plan's frozen base tip | `a5f7459f99bb27bf697e9438362e75ac5833eca8` |
| `corpus/SOURCES.md` at `a5f7459f` | sha256 `3eedcecaa1adea18422e77cd0bc08d4b088596983887af25be10568dcb6a7122` |
| `corpus/SOURCES.md` at HEAD | sha256 `3eedceca…` — identical to the base tip |
| `corpus/SOURCES.md` working tree | sha256 `aaed976a4f77e15826271925997413b4a6409fad55bc7f90ed057002bae9b7c4`, `git diff --numstat` = `6 0` (six appends, zero deletions) |
| Staged package | `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md`, sha256 `e2bdff3fe7b1a44bc764f180c6bda2ba73e9c625bbe9dd28eec3d9cef7090aaf` |
| Staged file git state | `M` in `shokuknow`; tracked `HEAD` version yields **143** ids, working tree yields **188** (`git diff --numstat` = `188 143`) |

The staged input is therefore an **uncommitted working-tree file in another repo**. `188` is
reproducible only against that sha256, not from any commit; pin the hash in any receipt that quotes it.

## 2. Frozen pipeline — exact commands and exact output

```bash
S=/home/vgpnk/Projects/shokuknow
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
W=/tmp/ecg69-scratch/run; rm -rf "$W"; mkdir -p "$W"; cd "$W"

# frozen bytes of the revision the plan measured (a5f7459f; == HEAD for this file)
git -C "$L" show a5f7459f99bb27bf697e9438362e75ac5833eca8:corpus/SOURCES.md > SOURCES.md

grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' SOURCES.md                                  | grep -oE 'S[0-9]+' | sort -u > reg-ids
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' "$S/merge/kotoba/SOURCES.append.md"        | grep -oE 'S[0-9]+' | sort -u > staged-ids
comm -12 reg-ids staged-ids > collisions
wc -l reg-ids staged-ids collisions
echo "collisions bytes=$(wc -c < collisions)"
```

Output:

```
 128 reg-ids
 188 staged-ids
   0 collisions
 316 total
collisions bytes=0
```

- **128 / 188 / **0** — reproduced.** `collisions` is a zero-byte file, not a file containing a blank line.
- `reg-ids` sha256 `3f00449b34f4a69dd757b85b934a31c59747977497fe383bfab309515e380b29`;
  `staged-ids` sha256 `02a4098845c47a384a5bc4213e6d3bb5e4b04cb7c072f7cce98eb573959fe4e6`.
- Zero duplicate ids in either input: `uniq -d` on the registry rows and on the staged rows both return 0.
- `LC_ALL=C` rerun gives `0` collisions; both id files pass `LC_ALL=C sort -c`, so `comm`'s sortedness
  precondition holds under byte collation as well as the ambient locale.
- The staged id space is exactly contiguous `S203 … S390` (188 = 390 − 203 + 1, no gaps), which is why
  an empty intersection at the frozen base is a structural fact, not luck: the registry at
  `a5f7459f` stops at `S202`.
- Neither input contains an indented table row at the frozen revision
  (`grep -cE '^ {1,3}\|'` → registry `0`, staged `0`), so both patterns would agree there. That is
  precisely why the guard needs a fixture to be shown capable of failing.

## 3. Live working tree — the same pipeline, measured as it actually is

```bash
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' "$L/corpus/SOURCES.md" | grep -oE 'S[0-9]+' | sort -u > reg-wt-ids
comm -12 reg-wt-ids staged-ids > collisions-wt
wc -l reg-wt-ids collisions-wt
```

```
134 reg-wt-ids
  6 collisions-wt
140 total
```

`collisions-wt` = `S203 S204 S205 S206 S207 S208` — the six rows the draft appended, each colliding
with a staged id that names a different document:

| colliding id | lane row (working tree) | staged row |
|---|---|---|
| S203 | Roo Code Documentation — Skills | S203 OpenAI Model Spec (2026/08/18) |
| S204 | Amp — Agent Skills | S204 anthropics/skills — skill-creator/SKILL.md |
| S205 | Deep Code — Agent Skills (English) | S205 Qwen Code Docs — Agent Skills (English) |
| S206 | Junie — Agent Skills | S206 Qwen Code Docs — Agent Skills (中文) |
| S207 | opencode — Agent skills (served docs page) | S207 Qwen Code Docs — Agent Skills (日本語) |
| S208 | Microsoft Agent Framework (supersedes S201) | S208 Qwen Code 周报 (weekly update) |

**How this reads.** The plan's constraint is "adopted ids continue the lane registry from S203", and the
package's first id is `S203` — measured one past the lane's last id at the frozen base (`S202`). Those
two facts make numeric overlap after the append unavoidable, so `6` here is geometry, not a violation
of the pre-append guard: the pre-append precondition it enforces was `0`, and it was `0`. What `6`
does mean is that the lane's `S203–S208` and the package's `S203–S208` are now different documents
under the same numbers, so the package's rows for those numbers can never be appended by number and
must be matched by URL.

## 4. Non-vacuity proof (the guard can fail)

### 4.1 Controlled fixture, in scratch

```bash
printf '%s\n' '| S001 | base row |' '  | S203 | indented two-space colliding row |' > novac.md   # sha256 28da9f9a…
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' novac.md | grep -oE 'S[0-9]+' | sort -u          > novac-03
grep -oE '^\|[[:space:]]*S[0-9]{3,}'      novac.md | grep -oE 'S[0-9]+' | sort -u          > novac-col0
```

```
03-ids=[S001 S203 ] col0-ids=[S001 ]
03 catches S203=1 col0 catches S203=0
```

Against a staged set containing only `S203`: `comm -12` gives **1** collision (`S203`) under the
0–3-space pattern and **0** (zero bytes) under the column-zero-only pattern.

The same fixture under `set -x` shows the match itself, so the extraction cannot be passing by
accident on a substring:

```
+ grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' novac.md
| S001
  | S203
+ grep -oE '^\|[[:space:]]*S[0-9]{3,}' novac.md
| S001
```

Boundary check: a four-space-indented row (`    | S204 | …`) is matched by **neither** pattern
(0 matches each) — correct, since four spaces open a CommonMark code block, and the census parser's
own rule is 0–3 leading spaces.

### 4.2 The L1's `assimilation/guard-proof/` fixture, re-derived from the frozen bytes

The seat did not trust the existing files; it rebuilt the fixture from the frozen revision and
injected the single indented row itself:

```bash
git -C "$L" show a5f7459f:corpus/SOURCES.md > gproof.md
printf '%s\n' '  | S203 | guard-proof fixture row — indented colliding id |' >> gproof.md
```

```
 129 gp-ids-03
 128 gp-ids-col0
   1 gp-coll-03          -> S203
gp col0 collisions bytes=0
```

Byte-identity with the checked-in control:

```
a0440fa8…  assimilation/guard-proof/reg-ids
3f00449b…  assimilation/guard-proof/reg-ids-col0
a0440fa8…  my re-derived gp-ids-03
3f00449b…  my re-derived gp-ids-col0
```

`assimilation/guard-proof/SOURCES.md` differs from the frozen `corpus/SOURCES.md` by exactly one
added line (`347a348 > "  | S203 | guard-proof fixture row — indented colliding id |"`), and
`guard-proof/collisions` contains `S203` (5 bytes) while `guard-proof/collisions-col0` is empty.
Independently reproduced, so the proof is not a self-check of the seat's own copy.

## 5. Consistency observations (evidence, not verdicts)

**5.1 Pattern parity with the instruments.** The guard's 0–3-space pattern is the fleet census
parser's own rule: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh:541`
`table_re='^ {0,3}\|'` and the shared row parser at `:573` ("Markdown table rows with 0-3 leading
ASCII spaces"). The C1 counter consumes the same rule: `verifiers/check_skill_precedence.py:117`
`if not re.match(r"^ {0,3}\|", line)` in `_source_rows`. So the guard is aligned with the two
readers that decide what an id row is.

**5.2 The other ten verifiers are column-zero-only.** `verifiers/` holds ten files with
`SOURCES_ROW_RE = re.compile(r"^\|[ \t]*S[0-9]{3,}[ \t]*\|")`
(`check_agent_definitions`, `check_command_files`, `check_description_thresholds`,
`check_explicit_invocation`, `check_hook_files`, `check_mcp_instructions`, `check_plugin_manifests`,
`check_scoped_rules`, `check_scoped_rules_v31`, `check_scoped_rules_v32`). A registry row indented
1–3 spaces is a legal row to the census and to the C1 counter, and invisible to all ten. This is a
pre-existing divergence class, not something round 69 created; the guard catches it on the way in,
which is exactly why the fixture proof matters.

**5.3 `0` collisions is an id-space statement, not a duplicate-document statement.** Matching
normalized URLs (scheme kept, trailing slash stripped) between the frozen registry and the staged
file yields **11 document twins**, e.g. `S123↔S203` (OpenAI Model Spec), `S124↔S204`
(anthropics skill-creator), `S129↔S209` (arXiv 2604.09443), `S200↔S273` (Kilo Code). With the draft
rows added the count is **16**; the five new twins are

```
docs.roocode.com/features/skills              S203 ↔ S265
ampcode.com/docs/customize/skills             S204 ↔ S276
deepcode.vegamo.cn/en/docs/configuration/...  S205 ↔ S250
junie.jetbrains.com/docs/agent-skills.html    S206 ↔ S252
learn.microsoft.com/.../agent-framework/agents/skills  S208 ↔ S274
```

(`S207`'s English `opencode.ai/docs/skills/` page has no staged twin; the package stages only the
Japanese `…/docs/ja/skills/` pages as S230/S259.) The plan (item 10) requires that "each staged row is
re-pointed by document (URL), never by arithmetic, and the renumber map lands in the lesson". The
lesson's collision paragraph says instead "no renumbering was needed and no citation was re-pointed by
arithmetic" (`corpus/lessons/round-69.md:73-78`) and carries no map. The lane rows are *not* literal
copies of the staged twins — e.g. staged `S265` anchors on `"Roo-specific (higher priority)"` plus the
scope line, while lane `S203` anchors on `"Project skills override global skills, mode-specific
override generic"` plus a re-labelled native root; staged `S276` says "eight-location ordered list",
lane `S204` quotes the masking sentence — which is what "re-grounded in-round" looks like and supports
reading the adopted set as empty. If it is empty, the map is legitimately empty and one sentence
saying "0 package rows adopted, so the map is empty" would close the obligation; as written, the
lesson's claim and the measured 16 twins do not line up.

**5.4 Duplicate-URL warnings move 16 → 18, and that matches the plan's baseline.** Running the fleet
census read-only on a `/tmp` copy: `validate --file` reports `16` W04 at the frozen base — the number
`controls/census-before.txt` already records — and `18` on the live draft. The two new warnings are
`S207 duplicate url opencode.ai/docs/skills` (against S024; the trailing slash is normalized away) and
`S208 duplicate url learn.microsoft.com/en-us/agent-framework/agents/skills` (against S201). Both are
intentional second-scope/supersede rows and match existing precedent (S018/S019/S021/… are already
W04). Note that this same `/tmp` invocation also emits E11 elements because
`--file` outside a mirror cannot resolve `used-by` paths; those E11s are environmental and are **not**
evidence about the draft, so no census verdict is claimed here.

## 6. What this seat did not do

- Did not modify `SKILL.md`, `corpus/`, `verifiers/`, `PROVINCE.md`, `plans/`, any committed file,
  the lane's jj state or its Git index; did not `git checkout`/`git write` anywhere.
- Did not judge C1/C2/C3, did not run the verifiers that execute code, and did not re-run any
  sibling's claim except the artefacts in §4, which were re-derived from frozen bytes.
- Did not treat the `/tmp` census run as a gate result (see §5.4).

## 7. Files changed / installs / risks

- Changed: this report only.
- Installs: none.
- Risk if read naively: the triple `128 / 188 / 0` is true of the frozen revision and false of the
  live file (`134 / 188 / 6`). Any closure sentence quoting it must name the revision, or it will be
  false by the time it is committed.
- Risk carried forward: the ten column-zero verifiers (§5.2) would silently ignore a legal indented
  registry row; the guard is the only pre-append defence.
- Re-run notes: scratch lives at `/tmp/ecg69-scratch` (ephemeral). §2–§4 contain every command and
  every output needed to reproduce the numbers without it.
