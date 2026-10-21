verdict: 2 XML-tag-shaped tokens in 1 of 12 installed SKILL.md path occurrences (11 unique files, 10 skill names) — both are `<id>` placeholders in `shokunin`; the scan root `~/.omp/agent/skills` does not exist, and the lane's own `<skills>` (SKILL.md:14) sits outside every scanned root.

# Scoped findings — C2HostSkillsScan (round 47 BUILD)

Leaf, report-only. No production file edited; no patch produced. Writes: this file plus
`C2HostSkillsScan.json` (6563 bytes, sha256 `6de80e5254136ef1869c4d8c847a249e40b5eced0bdcbf340de561017c40d084`)
in `.ufo/waves/round-47/build/`. Scratch: `/fast/scratch/kotoba-r47/C2HostSkillsScan-9/`.
Lane HEAD at scan time: `git -C … rev-parse HEAD` → `c61a973b2e02e1ded169703ddcb06466f4edd8bd`, exit 0 (== BASE).
No tool installed or upgraded; nothing was fetched.

## 1. Corpus census (target roots, as assigned)

| root | assigned form | exists | SKILL.md paths | unique |
|---|---|---|---|---|
| `~/.agents/skills` | `*/SKILL.md` | yes | 10 direct + 1 nested (`tower/swarm`) = 11 | 10 inodes |
| `~/.omp/agent/skills` | `**/SKILL.md` | **NO** | 0 | 0 |
| `~/Projects/kimi-shokunin/skills` | `*/SKILL.md` | yes | 1 | 1 |

Totals: **12 path occurrences, 11 unique inodes, 10 unique `name` values.** The extra path is
`~/.agents/skills/tower/swarm/SKILL.md`, the same inode (`57:803446`) as
`~/.agents/skills/swarm/SKILL.md` (`~/.agents/skills/tower` → `…/ompskills/.omp/skills/tower`,
and `…/tower/swarm` is the same directory as the `swarm` symlink target). A per-path count
double-counts `swarm`; a plain `find` (without `-L`) sees 6 of the 12 paths (the five real
`.agents` directories plus kimi) because five `.agents` entries are symlinks. Names: create-toolset, godspeed, omarchy, reverse-engineer-anything, shokunin, swarm,
tower, ufo, unreal-mcp, unreal-skill (+ kimi-shokunin's `shokunin`).

## 2. Token inventory (the whole result)

| name | token | count | path:line (host) | description offset / len | sha256[:12] |
|---|---|---|---|---|---|
| shokunin | `<id>` | 2 | `~/.agents/skills/shokunin/SKILL.md:8` (realpath `~/Projects/ompskills/.omp/skills/shokunin/SKILL.md`) | 303, 317 / 415 | `59ca05018dbf` |

All other 10 unique files: 0 tokens. The token is inside `"train <id>", "teach <id>"` in the
folded `>` description — placeholder prose, not markup. The kimi-shokunin copy of the same skill
name (`~/Projects/kimi-shokunin/skills/shokunin/SKILL.md`, sha256 `34be71885eb8`) has a different,
tag-free description: same name, two copies, different descriptions.

Out-of-root adjacency, same regex, not counted in the totals above:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/SKILL.md:14` → 1 × `<skills>` at offset 750 of an
814-char description (the C2 repair target; the file is not in any omp discovery root, and its
own portability line says so at `SKILL.md:151`).

## 3. Regex used, and why this one

```
</?[A-Za-z][A-Za-z0-9._:-]*(?:\s[^<>]*?)?/?>
```

XML tag grammar: optional `/` (end tag), name starting with an ASCII letter (`:` admitted for
namespaces), optional whitespace-delimited attributes, optional self-close, closed by `>`.
`[^<>]*` keeps a match from spanning two tags. Reported totals use this regex exclusively.

Candidate comparison, measured on the same 13 descriptions (12 roots + lane SKILL.md) and on
probe strings (`python3 -B`, exit 0):

| candidate | corpus occ / files | `<https://example.com>` | `a <= b` | `<3 hearts>` |
|---|---|---|---|---|
| `<[^<>]+>` (naive) | 3 / 2 | **match (FP)** | no | no |
| `<[A-Za-z][^<>]*>` | 3 / 2 | **match (FP)** | no | no |
| `<[^>\s/][^>]*>` (sibling `C2SimplifyFrontmatter.md:20` draft) | 3 / 2 | **match (FP)** | no | no |
| **grammar (used here)** | **3 / 2** | **no** | no | no |

All four agree on this corpus; they diverge only on inputs the corpus does not yet contain.
The grammar shape is the only one of the four that rejects a bare URL autolink. Its known limits,
stated rather than hidden: ASCII-only name start, so `<Ünïcode>` (a legal XML name) is not matched
— the angle-bracket census below shows this is inert here; and `<<skills>>` matches the inner
`<skills>` substring (tag-shaped substring, not a well-formed tag). Since `parse_frontmatter`
folds block scalars to single spaces, a tag can never be split across a folded newline.

Angle-bracket census over all 13 descriptions: exactly 3 `<` characters exist, all 3 are inside
a matched token (`shokunin` 2, lane 1); zero unmatched `<`, zero Unicode-only tag candidates.
There is no hidden tag the regex misses on this host.

## 4. Counterexamples and calibration data

**C-1 — the middle root is absent, and current binaries do not name it.** `~/.omp/agent/skills`
does not exist (`test -d` false; `find ~/.omp -maxdepth 4 -type d -name skills` → nothing).
The frozen snapshots agree: `grep -c '\.omp/agent/skills'` → **0** in both
`/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings` and `…/opencode-1.19.3.strings`, while
`.agent/skills` 2, `.agents/skills` 2, `.config/opencode/skills` 2, `.claude/skills` 2,
`.claude/plugins/cache` 2 in the omp dump. Two records still assert it: `verifiers/verify_harness_claims.py:59-66`
("Verified 2026-09-28 against the 17-name catalogue", `USER_ROOTS` includes
`HOME / ".omp/agent/skills"` at line 64) and `corpus/knowledge/harness-router-models-round9.md:80,86`
("`~/.omp/agent/skills/ufo` wins over `~/.config/opencode/skills/ufo`"; "carries the other two").
Both are stale on this host at BASE. [INFERENCE] a path built dynamically would leave no literal,
so the strings result is evidence, not proof, that 18.12.5 dropped the root — the missing
directory is the direct observation.

**C-2 — the only hit is not markup.** Under S003's literal wording ("cannot contain XML tags",
`corpus/SOURCES.md:16`) the shokunin description FAILs with `<id>`. Under a markup reading (a
tag name a renderer would treat as an element, i.e. the router's own `<skills>`) it passes. This
is the false-positive class a hand-written check inherits: a grammar check flags legitimate
placeholder prose. Consequence for C2's after-value — on this host the rule as literally worded
is 1 FAIL / 10 PASS over the 11 unique files, while the repair target itself is a genuine tag name.
Whatever the check decides, the decision should be recorded as a rule, not as a corpus accident.

**C-3 — the tagged tokens are never router-visible.** `<id>` sits at offsets 303/317 and the
lane's `<skills>` at offset 750, all past the 99-char cliff (`verifiers/verify_harness_claims.py:72`
`CLIFF = 100`; `corpus/knowledge/harness-router-models-round9.md:89` "hard cliff at offset 99").
The rendered catalogue cannot show either token, so the rule is source validity, not render
visibility; a check that measures rendered output would read 0 everywhere and prove nothing.

**C-4 — parser text ≠ strict YAML text, without changing the tag answer.** `unreal-mcp`
description: repo `parse_frontmatter` 1015 chars, PyYAML 6.0.3 1005 chars — the structural parser
keeps `\"Unreal\"` literally where YAML unescapes to `"Unreal"`. Same file has 0 tags under both
readings. A C2 check may use the structural parser (cheap, stdlib) but must not claim its string
equals the YAML scalar.

**C-5 — a naive per-path census double-counts.** See §1: `tower/swarm` and `swarm` are one inode;
`find` without `-L` sees 6 of 12 paths. Any recorded total must state which of the three
counting conventions it uses (path occurrences / unique inodes / unique names).

**C-6 — adjacent roots.** `.claude/skills` exists (12 paths, 0 tokens; 11 synced Claude skills +
the omarchy inode shared with `.agents/skills`), and `.config/opencode/skills` and
`.claude/plugins/cache` are both missing. `.claude/skills` is a real omp root per the 18.12.5
strings (line 557952: "Load skills from .claude/skills/*/SKILL.md") and is excluded from the
assigned roots; the assigned census is therefore not the full offered set.

**C-7 — cache adjacency, not re-derived.** `~/.omp/agent/skill-descriptions.db` holds 17 rows in
`skill_descriptions(key TEXT PRIMARY KEY, description TEXT)` (keys are hashes; `baseline.json:11`
records 14 rows at round 18 — append-only growth, not drift). The 17 stored description values
contain **0** `<` characters (`select count(*) … where description like '%<%'` → 0, exit 0), so no
tag is router-visible through the cache either. I did not reproduce the hash key, so per-skill
cache coverage (the plan's "cache rows absent" item) is not measured here.

## 5. Commands and exit codes

```
find -L ~/.agents/skills ~/.omp/agent/skills ~/Projects/kimi-shokunin/skills \
     -name SKILL.md 2>/dev/null | wc -l
→ 12        pipeline exit 0; find's own exit 1 (the missing ~/.omp/agent/skills root, stderr suppressed)
```
```
R='</?[A-Za-z][A-Za-z0-9._:-]*(?:\s[^<>]*?)?/?>'
find -L <same three roots> -name SKILL.md | while read -r f; do
  awk 'NR==1&&/^---$/{g=1;next} g&&/^---$/{exit} g' "$f"; done \
| grep -oP "$R" | sort | uniq -c
→ "      2 <id>"      pipeline exit 0
```
```
python3 -B /fast/scratch/kotoba-r47/C2HostSkillsScan-9/scan.py
→ files=12 unique_inodes=11 files_with_token=1 unique_inode_files_with_token=1
  totals: {'<id>': 2}     exit 0
```
```
python3 -B scan.py --json > scan.json     exit 0  (payload mirrored in C2HostSkillsScan.json)
grep -c '\.omp/agent/skills' omp-18.12.5.strings      → 0   (opencode-1.19.3.strings → 0)
grep -c -F '<skills>' omp-18.12.5.strings             → 1   (`</skills>` 1, `<available_skills>` 1)
grep -c -F '<skills>' opencode-1.19.3.strings         → 0   (`<available_skills>` 2)
sqlite3 -readonly ~/.omp/agent/skill-descriptions.db ".schema skill_descriptions"  → 1 table, exit 0
```

## 6. What I did NOT check

- `~/.config/opencode/skills`, `~/.claude/plugins/cache` (missing) and project-walk-up
  `.agent/skills`/`.agents/skills` from a working directory with such a tree; only the three
  assigned roots plus a tag-count look at `.claude/skills` (12 paths, 0 tokens).
- Whether omp/opencode 18.12.5/1.19.3's own JS frontmatter reader agrees with the Python
  `parse_frontmatter` on every file (only the PyYAML comparison in C-4 was run).
- YAML validity of the installed descriptions beyond that one parity diff; plain-scalar `: `
  legality (S002/S008) is untouched by this scan.
- The cache-key derivation, per-skill cache-row coverage, and `verify_harness_claims.py` (not run:
  outside this item's named verifiers).
- Rendering: no omp/opencode session was launched, so the `<skills>` catalogue itself was not
  observed; the cliff/offset statements come from the repo constants and description offsets.

## Appendix — condensed scanner extract (full script at `/fast/scratch/kotoba-r47/C2HostSkillsScan-9/scan.py`)

The snippet prints only `files`/`token_totals`/`skills`; the full script additionally emits
`unique_inodes`, `files_with_token`, `duplicate_of`, `non_tag_angles`, `first_token_line` and
per-file `sha256`/`bytes`, and its exact output is mirrored in `C2HostSkillsScan.json`.

```python
import hashlib, json, os, re, sys
LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
sys.path.insert(0, os.path.join(LANE, "verifiers"))
import verify_skill_checklist as vsc
ROOTS = [os.path.expanduser(p) for p in
         ("~/.agents/skills", "~/.omp/agent/skills", "~/Projects/kimi-shokunin/skills")]
TAG_RE = re.compile(r"</?[A-Za-z][A-Za-z0-9._:-]*(?:\s[^<>]*?)?/?>")
def walk(root):
    if not os.path.isdir(root): return []
    return [os.path.join(dp, "SKILL.md") for dp, dn, fn in os.walk(root, followlinks=True)
            if "SKILL.md" in fn]
rows, tokens = [], {}
for root in ROOTS:
    for path in walk(root):
        text = open(path, encoding="utf-8").read()
        fm, problem = vsc.parse_frontmatter(text.splitlines())
        desc = (fm or {}).get("description", "")
        hits = [m.group(0) for m in TAG_RE.finditer(desc)]
        for h in hits: tokens[h] = tokens.get(h, 0) + 1
        rows.append({"path": path, "sha256": hashlib.sha256(text.encode()).hexdigest(),
                     "bytes": len(text.encode()), "name": (fm or {}).get("name", ""),
                     "fm_problem": problem, "desc_len": len(desc), "tokens": hits})
print(json.dumps({"files": len(rows), "token_totals": tokens, "skills": rows}, indent=2))
```
