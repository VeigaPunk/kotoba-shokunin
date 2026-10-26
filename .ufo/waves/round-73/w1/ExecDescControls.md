# ExecDescControls — round-73 wave 1 (C2 replacement: own description)

## Verdict

All seven overlay worlds are built, committed inside a throwaway `--shared` clone only, and
measured. **None of the six shortcut worlds (1–6) reads 3 of 3; the honest world (7) reads
`own-description rules held 3 of 3`, exit 0.** Readings for 1–6 are 2, 2, 2, 1, 2, 2 — every one
below the kill line, so on this pinned counter version these six shortcuts are all refused. The
committed do-nothing control is reproduced independently: base `072048f` reads `1 of 3`, exit 1
(R1 150 chars, R2 no quoted trigger, R3 pass). Two counter draft versions were exercised and
produced byte-identical rule lines for all seven worlds.

Deliverables: `.ufo/waves/round-73/w1/build/ExecDescControls/` — one directory per world with a
full `SKILL.md` overlay (body byte-identical to base; only the frontmatter `description` replaced)
and a README carrying the folded description, its length, replay commands and observed gate
output. Index: `build/ExecDescControls/README.md`.

## Matrix (all measured this wave)

Counter measured: `build/ExecDescCounter/check_own_description.py`, sha256
`58f65a3713925b164e56f2e54896331bac623197e957191a161240fd715627e9` (unchanged before base run,
before the seven-world pass, and after it). Earlier draft `d063168e…` gave byte-identical output.

| # | world | desc | 1st sent. | R1 | R2 | R3 | counter | census exit / last line | checklist exit / first FAIL |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `w1-no-quoted-trigger` | 967 | 98 (99 w/ `.`) | pass | **fail** | pass | 1, 2 of 3 | 0 / `skill description length 967 of 1024` | 0 / none |
| 2 | `w2-first-sentence-under-40` | 891 | 22 (23) | **fail** | pass | pass | 1, 2 of 3 | 0 / `… length 891 of 1024` | 0 / none |
| 3 | `w3-quote-not-in-triggers` | 958 | 89 (90) | pass | **fail** | pass | 1, 2 of 3 | 0 / `… length 958 of 1024` | 0 / none |
| 4 | `w4-cut-to-99-drop-triggers-siblings` | 76 | 76 | pass | **fail** | **fail** | 1, 1 of 3 | 1 / `… length 76 of 1024` | 1 / `trigger.literal_trigger_string` |
| 5 | `w5-over-1024` | 1130 | 87 (88) | pass | pass | **fail** | 1, 2 of 3 | 1 / `… length 1130 of 1024` | 0 / none |
| 6 | `w6-midphrase-period` | 1018 | 60 (61) | pass | **fail** | pass | 1, 2 of 3 | 0 / `… length 1018 of 1024` | 0 / none |
| 7 | `w7-honest-rewrite` | 956 | 87 (88) | pass | pass | pass | **0, 3 of 3** | 0 / `… length 956 of 1024` | 0 / none |

Census command: `python3 -B verifiers/check_sibling_census.py
corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md`
(lane root of the fleet-shaped sandbox). Checklist: `python3 -B verifiers/verify_skill_checklist.py`.
Counter: `python3 -B <build>/ExecDescCounter/check_own_description.py --repo <sandbox-clone> --rev <overlay-commit>`.

Overlay identities (file sha256, description sha256), all round-tripped through
`check_sibling_census.description_of`:

| world | file sha256 (12) | desc sha256 (12) | frontmatter lines |
|---|---|---|---|
| w1 | `1e98c28078ab` | `f3da022b0e28` | 19 |
| w2 | `2777e75fbb0c` | `7c532a8964a0` | 19 |
| w3 | `1101c95df2fe` | `79391a5e4196` | 19 |
| w4 | `258de185c266` | `c1df529faf30` | 5 |
| w5 | `a0cf83984da8` | `e7956ce1828e` | 19 |
| w6 | `900931ef8f4b` | `b5f665133b32` | 19 |
| w7 | `1b8507f72d8b` | `65b9fee4d851` | 19 |

## How it was built and measured

Sandbox (fleet-shaped; `--shared` clone; every git write inside it):

```sh
P=$(mktemp -d /tmp/k73fleet-ExecDescControls.XXXX)
for e in /home/vgpnk/Projects/shokunin/* /home/vgpnk/Projects/shokunin/.[!.]*; do
  b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$b"; done
git clone --shared -q --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin "$P/kotoba-shokunin"
git -C "$P/kotoba-shokunin" checkout -q 072048fa8e8a52c707d25f7079772fa317244eb7
```

Per world: `git checkout -q -B k73w1/<world> 072048f`, copy the overlay `SKILL.md`, commit, run
both gates, then `git diff --numstat 072048f <rev> -- SKILL.md`. Worlds 1–3, 5–7 give
`15 15 SKILL.md` (net 0 inside the frontmatter); world 4 gives `1 15` (deliberately cut).

Independent pre-check: I re-implemented R1/R2/R3 over `description_of(<overlay>)` before running
the counter and predicted 2/2/2/1/2/2/3; the counter printed exactly those numbers, so the two
readings agree.

## Findings

**F1 — the six shortcuts are refused, the honest world is admitted (the claim's own control).**
Counter, honest world:

```
$ python3 -B .../check_own_description.py --repo <sandbox> --rev ac04bc60…
first sentence 87 characters: Prompt & skill craft — audits a "skill file" for prompt triggering and decision density
R1 pass: first sentence 87 characters is inside 40-99
R2 pass: whole words skill+prompt yes; quoted trigger "skill file" (in the Triggers list)
R3 pass: description 956 <= 1024; verifiers/check_sibling_census.py exit 0
frontmatter lines 19->19 (inserted 15, deleted 15 inside the frontmatter)
own-description rules held 3 of 3
```
exit 0. World 4 (census arm):

```
R3 fail: description 76 <= 1024; verifiers/check_sibling_census.py exit 1: FAIL skill description
does not name the non-none census lane chousa | … kagi | … kake
own-description rules held 1 of 3
```
World 5 (ceiling arm, same first sentence as world 7 plus padding):
```
R3 fail: description 1130 > 1024; verifiers/check_sibling_census.py exit 1: FAIL skill description
length 1130 is outside 1-1024 characters (S018: the description field must be 1-1024 characters)
```

**F2 — the existing gates do not cover R1/R2 at all; the counter is not redundant with them.**
Worlds 1, 2, 3 and 6 pass both `check_sibling_census.py` (exit 0, `skill description names 9 of 9
non-none lanes`) and `verify_skill_checklist.py` (exit 0) while the counter fails them. World 5
fails the census on length but passes the checklist: `verify_skill_checklist.py`'s frontmatter
check only parses and counts, it does not enforce 1,024 characters (`PASS
trigger.frontmatter_parses: … description 1130 chars`). So C2's counter adds measurement the lane
did not have; the two older gates cannot substitute for it.

**F3 — the counter draft has no stable identity inside the wave; results are pinned to a hash.**
Four hashes in ~90 s: `67ce5b8b…`, `8f6963…`, `4f565e2c…`, `d063168e…`, `58f65a37…`. One of them
failed at import:

```
$ python3 -B .../check_own_description.py --rev 072048f…
  File ".../check_own_description.py", line 72, in _lane_root
    if (direct / SKILL).is_file():
NameError: name 'SKILL' is not defined
```
(caught mid-edit; hash at that moment `67ce5b8b…`). The two versions I pinned,
`d063168e…` and `58f65a37…`, agree byte-for-byte on all seven worlds
(`diff <(grep -v '^own-description rev' a) <(grep -v '^own-description rev' b)` empty, each); an
earlier unpinned build at ~21:03 produced the same N values but was not compared byte-wise. The L1
must re-run the seven worlds against the integrated counter; every number here belongs to
`58f65a37…` only.

**F4 — sandbox shaping must include hidden fleet entries.** My first sandbox looped over
`/home/vgpnk/Projects/shokunin/*` only; `../.ufo/...` citations then dangled and the checklist
exited 1 for reasons unrelated to the description:

```
FAIL trigger.citation_resolves: evaluated 187 — line 558: '../.ufo/reports/round-7/kotoba.md' does not resolve from …
FAIL governance.citation_resolves: evaluated 1283 — … 17 more) …
```
After adding `/home/vgpnk/Projects/shokunin/.[!.]*` the same base tree reads `PASS
trigger.citation_resolves: evaluated 187` and `PASS governance.citation_resolves: evaluated 1280`,
exit 0 — which also reproduces the plan's "checklist by hand exits 0 at base". This is the same
class of hand-run/sandbox divergence as M127 and is recorded in every world README's replay block:
`build_sandbox` uses `fleet.iterdir()` (hidden included); a shell `/*` loop is not equivalent.

**F5 — R1 is off by one between the plan's prose and the counter, harmlessly.** The addendum calls
the base first sentence 151 characters (period included); the counter measures the text before
the separating `.` and prints `first sentence 150 characters`. World 1 is therefore 98 by the
counter and 99 with its period. Both readings stay inside 40–99 for every world that must pass R1,
so no world's reading changes side.

**F6 — world 6 is the pre-registered hollow pass on R1 and it prints itself as such.** The counter
reports `first sentence 60 characters: Prompt & skill craft — audits, writes, and rewrites
SKILL.md` while the old 151-character sentence continues (`AGENTS.md / dispatch prompts / system
prompts for …`). R1 is satisfied by a fragment; R2 still refuses it. The addendum assigns the
hollowness judgement to the non-author reviewer — flagged here, not claimed as clean.

## Risks / limits

- The counter is a wave-1 draft under `build/ExecDescCounter/` and was still being rewritten when
  measured; a later hash could change a rule line. Re-run required at integration.
- R2 counts double-quoted spans only (the counter's `QUOTED` regex), which matches the predicate's
  wording; single-quoted/backticked triggers would not count, so a future author rewriting the
  description with backticks would fail R2 by wording, not intent.
- My own predicate harness and the counter share `description_of` (the pinned census reader), so
  they are not independent on the *parsing* half of R2; they are independent on rule evaluation.
- Overlay commit shas quoted in the per-world READMEs exist only in a throwaway clone under `/tmp`
  and are not lane objects; the overlay file sha256 is the stable identity.
- No lane file was modified: `git status --porcelain` in the lane shows only the untracked
  `.ufo/waves/round-73/w1*` paths owned by the L1. No tool was installed. Scratch directories
  (`/tmp/k73w1-ExecDescControls.*`, `/tmp/k73fleet-ExecDescControls.*`) were removed before return.
