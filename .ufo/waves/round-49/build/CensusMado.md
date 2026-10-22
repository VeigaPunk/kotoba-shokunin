ROW | mado | master (HEAD detached at the same commit) | e33ea30461f6e9bbeee40beef19770a953f7a105 | SKILL.md | none | no | no | SKILL.md:8 | "desktop & compositor craft playbook — the Hyprland/waybar/walker/terminal config plane"

# Round 49 C1 — sibling-overlap census: mado-shokunin

Date 2026-10-22. Seat KotobaR49.CensusMado (leaf, no dispatch). Lane kotoba-shokunin
read-only except this file; mado-shokunin read-only throughout via
`git -C … rev-parse/symbolic-ref/branch/ls-tree/show/grep`. No jj, no git write, no pacman
install (nothing needed), no web fetch this seat.

## Findings

1. **Classification `none`.** mado claims no part of kotoba's core: no skill-document
   craft, no prompt wording, no agent-definition or AGENTS.md craft, no instrument over
   those surfaces. Its declared surface is the desktop/compositor config plane, read-only
   measure-and-recommend (`PROVINCE.md:6-12`; `SKILL.md:371-391`).
2. **Frontmatter description names no lane at all.** `SKILL.md:3` reads verbatim
   `description: Domain specialist — desktop & compositor craft. Rank: shonen (probation).`
   It names kotoba: **no**; it carries no sibling arbitration rule: **no** (`git show
   <c>:SKILL.md | grep -c kotoba` → `0`, exit 1).
3. **PROVINCE.md never names kotoba** — 0 occurrences (`git show <c>:PROVINCE.md | grep -c
   kotoba` → `0`, exit 1). Its Refuses paragraph routes only three lanes, none of them
   kotoba: secrets → kagi, model endpoints → kama, model quality → kengaku
   (`PROVINCE.md:14-16`). The mint roster scan also skipped kotoba entirely
   (`MINT.md:13-16`: kagi, kama, kumitate, kake).
4. **No `Adjacent` section exists.** `PROVINCE.md` is 20 lines / 1,950 B with title,
   Domain, Owns, Refuses, one round-19 refinement and an out-of-province line only — so
   there is no reciprocal arbitration statement to cite, in contrast to kumitate
   (`PROVINCE.md:27`), which names kotoba on both sides.
5. **The nearest boundary is descriptive, and mado itself disclaims it.**
   `corpus/knowledge/terminals-and-omarchy.md:115-151` is a section titled "omarchy skill
   anatomy" that lists the omarchy `SKILL.md` frontmatter, its trigger line, and a
   line-ranged body section map. It is read to ground *which terminal config paths that
   skill covers* (`:158-159`), not to judge the document. mado's own overlap census
   classifies that facet as kotoba's and "not as owned ground"
   (`.ufo/waves/round-18/w1/reports/SiblingOverlap18.md:81`, quoting kotoba's
   `SKILL.md:397`) and states the same rule in its own playbook:
   `SKILL.md:371` "## Omarchy boundary — skill instructs, mado measures".
6. **Same for its instruments.** `tools/mado-verify.sh:3679,3687` resolves the omarchy
   skill leaf only to hash it (`sha256sum`, P4 pin at `SKILL.md:901`: 392 L / 14,908 B).
   No instrument reads a lane's SKILL.md/prompts/AGENTS.md; `tools/` is five files over
   its own config plane (`git ls-tree <c>:tools/`).
7. **Self-applied craft criterion — noted, not a claim.** `SHONEN.md:5` requires
   "SKILL.md contains real decision tables, error patterns, checklists, cited sources" and
   `tools/mado-assessment.py:21` encodes that promotion item. It is a probation gate over
   mado's *own* file, applied to no other lane, so it does not contest kotoba's core under
   the `contested` test (writing/auditing those surfaces *for other lanes*).
8. **Consistent with kotoba's current line.** `PROVINCE.md:34` already places mado in the
   "no overlap observed" bucket. This census confirms it with a pinned sweep; only the
   count-of-lanes-named side of C1 changes, not mado's substance.

## Negative claim and its sweep (Q14)

Command (date 2026-10-22, pinned commit):

```
git -C /home/vgpnk/Projects/shokunin/mado-shokunin show e33ea30461f6e9bbeee40beef19770a953f7a105:SKILL.md \
 | grep -Ec 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'
```

Sweep over the eight governing documents at the pin (concatenated, same pattern):

| file | matching lines |
|---|---|
| SKILL.md | 28 |
| PROVINCE.md | 0 |
| README.md | 1 |
| AGENTS.md | 0 |
| MINT.md | 1 |
| SHONEN.md | 1 |
| SCORECARD.md | 13 |
| LOG.md | 30 |
| **total (8 files, exit 0)** | **74** |

Per token over the same eight files: `SKILL.md` 58 · `prompt` 7 · `AGENTS.md` 1 ·
`frontmatter` 0 · `trigger` 2 · `description` 7 · `kotoba` **0**. Lines can match more
than one token, so the per-token sum exceeds the 74 matching lines.

All 74 are self-reference or incidental prose, verified line by line:
- 58 × `SKILL.md` = mado's own file, or the read-only omarchy skill leaf
  (`SKILL.md:373,901,1736,1773,1797,1816,1860-1908` erratum history).
- 7 × `prompt` = mado's own wave prompt paths (`SCORECARD.md:224`,
  `LOG.md:658-659,675,771`) — pointers, no craft rule.
- 1 × `AGENTS.md` = `SKILL.md:982`, a reference to its own `AGENTS.md:3`.
- 2 × `trigger` = its severity-classification triggers (`SKILL.md:181`, one severity table
  row), unrelated to frontmatter triggers.
- 7 × `description` = the frontmatter line itself, plus prose about surface-image
  descriptions and source supersession.
- 0 × `frontmatter` in any governing document; the 6 repo-wide hits are corpus/wave
  reports describing the omarchy skill or the Omarchy manual.

Repo-wide `kotoba` at the pin: `git grep -il kotoba <c> -- . | wc -l` → **34 files**,
`git grep -in kotoba <c> -- . | wc -l` → **226 lines**, **all** inside `.ufo/waves/**`
and `corpus/`, **none** in the eight governing documents
(`git grep -in kotoba <c> -- SKILL.md PROVINCE.md README.md AGENTS.md MINT.md SHONEN.md
SCORECARD.md LOG.md` → no match, exit 1). The substantive occurrences are mado's own
sibling censuses: `SiblingOverlap.md:37,46` (roster list), `SiblingOverlap18.md:34,64,81`
(assigning the omarchy-document-instance facet to kotoba), `ConnProvinceRoster.md:9,15,29,33`
(omarchy-tree census, kotoba held 170 substrate-evidence files, no province claim).

## Evidence

Pin (date 2026-10-22), all exit 0 except `symbolic-ref`:

```
$ git -C …/mado-shokunin rev-parse master            → e33ea30461f6e9bbeee40beef19770a953f7a105  (exit 0)
$ git -C …/mado-shokunin rev-parse HEAD              → same 40-hex                              (exit 0)
$ git -C …/mado-shokunin symbolic-ref -q HEAD        → no output                                (exit 1, detached)
$ git -C …/mado-shokunin branch -a --contains e33ea30
* (no branch) / master / remotes/origin/HEAD -> origin/master / remotes/origin/master
$ git -C …/mado-shokunin log -1 --format='%H %ci %s'
e33ea30… 2026-10-21 13:39:30 -0300 round-22: retain final intervention proof and strict nonadmission
$ git -C …/mado-shokunin ls-tree --name-only <c> | head -3   → .gitignore .ufo AGENTS.md …
$ … ls-tree -r --name-only <c> | grep -E '^(skills?/[^/]+/)?SKILL\.md$' → SKILL.md   (exit 0)
$ git -C …/mado-shokunin show <c>:SKILL.md    | sha256sum
f8f856c5f583394fc830b4cfb6c1e340505b2962a20957dbabbd7af0a2fbca42   1985 L / 169,402 B
$ git -C …/mado-shokunin show <c>:PROVINCE.md | sha256sum
1b25bb1e980925b356663602d002c1c15307a0dfac8bfafd9988bd4d8df7464b     20 L /   1,950 B
```

Scope quote, verbatim, `SKILL.md:8` (od-verified, line ends after "plane"; line 9
continues "and display behavior on this host."):

> desktop & compositor craft playbook — the Hyprland/waybar/walker/terminal config plane

Fuller province text, `PROVINCE.md:3-4` (bold markers as in file; line breaks after
"walker"):
> **Domain:** desktop & compositor craft — the Hyprland/waybar/walker
> configuration plane and display behavior on this host.

Near-boundary quotes (recorded for the connector; `none` rows carry no overlap quote):
- `SKILL.md:371` — "## Omarchy boundary — skill instructs, mado measures"
- `.ufo/waves/round-18/w1/reports/SiblingOverlap18.md:81` — "omarchy skill **as a document
  instance** (frontmatter/anatomy survey), not as owned ground | kotoba | `SKILL.md:397`"
  (that anchor is kotoba's own file, read at `a5adc146` this session).

## Remaining unknowns

- `symbolic-ref` is empty (detached HEAD); "master" comes from `rev-parse master` and
  `branch --contains`, which agree on the commit. A later pin needs the same check.
- `.ufo/` in mado is tracked, so the repo-wide greps cover it; untracked scratch is not
  covered by `git grep` and I did not open the working tree (bounds).
- I read only the 13 sweep-matching `SCORECARD.md` lines, not its full rubric, so a hidden
  craft criterion there beyond the SHONEN promotion item is unlikely but not excluded
  (`frontmatter` 0, `kotoba` 0).
