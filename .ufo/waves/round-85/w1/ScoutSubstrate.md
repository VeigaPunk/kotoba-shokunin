# ScoutSubstrate — round-85 C2 host substrate recon (report)

Seat: ScoutSubstrate (scout, leaf — no subagent dispatch). Date: 2026-11-04. Host: linux x86_64.
Scope: recon the host substrate that C2 re-pins. Read-only: `verifiers/` and `SKILL.md` untouched.
Full evidence file: `.ufo/waves/round-85/w1/ScoutSubstrate/recon.txt`.

## Bottom line

C2's substrate on this host is `/home/vgpnk/.local/bin/omp` — **the ELF itself**, with **no wrapper
hop**, and `omp.real` **does not exist anywhere** on this host. The pin triple C2 must record:

| pin key | value |
|---|---|
| omp path | `/home/vgpnk/.local/bin/omp` |
| `omp_binary_sha256` | `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f` |
| `omp_binary_mtime` | `2026-11-01T17:11:07.281808804-03:00` (ns-exact, 9 digits, `-03:00`) |
| version / bytes | `omp/18.15.0` / 276,785,328 |
| `opencode_binary_sha256` | `ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7` — **UNCHANGED** |

**IDs that would change: NONE.** All 42 baseline ids, their literals, kinds and verdicts hold; all
3 ledgered-gone opencode classes are still gone; the opencode side of the ledger matches the host
byte-for-byte.

## The five requested items (condensed; full transcripts in recon.txt)

**1. The binary.**
`file` → ELF 64-bit LSB executable, x86-64, dynamically linked, BuildID `588d7307…`, not stripped.
`ls -l` → 276,785,328 B, Nov 1 17:11. `--version` → `omp/18.15.0`. `sha256sum` →
`6737ee24…b7b0f`. `stat -c '%y'` → `2026-11-01 17:11:07.281808804 -0300`. ns-exact ISO (two
independent derivations — `stat %y` reformatted and `os.stat().st_mtime_ns` reformatted — both
agree): **`2026-11-01T17:11:07.281808804-03:00`** (epoch ns `1793563867281808804`).
Note: `stat -c '%Y-%m-%dT%H:%M:%S.%N%:z'` is **not** a valid GNU stat format (no `%N`-as-ns, no
`%:z`) and yields garbage — derive the ns stamp from `%y` or `st_mtime_ns` instead.

**2. Wrapper hop / `omp.real`.** **No wrapper hop.** `command -v omp` → the one path;
`readlink -f` → itself (not a symlink); the file's first bytes are `\x7fELF`; `omp --version`
runs directly. `ls -l ~/.local/bin/omp.real` → "No such file or directory" (exit 2);
`find /home/vgpnk -maxdepth 6 -name 'omp.real*'` → empty; `grep -c 'omp\.real'` in the ELF's own
strings dump → 0. The round-72 premise ("`omp` is a 1,680-byte crash-restart wrapper whose BIN is
`omp.real`") is **false on this host**. The only other omp-named file in that directory is
`omp-swarm` (11,185 B, bash script, 2026-10-06) — unrelated.

**3. `verify_surfaces.py`.**
- No override, pre-ExecC2Pin: `{"error": "omp binary not found: /home/vgpnk/.local/bin/omp.real"}`,
  exit 2 — the recorded exit-2 error, verbatim.
- No override, **current worktree** (ExecC2Pin already re-pointed `DEFAULT_BINARIES`): **pass 7,
  fail 0, exit 0, error None** — all seven ids PASS (`literal_present` "39 loader-kind entries
  verified", `no_uncovered_class` "all 8 extracted loader class(es) declared", `opencode_extract`
  "6/6 declared (+3 ledgered removals) from 7/7 rules", `table_parity` "42 ids",
  `literal_parity` "42 literals", `kind_parity` "42 kinds", `excluded_reason` "8 excluded
  entries").
- With `--omp-binary /home/vgpnk/.local/bin/omp`: **pass 7, fail 0, exit 0**, identical verdicts,
  and `substrate.omp` = path `/home/vgpnk/.local/bin/omp`, sha256 `6737ee24…`, mtime
  `1793563867.2818089`, 276,785,328 B.
⇒ The exit-2 is cured by the **path re-point alone**; no override is needed on this host.

**4. The 42 baseline ids / `census-removals.json`.**
Dumps: `strings -n 4` on omp → 2,550,839 lines / 47,635,680 B / sha256
`bf6801e13b8fe7bb37d2d36608083f08610dfdb4c4f320536dd753d6ea1249fb`; on opencode → 1,237,844
lines / sha256 `020fb253…9fb` (**matches** the ledger's recorded `dump_sha256`).
- **All 42 ids resolve.** Baseline literals that do not occur, unexcused: **`[]` (empty)**.
- The 8 omp loader-group classes extract exactly as declared: `(agents-md, AGENTS.md)`,
  `(claude-md, CLAUDE.md)`, `(opencode, AGENTS.md)`, `(gemini, GEMINI.md)`, `(gemini, system.md)`,
  `(gemini, SYSTEM_TEMPLATE.md)`, `(github, copilot-instructions.md)`,
  `(windsurf, memories/global_rules.md)`.
- `census-removals.json`: **no declared-gone class reappears.** `CONTEXT.md` → 0 literal hits,
  anchor 0; `instructions/CLAUDE.md` → literal 3 hits (bare string-table entry + prompt prose,
  no loader role), anchors `disableClaudeCodePrompt` 0 and the AGENTS/CONTEXT name-priority array
  0; `claude-home/CLAUDE.md` → literal 3 hits, the `.join(<x>.home, ".claude", …)` anchor 0.
  `removal_problems()` → `problems: []`, excusing exactly those 3 ids.
- opencode ledger `measured_against` all match live (binary sha256, dump sha256, version v2.1.4).

**5. The description render cut.**
- `_8n` → 4 hits, offsets `1710510 / 46011151 / 46011330 / 46178794`; **all four are incidental
  substrings of unrelated minified identifiers** (`_8n]nF`, `_8nD`, `y_8n`, `6_8nXs`), **not** the
  render constant. `grep -c 'slice(0, _8n-1)'` → 0; `grep -c '_8n = 100'` → 0.
- The constant **still exists, renamed**: `var k = 100;` at offset `25501926` (unique), in
  `packages/coding-agent/src/extensibility/skill-descriptions.ts`; the truncator is `function dnt(e)`
  (offset `25503747`), exported as `previewSkillDescription`; the compressor factory is `cnt`
  (exported as `createSkillDescriptionCompressor`). The **algorithm is byte-for-byte the same**:
  `if (t.length <= k) return t; const r = t.slice(0, k - 1);` (= offset 99) then
  `r.match(/^.*?[.!?](?=\s|$)/)?.[0]` kept if `>= E` (40) chars, else last-space + `…`.
- `available_skills` → 2 hits, first at offset `46379374` (line 2526948): the template
  `<available_skills>{{#each skills}}<skill><name>{{name}}</name><description>{{description}}</description>…`
  — the listing is **XML-shaped** in 18.15.0, which is the substrate reason behind C1's R7
  `no_xml_tag`. (The older `<skills>` / `- {{name}}: {{description}}` background-session variant
  also still exists, line 2530773/2530775.)
- `skill-descriptions` → 14 hits, first at offset `9222668` (line 611279): chunk paths, the
  agent-scoped `skill-descriptions.db`, the `skill_descriptions` SQLite table and its
  `INSERT OR REPLACE` — the cache mechanism is intact.
- Bonus: the **1024 spec ceiling (C1's R3)** is corroborated in the binary — the frontmatter
  validator returns `"description" exceeds 1024 characters` (line 970518) and
  `packages/wire/src/skillshare.ts` carries `descriptionLength: 1024` (line 939150).

## Guard non-vacuity, verified (read-only runs in my scratch)

| arm | command | observed |
|---|---|---|
| candidate pins + real ELF | `check_substrate_pins.py --baseline $S/candidate-baseline.json --omp-binary ~/.local/bin/omp` | `OK 3/3 pins hold`, exit **0** |
| **wrong ELF** (opencode) | same baseline, `--omp-binary ~/.opencode/bin/opencode` | `DRIFT 2/3 pins failed`, exit **1** |
| **deleted pin** | candidate baseline minus `omp_binary_sha256` | `PIN_ABSENT 1/3 pins failed`, exit **1** |
| current committed pins | `check_substrate_pins.py` (worktree) | `DRIFT 2/3 pins failed`, exit **1** (delta_ns `938022666258967`) |

⇒ The guard is **not vacuous**: a wrong binary and a deleted pin both exit 1. C2's kill rule passes.

## Final C2 predicate, measured on the current worktree

After ExecC2Pin's path re-point **and** the `verifiers/baseline.json` re-pin landed, both
conjuncts of the frozen C2 predicate read green on this host:

```
$ python3 -B verifiers/check_substrate_pins.py
PASS omp_binary_sha256: 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f
PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
PASS opencode_binary_sha256: ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7
OK 3/3 pins hold                                                        exit 0

$ python3 -B verifiers/verify_surfaces.py --json          # no --omp-binary override
pass 7   fail 0   exit 0                                    (all 7 check ids PASS)
```

The landed `omp_round85_note` in `verifiers/baseline.json` agrees with every value this recon
measured independently (same sha, same ns stamp, `delta 0 ns / tolerance 0 ns`, `omp.real` absent,
`verify_surfaces.py` retains pass 7 fail 0).

## Findings for the L1 (documentation, NOT pin values)

1. **SKILL.md citation drift** — `SKILL.md:29-30` and `SKILL.md:565-566` cite `_8n=100` /
   `slice(0, _8n-1)`. Those exact strings do **not** occur in omp 18.15.0; the constant is
   `var k = 100;` and the truncator is `dnt`. The documented *behaviour* (offset 99, first-sentence
   ≥ 40, last-space + `…`) is unchanged, so C1's R1 bound of 99 still holds — but the cited symbol
   no longer resolves. The lane's other cited anchors all still resolve
   (`previewSkillDescription` 2, `createSkillDescriptionCompressor` 2, `A8n` 6, `K7s` 4,
   `compress-description` 4). → in scope for ScribeLesson's correction block.
2. **Stale round-72 comments** — `verifiers/check_substrate_pins.py:64-66` and
   `verifiers/verify_surfaces.py:163-167` still assert the wrapper/`omp.real` premise that is false
   here. ExecC2Pin added a round-85 line but the round-72 line remains above it.
3. `verifiers/baseline.json` `omp_round72_note` still describes the `omp.real` pin — the round-85
   re-pin should ADD a new note (as r44/r51/r72 did), not rewrite history.
4. `verifiers/check_substrate_repin_v2.py:12-13` prose still says "a path move onto
   `~/.local/bin/omp.real`" — stale, names a nonexistent path.
5. `verifiers/check_report_pointers.py:80,658,772` mentions `omp.real` only as a **dotted
   non-pointer fixture string** in the report-pointer checker — not a path constant. Do not "fix" it.
6. `stat -c '%Y-%m-%dT%H:%M:%S.%N%:z'` is invalid GNU stat — use `%y` or `st_mtime_ns`.

## Scope / limits

- Did not run `verify_harness_claims.py` / `verify_harness_independent.py` (they read omp session
  bodies and the live skills DB — outside this seat's read-only scope and the privacy boundary
  other rounds noted). Their omp path constants were re-pointed by ExecC2Pin and were not
  re-measured here.
- Did not edit `verifiers/` or `SKILL.md`; ran no git write; wrote only under
  `.ufo/waves/round-85/w1/ScoutSubstrate/` and my own scratch dir (removed on exit).
- No tool was installed or upgraded by this seat (nothing in the recon needed it), so the
  tooling-directive record is empty: tool/version/channel/reason — none.
