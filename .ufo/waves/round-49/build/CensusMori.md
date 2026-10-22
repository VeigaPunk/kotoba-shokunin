ROW | mori | master (detached HEAD, same commit) | 28b79d3d1b76824f0c825aabe6cb6c5dc49961bf | SKILL.md | none | no | yes | PROVINCE.md:3-4 | "fleet & host observability (森) — whether the fleet, its waves and its host are alive and progressing."

# Round 49 C1 — sibling-overlap census: mori-shokunin

Date 2026-10-22. Seat KotobaR49.CensusMori (leaf, no dispatch). Surface
`/home/vgpnk/Projects/shokunin/mori-shokunin`, read-only via
`git -C … rev-parse/symbolic-ref/ls-tree/show/grep/branch/log`. No edit, no jj, no git
write, no pacman transaction, no tool install (nothing needed).

## Findings

1. **Pin.** `master` = `28b79d3d1b76824f0c825aabe6cb6c5dc49961bf`, subject
   `round-24 verifier spot-check (integrator, hyaku): non-author admit/reject`
   (2026-10-22 06:34:28 -0300). The checkout is a **detached HEAD at that same commit**
   (`symbolic-ref -q HEAD` exits 1; `branch --contains` lists `* (no branch)`, `master`,
   `origin/master`). `rev-parse master` and `rev-parse HEAD` return the identical 40-hex.
2. **Skill files.** Exactly one, `SKILL.md` at the repo root (642 lines, sha256
   `b043f709…aa04d68`). No `skills/` directory, no second `SKILL.md` at any depth. 13
   top-level entries at that commit (`.gitignore`, `.ufo`, `AGENTS.md`, `LOG.md`,
   `MINT.md`, `PROVINCE.md`, `README.md`, `SCORECARD.md`, `SHONEN.md`, `SKILL.md`,
   `considerthese`, `corpus`, `tools`).
3. **Frontmatter.** `name: mori-shokunin`; description "Fleet & host observability (森) —
   detect and report fleet liveness, wave settlement, kill/OOM events and resource
   runway … Rank: shonen" (`SKILL.md:3`). It **does not name kotoba**
   (`git show <c>:SKILL.md | grep -c kotoba` → 0).
4. **Arbitration clause: yes, against three siblings.** `SKILL.md:3` carries
   "Anti-trigger: NOT dispatch/orchestration (kumitate), NOT OS package/systemd/driver
   state (tsukuroi), NOT endpoint health (kama)" — a concrete anti-trigger rule naming
   kumitate, tsukuroi, kama. None of the three is kotoba.
5. **PROVINCE.md.** Domain `:3-4`; Owns (read-only probes) `:6-10`; Refuses `:12-16`
   (dispatch/orchestration → kumitate; OS package/systemd/driver/boot → tsukuroi;
   endpoint/model serving → kama; credentials → kagi; "Detection and report only — never
   remediation"). Core `:20-28`: watchdog liveness, wave settlement, kill/OOM catalog-ID
   classes, same-boot journal window, resource runway, tmux relevance, lane silence.
   Frontier FR1–FR14. Adjacent table `:63-69` names five siblings — kumitate, tsukuroi,
   kama, kagi, souji — and **not kotoba**
   (`git show <c>:PROVINCE.md | grep -c kotoba` → 0).
6. **Classification `none`.** mori claims no part of kotoba's Core: not SKILL.md
   trigger/frontmatter craft, not anatomy/compression, not decision-table or fidelity
   checklist craft, not agent-definition/AGENTS.md-class/dispatch-prompt craft, and no
   executable instrument over those surfaces. Its 24 `tools/` entries are all fleet/host
   observation gates (census, settlement, journal window, pressure, retention,
   freeze-order, dispatch ledger, seat terminal, routings); there is no `verifiers/`
   directory. The seven-term sweep over the pinned top-level files returns 45 matches,
   every one a self-reference: its own `SKILL.md` line pointers, the word "trigger"
   meaning the kernel **PSI** trigger (`SKILL.md:615-616,635`), and its own frontmatter
   `description`. `kotoba` appears 0 times in the top-level files. The tree-wide 251
   `kotoba` lines are lane-id roster and census data
   (`corpus/knowledge/roster-truth-r12.md:9`, `corpus/knowledge/progressing-weak-r2.md:144`,
   `corpus/knowledge/observability-surfaces-r2.md:78`) — observation of kotoba *as a
   lane*, never a claim to author or audit kotoba's craft.
7. **Nearest contact, and why it is still not `adjacent`.** `tools/mori-dispatch-ledger.py`
   hashes a dispatch task call's `{"context","tasks"}` bytes (`payload_sha256`,
   `payload_bytes`, `:120-165`) — but only for **mori's own wave attempts**, as its own
   record calibration; `PROVINCE.md:134-138` leaves "Planning, slot acquisition, retrying
   and adjudicating dispatch" to kumitate/operator. No mori tool reads `.ufo/prompts/`
   (`git grep -n '\.ufo/prompts' <c> -- tools` → 0), and none reads another lane's
   `SKILL.md`, `AGENTS.md` or prompt text. kotoba's C2 instrument audits fleet prompt
   wording; mori binds identity bytes of its own dispatch record — different artifacts,
   no shared verdict and no shared ownership half. `tools/mori-routed-check.py:57-64`
   scans `SKILL.md` only as one of mori's *own* self-assessment surfaces.
8. **Cross-check (not the basis of the row).** kotoba's current `PROVINCE.md:34` already
   carries mori as "fleet observability — no overlap observed"; reached here
   independently from mori's pinned bytes.

## Evidence

```sh
git -C …/mori-shokunin rev-parse master            # 28b79d3d1b76824f0c825aabe6cb6c5dc49961bf  exit 0
git -C …/mori-shokunin rev-parse HEAD              # same 40-hex, exit 0
git -C …/mori-shokunin rev-parse --abbrev-ref HEAD # HEAD (exit 0)
git -C …/mori-shokunin symbolic-ref -q HEAD        # no output, exit 1
git -C …/mori-shokunin branch -a --contains 28b79d3d
# * (no branch) / master / remotes/origin/HEAD -> origin/master / remotes/origin/master
git -C …/mori-shokunin log -1 --format='%H %ad %s' --date=iso 28b79d3d
# 28b79d3d… 2026-10-22 06:34:28 -0300 round-24 verifier spot-check (integrator, hyaku): non-author admit/reject
git -C …/mori-shokunin ls-tree --name-only 28b79d3d | wc -l   # 13
git -C …/mori-shokunin ls-tree -r --name-only 28b79d3d | grep -E '^(skills?/[^/]+/)?SKILL\.md$'
# SKILL.md  (1 line, exit 0)
git show 28b79d3d:SKILL.md | wc -l    # 642
git show 28b79d3d:SKILL.md | sha256sum
# b043f70958a100e9750cf4857967ba4b0825f6b63b94d568005635405aa04d68
git show 28b79d3d:PROVINCE.md | sha256sum
# 81325bde6bf149397ac50e15b5641bed09563b4b8929a647c0ec21cc23e53540
```

Quoted scope text, verbatim, `PROVINCE.md:3-4` — line 3 is `**Domain:** fleet & host
observability (森) — whether the fleet, its waves and`, line 4 is `its host are alive and
progressing.` The ROW quote drops the `**Domain:**` marker, joins the two lines (17
words) and is otherwise byte-identical.

kotoba counts per pinned file (`git show <c>:<f> | grep -c kotoba`; exit 1 = 0 matches):
SKILL.md 0, PROVINCE.md 0, README.md 0, AGENTS.md 0, MINT.md 0, SHONEN.md 0,
SCORECARD.md 0, LOG.md 0.

Sweep (classification `none`, Q14):

```sh
cd …/mori-shokunin && C=28b79d3d1b76824f0c825aabe6cb6c5dc49961bf
git ls-tree --name-only $C | while read -r f; do git show "$C:$f" 2>/dev/null; done \
  | grep -cEi 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'
# 45   exit 0
```

Per term in the same pipeline: `SKILL\.md` 23, `trigger` 16, `prompt` 3, `description` 3,
`AGENTS\.md` 1, `frontmatter` 0, `kotoba` 0. Distribution of the 23 `SKILL\.md` lines:
LOG.md 17, README.md 2, PROVINCE.md 1, SCORECARD.md 1, SHONEN.md 1, SKILL.md 1 — all
pointers to mori's own file (`SKILL.md:538` cites its own historical revision
`da40bb20…:SKILL.md`). The single `AGENTS\.md`
hit is `LOG.md:632` "(LANE/AGENTS.md rule 2, line 4)" — its own rule file. The 16
`trigger` hits split into kernel PSI triggers (`SKILL.md:615-616,635`; `PROVINCE.md:55,251,259-260`)
and "trigger" meaning motivating evidence; the 3 `prompt` hits are all LOG.md prose
(`:648` cites its own round-12 dispatch prompt as a path, `:698` and `:788` are wave-seat
prose). None concerns authoring or auditing another lane's skill, prompt or always-on
file.

Tree-wide context for the same term set, so the row cannot be read as a narrow sweep:
`git grep -lEi '<pattern>' $C | wc -l` → 1379 files; `git grep -Eic … | awk -F: '{s+=$NF}
END{print s}'` → 8158 lines; `git grep -ic kotoba $C | awk -F: '{s+=$NF} END{print s}'`
→ 251 lines, all lane-id/roster occurrences in `roster-truth-r12.md:9-10`,
`progressing-weak-r2.md:144,159,165`, `observability-surfaces-r2.md:78,299`,
`2026-10-15-free-lunch-measurements-counter-baselines.md:156,161` and the census evidence
logs (which embed the 20-id roster).

Contested/adjacent probes:

```sh
git grep -niE 'AGENTS\.md|SKILL\.md|prompt' $C -- tools | wc -l  # 17: all GIT_TERMINAL_PROMPT
                                                                 # env vars + own-SKILL.md registry refs
git grep -n '\.ufo/prompts' $C -- tools | wc -l                  # 0
git ls-tree --name-only $C:tools | wc -l                         # 24 tools; no verifiers/
```

`tools/mori-dispatch-ledger.py:120-165` (`_payload_identity`) hashes the
`{"context","tasks"}` bytes of a preferred `run`/`taskCall` node in a **mori** wave
dispatch JSON; `PROVINCE.md:134-138` bounds it: "one ledger row per whole-wave task call
binds the committed payload digest to the observed result … Planning, slot acquisition,
retrying and adjudicating dispatch remain **kumitate/operator**-owned."

## Remaining unknowns

None material to the row. Two notes for the census author, not used in the
classification: `README.md:12-13` still calls `SKILL.md` "absent on lanes still in shonen
seed form" (a stale README copy, not a province claim); and the pinned commit is labelled
"round-24" while `PROVINCE.md:234` is the newest appended round-24 section — the lane's
round clock is unrelated to scope.
