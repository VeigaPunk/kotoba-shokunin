Result: HOLDS — the R2 README correction's stated S086/S087/S088 roles are exact against SOURCES.md and the round-57 Gate, and sweep row `r58-r2-readme-plugin-sources` fires red on the old note alone and stays green at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`.

# Scope and target

Attacked at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`:
- The correction sentence `corpus/README.md:160-162`, appended after the round-57 note (`:150-159`) with no intervening blank line:
  > Round 58 correction (round-57 spot-check R2): the plugin entry and `../SKILL.md` § Plugin manifests by client also rest on the correction rows S086–S088 (S086 Codex scaffold contents, correcting S080; S087 opencode plugin discovery, correcting S085; S088 Cursor plugins reference), so the note's source set is S079–S088.
- Registry row `verifiers/check_correction_sweep.py:82-84`: `{"id": "r58-r2-readme-plugin-sources", "file": "corpus/README.md", "stale": r"the plugin half is recorded, not held as a verified claim", "declared": r"S086–S088", "lead": False}`.
- Sandbox for execution: `git clone` of the lane to `/fast/scratch/hyaku/kotoba-r58/ReviewR2Note`, `checkout 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`; no lane files touched except this report; no sandbox commits.

# Role claims vs `corpus/SOURCES.md` and `corpus/lessons/round-57.md`

- **S086 "Codex scaffold contents, correcting S080"** — `SOURCES.md:99` scope "Codex plugin-creator scaffold contents as the page states them"; teaches `supersedes S080 — its teaches clause … is wrong: the scaffold always creates only .codex-plugin/plugin.json`; Gate `lessons/round-57.md:23` labels it "(correction row for S080)". EXACT.
- **S087 "opencode plugin discovery, correcting S085"** — `SOURCES.md:100` scope "opencode plugin discovery folders, project and global"; teaches `supersedes S085 — its anchor names this page only as plugins.mdx, a path that does not resolve beside index.mdx (HTTP 404)`; Gate `lessons/round-57.md:24` labels it "(correction row for S085)". EXACT.
- **S088 "Cursor plugins reference"** — `SOURCES.md:101` source title "Cursor Docs — Plugins reference"; Gate `lessons/round-57.md:25` same URL. The sentence carries no "correcting" clause for S088 — consistent with SOURCES (S088's teaches has no `supersedes` opener) and with `lessons/round-57.md:58` which names only "S086 and S087 are append-only correction rows". EXACT.
- Premise "the plugin entry and `../SKILL.md` § Plugin manifests by client also rest on the correction rows S086–S088" — the entry cites all three: `corpus/knowledge/plugin-manifests-round57.md:2` (source line), `:15` (S087), `:55` (S086 in the Codex ship cell), `:59` (S088), `:60` (S087); `SKILL.md:95` basis names "(S079–S088; S086 and S087 correct S080 and S085)". HOLDS — and SKILL's "S086 and S087 correct S080 and S085" matches the sentence's per-row roles.
- "the note's source set is S079–S088" — matches README row `corpus/README.md:93` "(S079–S088, S028 for Copilot CLI component fields)". HOLDS.

# Sweep row behavior (observed, sandbox)

Script run from the `46b4a70` checkout (the row exists only there and later):

```
timeout 60 python3 -B verifiers/check_correction_sweep.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
correction sweep: 0 stale block(s)        EXIT=0
timeout 60 python3 -B verifiers/check_correction_sweep.py --rev a39942c94027cd3875144284112422d1aa642260
FAIL r58-r2-readme-plugin-sources corpus/README.md:150 stale claim without the declared result
correction sweep: 1 stale block(s)        EXIT=1
timeout 60 python3 -B verifiers/check_correction_sweep.py --rev 3de87aad29e960c95ed35840442f424c48c29729
FAIL r58-r2-readme-plugin-sources corpus/README.md:150 ... EXIT=1
timeout 60 python3 -B verifiers/check_correction_sweep.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
FAIL r58-r2-readme-plugin-sources corpus/README.md:150 ... EXIT=1
timeout 60 python3 -B verifiers/check_correction_sweep.py --rev 8e52f064f21580dff368b50a2a2d304ecccaaea9
correction sweep: 0 stale block(s)        EXIT=0
timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test
0 failure(s) over 25 assertions           EXIT=0
```

- At `a39942c` (erratum 1 — old note present, correction absent) the row is the **only** FAIL: red on the old note alone, exactly as required. Same single-FAIL result at freeze `3de87aa` and base `f56f6e1`.
- Green at the content commit and at lane tip `8e52f064`.
- Same-block mechanics verified: `cat -A` shows no blank line between the stale note and the correction sentence; `blocks()` (`check_correction_sweep.py:98-118`) splits on blank lines/items/headings, so stale (`:150`) and declared (`:161`) share one block. `lead: False` correct — declaration trails the stale text.
- Stale regex is unique in the file (`grep -c` → 1), so it selects exactly the round-57 note block. Declared regex `S086–S088` uses the en dash `e2 80 93` byte-exact in both registry (`sed -n '82,84p' | cat -A` → `S086M-bM-^@M-^SS088`) and README `:161`; the self-test's dedicated fixtures "r58 readme plugin sources red"/"r58 readme plugin sources green" (`check_correction_sweep.py:261-268`) both pass in the 25-assertion run.

# Observations (no defect)

- `lessons/round-57.md:58` technically reserves "append-only correction rows" for S086/S087 (S088 is a new row, not a supersede). The sentence's collective phrase "the correction rows S086–S088" is loose, but its parenthetical drops "correcting" for S088 — the per-row claims are exact, and all three arrived as the spot-check's corrections. Consistent enough; not a finding.
- The landed sentence is shorter than ScribeR2Note's draft (`.ufo/waves/round-58/build/ScribeR2Note.md:7`), and the landed declared regex is `S086–S088` rather than the drafted `Round 58 correction:.*S079–S088`. Both variants put a correct declaration in the stale block; no loss of detection power since the stale regex, not the declared regex, does the selecting.

# Findings

None. R2 holds: roles byte-accurate against the registry and Gate, premise true in the entry and SKILL.md, sweep row red on the old note alone and green at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`.

# Bounds and tooling

- Lane read-only (all `git show`/`grep` read-only); verifier executed only inside the sandbox clone at `46b4a70`; no lane commits, no jj commands, no pushes; every run capped by `timeout` ≤120 s.
- No sources fetched (all checks against committed lane text); no tools installed or updated (python3, git, grep, coreutils already present; pacman untouched).
- Report path: `.ufo/waves/round-58/falsify/ReviewR2Note.md`.

Report: .ufo/waves/round-58/falsify/ReviewR2Note.md
