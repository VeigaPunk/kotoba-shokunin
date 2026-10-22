# OmpCalleeCensus — independent falsifier for C1 (omp 18.12.6 loader classes)

Result: the 18.12.6 dump carries exactly 11 `(<ctx>, <group>, "<file>.md")` registration shapes covering the
8 declared loader-group classes through three callees absent from the round-50 allowlist — `bq`, `Kl`, `Ho`.
Adding those three alone extracts 8 pairs but still FAILs: `omp:claude-md/CLAUDE.md` is var-bound to `S$`,
which is bound twice (`"title"` L843423, `"claude-md"` L895604), and the shipped first-seen, conflict-dropping
constant table drops it to `<unresolved-var:S$>`. 7 of 7 is reachable only with a binding rule that takes the
nearest preceding binding (or the enclosing module), plus the three callees.

## Observed facts

Binary: `omp --version` → `omp/18.12.6` (exit 0); sha256
`85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`; size 256702432; mtime
`2026-10-21 20:37:24.615549837 -0300` (2026-10-21T23:37:24Z); dump `strings -n 4` exit 0, 2444467 lines,
48148449 bytes, sha256 `953b19dffc4d51bd877330b90f0e994db38e90ee5f80575f08a31f3b73e7d96f`.

Eight declared classes (`verifiers/surfaces-baseline.json`, kind `loader-group`, all `governed`) and every
call that registers each one. Line numbers are lines of the strings dump.

| class id | callee(s) | argument shape | group token | dump line | excerpt |
|---|---|---|---|---|---|
| `omp:agents-md/AGENTS.md` | `bq` | `bq(<ctx>, <group-var>, "<file>.md")` | identifier `v$` = `"agents-md"` | 895593/895596 | `var v$ = "agents-md";` … `return bq(u, v$, "AGENTS.md");` |
| `omp:claude-md/CLAUDE.md` | `bq` | same | identifier `S$` = `"claude-md"` | 895604/895607 | `var S$ = "claude-md";` … `return bq(u, S$, "CLAUDE.md");` |
| `omp:opencode/AGENTS.md` | `Kl` | `Kl(u, "<group>", "<file>.md")` | literal `"opencode"` | 899557 | `Kl(u, "opencode", "AGENTS.md");` |
| `omp:gemini/GEMINI.md` | `Kl`, `Ho` | same, both callees | literal `"gemini"` | 899323, 899334 | `Kl(u, "gemini", "GEMINI.md");` / `Ho(u, "gemini", "GEMINI.md");` |
| `omp:gemini/system.md` | `Kl`, `Ho` | wrapped: call sits inside a parent call | literal `"gemini"` | 899462, 899460 | `Kl(u, "gemini", "system.md"), "user", "text");` |
| `omp:gemini/SYSTEM_TEMPLATE.md` | `Kl`, `Ho` | wrapped | literal `"gemini"` | 899461, 899459 | `Kl(u, "gemini", "SYSTEM_TEMPLATE.md"), "user", "template");` |
| `omp:github/copilot-instructions.md` | `Ho` | `Ho(u, "<group>", "<file>.md")` | literal `"github"` | 899795 | `Ho(u, "github", "copilot-instructions.md");` |
| `omp:windsurf/memories/global_rules.md` | `Kl` | `Kl(u, "<group>", "<file>.md")` | literal `"windsurf"` | 900706 | `Kl(u, "windsurf", "memories/global_rules.md");` |

Callee bodies (argument shape: context, group, file):
- `async function bq(e, t, n)` L863364 — resolves `e.home` / `e.cwd` / `e.repoRoot`, `t` = group, `n` = file.
- `function Kl(e, t, n)` L863058 — `if (!Mi(t, e)) return null; return pLe(e, t, n);`
- `function Ho(e, t, n)` L863062 — `const r = SO[t]; if (!r.projectDir) return null; return c.join(e.cwd, r.projectDir, n);`

Corroboration that the group token is the class id: registry inserts `Le(Tl.id, { id: v$, … })` L895597 and
`Le(Tl.id, { id: S$, … })` L895608, and provider bindings `var mo = "gemini"` L899269, `var Fo = "github"`
L899789, `var ho = "opencode"` L899492, `var Cm = "windsurf"` L900655 match the quoted groups.

Every identifier used as a group argument, and every `var/let/const <id> = "..."` binding of it:

| identifier | bindings in dump | values |
|---|---|---|
| `v$` | 1 | `"agents-md"` (L895593, chunk `discovery/agents-md.ts`) |
| `S$` | 2 | `"title"` (L843423, chunk `session/session-entries.ts`), `"claude-md"` (L895604, chunk `discovery/claude-md.ts`) |

No other identifier is used as a group argument; the remaining groups are string literals (`"gemini"`,
`"opencode"`, `"github"`, `"windsurf"`), and no extra `.md` registration shape exists anywhere in the dump.

## Answers

1. Callees the allowlist must add: `bq`, `Kl`, `Ho` — exactly, as names. Current allowlist
   (`Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo|lq|Xl|Fo`) extracts 0 pairs from this dump. The three
   names are the 18.12.6 descendants of the 18.12.5 fixture's `lq/Xl/Fo`; keeping the old names is
   harmless here (0 matches) but adds no protection.
2. Is `S$` rebound to different strings: yes, twice — `"title"` at L843423 and `"claude-md"` at L895604
   (`var/let/const` count 2, no other assignment). The binding nearest before `bq(u, S$, "CLAUDE.md")`
   (L895607) is `var S$ = "claude-md"` (L895604), three lines earlier inside the same module chunk
   (`// packages/coding-agent/src/discovery/claude-md.ts`). Consequence with the shipped `constant_table`
   rule (first-seen, conflicts dropped): `S$` is unresolvable, so the extractor emits
   `omp:<unresolved-var:S$>/CLAUDE.md` — `surfaces.literal_present` still fails the claude-md row and
   `surfaces.no_uncovered_class` reports one undeclared class (reproduced below).
3. Over-match if the allowlist were widened to any two-letter callee: not in this dump. Exactly 11 matches,
   the same 8 pairs, 0 extra classes (`[A-Za-z_$][A-Za-z0-9_$]`). Any-1-char, any-3-char and any-length
   callee patterns add no new group here (any-1-char and any-3-char: 0 matches; any-length: only the same
   `<unresolved-var:S$>` pair). The risk is latent, and the guard is the `.md` suffix,
   not the callee: the same helpers take non-`.md` files in the same chunks — `Kl(u, "gemini", "settings.json")`
   L899281, `Ho(u, "gemini", "extensions")` L899358, `Kl(u, "opencode", "skills")` L899668,
   `Ho(u, "github", "instructions")` L899835, `Kl(u, "windsurf", "mcp_config.json")` L900679,
   `Ho(u, "gemini", "")` L899338. A future build that names a non-instruction file `*.md` would be counted
   as a class and fail parity spuriously. The 18.12.5 fixture already carries a planted alias decoy —
   `const q = Xl; var decoy = q(u, "evil", "EVIL.md")` — which any-identifier widening extracts as
   `omp:evil/EVIL.md`; it is a one-character alias, so an exactly-two-letter widening misses it. That shows
   the "two-letter" boundary is arbitrary, not safe.

## Consequence for the C1 fix (advisory, not integrated here)

- Callees `bq|Kl|Ho` plus the shipped resolver: 8 pairs, one of them `<unresolved-var:S$>`; both FAILs persist
  (`surfaces.literal_present` names `omp:claude-md/CLAUDE.md`, `surfaces.no_uncovered_class` names
  `omp:<unresolved-var:S$>/CLAUDE.md`). Verified by calling the shipped `extract_classes`,
  `check_literal_present` and `check_no_uncovered_class`.
- With nearest-preceding-binding resolution (same three callees) the extraction is exactly the 8 declared
  pairs, `surfaces.no_uncovered_class` returns `all 8 extracted loader class(es) declared`, and the omp clause
  of `surfaces.literal_present` clears (the only rows left in my simulated run were opencode rows, because I
  passed an empty opencode dump; the real run passes those).
- Fixture arm: a trimmed 18.12.6 fixture that omits the `S$ = "title"` rebind will pass while the live dump
  fails (fixture-only fixture). The arm must include a conflicting `S$` binding, or assert on the live dump.

## Evidence (commands and exit codes)

Run in `/fast/scratch/hyaku/kotoba-r51/build/OmpCalleeCensus/`:
```
/home/vgpnk/.local/bin/omp --version                                  -> omp/18.12.6                      exit 0
sha256sum /home/vgpnk/.local/bin/omp                                 -> 85d9daf3…ccfa4                   exit 0
stat -c '%y %s %n' /home/vgpnk/.local/bin/omp                        -> 2026-10-21 20:37:24 … 256702432   exit 0
strings -n 4 /home/vgpnk/.local/bin/omp > omp.strings.txt            -> 2444467 lines, 48148449 bytes    exit 0
grep -o -- 'var v\$ = "agents-md"' omp.strings.txt | wc -l           -> 1
grep -o -- 'var S\$ = "title"'     omp.strings.txt | wc -l           -> 1
grep -o -- 'var S\$ = "claude-md"' omp.strings.txt | wc -l           -> 1
grep -o -- 'bq(u, v\$' omp.strings.txt | wc -l                       -> 1
grep -o -- 'bq(u, S\$' omp.strings.txt | wc -l                       -> 1
grep -n -o -- 'Kl(u, "gemini", "SYSTEM_TEMPLATE.md")[^;]*' omp.strings.txt
                                                                     -> 899461:Kl(u, "gemini", "SYSTEM_TEMPLATE.md"), "user", "template")  exit 0
grep -c -- 'Le(Tl.id, {' omp.strings.txt                              -> 10                               exit 0
```
Lane checkout, read-only:
```
python3 -B verifiers/verify_surfaces.py --json                       -> exit_code 1, pass 5, fail 2      exit 1
  surfaces.literal_present FAIL   : 8 loader literal(s) not verifiable (all eight omp loader-group rows)
  surfaces.no_uncovered_class FAIL: vacuity: 0 loader class(es) extracted from the omp dump while the
                                    baseline declares 8 loader-group class(es); extractor blind: 33 declared
                                    literals present but no registration shape extracts
python3 -c 'import json; [print(e["class_id"], e["literal"]) for e in json.load(open("verifiers/surfaces-baseline.json"))["classes"] if e["harness"]=="omp" and e["context_kind"]=="loader-group"]'
                                                                     -> the 8 ids in the table above        exit 0
```
Extraction replays (Python in the scratch dir, importing the lane verifier read-only; shipped regexes and
`constant_table` reused verbatim): shipped allowlist 0 pairs; `+bq|Kl|Ho` 8 pairs incl.
`('<unresolved-var:S$>','CLAUDE.md')`; nearest-preceding binding 8 declared pairs; any-2-letter callee 11
matches / 8 pairs, `omp:evil/EVIL.md` appears only on the 18.12.5 fixture under any-length widening.

No tools installed or upgraded in this seat.

## Confidence and remaining unknowns

High: call-shape inventory, callee names, group tokens, the `S$` double binding, the nearest binding, the
base-run failures — all deterministic scans of the pinned binary, replayed with the shipped code.
Inference (marked): the `"title"` binding belongs to a different module scope (`session-entries.ts`) and
cannot bind at the claude-md call, so nearest-preceding and per-module scoping agree here; I did not verify
Bun's scope handling beyond the textual chunk comments.
Unknown: whether the integrated fix chooses nearest-preceding or module scoping, and whether the new
18.12.6 fixture reproduces the `S$` conflict; I did not read the SurfacesRepin seat's work and did not run
the after-state.
