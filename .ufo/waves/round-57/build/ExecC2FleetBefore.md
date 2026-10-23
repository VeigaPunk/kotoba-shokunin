Result: DONE — measured the C2 before-state with the current instrument over all 18 lanes that carry a root SKILL.md: 171 FAIL subjects in 10 lanes, of which 105 (61%) come from 14 info-less fences and 105/105 of those are non-command line shapes (0 real commands); the TSV is delivered with full per-row provenance.

# ExecC2FleetBefore — real-input before-state for C2

Round-57 BUILD wave, item ExecC2FleetBefore (executor, axes operability + adjacency).
Cross-lane findings are **reported, never fixed**: no lane file, counter, verifier or
configuration was written or edited. Files written by this seat: this report and
`.ufo/waves/round-57/build/ExecC2FleetBefore.tsv` only.

## Method

- Instrument: sandbox clone `/fast/scratch/hyaku/kotoba-r57/ExecC2FleetBefore` checked out at
  `01312a77e36317feb6e961aba77841ddab1225ca` (the work revision named by the wave).
  `verifiers/verify_skill_checklist.py` sha256
  `629867d19e16a3bd125a11437a624895222c2c602d449c06128ef056e7c56cab`, **byte-identical to the
  live kotoba lane file** (same sha256 measured at
  `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_skill_checklist.py`), so the
  run is the current instrument, not a stale copy.
- Command, once per lane, read-only (`--skill` is the lane's file, `--repo` the lane root):
  `timeout 120 python3 -B <sandbox>/verifiers/verify_skill_checklist.py --skill <lane>/SKILL.md --repo <lane> --check trigger.command_binary_resolves --json`
- Start stamp: `Fri 23 Oct 2026 04:47:11 AM UTC` (`date -u`). Every invocation returned rc 0
  (PASS) or rc 1 (FAIL) — 18 of 18 completed, no timeouts, no rc 2/3.
- Lane heads recorded per lane with `git --no-optional-locks -C <lane> rev-parse HEAD`; each
  measured lane's `SKILL.md` is clean against its HEAD (`git status --porcelain -- SKILL.md`
  empty) **except kotoba-shokunin**, which is `M SKILL.md` (the in-flight build wave, see Limits).
- Population: `/home/vgpnk/Projects/shokunin/*-shokunin` = 21 dirs. Three have no root
  `SKILL.md` and were skipped with no record: `audio-shokunin`, `game-dev-2d-shokunin`,
  `revenger-shokunin` (`ls` → "No such file or directory").
- FAIL subjects were re-derived by importing the same module inside the sandbox
  (`command_subjects` + `safe_resolve` + a replay of `fenced_regions`' state machine that also
  records each fence opener's info string), because the CLI message truncates after four items
  with `… (+N more)`. The re-derivation matches every lane's JSON exactly: total FAIL subjects
  from the message (shown + `+N more`) equals the probe count in 18/18 lanes, and `evaluated`
  equals the probe subject count in 18/18 lanes (0 mismatches).

## Per-lane result (18 measured)

`status` is this single check; `subj`/`seg` are `evaluated`/segments from the run; FAIL is split
by where the subject came from. `fences` = info-less fences / command-eligible fences
(`FENCED_INFO = {'', bash, sh, shell, console}`, verifier:347).

| lane | head (12) | rc | subj | seg | FAIL | info-less | shell-tagged | inline | fences |
|---|---|---|---|---|---|---|---|---|---|
| chousa-shokunin | ee1024fd4921 | 0 PASS | 37 | 18 | 0 | 0 | 0 | 0 | 0/1 |
| game-dev-3d-shokunin | 89dd182b7094 | 1 FAIL | 33 | 22 | 5 | 0 | 0 | 5 | 0/0 |
| kagi-shokunin | 899c50b42634 | 0 PASS | 104 | 64 | 0 | 0 | 0 | 0 | 0/0 |
| kaidoku-shokunin | f2f5977b8266 | 1 FAIL | 38 | 28 | 1 | 0 | 0 | 1 | 0/0 |
| kake-shokunin | b7d821e3a79b | 1 FAIL | 97 | 51 | 3 | 0 | 0 | 3 | 0/3 |
| kama-shokunin | a720399e627b | 0 PASS | 140 | 74 | 0 | 0 | 0 | 0 | 0/0 |
| kasegi-shokunin | 1fafde8f1145 | 1 FAIL | 25 | 18 | 21 | 20 | 0 | 1 | 2/2 |
| kengaku-shokunin | 1f3b0f1ec41e | 0 PASS | 63 | 33 | 0 | 0 | 0 | 0 | 0/0 |
| kotoba-shokunin | 27af04a7ed8c | 0 PASS | 34 | 19 | 0 | 0 | 0 | 0 | 0/0 |
| kotodama-shokunin | 9c82a6eb60b1 | 0 PASS | 34 | 16 | 0 | 0 | 0 | 0 | 0/1 |
| kumitate-shokunin | 3632602c6f68 | 0 PASS | 78 | 40 | 0 | 0 | 0 | 0 | 0/0 |
| lore-shokunin | 380ef3abc7c7 | 0 PASS | 16 | 9 | 0 | 0 | 0 | 0 | 0/0 |
| mado-shokunin | 41cc04c8d593 | 1 FAIL | 237 | 174 | 9 | 0 | 0 | 9 | 0/1 |
| mori-shokunin | f10a320d9056 | 1 FAIL | 106 | 57 | 1 | 0 | 0 | 1 | 0/0 |
| souji-shokunin | 4edb25dfe262 | 1 FAIL | 141 | 73 | 2 | 0 | 0 | 2 | 0/0 |
| tabi-shokunin | e3cf4e0d30bb | 1 FAIL | 281 | 216 | 31 | 0 | 23 | 8 | 0/5 |
| tameshi-shokunin | 9ed6db840dc9 | 1 FAIL | 225 | 140 | 37 | 27 | 4 | 6 | 4/8 |
| tsukuroi-shokunin | 1f521b933875 | 1 FAIL | 1087 | 699 | 61 | 58 | 0 | 3 | 8/10 |

Full 40-character heads are in column 2 of every TSV row.

## Counts per class (the deliverable)

Source of the subject (decided from the fence membership of the subject's line, replaying the
instrument's own container/fence rules):

| source | n | share |
|---|---|---|
| info-less fence (empty info string) | 105 | 61.4% |
| shell-tagged fence | 27 | 15.8% |
| inline span | 39 | 22.8% |
| **total** | **171** | **100%** |

Info-less fence FAILs by line shape (the required taxonomy; applied per line):

| shape | n |
|---|---|
| key: value | 45 |
| other | 27 |
| table | 18 |
| arrow | 15 |
| real command | **0** |
| box/tree | 0 |
| ascii box | 0 |
| **total** | **105** |

`other` = selftest verdict records (`PASS healthy: …`, 17 rows), output banners
(`tsukuroi-census census-v1 — host=… — …`, 3 rows) and `=` formulas (`p_success = …`, 5 rows);
the remaining 2 are `MUTATE: DONE (…)` records, which the classifier excludes from `key: value`
by its verdict-marker rule (`MUTATE` is in the `PASS/FAIL/OK/DONE/SKIP/MUTATE` set). `table` in the
info-less class is the column-aligned, pipe-free hash/status table (18 rows, tameshi), and
`key: value` covers both the tameshi `<field>: <template>` block (9) and the tsukuroi `PLANE …:` /
`TSUKUROI_CENSUS: …` status records.

Info-less FAILs split 95 head subjects / 10 argument subjects. **Not one of the 105 is a real
command**: no head is a binary (`policy`, `authorization`, `p_success`, `id:`, `class:`,
`js-kimi-census`, `PASS`, `PLANE`, `TSUKUROI_CENSUS:`, `tsukuroi-census`, …) and no argument is a
command path. A vocabulary change or a `PATH` change cannot clear any of them.

Shape counts for the other two sources (same classifier, informational):

| source | shapes |
|---|---|
| shell-tagged fence (27) | table 22, real command 5 |
| inline span (39) | other 19, table 15, arrow 4, key: value 1 |

## The 14 info-less fences that produced FAILs

`h/a` = head / argument subjects.

| lane | opener line | failing lines | FAILs | h/a | shapes |
|---|---|---|---|---|---|
| kasegi-shokunin | 38 | 39–47 | 15 | 9/6 | arrow 15 |
| kasegi-shokunin | 827 | 828–832 | 5 | 5/0 | other 5 |
| tameshi-shokunin | 254 | 255–261 | 9 | 9/0 | key: value 9 |
| tameshi-shokunin | 1042 | 1044–1049 | 6 | 6/0 | table 6 |
| tameshi-shokunin | 1171 | 1173–1178 | 6 | 6/0 | table 6 |
| tameshi-shokunin | 1402 | 1404–1409 | 6 | 6/0 | table 6 |
| tsukuroi-shokunin | 262 | 263–264 | 5 | 5/0 | key: value 5 |
| tsukuroi-shokunin | 274 | 275–292 | 18 | 18/0 | other 17, key: value 1 |
| tsukuroi-shokunin | 299 | 300–304 | 6 | 6/0 | key: value 5, other 1 |
| tsukuroi-shokunin | 582 | 583 | 1 | 1/0 | other 1 |
| tsukuroi-shokunin | 610 | 611 | 1 | 1/0 | other 1 |
| tsukuroi-shokunin | 879 | 880–885 | 9 | 8/1 | key: value 8, other 1 |
| tsukuroi-shokunin | 1040 | 1041 | 3 | 2/1 | key: value 3 |
| tsukuroi-shokunin | 1209 | 1210–1216 | 15 | 13/2 | key: value 14, other 1 |

kasegi-shokunin is the extreme case: its only two command-eligible fences are both info-less,
so 20 of its 21 FAIL subjects exist only because an untagged fence is read as shell. tsukuroi's
eight info-less fences yield 58 of its 61 FAIL subjects. All 14 opener lines were re-read
directly (`sed -n '<n>p' <lane>/SKILL.md | cat -A`) and each is a bare fence line (three
backticks, no info string), independent of the replay scanner.

Verbatim instrument detail for two lanes that shows the mechanism (the `|` of an enumeration is a
segment separator, so `DEGRADED` and `1` become "commands"):

```
tsukuroi: 699 segments; line 263: 'TSUKUROI_CENSUS:' (fenced, segment 'TSUKUROI_CENSUS: HEALTHY') does not resolve; line 263: 'DEGRADED' (fenced, segment 'DEGRADED') does not resolve; line 263: 'BLOCKED' (fenced, segment 'BLOCKED (packages=.. systemd=.. drivers=..)') does not resolve; line 264: '1' (fenced, segment '1 DEGRADED') does not resolve … (+57 more)
kasegi: 18 segments; line 39: 'policy' (fenced, segment 'policy read (AR14, passive only)          → evidence/<program>/scope-snapshot.json') does not resolve; …
```

## Shell-tagged fence FAILs (27) — not a C2 property

| class | n | witnesses |
|---|---|---|
| `sh`-tagged fence whose body is captured `sha256sum` **output** (hash, name, line count) | 22 | tabi 815–825 |
| assignment swallows the command word, leaving a flag as the head | 2 | tabi 229 `SURV=$(ps -eo …)` → head `-eo`; tameshi 1767 `W=$(mktemp -d …)` → head `-d` |
| path relative to the fleet root, not the lane root | 2 | tameshi 545/613 `cp -p kumitate-shokunin/scripts/…`, `cp -p kagi-shokunin/corpus/…` |
| `<rev>:<path>` git object spec | 1 | tameshi 1768 `364f1d59…:scripts/round-gate.mjs` |

Tags seen: `sh` 25 rows, `bash` 2 rows. The tag is honest in 5 of 27 rows (real commands); in the
other 22 the fence is tagged `sh` while carrying output.

## Inline-span FAILs (39) — adjudicated

| class | n | note |
|---|---|---|
| `<rev>:<path>` git object spec harvested as a path | 11 | path exists after the rev prefix is stripped (e.g. `HEAD:SKILL.md`, `9011581:.ufo/…`) |
| cwd/prefix-relative path that exists elsewhere in the lane | 7 | e.g. tabi `MANIFEST.txt` ×4 live only inside `corpus/evidence/<group>/`; kake `DIR/manifest.json` |
| work-dir or planned-file artifact named in prose (absent by design) | 4 | tameshi `pristine.mjs`, `mutant-Bx.sh`, `pristine.sh`; tsukuroi `HANDOFF.md` |
| placeholder argument in a usage template | 2 | kake `IN.json`, souji `W.json` |
| dangling reference, no such file anywhere in the lane | 10 | mado `01-filebytes.sh`, `02-hyprctl.sh`, `03-consumers.sh`, `check-getoptions.py`, `corpus/knowledge/arc-closeout.md` ×2; kasegi `ops/rank.mjs`; tabi `corpus/knowledge/training-closeout.md`; tameshi `tools/mado-verify.sh`; tsukuroi `plans/round-1.plan.md` |
| trailing-`)` token dressing (also cwd-relative) | 5 | game-dev-3d 46/47/90 |

The last row is a double cause: `strip_token_dressing` (verifier:1034-1039, `TRAILING_PUNCT =
",;:)]}\"'"`) strips `)` **for the predicate** `path_like_arg` (:1049-1051) but `arg_subjects`
appends the **raw** token as the subject (:1079-1080), so `…hooks.json)` is tested verbatim; and
the `cd corpus/knowledge/unreal-mcp &&` prefix of the same span is dropped (inline spans have no
`cd` tracking, :1157-1192) so even a clean token would resolve from the repo root.

## Cross-lane observations (reported, never fixed)

1. **Info-less fences are shell input by fiat** (`FENCED_INFO` includes `""`, verifier:347). The
   measured cost fleet-wide is 105/171 FAIL subjects (61%) and 0/105 genuine broken commands.
   This is the before-state C2 needs; no fix is proposed here (round-57 forbids sketching one).
2. **`|` inside prose is a segment separator** (`SEGMENT_SPLIT_RE`), so enumeration text yields
   heads such as `DEGRADED`, `BLOCKED`, `1`, `2`, `+` (tsukuroi 263–264).
3. **An assignment whose value starts a command substitution loses the command word**:
   `SURV=$(ps …` and `W=$(mktemp …` yield heads `-eo` and `-d` (tabi:229, tameshi:1767).
4. **Token dressing is applied to the predicate, not to the recorded subject** (see above), and
   `<rev>:<path>` specs are recorded as repo paths — 12 rows across the fleet (11 inline + 1
   shell-tagged).
5. **Inline-span provenance is mislabelled in the message**: `arg_subjects` hardcodes
   `"source": "fenced-arg"` for both call sites, so a markdown-table cell is reported as
   `(fenced-arg, …)`. Witness: game-dev-3d's fresh detail names line 46 (a `|`-table row outside
   any fence) as `fenced-arg`.
6. **Only 1 of 21 lanes carries `verifiers/`** (`ls -d *-shokunin/verifiers` → kotoba only). The
   other 17 measured lanes have no instrument at all; their verdict exists only when kotoba's
   instrument is pointed at them, and their command vocabulary is whatever kotoba's file declares
   (28 heads at `01312a77`).

## Limits

- **kotoba-shokunin is dirty**: `git status --porcelain -- SKILL.md` → `M SKILL.md` (build wave
  in flight), head `27af04a7ed8cee74291fd8237f5c73c43243ce02`. Measured on the working file
  (PASS, 19 segments / 34 subjects) **and** on the sandbox copy at `01312a77` with
  `--repo kotoba-shokunin` — identical verdict and identical numbers, so the in-flight edit does
  not change this check.
- `safe_resolve` consults `shutil.which` (:913), so verdicts depend on the invoking `PATH`
  (round-21 F7). All 18 runs used one session `PATH`; nothing was pinned.
- Shapes are a per-line reading, not a semantic parse: 15 `arrow` rows are one column-aligned
  pipeline table (kasegi 39–47), the 18 info-less `table` rows are aligned hash columns, and the
  45 `key: value` rows are status records. A line carrying two subjects is counted once per
  subject (171 rows over 129 distinct lane/line pairs).
- Not measured: info-less fences in PASS lanes (their path-like tokens either resolve or are
  absent), and the behaviour of the withdrawn info-less-fence counter — C2 is not a claim this
  round.
- Scratch (`/fast/scratch/hyaku/kotoba-r57/ExecC2FleetBefore/run/`) holds the 18 per-lane JSON
  files, `fails.json`, `evidence.json` (opener + fence info + segment per FAIL) and the probe
  scripts `probe_fails.py` / `make_tsv.py`. Scratch is volatile; the TSV below is the durable
  artefact.

## Deliverable

`.ufo/waves/round-57/build/ExecC2FleetBefore.tsv` — 171 rows, sha256
`bfa7f262d80b5a1f6297ffb36351a3ef52f093b1ae444a0b178416b838d8f1ed`, header-free, tab-separated,
columns `lane, head, line, source, shape, subject`; `head` is the full 40-character
`git rev-parse HEAD` of the lane at measurement time; `source` ∈ {`info-less fence`,
`shell-tagged fence`, `inline span`}; `shape` uses the taxonomy documented above; `subject` is the
token the instrument reported (`(fenced-arg, …)` rows carry the argument token, head rows the
command word).

No tool was installed or upgraded (none was needed); no package manager ran.
