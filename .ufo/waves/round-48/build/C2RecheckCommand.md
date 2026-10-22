# C2 recheck commands — runnable-today gate for the frontmatter-rule-authorities entry

Seat: `KotobaR48.C2RecheckCommand` (leaf executor). Date: 2026-10-22.
Scope: Q04 / Q12 of round-48 — write and run the `recheck:` commands the planned entry
`corpus/knowledge/frontmatter-rule-authorities-round48.md` will carry, one per authority, each a
one-line `curl -fsSL <url> | grep -c '<fixed string>'` returning a positive count **today** and
0 if that authority's rule text changed. Read-only on the lane; all work in
`/fast/scratch/hyaku/kotoba-r48-a2/seats/c2-recheck-command/`.

## Findings

- **F1 — Five commands, all green today, one per authority.** Each printed a positive count and
  exited 0 on 2026-10-22T08:15:26Z, on three consecutive runs (counts R1=1 R2=1 R3=1 R4=1 R5=2).
- **F2 — The negative control fails exactly as required.** A wrong string on a live URL prints `0`
  and exits **1** (`grep -c` exits 1 on zero matches), so the gate is not vacuously green: a
  changed rule text turns the count to 0 and the exit to 1. Verified three ways — wrong string on
  a live URL, wrong string on the spec, and a dead (404) URL.
- **F3 — Mutation sensitivity proven, not asserted.** For each source I fetched the bytes, made a
  local copy with only that one rule string changed (e.g. `Must be 1-1024 characters` →
  `Must be 1-2048 characters`), and re-ran the same `grep -c`. All five fell to **0 / exit 1**,
  and the replacement was present in the mutated copy. The commands detect rule-text drift, not
  just source liveness.
- **F4 — R3 and R4 are the same bytes today, by upstream's own doing.** `refs/heads/main` of
  `anthropics/skills` **is** the S012 pin `dbd4588f9e1033efb41dad4bef2f7947c8993d44` (committed
  2026-10-09T18:45:49Z); both fetches give sha256 `67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365`
  (3972 B), `diff` empty (exit 0). Keeping both is still correct — R3 pins the cited commit, R4
  tracks the moving branch and is the one that goes red when upstream lands a change.
- **F5 — R2's pin is the validator's only commit, and its bytes still equal main.**
  `skills-ref/src/skills_ref/validator.py` has exactly one commit in its history
  (`547831f3a23724ba64a9b79bbf59c5e0bc8f2d1a`, 2025-12-18, "Add skills-ref library (#2)"); at
  that pin and at `main` (`69ef37e9424c0a7ea9dd2293b559e43ec8176379`) both give sha256
  `b5ee3d8537c83c959c31c2cb080a5227646ede5aea545f1ac835ed3c4645f6c5`, `diff` empty (exit 0).
  `MAX_DESCRIPTION_LENGTH = 1024` is the only place that file states the 1024 limit, and the
  sibling scout's finding that it holds **no** angle-bracket predicate is what makes the R2 count
  meaningful for this entry.
- **F6 — Caution: the spec's `.md` and HTML forms count differently.**
  `https://agentskills.io/specification.md` (publisher's markdown rendering, `Content-Type:
  text/markdown`) yields **1** for the description-length rule; the HTML page
  `https://agentskills.io/specification` yields **2** for the same string — once in the rendered
  list, once in the page's embedded payload. The item asks for the spec *markdown*, so R1 uses
  the `.md` form; do not swap in the HTML URL expecting the same number.
- **F7 — `grep -c` counts matching lines, not occurrences.** R5's `Cannot contain XML tags` sits
  on two lines of the Anthropic page (the `name` and `description` field lists), so R5
  legitimately counts 2. The other four strings occur on exactly one line each.
- **F8 — Lane's own lexical checker re-run green (supplementary).** `python3 -B
  verifiers/verify_skill_checklist.py --self-test` from the lane root printed `0 failure(s) over
  1845 assertions`, exit **0**.

## The five commands, verbatim

Run from anywhere; no credentials, no local checkout needed. All five are single lines.

```
# R1 — open spec (S001), the description field rule
curl -fsSL https://agentskills.io/specification.md | grep -c 'Must be 1-1024 characters'
# R2 — reference validator skills-ref, pinned commit (547831f3 = its only commit)
curl -fsSL https://raw.githubusercontent.com/agentskills/agentskills/547831f3a23724ba64a9b79bbf59c5e0bc8f2d1a/skills-ref/src/skills_ref/validator.py | grep -c 'MAX_DESCRIPTION_LENGTH = 1024'
# R3 — Anthropic packager quick_validate.py at the pinned commit dbd4588 (S012)
curl -fsSL https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py | grep -c 'Description cannot contain angle brackets (< or >)'
# R4 — the same file at current main (moving branch; the drift detector)
curl -fsSL https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/scripts/quick_validate.py | grep -c 'Description cannot contain angle brackets (< or >)'
# R5 — Anthropic best practices (S003), the XML-tag rule
curl -fsSL https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md | grep -c 'Cannot contain XML tags'
```

Run log, 2026-10-22T08:15:26Z (URLs abbreviated; the script is `final2.sh` in the seat scratch):

```
[R1] .../agentskills.io/specification.md | grep -c 'Must be 1-1024 characters'   stdout: 1  exit: 0
[R2] .../agentskills/547831f3.../validator.py | grep -c 'MAX_DESCRIPTION_LENGTH = 1024'   stdout: 1  exit: 0
[R3] .../anthropics/skills/dbd4588f.../quick_validate.py | grep -c 'Description cannot contain angle brackets (< or >)'   stdout: 1  exit: 0
[R4] .../anthropics/skills/main/.../quick_validate.py | grep -c 'Description cannot contain angle brackets (< or >)'   stdout: 1  exit: 0
[R5] .../agent-skills/best-practices.md | grep -c 'Cannot contain XML tags'   stdout: 2  exit: 0
```

### The required failure (wrong string → 0, exit 1)

```
[NEG-A] curl -fsSL https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py | grep -c 'Description must not contain angle brackets'
  stdout: 0   exit: 1
```

The string differs from the live one only by `must not` vs `cannot`. Two more failure modes
confirmed: `'Must be 1-2048 characters'` on the spec → `0`, exit **1**; a dead URL
(`…/quick_validate-NOPE.py`) → curl prints `curl: (22) The requested URL returned error: 404`,
the pipeline prints `0`, exit **1** (with `set -o pipefail` the exit becomes curl's 22 — still
non-zero, so the gate is red either way).

## Ready-to-paste `recheck:` line for the planned entry

For `corpus/knowledge/frontmatter-rule-authorities-round48.md` frontmatter, in the lane's shape
(`recheck: <command> — expect N`):

```
recheck: five source recheck commands — `curl -fsSL https://agentskills.io/specification.md | grep -c 'Must be 1-1024 characters'` (expect 1); `curl -fsSL https://raw.githubusercontent.com/agentskills/agentskills/547831f3a23724ba64a9b79bbf59c5e0bc8f2d1a/skills-ref/src/skills_ref/validator.py | grep -c 'MAX_DESCRIPTION_LENGTH = 1024'` (expect 1); `curl -fsSL https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py | grep -c 'Description cannot contain angle brackets (< or >)'` (expect 1); `curl -fsSL https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/scripts/quick_validate.py | grep -c 'Description cannot contain angle brackets (< or >)'` (expect 1); `curl -fsSL https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md | grep -c 'Cannot contain XML tags'` (expect 2) — each run 2026-10-22 (1, 1, 1, 1, 2); a wrong string returns 0 and exits 1
```

Q12 also requires `source:` naming an S### row plus URL/anchor and `verified-at:`. The five
authorities map to S001 (open spec), the new `skills-ref` row, S012 (Anthropic packager), S012
again at main, and S003 (Anthropic best practices). The row id for `skills-ref` is the entry
author's to set; I did not edit `corpus/`.

## Evidence

Access time for all five fetches: **2026-10-22T08:12:41Z** (second pass 08:15:26Z), HTTP 200 on
all five. sha256: R1 `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` (7608 B);
R2 `b5ee3d8537c83c959c31c2cb080a5227646ede5aea545f1ac835ed3c4645f6c5` (5154 B); R3 and R4 both
`67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365` (3972 B); R5
`f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960` (42169 B).

Pin resolution (GitHub API, exit 0 each): `agentskills/agentskills` commits touching
`skills-ref/src/skills_ref/validator.py` → one entry, `547831f3a23724ba64a9b79bbf59c5e0bc8f2d1a`
(2025-12-18T14:39:21Z); `commits/main` → `69ef37e9424c0a7ea9dd2293b559e43ec8176379`
(2026-08-09T20:36:04Z). `anthropics/skills` `commits/main` →
`dbd4588f9e1033efb41dad4bef2f7947c8993d44` (2026-10-09T18:45:49Z), identical to the S012 pin;
commits touching the script → newest `1ed29a03dc85` (2026-02-06T21:19:32Z). `diff` R2-pinned vs
R2-main: empty, exit 0. `diff` R3 vs R4: empty, exit 0. Mutation table (local copies in the seat
scratch; original count → mutated count): R1 spec 1→0 exit 1; R2 validator 1→0 exit 1;
R3/R4 quick_validate 1→0 exit 1; R5 best practices 2→0 exit 1. Reproducibility: three
consecutive full runs → identical counts (1,1,1,1,2) and exits (0,0,0,0,0) every time.

Tooling: `curl 8.23.0`, GNU grep 3.12 at `/usr/bin/grep` (the PATH `grep` is pi-uu-grep 0.2.0;
both give the same counts — `/usr/bin/grep` checked separately: R1=1 exit 0, R5=2 exit 0),
Python 3.14.8. **No packages installed or upgraded**; no pacman/npm/cargo action; no host
service restarted.

## Risks / limits

1. The commands read **live** URLs; they are recheck commands, not reproducible archive reads.
   The counts pin today's bytes, not a frozen receipt. A lane-local copy under `.ufo/` would fix
   bytes but would then never detect drift — the live form is correct for a freshness gate.
2. R1's count is tied to the publisher's `.md` rendering. If agentskills.io drops or rewrites the
   `.md` endpoint, R1 goes red for a reason unrelated to the rule — a true signal (the cited
   surface changed) that the entry should say so about.
3. R2's string is a constant assignment, not prose: it detects edits to the 1024 limit but not a
   wholesale rewrite of the validator under a new constant name. A future recheck may need a
   second string for the description rule; the file has one commit of history, so risk is low.
4. `grep -c` counts lines. An upstream reflow that keeps the string but splits it across lines
   would return 0 — the intended fail-closed direction, but a red R5 of 0 needs a human read, not
   an automatic "rule removed" verdict.
5. The five commands do not cover the Codex source (S013) or the lane's own lexical checker as
   *source* rechecks — outside the item's list. The lane self-test is recorded in F8.

## Files changed

- This report only: `.ufo/waves/round-48/build/C2RecheckCommand.md`. No other lane file was
  created, edited or deleted; no git/jj write command was run in the lane, the fleet repo or any
  sibling lane. Scratch artifacts live in
  `/fast/scratch/hyaku/kotoba-r48-a2/seats/c2-recheck-command/`.
