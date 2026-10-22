# ReviewScopeRule: module-scope binding rule in verify_surfaces.py (round 51)

VERDICT: FAILS (narrow scope). The three fixtures you named hold: none resolves to a wrong declared pair. But HEAD resolves a function parameter that shadows `S$` to the module's own `claude-md` binding and passes silently (probe 09, exit 0). BASE, and HEAD with the rule switched off, both fail loud on that dump. The live 18.12.6 dump is not affected by what I checked (see F1).

Scope: verifiers/verify_surfaces.py at HEAD 59903b2637689739a5b9901956301da72d0effe1 vs BASE 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10 (diff stat: 1 file, 268 insertions, 13 deletions). All runs in /fast/scratch/hyaku/kotoba-r51/falsify/ReviewScopeRule/. The lane was read-only; this file is the only write there.

## How the rule finds a module (HEAD)
- MODULE_MARKER_RE (line 218): `^//[ \t]*\S+\.(?:[cm]?[jt]sx?)[ \t]*$`, multiline. A module is opened by a whole line that starts with `//` and holds one token ending in a JS or TS extension. No other bundle metadata is read.
- module_scopes (374-384): each marker opens a span that runs to the next marker. Text before the first marker is its own span.
- scope_table (399-409): with no marker, the whole dump is one span and the scope table is empty. Otherwise the span's bindings go through constant_table, the same first-seen, drop-on-conflict policy as the dump-wide table.
- extract_classes line 430: `consts = {**scope_table(...), **global_table}`. The dump-wide table wins wherever it has an entry. So a name with one value anywhere in the dump takes that value, whatever module the call sits in.

## Findings

F1. HEAD silently resolves a shadowed name to the module binding. Severity: medium. No live exposure found.
- Fixture 09 (fx/09-shadow-param.txt): the claude-md module binds `var S$ = "claude-md";`. The call is inside `async function XBt(u, S$)`, so `S$` is a parameter. Another module binds `var S$ = "title";`, so the dump-wide table drops `S$`.
- HEAD: rc 0, pairs claude-md/CLAUDE.md and gemini/GEMINI.md, all seven checks PASS. The parameter's value is not in the dump, so the claude-md pair has no evidence behind it.
- Ablated HEAD (module_scopes forced to one span): rc 1, FAIL literal_present and FAIL no_uncovered_class naming `<unresolved-var:S$>`. BASE with renamed callees: rc 1.
- Live dump: the one live S$ call (line 895607) sits in `async function XBt(u) {` (line 895606), which has no S$ parameter. A single-line scan of the 118 dump lines that contain S$ found 0 in a parameter list (python eval). That scan is heuristic and single-line only.
- Advice: refuse scope resolution when the identifier is a parameter or is redeclared inside the call's enclosing function. Add a fixture arm for probe 09 that expects exit 1.

F2. A strings split can remove a binding, and the rule does not close this. Severity: medium, pre-existing (BASE gives the same result).
- Fixture 08 was built with GNU strings 2.47 on a file whose title literal contains byte 0x01. The dump splits the binding into `var S$ = "ti` and `tle";`.
- The ASSIGN_RE value class `[^"\\\n]` cannot span that split, so the title binding vanishes. The claude-md binding is now the only value, so the dump-wide table (line 430) resolves the session-module call to claude-md.
- Results: HEAD rc 0 (silent), ablated rc 0, BASE with renamed callees rc 0.
- Same mechanism: ASSIGN_RE ignores any value longer than 80 characters (python eval: `var S$ = "` + 90 `a` + `";` gives []).

F3. Missing, repeated, or glued markers fail closed in every shape I ran.
- 05 (markers removed): rc 1 at all three runs. `<unresolved-var:S$>` FAIL.
- 06 (claude-md marker repeated just before the call): rc 1 at all three runs. The call's span has no S$ binding, and the dump-wide table is conflicted, so the call stays unresolved.
- 07 (marker glued after code, `var I7 = "CLAUDE.md";// packages/...`): rc 1 at all three runs. The regex anchors at line start (python eval: glued gives no match, standalone gives a match), so two modules merge and S$ conflicts.
- A silent path needs the call's own binding to be absent from its span (F1) or lost (F2).

F4. ASSIGN_RE's `\s*` crosses newlines (python eval: `S$` newline `= "claude-md";` gives `[('S$', 'claude-md')]`). A strings split between an identifier and `=` is joined back. Harmless in the probes; not analysed further.

## The three named fixtures
| fixture (scratch/fx/) | HEAD rc | ablated rc | BASE rc (renamed) | HEAD result |
|---|---|---|---|---|
| 02 same-module decoy between binding and call (design window-decoy) | 1 | 1 | 1 | loud FAIL; names `omp:<unresolved-var:S$>/CLAUDE.md` |
| 03 second declarator `var A = "x", zou = "claude-md";` (global conflict on zou) | 0 | 1 | 1 | PASS; claude-md is correct |
| 04a only S$ binding in call's module is foreign (`"title"`), claude call elsewhere | 1 | 1 | 1 | loud FAIL; undeclared `omp:title/CLAUDE.md` |
| 04b same as 04a, no claude call anywhere | 1 | 1 | 1 | loud FAIL; undeclared `omp:title/CLAUDE.md`; claude-md unwitnessed |

Other runs:
| fixture | HEAD rc | ablated rc | BASE rc (renamed) | HEAD result |
|---|---|---|---|---|
| 01 module-scoped clean base (control) | 0 | 1 | 1 | PASS; the rule fixes this shape |
| 05 markers missing | 1 | 1 | 1 | loud FAIL |
| 06 claude marker repeated | 1 | 1 | 1 | loud FAIL |
| 07 marker glued | 1 | 1 | 1 | loud FAIL |
| 08 strings split drops title binding | 0 | 0 | 0 | SILENT wrong pair (claude-md for a title call), F2 |
| 09 parameter shadows S$ | 0 | 1 | 1 | SILENT wrong pair (claude-md for a parameter), F1 |
| calibration: strings-omp-clean.txt | 0 | 0 | 0 | PASS |

## Evidence (commands and exit codes)
E1. `git clone -q <lane> <scratch>/lane` then `git -C <scratch>/lane checkout -q 59903b26…`: exit 0. `git cat-file -t 43ca0bfb…`: commit.
E2. `git -C <clone> diff --stat 43ca0bfb… 59903b26… -- verifiers/verify_surfaces.py`: `1 file changed, 268 insertions(+), 13 deletions(-)`, exit 0.
E3. `xd://lsp` read: `No such tool: xd://lsp. Mounted devices: ast_edit, debug.` No semantic caller or definition check was possible. I read the functions directly and ran them.
E4. Live freshness at HEAD: `python3 -B verifiers/verify_surfaces.py --json` in the clone (installed omp 18.12.6, sha256 85d9daf3…, 256,702,432 bytes): exit_code 0, pass 7, fail 0. The C1 claim reproduces.
E5. `python3 -B verifiers/verify_surfaces.py --self-test` at HEAD: `0 failure(s) over 115 assertions`, exit 0. The three `ERROR …` lines on stderr come from the self-test's own missing-file arms.
E6. Fixture runs: `python3 -B verifiers/verify_surfaces.py --repo <rev> --omp-strings <fixture> --opencode-strings verifiers/fixtures/surfaces/strings-opencode-clean.txt --baseline verifiers/fixtures/surfaces/baseline-clean.json --inventory verifiers/fixtures/surfaces/inventory-clean.md`, for three revs:
   - HEAD clone.
   - Ablated copy (scratch/ablate/verify_surfaces_ablate.py): HEAD with `return [(0, len(dump))]` inserted at the top of module_scopes. This gives BASE's resolution with HEAD's callee list.
   - BASE clone with renamed callees: BASE's callee list has no Kl, Ho or bq, so unchanged fixtures cannot reach its scope logic. Copies in scratch/fx-base-callees/ rename `bq(` to `jDe(` and `Kl(`/`Ho(` to `Id(`.
   Pair sets were also read with extract_classes in each module (python eval).
E7. Live census (python eval over scratch/live-omp-strings.txt, which is `strings -n 4 /home/vgpnk/.local/bin/omp`, 2,444,467 lines):
   - 3239 markers, 3240 spans.
   - S$ string bindings: line 843423 `"title"` (span 864) and line 895604 `"claude-md"` (span 1083). These match ReviewSurfacesDesign.md.
   - S$ call at line 895607, span 1083 (same span as the claude-md binding).
   - 11 loader-shaped calls: Kl 5, Ho 4, bq 2. Also matches the design.
   - Live extracted pairs: agents-md, claude-md, gemini (3 files), github, opencode, windsurf.
E8. Calibration: strings-omp-clean.txt gives rc 0 at HEAD, ablated and BASE, with all seven checks PASS at HEAD.
E9. Cross-module decoy (fx/10-decoy-other-module.txt): a same-name `var S$ = "gemini"` sits in another module between the true claude-md binding and a second claude-md span that re-binds `S$ = "claude-md"` before the call. HEAD rc 0 with claude-md (correct: the call's own module binds it). Ablated rc 1 and BASE with renamed callees rc 1 (loud). No wrong pair.

Tooling: nothing installed or upgraded. Tools used as found: python3 3.14.8, GNU strings 2.47 (binutils), git 2.56.0. No jj command was run.

## Residual risk and gaps
- Probe 09 is my construction. The one live S$ call has no parameter shadow, but my parameter-list scan was single-line only.
- No semantic reference or definition check (lsp not mounted).
- ReviewSurfacesDesign.md specifies (b′) fixtures for a rule that is not implemented at HEAD. I compared only the cases where HEAD behaves comparably (02, 03).
- Not run: multi-line parameter lists; split points other than the probes in 07 and 08; a repeated marker that brings a different same-name binding into the call's span (reasoned from the code only, [INFERENCE]).
