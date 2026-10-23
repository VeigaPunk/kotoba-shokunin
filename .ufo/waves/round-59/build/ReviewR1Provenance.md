Result: DONE — the R1 repair holds: the lane copy of ReviewBudgetMove.md is byte-identical to the fleet-root original, the provenance note states only verified facts, the report's F1 was acted on in round 58 at 6de8e2eb, and bounds.md carries the output-dir pin.

## 1. Lane copy vs fleet-root copy — byte-exact, verified

- Lane at freeze `4b2125c` has `.ufo/waves/round-58/falsify/ReviewBudgetMove.md` (37,160 B? no — 10,299 B; I did not wc it; see sha below) and `ReviewBudgetMove.provenance.md` (git ls-tree at `4b2125c`, listed).
- `git show 4b2125c:.ufo/waves/round-58/falsify/ReviewBudgetMove.md | sha256sum` → `c288bbd8427b38cda487b6693fe3a3774a674d9dcff944dd7f27fa7d9295cb8d` (exit 0).
- `sha256sum /home/vgpnk/Projects/shokunin/.ufo/waves/round-58/falsify/ReviewBudgetMove.md` → `c288bbd8427b38cda487b6693fe3a3774a674d9dcff944dd7f27fa7d9295cb8d` (same).
- `cmp` lane copy vs fleet copy → exit 0, no output. Identical.
- Fleet-root copy is untracked: `git --git-dir=/home/vgpnk/Projects/shokunin/.git ls-files -- .ufo/waves/round-58/falsify/` → empty, exit 0 (fleet repo is not a git work tree of itself; bound `never any git … command with the fleet root … as cwd` observed — no `-C`/cwd change, `--git-dir` only).
- Fleet-root stat: 10,299 B, mtime 2026-10-23 05:34:09.381723202 -0300 — matches the spot-check's record (10,299 B, mtime 05:34:09-03:00) and the provenance note's record (10,299 B; mtime 2026-10-23 05:34:09 -0300).

## 2. Provenance note — states only verified facts

File `.ufo/waves/round-58/falsify/ReviewBudgetMove.provenance.md` at `4b2125c`:

| Claim | Verified |
|---|---|
| The report was written into the fleet root, not into the lane | fleet-root file exists untracked (above); also spot-check §7 R1 ("wrote its report to the **fleet root** … never reached the lane") |
| "untracked" | `ls-files` empty (above) |
| 10,299 B; mtime 2026-10-23 05:34:09 -0300 | `stat` exact match (above) |
| The round-58 report did not account for it (routed defect R1, `corpus/lessons/round-58-verifier-spotcheck.md` § 7) | `git show 4b2125c:corpus/lessons/round-58-verifier-spotcheck.md` §7:1: "R1 — misrooted, undisclosed seat report" with the same facts; "The report's seat paragraph omits it. The misroot sweep … ran before that write" |
| Round 59 (L1 `KotobaR59`) copied it byte-exact: cmp exit 0; sha256 `c288bbd8…` | independently reproduced (above) |
| The fleet-root copy is left in place: the spot-check names its removal as operator-side | spot-check §7:1: "Removing the fleet-root file is operator-side." Same in plan R1 row ("fleet copy left for the operator, as the spot-check says"). [INFERENCE] the fleet-root file at review time is the same one the spot-check saw, since no fleet-side mutation is observed |
| The content is the seat's own and unedited | not cryptographically provable; supported by (a) byte-identity with the seat-written fleet copy, (b) spot-check R1 naming the seat as the writer, (c) the report is a self-consistent falsify report (header/scope/findings/verdict, lines 1–34). [INFERENCE] for "the seat's own" |

No statement in the note exceeds the evidence. No unverified or speculative statements found.

## 3. F1 acted on in round 58 — yes, at `6de8e2eb`

- `git show 6de8e2eb` (2026-10-23T05:41:15-03:00) touches `corpus/knowledge/claim-census-round12.md` (+4) — commit message names "claim-census notes".
- The appended note is the F1 repair: "Round 58 note (append-only): the row `F:6` anatomy recipe reads `0` from round 58 on because § Skill-file anatomy moved verbatim to `anatomy-and-compression.md` … run the same `awk` over that file to re-derive `9` and `7`."
- I independently re-derived the F1 mechanics: `awk '/^## Skill-file anatomy/,/^## Instruction surfaces/' SKILL.md | grep -c '^|'` → `9` at `3de87aad`, `0` at `46b4a706` — exactly what the report's F1 claims, and the note explains it.
- The spot-check §7 R1 confirms: "The L1 did act on its F1 (the claim-census note at `6de8e2eb`)." Plan R1 row (freeze) also records the fix as done.

## 4. `.ufo/waves/round-59/bounds.md` carries the output-dir pin — yes

- `git show 4b2125c:.ufo/waves/round-59/bounds.md`: "Output directory (round-58 routed R1: seat `ReviewBudgetMove` wrote its report into the FLEET root `/home/vgpnk/Projects/shokunin/.ufo/waves/round-58/falsify/`): your report goes ONLY under /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/<wave>/. A path that begins /home/vgpnk/Projects/shokunin/.ufo/ is the fleet root and is WRONG."
- Carries both the R1 back-reference and the positive pin, with the WRONG-path test, plus the `ls -l` paste requirement.

## Other observations (scope-adjacent)

- The byte-exact copy + provenance note landed in commit `a3e70a3` (round-59 plan draft, 2026-10-23T06:00:07-03:00), the first round-59 commit after the round-58 tip `ed44e0c4` (both `--follow` log and `ls-tree` at the tip confirm the report was absent from the lane at `ed44e0c4`).
- Report's other headline claims (outside this review's scope) were spot-checked with cheap re-derivations and hold: F1 awk recipe numbers (above); move target exists at `46b4a706`; the move block sha256 `038880d0…` matches the spot-check §3. No claim in the report was found to contradict the lane tree.

## Residual risk / gaps

- "The seat's own" authorship of the fleet-root file is [INFERENCE] (no cryptographic authorship record); byte-identity and the spot-check's naming of the seat cover it.
- I cannot verify the fleet-root file is byte-stable over time (the lane copy is a snapshot at `a3e70a3`); at review time both sides are byte-identical.
- No tools installed or updated (git/sha256sum/cmp/awk/grep already present; pacman paused; nothing else needed).

## Checks run (commands, exit codes)

- `git ls-tree -r --name-only 4b2125c -- .ufo/waves/round-58/falsify/ | grep -c ReviewBudgetMove` → 2 (report + provenance), exit 0.
- `git show 4b2125c:.ufo/waves/round-58/falsify/ReviewBudgetMove.md | sha256sum` → `c288bbd8…`, exit 0.
- `sha256sum /home/vgpnk/Projects/shokunin/.ufo/waves/round-58/falsify/ReviewBudgetMove.md` → `c288bbd8…`, exit 0.
- `cmp /tmp/rbm-lane.md <fleet copy>` → exit 0, no output.
- `git --git-dir=/home/vgpnk/Projects/shokunin/.git ls-files -- .ufo/waves/round-58/falsify/` → empty output, exit 0 (untracked).
- `stat -c '%s … %y' <fleet copy>` → `10299 bytes | mtime 2026-10-23 05:34:09.381723202 -0300`.
- `git show 6de8e2eb -- corpus/knowledge/claim-census-round12.md` → the +4 append-only note.
- `git show 3de87aad:SKILL.md | awk '/^## Skill-file anatomy/,/^## Instruction surfaces/' | grep -c '^|'` → 9; same at `46b4a706` → 0.
- `git log --follow -- .ufo/waves/round-58/falsify/ReviewBudgetMove.md` → `a3e70a3` (2026-10-23T06:00:07-03:00); `ls-tree ed44e0c4` → empty (absent at tip).
- `git show 4b2125c:.ufo/waves/round-59/bounds.md` → output-dir pin present.
- `git show 4b2125c:corpus/lessons/round-58-verifier-spotcheck.md` §7 → R1 confirmed.
