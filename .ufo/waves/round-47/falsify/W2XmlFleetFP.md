verdict: HOLDS — C2's fleet-wide XML claim and the new `trigger.no_xml_tag` gate survive: 18/18 fleet-root `SKILL.md` carry zero angle characters in `name`/`description`, the gate is wired (injected `<skills>` flips the full battery exit 0→1), the S012 line citation is exact; the sweep found one true S003 violation in a user skill (outside the fleet), three latent false-positive mechanisms and three false-negative surfaces (two declared at `:210-213`, zero live instances).

# W2XmlFleetFP — false-positive/negative sweep of `trigger.no_xml_tag` over host SKILL.md

Tip under attack: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (BASE `c61a973`).
All repo citations are at 7ad7fad. Digests of the files I imported/read:
`verifiers/verify_skill_checklist.py` `4ea2100dee220077eead8ed8cfc2c5acb311ffff8746451bb5fd12b202c5e38a`;
`SKILL.md` `24df651bdc74f057fa8252271970bfd65b5e5ceac8519c1d21f3bb88ee901d87`;
`corpus/SOURCES.md` `bd7282c31d3fed54bfb2c1b220f78f71154b083eb3f70606caa885edcffe7951`.

## 1. What the check is (observed)

`check_no_xml_tag` at `verifiers/verify_skill_checklist.py:1294-1313` parses the frontmatter with
`parse_frontmatter`:515-601, then applies `XML_TAG_RE` (:404-407) and `YAML_ANGLE_ESCAPE_RE` (:409) to
the parsed `name` and `description`. Dispatch is `:2391-2392`; the id is in `CHECK_IDS` at `:309-310`.
The row's declared limit text (`:1307-1308`) says the check "reads S003's words, not Anthropic's packager";
`:210-213` additionally declares `when_to_use`, fullwidth, YAML aliases and plain-scalar `#` outside the parse.

## 2. Population and coverage

Target population exactly as assigned: every `<repo>/SKILL.md` for the 18 `*-shokunin` repos under
`/home/vgpnk/Projects/shokunin`, plus every `SKILL.md` under `~/.agents/skills`, `~/.claude/skills`,
`~/.codex/skills`, `~/.config/opencode/skills`.

| root | paths | unique realpaths | FAIL |
|---|---|---|---|
| fleet root (`*-shokunin/SKILL.md`) | 18 | 18 | 0 |
| `~/.agents/skills` (symlinks followed) | 11 | — | 1 |
| `~/.claude/skills` | 12 | — | 0 |
| `~/.codex/skills` | 6 | — | 0 |
| `~/.config/opencode/skills` | 0 | — | **directory absent** (`ls: cannot access`) |
| **total** | **47** | **44** | **1** |

21 `*-shokunin` dirs exist; `audio-`, `game-dev-2d-` and `revenger-` ship no `SKILL.md` (0 files there to scan).
Duplicates by realpath: `omarchy` resolves to `/home/vgpnk/.local/share/omarchy/default/omarchy-skill/SKILL.md`
from three roots (agents/claude/codex); `swarm` and `tower/swarm` both resolve to
`/home/vgpnk/Projects/ompskills/.omp/skills/tower/swarm/SKILL.md`. 29 user paths → 26 unique user files.

Coverage defect in the obvious method (mine, corrected): a `Path.rglob("SKILL.md")` sweep does **not**
descend symlinked skill dirs on Python 3.14.8; my first pass scanned 21 of 29 user paths and 0 of the
8 symlink-derived paths (7 unique files) — including the only hit.
`os.walk(..., followlinks=True)` / `find -L` is required.
Supplemental population (beyond the assigned roots, for classification only): 4047 nested `SKILL.md`
under the fleet repos — 48 FAIL, all intended-negative fixtures or a tracked historical copy (§3).

## 3. Hits, classified

| path:line | field | match | class |
|---|---|---|---|
| `~/.agents/skills/shokunin/SKILL.md:8` → realpath `/home/vgpnk/Projects/ompskills/.omp/skills/shokunin/SKILL.md:8` | `description` | `<id>` ×2 | **true S003 violation** (TP) |
| `kotoba-shokunin/.ufo/round-33/SKILL.md:14` (tracked at tip) | `description` | `<skills>` | true violation, non-production historical copy |
| `.tower/jj-probe/kotoba-shokunin/SKILL.md:14` (outside the repo) | `description` | `<skills>` | true violation, stale worktree copy |
| 47 nested files under `verifiers/fixtures/checklist/`, kaidoku `.ufo/**/EX-15/fixtures/roots/`, kake `.ufo/round-20/frozen/` | `description`/frontmatter | various | intended-negative fixtures (not FPs) |

The one live hit is a true positive, not a false positive: line 8 reads
`  round", "train <id>", "teach <id>". Anti-trigger: general orchestration and` inside the folded
`description:` block (lines 3-9). `<id>` is a lexical start-tag shape, S003 (`corpus/SOURCES.md:16`)
says the description cannot contain XML tags, and S012's packager rejects any `<` outright.
Impact is bounded: omp renders a derived one-liner (`SKILL.md:22-24` describes
`cache.get(key) ?? previewSkillDescription`), so the raw `<id>` reaches only clients that ingest the
raw description, and packaging. It is outside the fleet root and outside my write scope — reported, not fixed.

Fleet root: **0 hits**. `kotoba-shokunin/SKILL.md` frontmatter (`:1-17`) contains no angle character in
either field; the only `<`/`>` in that range is the block-scalar indicator `description: >` at line 3.
At BASE `c61a973`, the same frontmatter carried exactly one `<skills>` at `SKILL.md:14`; at tip the
frontmatter count is 0 (whole-file count 8→6, remaining occurrences are body prose). The C2 sub-claim
"frontmatter count 1→0" is confirmed. Independent confirmation not using `parse_frontmatter` (awk over
the raw `---` block of all 47 targets) returns only that one `<id>` line plus eleven
`description: >` block-scalar indicators — so there are **zero character-level false negatives** on this population:
every field value containing `<` or `>` is flagged.

## 4. False-positive mechanisms (latent; no host file triggers them)

**FP-1 — the YAML-escape rule ignores quoting style (the concrete defect).**
`YAML_ANGLE_ESCAPE_RE` (:409) is applied to the unquoted value (:1300-1301) with no knowledge of the
scalar's quoting, but its docstring scopes it to "a YAML **double-quoted** ``\\x3c``/``\\u003c`` escape"
(:100-101). YAML only decodes the escape in a double-quoted scalar; in a single-quoted, plain, or
double-quoted-with-escaped-backslash scalar the value is the literal six characters. PyYAML 6.0.3 confirms:

```
single-quoted      checker=FAIL yaml_value='use \\u003c here'  yaml_has_lt=False
plain-scalar       checker=FAIL yaml_value='use \\u003c here'  yaml_has_lt=False
double-quoted      checker=FAIL yaml_value='use < here'        yaml_has_lt=True   <- correct
dq-escaped-bs      checker=FAIL yaml_value='use \\u003c here'  yaml_has_lt=False
```

Three of four FAILs are false positives relative to both S003 and S012 (the string has no `<`).
No scanned file contains `\u003c`/`\x3c`, so the defect is latent, but it is a real divergence
between the row's stated scope and its code. Repro: `sh .ufo/waves/round-47/falsify/W2XmlFleetFP.repro.sh`.

**FP-2 — a `>` escape alone FAILs.** `description: just \x3e` → FAIL with match `\x3e` (:409 matches
both `x3c` and `x3e`). A lone `>` cannot form an XML tag, so this is overreach against S003's wording;
it is consistent with S012's any-angle rule, which the row's own limit text discloses (:1307-1308).
Latent (no host instance).

**FP-3 — prose `<`…`>` pairs.** `if a<b then c>d` → FAIL, match `<b then c>`, which is not well-formed
XML (`then` is not a `name="value"` attribute). A genuine prose comparison can be flagged. Latent.

**FP-4 (cosmetic) — declarations report only a prefix.** `use <!DOCTYPE html>` → detail says match
`<!D` because the alternation `<!\[CDATA\[|<\?[A-Za-z_]|<![A-Za-z]` (:406-407) returns the shortest
branch. Classification is still FAIL/correct; only the reported token is truncated.

## 5. False-negative surfaces (none live; all but one disclosed)

- `when_to_use:` is not parsed: a frame with `description: fine` + `when_to_use: use <skills>` returns
  PASS. Declared at `:210-213` ("Claude Code's ``when_to_use`` (appended to the listed description) …
  outside the structural parse"). No host file in the 47 uses `when_to_use` (grep: 0 hits).
- `< skills >` (space after `<`), autolinks `<https://example.com/a>`, and email autolinks pass — all
  fail Anthropic's packager, all declared at `:210-212` ("a ``a -> b`` passes here and fails packaging").
- HTML entities `&lt;skills&gt;` pass and are **not** in the declared-limit list. This is consistent with
  both sources as written (the string contains no `<`), so I record it as an interpretive gap, not a
  defect: a client that HTML-renders the description would display `<skills>`. `[INFERENCE]` no client
  behaviour was observed.
- `name` is scanned too (only `description` is governed by S003 at `SOURCES.md:16` and by S012 at
  `quick_validate.py:79-81`). It is a deliberate superset, redundant with the kebab-case name rule, and
  no host file has an angle in `name` — no FP risk on this population.

## 6. Operability and mutation test (gate is load-bearing at tip)

Commands in the scratch clone at 7ad7fad:

| command | exit | key output |
|---|---|---|
| `python3 verifiers/verify_skill_checklist.py --self-test` | 0 | `0 failure(s) over 1845 assertions` |
| `python3 verifiers/verify_skill_checklist.py --json` (default target) | 0 | 11 PASS / 0 FAIL, `trigger.no_xml_tag` PASS |
| `… --check trigger.no_xml_tag --json` on the shokunin user file | 1 | FAIL `XML tag in description: '<id>'` |
| mutation: inject `<skills>` into `SKILL.md` description | — | mutated copy `never reach the <skills> router` |
| `… --check trigger.no_xml_tag --json` after mutation | 1 | FAIL `'<skills>'` |
| `… --json` after mutation | 1 | 10 PASS / 1 FAIL, sole failure `trigger.no_xml_tag` |
| `git checkout -- SKILL.md` (clone) then `git diff --stat` | 0 | empty — clone restored |

So the new row changes the battery's verdict on a single description edit; it is not decorative.

S012 citation check (freshness): `corpus/SOURCES.md:25` cites
`quick_validate.py:79-81` at tree `dbd4588` (2026-10-09). I fetched the pinned upstream file
(`curl` exit 0, 3972 bytes) and `grep -n` shows exactly lines 79 `# Check for angle brackets`,
80 `if '<' in description or '>' in description:`, 81 `return False, "Description cannot contain angle brackets (< or >)"`.
The claim "S012 stricter" holds: S012 rejects any `<`/`>`, while `XML_TAG_RE` requires a tag shape.
Note: the local mirror at `~/.claude/skills/synced/…/skill-creator/scripts/quick_validate.py` is a
different revision (the same rule sits at :121-124) — it is not the pinned tree and is not what the row cites.

## 7. Commands run (with exit codes)

```
git clone --no-hardlinks … && git checkout --detach 7ad7fad…        # CLONE_OK, HEAD=7ad7fad
python3 sweep.py > sweep.out.json                                   # 0; SCANNED 4086 (48 FAIL) — no symlink follow
python3 (os.walk followlinks) > sweep_follow.out.json               # 0; SCANNED 29 user files, 1 FAIL
python3 verifiers/verify_skill_checklist.py --self-test             # 0; 1845 assertions
python3 verifiers/verify_skill_checklist.py --json                  # 0; 11 PASS 0 FAIL
python3 verifiers/verify_skill_checklist.py --check trigger.no_xml_tag --json --skill <user skill>  # 1
python3 verifiers/verify_skill_checklist.py --json   (mutated SKILL.md)                             # 1; 10 PASS 1 FAIL
awk '… c==1 && /[<>]/' over targetlist.txt                          # 0; only <id> + block-scalar '>' lines
curl -sSL raw.githubusercontent.com/anthropics/skills/dbd4588…/quick_validate.py                    # 0; 3972 B
python3 + PyYAML 6.0.3 escape semantics                              # FP-1 table above
sh .ufo/waves/round-47/falsify/W2XmlFleetFP.repro.sh                 # 0
```

No tool installs or upgrades were needed or performed.

Artifacts (this lane): `W2XmlFleetFP.hits.json` (48 records: 47 target SKILL.md paths plus the absent opencode dir;
primary FAILs; supplemental classification), `W2XmlFleetFP.probe.json` (synthetic battery), `W2XmlFleetFP.repro.sh` (re-runs §4/§5
and the live hit).

## 8. What I did NOT check

- I did not run the full verifier battery against the 26 unique user skills — only `trigger.no_xml_tag`
  on them; their box maps, command vocabulary and citations are outside this lane's question.
- I did not scan every `SKILL.md` on the host: only the assigned roots plus the 4047 nested files under
  the fleet repos. Other checkouts under `~/Projects` (e.g. unlinked skills under
  `~/Projects/ompskills/.omp/skills`), package caches and `node_modules` were not enumerated; symlinked
  subdirectories inside the fleet repos were not followed by the fleet glob.
- I did not execute Claude Code / Anthropic packaging to observe raw-description ingestion or entity
  rendering; the `&lt;` gap is inference.
- I did not test BOM/CRLF/tab-indented frontmatter robustness (no such file exists in the population).
- I did not verify the round-47 ledger/census or the C1 surface pins — other lanes own those.
