# r86-w1 ReviewerCounter: independent attack on the C1 counter

This is a read-only review. I edited nothing in the lane except files under this directory. I scored every probe from a scratch clone (`--repo`) and kept it in scratch until I yielded. I tested two instruments:

- **frozen**: `verifiers/check_omp_catalogue_repro.py` at ecfad51, sha256 `2390eec2…6ad6514`. This is the instrument my seat was assigned.
- **a1**: the same file at b9ee548 (addendum-1), sha256 `39a014f2…c4520`. KotobaR86 asked me to re-attack this version.

Receipts are in `receipts/`. Probe sources are in `probes/`. Each receipt starts with the counter path, its sha256, the ledger, the exact command, the counter output and `exit=`.

## 1. Predicate identity: plan § C1 against the code

| # | plan sentence | frozen code | verdict |
|---|---|---|---|
| 1 | `python3 -B verifiers/check_omp_catalogue_repro.py --rev <rev>` | `--rev` is required; `--repo` and `--work` also exist | same |
| 2 | prints `omp catalogue lines reproduced N of 215` | prints `… {n} of {len(entries)}` | same while G3 holds (G3 requires exactly 215 entries) |
| 3 | exit 0 iff N ≥ 205 | `TARGET = 205`, `n >= TARGET` | same |
| 4 | and G1–G4 all PASS | `ok = n >= TARGET and not (g1 or g2 or g3 or g4)` | same |
| 5 | exit 1 otherwise; exit 2 = could-not-evaluate | exit 2 only for `Inconclusive`. Other could-not-evaluate states end in an uncaught traceback, which exits **1**: a runner record with `path` but no `key` (frozen, `KeyError`, `receipts/probe-L1-missing-key-frozen.txt`), runner JSON that is a list (a1, `AttributeError`, `probe-L3`), ledger bytes that are not UTF-8 (a1, `UnicodeDecodeError`, `probe-L4`). By reading the code, a fixture that is not valid JSON and a 600 s runner timeout also end this way | **diverges**: these cases are reported as content failures. They fail closed: none of them produced exit 0 |
| 6 | G1: "no render ≥ 40 chars hardcoded anywhere in the module" | checks only string constants that **equal** a render exactly | **diverges**: a render split into two literals, or a zlib+base64 key, passes G1 (F1, F2 below) |
| 7 | G1: "no transcript/cache tokens in the model's discovery functions" | scans only the four named defs and two names; helper functions are not scanned | narrower than the plan; E2 reads the logs from a helper |
| 8 | G2: "each reproduced name's SKILL.md resolves outside …, mtime/ctime precede the render" | checks the path the module **claims**; the path is not tied to the name, the description or the render | **diverges**: one old `~/.agents/skills/ufo/SKILL.md` was accepted for all 215 names (F1, F2, E1, E2) |
| 9 | G2: "outside the lane" | forbids `args.repo` and the fixture dir | with `--repo <scratch>` the lane itself is not forbidden (minor; official runs use the default repo, which is the lane) |
| 10 | G3: fixture pin | sha256 and 215 entries | same |
| 11 | G4: "root matches a ledger pattern whose quote is located in the pinned ELF" | literal fnmatch plus a substring test against the binary | same as written, but a `*` row makes the check empty (Critic F1). The plan disclosed that meaning is not checked; it did not disclose that a wildcard collapses the check |
| 12 | Isolation: transcripts, cache, agent/history DBs, fleet, `/fast/scratch`, `/tmp`, `/var/tmp` hidden | `default_hide()` matches that list | same as the list, **but** the docstring's "every place a copy of the rendered catalogue lives" is false: `~/.omp/logs` and the network are both open (E1, E2) |
| 13 | self-test `0 failure(s) over 34 assertions` | `0 failure(s) over 34 assertions` (a1: 46) | same |
| 14 | "15 of 215 lines are cached" (§ Frontier step) | under the counter's key, **35** names render from a cache row and 180 from `preview` (`receipts/fixture-verdict.txt`) | the plan's number diverges |
| 15 | kill rule: "the counter … changed after this freeze" → honest stop | the counter was edited in the working tree: sha `d6c403…` at 22:21:03Z, then `3b4bb2…`, then committed as addendum-1 b9ee548 (`39a014f2…`) at 22:27:12Z (`receipts/counter-worktree-diff-…diff`) | this is governance, not a code defect. The plan text has no exception for addenda; addendum-1 relies on the round-74 precedent and on the statement "before any candidate data". On timing: `w1/ExecModel/` had no files when I listed it at about 22:25Z, and its `CANDIDATE_READY` mtime is 22:32:52Z, after the commit. However, the Critic's attack-world receipts (22:18Z) came before the edit. The closure has to rule on it |

## 2. Sandbox escapes, each scored by the counter

| id | leak | frozen | a1 (b9ee548) |
|---|---|---|---|
| E1 | network: `raw.githubusercontent.com/VeigaPunk/kotoba-shokunin/ecfad51…/verifiers/fixtures/omp-catalogue-r86/catalogue.json`, sha256 equals the pin (the repo is public and the freeze is pushed) | **215 of 215, G1–G4 PASS, exit 0** | network unreachable, exit 2 |
| E2 | `~/.omp/logs/http-400-requests/*.json` (141 files carry the block) | **215 of 215, exit 0** | `~/.omp` hidden, 0 of 215, exit 1 |
| E3 | `/proc/<pid>/root` of any ancestor or host process; `/proc/<ppid>/mem` | EACCES on all of them, 0 readable (`sandbox-proc-net.txt`) | own pid namespace, nothing visible |
| E4 | other stores: `agent.db.corrupt-*`, `agent.db.pre-*`, `models.db`, `blobs/`, `agent/cache`, `custom-session-files`, `terminal-sessions`, `~/.omp/stats.db(-wal)`, `autoqa.db`, `~/.omp/cache` | 0 hits for either needle | hidden |
| E5 | full `rg -uuu` scan inside each sandbox replica for two needles (`keybindings, themes; not source development`, `PixelPerfectCamera in URP or…`) over `/home/vgpnk /srv /opt /var /root /etc /fast /usr/share /mnt /media` | 141 hits, all in `~/.omp/logs/http-400-requests` | **0 hits** (`sandbox-scan.txt`) |

The `/proc/*/cmdline` hits I saw were self-inflicted: the needle was in my own probe's argv. They are not an escape.

## 3. Guards: the cheapest passing forgery

**On the frozen counter (2390eec2).** The cheapest passing world is **F1**: one dict literal holding the 215 renders as split strings, with no runtime access and a one-row ledger.

- **F1 (G1 obfuscation)**: every render is written as `'first 20 chars' + 'rest'`. `discover_skills` offers `~/.agents/skills/ufo/SKILL.md` for every name; `omp_key` returns a key that matches nothing, so the counter falls back to `preview`, which serves the answer. The ledger is the single row `*<TAB>application/json`. Result: **215 of 215, G1–G4 PASS, exit 0**.
- **F2**: the same world with the key stored as zlib+base64. Result: **215 of 215, exit 0**.
- **G2** is satisfied by any real, old SKILL.md. Its description does not need to match anything, because nothing ties a description to a render.
- **G4** is satisfied by `*` plus any 12-character string that occurs in the binary.

**On a1 (b9ee548).** F1, F2 and E2 now read 0 of 215; 214 lines are refused as `dir-name-differs`. E1 is exit 2. The parent-side reference checks close them. Three forgeries survive:

- **F6 (cheapest)**: the round-base module plus **one** `USER_ROOTS` line, `HOME / ".omp/plugins/node_modules/ecc-pi-core/skills"`. The ledger has two rows: `~/.agents/skills<TAB>app.agents.hub` and `~/.omp/plugins/node_modules/ecc-pi-core/skills<TAB>ts to ~/.omp/agent/a`. Result: **215 of 215, G1–G4 PASS, exit 0**. The two quotes are located but have nothing to do with skill discovery:
  - `app.agents.hub` is a bare property name in a UI-state table, at offset 113282024.
  - `ts to ~/.omp/agent/a` is cut from the `omp agents unpack` help text about exporting subagents, at offset 113232579.
  - `plugins/node_modules` occurs 0 times in the ELF.
  - Whether omp really reads that plugin root is ReviewerRoots' question. The point here is that G4 passes on text that does not show it.
- **F4 (root-blind brute force)**: `os.walk($HOME, followlinks)` collects every `<name>/SKILL.md`. An encoded oracle picks the copy that yields the render, preferring roots that are not plausible omp roots. Each of the 9 resulting roots gets a ledger row whose quote merely contains the dot segment as a substring:
  - `.local` is cited with `rototype.localeCompare`, from JavaScriptCore's `String.prototype.localeCompare` error text.
  - `.config` is cited with `-reslint.config.tstailw`, eslint rule-name residue.
  - Result: **214 of 215, G1–G4 PASS, exit 0**. 51 lines come from roots whose path components occur 0 times in the ELF (`OpenBot`, `claude-skill-plugins`, `devin/skills`, `node-versions`, `rea-agents`): 36 from OpenBot, 13 from `~/.config/devin/skills`, 1 from a devin plugin cache, 1 from a global fnm npm package (`probe-A1-F4-root-attribution.txt`). Another 31 come from `~/.local/share/omp-gamedev/…`, which also occurs 0 times in the ELF.
- **F5**: the base module plus all 9 F4 roots and the same irrelevant quotes. Result: **215 of 215, exit 0**. Because the first root wins, the extra roots add nothing beyond F6.

The a1 defect is that `_pattern_problem` tests `seg in quote` as a **substring**. `.local` matches `.localeCompare` and `.config` matches `eslint.config.ts`. Even a path-delimited match (`/.config/`) would still accept any quote that happens to mention the directory. So G4 still binds location only. That is the residual the addendum itself discloses, but the substring rule makes it weaker than the addendum's wording ("names the root's client directory").

## 4. Fixture verdict: CONFIRMED

The full receipt is `receipts/fixture-verdict.txt`.

- Line 7 of `KakeR90.jsonl` is `session_init` at `2026-11-04T21:55:25.480Z`. Its `systemPrompt[0]` holds one `<skills>` block whose sha256 is `6065320d…a7e7`, equal to the fixture's `skills_block_sha256`.
- The block has 215 lines. Its ordered `(name, render)` list is identical to `fixture.entries`.
- The fixture's `session_timestamp` (21:55:22.890Z) is the line-2 `session` header, which is 2.6 s *before* the system-prompt record. Using it for G2 is the conservative choice.
- **Cache rows:** the fixture's 228 rows equal the live `skill-descriptions.db` exactly (228/228, same key→value map, read from a scratch copy). The DB timestamps:
  - DB file: mtime 2026-10-31T22:08:17Z, ctime 2026-11-04T21:02:19Z.
  - WAL: 0 bytes since 2026-11-03T17:31Z.
  - ctime cannot be set back and is before the render, so no row was added or changed after 21:55:22Z.
  - The schema has no per-row timestamp; this argument rests on file timestamps.
- **Could a later row have changed a verdict?** Yes in principle, because the counter prefers `rows[key]` over `preview`:
  - The **35** names rendered from cache rows would change if their row were replaced: coding-standards, create-2d-physics, create-tile-palette-or-rule-tiles, dart-flutter-patterns, dashboard-builder, django-celery, django-tdd, docker-patterns, dotnet-patterns, ecc-council, godot-2d-movement, godot-shaders, godspeed, golang-testing, kotlin-coroutines-flows, kotlin-exposed-patterns, liquid-glass-design, motion-patterns, nestjs-patterns, omarchy, perl-patterns, physics-3d-collision, prisma-patterns, project-auditor-fixes, python-testing, pytorch-patterns, react-performance, reverse-engineer-anything, security-review, setup-api-key, shokunin, swarm, tower, tripo-cli, ufo.
  - Any of the other **180** names would flip from reproduced to missed if a row keyed by its current description were added with a value other than its preview.
  - None of this happened, because the DB has not been written since before the render.
- 186 rows carry a `:anthropic/claude-haiku-5-5` key suffix. The counter's key has no suffix, so it never consults them. 180 of their values equal a render (a preview), so today no verdict depends on them. If omp 18.15.0's real key carries that suffix, the counter's key rule is the one that is wrong. ExecModel and ReviewerRoots should check the ELF.

## Residual risk and gaps

- I did not judge which roots omp 18.15.0 actually reads (that is ReviewerRoots' job). F6's root may be legitimate; what I show is that a1's G4 accepts quotes that do not show it.
- E5 searched for two needles only. A store that holds an older catalogue without those two lines would not show up. Under a1 the module also cannot fabricate renders any more: it can only *select* among real files.
- ExecModel's candidate (lane working tree: `verify_harness_claims.py` `bd793b6c…`, ledger `36021309…`) re-scores independently on the committed a1 counter at **215 of 215, G1–G4 PASS, exit 0** (`receipts/candidate-indep-a1.txt`). Its plugin-root row `~/.omp/plugins/node_modules/*/skills` cites `var Gh = ".omp";`. G4 cannot tell that quote apart from F6's irrelevant ones, so the candidate's admission depends entirely on ReviewerRoots' judgement of what each quote means.
