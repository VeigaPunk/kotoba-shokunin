Result: DONE — opencode 1.19.4 exposes a model-free reader for its read-channel instruction set and loads exactly one file per directory with `AGENTS.md` ahead of `CLAUDE.md` and `CONTEXT.md`; its always-on system-prompt instruction set is `not determinable without a model call`.

# Scout — measured opencode 1.19.4 instruction-file behaviour (model-free)

Seat: KotobaR53.ScoutOpencodeBehaviour (leaf, no dispatch). All measurements 2026-10-22
20:04–20:18Z. Scratch: `/fast/scratch/hyaku/kotoba-r53/ScoutOpencodeBehaviour/`. Lane read-only;
the only lane write is this report. No tool installs or upgrades. No paid model call: `opencode
run`, `claude -p`, `codex exec`, `gemini -p` were never invoked.

## 1. Client under test

- `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`,
  sha256 `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`,
  214,522,032 bytes, mtime 2026-10-22 14:50:30 −0300 (17:50:30Z).
- `opencode --version` → `1.19.4`, exit 0.
- All behaviour measurements below (sections 2–6) used an isolated `HOME`/`XDG_*` tree under the
  scratch clone (`$S/home`). The two host-state probes named in the caveat below were the only runs
  that saw the real data dir; no host config was loaded by the behaviour probes.

Host-state caveat: with the **real** `HOME`, `opencode debug info` and `opencode debug agent build`
both exited 1 with `Database is not empty and has no session table`
(`/home/vgpnk/.local/share/opencode/opencode.db`, 17,219,584 bytes, mtime 2026-10-17 19:26, unchanged
by the failed runs). All behaviour measurements are therefore from a fresh isolated data dir.

## 2. The command that reveals instruction files without a model

```
opencode debug agent build --tool read --params '{"filePath":"<path>"}'
```

Run from the directory above the case directory. Exit 0, no prompt, no model. The result carries
`result.metadata.loaded`, the exact instruction paths the read channel appended, and the appended
text is in `result.output` inside `<system-reminder>` with an `Instructions from: <path>` header.

What makes this model-free (observed, not assumed):

- The command is under `debug`, logs `mode=debug`, `model=undefined`; the session it creates has
  `cost=0`, all token counters 0, and empty message parts (`opencode export <session>`). The exported
  assistant message carries `providerID=opencode`, `modelID=big-pickle` as placeholders; with zero
  tokens/cost and no parts, that is not a model request.
- Re-run under `unshare -rn` (no network interfaces except loopback, `curl` to the internet fails
  with exit 7) produced byte-identical `loaded` lists and exit 0 for all four cases, stderr 0 bytes.
  Instruction resolution is local; nothing about it depends on a provider.
- A `strace -f -e trace=connect` of one run shows HTTPS connects to Cloudflare addresses;
  [INFERENCE] that is catalog/update metadata, not a model request (no prompt is recorded: zero
  tokens/cost, empty parts, sub-second return).

What it does **not** measure: the always-on system-prompt instruction set (`Instruction.systemPaths`
and the `core/instructions` context layer). No model-free command tried materializes that list; the
resolvers sit on the prompt path (see § 6, § 7).

## 3. The four requested directories — observed file lists

Layout at the scratch root (no root-level instruction file; `/fast/scratch/hyaku/kotoba-r53/` and
its ancestors carry none on this chain). Each case has `notes.txt`; probes read `<case>/notes.txt`
from the scratch root.

| case | contents | `metadata.loaded` | output marker | other marker present |
|---|---|---|---|---|
| (a) | `AGENTS.md` only | `['…/a/AGENTS.md']` | `AAA` | — |
| (b) | `CLAUDE.md` only | `['…/b/CLAUDE.md']` | `BBB` | — |
| (c) | `AGENTS.md` + `CLAUDE.md` | `['…/c/AGENTS.md']` | `CCC_AG` | `CCC_CL` 0 occurrences |
| (d) | `AGENTS.md`, `CLAUDE.md` → symlink to `AGENTS.md` | `['…/d/AGENTS.md']` | `DDD` | one `Instructions from:` only |

Exit 0 for all four; stderr 0 bytes each. `loaded` paths are absolute; shortened to `…` in the table.
Raw JSON: scratch `results/probe-{a,b,c,d}.json`; no-network reruns `results/netns-*.err` (0 bytes).
The exact arrays (2026-10-22T20:11–20:12Z):

```
(a) ["/fast/scratch/hyaku/kotoba-r53/ScoutOpencodeBehaviour/a/AGENTS.md"]
(b) ["/fast/scratch/hyaku/kotoba-r53/ScoutOpencodeBehaviour/b/CLAUDE.md"]
(c) ["/fast/scratch/hyaku/kotoba-r53/ScoutOpencodeBehaviour/c/AGENTS.md"]
(d) ["/fast/scratch/hyaku/kotoba-r53/ScoutOpencodeBehaviour/d/AGENTS.md"]
```

Reading `a/AGENTS.md` itself gives `loaded=[]` and no `<system-reminder>`. This is a real skip
(dump line 598311, `B===te`), not an absence: an instrument that probes by reading the instruction
file itself gets a false negative.

## 4. Additional measured behaviour (same command)

| probe | observed |
|---|---|
| `e/CONTEXT.md` only | loads `CONTEXT.md` (it is the third name in the list) |
| `f/AGENTS.md` + `f/CONTEXT.md` | loads `AGENTS.md` only; `CONTEXT.md` content absent |
| `g/sub/AGENTS.md` + `g/sub/deep/AGENTS.md` | loads `[g/sub/deep/AGENTS.md, g/sub/AGENTS.md]`, nearest first |
| `h/sub/AGENTS.md` + `h/sub/deep/CLAUDE.md` | loads `[deep/CLAUDE.md, sub/AGENTS.md]` — first match is per directory, not global |
| `imp/CLAUDE.md` containing a literal `@AGENTS.md`, no `AGENTS.md` file | loads `CLAUDE.md`; `@AGENTS.md` appears unexpanded in the output |
| config/home candidates present (`home/.config/opencode/AGENTS.md`, `home/.claude/CLAUDE.md`) | read channel ignores both; only the case-dir file loads |
| `OPENCODE_DISABLE_PROJECT_CONFIG=1` | read-channel result unchanged (case a still loads `a/AGENTS.md`) |

Scope limit measured, not inferred: the read-channel walk checks only directories **strictly below**
the instance directory. With cwd `hook`, file `hook/sub/deep/notes.txt`, `hook/AGENTS.md` was not
loaded while `hook/sub/AGENTS.md` was. Running the probe with cwd equal to the case directory and
reading a file directly in it returns `loaded=[]` even when the case directory has `AGENTS.md`.

## 5. Gate measurement

The list is gated by `OPENCODE_DISABLE_CLAUDE_CODE_PROMPT` (direct) or `OPENCODE_DISABLE_CLAUDE_CODE`
(broad); dump line 597580 binds both, and the list at 598309 uses `!i.disableClaudeCodePrompt`.

| case | env | `loaded` |
|---|---|---|
| (b) CLAUDE.md only | none | `b/CLAUDE.md` |
| (b) CLAUDE.md only | `OPENCODE_DISABLE_CLAUDE_CODE_PROMPT=1` | `[]` |
| (b) CLAUDE.md only | `OPENCODE_DISABLE_CLAUDE_CODE=1` | `[]` |
| (c) both | direct gate | `c/AGENTS.md` |
| (d) symlink | direct gate / broad gate | `d/AGENTS.md` in both |
| (e) CONTEXT.md only | direct gate | `e/CONTEXT.md` (not gated) |

## 6. Comparison with OC-1 … OC-6 (`verifiers/verify_surfaces.py`)

The frozen rules were applied directly to a `strings -n 4` dump of the 1.19.4 binary
(993,160 lines), independently of the whole-counter run:

```
OC-1 match: ["AGENTS.md",...!i.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]
OC-1 names: ['AGENTS.md', 'CLAUDE.md', 'CONTEXT.md']
OC-2 config: ['AGENTS.md']   OC-2 home: [('claude', 'CLAUDE.md')]
OC-3a: True                  OC-3b filter: True render: True
OC-4 fn hook: False          fn read: False       token: True
OC-5 env: True               globUp project: True  globUp config: True
OC-6 anchors: Key.make("core/instructions") False, targets:["AGENTS.md"] True,
              InstructionContext.observe True, system-context-builtins True
```

| rule (frozen) | artifact result | live/behavioural result |
|---|---|---|
| OC-1 name-priority list | PASS; exact array at dump line 598309 | Measured via read channel: AGENTS > CLAUDE (c), AGENTS > CONTEXT (f), CONTEXT loads alone (e), gate removes CLAUDE (b). Confidence: measured for the read channel. |
| OC-2 config/home candidates | PASS; `a=[pe.join(n.config,"AGENTS.md"),…pe.join(n.home,".claude","CLAUDE.md")…]`, dump 598309 | Not measurable through the read channel: both candidates were present in the isolated config/home and neither loaded. They belong to `Instruction.systemPaths` only. Confidence: code only. |
| OC-3a declared `instructions` | PASS; loop at dump 598309 | `opencode debug config` echoes a declared list including an `https://` entry (`cfgtest/opencode.json` → exit 0). Config plumbing observed; per-entry file/glob resolution not observed. |
| OC-3b remote filter + render | PASS; filter and `Instructions from: ` at dump 598309/597823 | Not measured (fetch + render happens during a model request). |
| OC-4 read hook | **FAIL**: `fn("Instruction.resolve")` and `fn("ReadTool.execute")` occur 0 times; 1.19.4 has `l("Instruction.resolve")` (dump 598311) and `l("ReadTool.execute")` (598484); `<system-reminder>` present | Behaviour works and is measured: `metadata.loaded`, `<system-reminder>`, `Instructions from:`, per-directory first match, nearest first. This is C1's defect: minified callee alias churn, not a loader change. |
| OC-5 resolution switch | PASS; env literal at dump 596470, both `globUp` shapes in `Instruction.systemPaths` at dump 598309 | `OPENCODE_DISABLE_PROJECT_CONFIG=1` does **not** change the read channel (measured above). The switch is inside `Instruction.systemPaths` (dump 598309), not `Instruction.resolve`. Confidence: measured negative plus code. |
| OC-6 second subsystem | **FAIL**: `Key.make("core/instructions")` 0; 1.19.4 has `Wr.make("core/instructions")` (dump 597822); the other three anchors present (597823, 597828) | Not runtime-measured (system-prompt layer). Code at 597822–597828 shows `core/instructions`, `InstructionContext.observe`, `targets:["AGENTS.md"]`, the `OPENCODE_DISABLE_PROJECT_CONFIG` gate, a `join(config,"AGENTS.md")` candidate, and `system-context-builtins`. Confidence: code only. |

Frozen counter at base, re-run this seat (read-only):

```
python3 -B verifiers/check_opencode_repin.py --rev e78dff667237fba2e3cf9eccb802eff5bc9ea302
opencode re-pin: surfaces pass 6 of 7 (opencode_extract FAIL); pins OK 2/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions
substrate opencode: … sha256 538fcb1b… bytes 214522032
exit=1
```

`verify_surfaces.py --json` names the same two rules and lists all four OC-6 anchors as missing
(its fail-closed report lists every anchor when one fails); the direct anchor probe above shows only
`Key.make(` is actually absent. OC-4 has two of three absent. This corroborates
`ScoutOcRelease.md` (source files byte-identical between 1.19.3 and 1.19.4; only the bundled alias
changed) and the docs quote there: both files present → only `AGENTS.md` is used.

**Consumer difference worth keeping straight** (code, dump 598309): the read hook resolves names
per directory (`Instruction.find`, first existing name in `f`), while `Instruction.systemPaths`
walks `findUp` for `AGENTS.md` first and stops at the first name with any match. If a parent has
`AGENTS.md` and a child has `CLAUDE.md`, the system channel loads the parent `AGENTS.md` and never
consults `CLAUDE.md`, whereas the read channel loads the child `CLAUDE.md` and the parent
`AGENTS.md`. The flat four-directory cases coincide; a nested case does not. Confidence: code.

## 7. System-prompt channel — what was tried, and the verdict

Every command below exited 0 unless stated; none returned a discovered instruction-file list for the
always-on prompt.

| command | result |
|---|---|
| `opencode debug --help` | lists 13 debug subcommands; none is an instructions/prompt reader |
| `opencode debug config` | resolved config only; echoes declared `instructions` (OC-3a), not discovered files |
| `opencode debug paths` | global paths (home/data/bin/log/repos/cache/config/state/tmp) |
| `opencode debug info` | `opencode version`, `os`, `terminal`, `plugins` only |
| `opencode debug startup --print-logs --log-level DEBUG` | exit 0; no line matching `instruction|AGENTS|CLAUDE|system.context` |
| `opencode debug v2` | `providers`, `default`, `small` only |
| `opencode debug agent build` | keys `description, mode, name, native, options, permission, tools`; no instruction field |
| `opencode debug file read a/notes.txt` | base64 content; no instruction hook |
| `opencode export <debug session>` | `messages[].parts` empty; no system text |
| `opencode serve --port 4789`, `GET /doc` | 200, 162 API paths; no system-prompt or instruction endpoint |
| `POST /api/session` `{}` then `GET /api/session/<id>/context` | 200 create, `{"data":[]}` context |
| `GET /api/session/<id>/history` | 200 `{"data":[],"hasMore":false}` |
| `GET /session/<id>/message` | 200, one assistant message with empty parts |
| `GET /experimental/capabilities`, `/experimental/resource`, `/api/reference`, `/api/skill` | capabilities/resource/reference empty of instructions; skill lists skills only |
| `opencode run --help` | no dry-run, print-prompt or system-prompt option |

Verdict: **`not determinable without a model call`** for the always-on system-prompt set. No
model-free command in 1.19.4 materialized it in any of the probes above; [INFERENCE] the prompt is
built per model request, and the read-channel measurement is a different consumer (see § 6).

## 8. Limits and implications

1. C1 re-pin: OC-4 lost `fn("Instruction.resolve")` and `fn("ReadTool.execute")` to the alias
   `fn`→`l`; OC-6 lost `Key.make(` to `Wr.make(`. Quoted names `("Instruction.resolve")`,
   `("ReadTool.execute")` and `make("core/instructions")` each still occur once, so an anchor on the
   quoted name (or on the source-stable frame) survives the rebuild; the live behaviour did not
   change. The frozen rules must not be widened this round; the re-derivation is the C1 executor's.
2. An instrument for OC-1/OC-4 using `debug agent --tool read` must run with cwd above the target
   directory, must read a non-instruction file, and must not reuse one session for a second probe:
   `loaded` reports only files newly added (claims are keyed per message; dump 598311), and the walk
   stops at the instance directory.
3. C2 / alwayson.07: the symlink form is effective here only because `CLAUDE.md` resolves to an
   existing `AGENTS.md` while `AGENTS.md` wins first; the symlink adds no second load (case d). A
   literal `@AGENTS.md` line is inert text to opencode (case `imp`). The import criterion comes from
   Claude Code's documented behaviour, so this opencode probe neither confirms nor denies that PASS
   case; it only rules out opencode expansion of the import.
4. OC-5's env switch does not belong to the read channel. A future fixture that expects
   `OPENCODE_DISABLE_PROJECT_CONFIG` to change `debug agent --tool read` output would be wrong.
5. Host-state caveat from § 1: any live probe must isolate `HOME`/`XDG_*`. With the real host data
   dir, `opencode debug paths` and `opencode agent list` worked, but `opencode debug info` and
   `opencode debug agent build` exited 1 on the existing `opencode.db`; the behaviour probes above
   therefore used a fresh data dir.

## 9. Reproduction (exact)

```
S=/fast/scratch/hyaku/kotoba-r53/ScoutOpencodeBehaviour
export HOME=$S/home XDG_CONFIG_HOME=$S/home/.config XDG_DATA_HOME=$S/home/.local/share \
       XDG_CACHE_HOME=$S/home/.cache XDG_STATE_HOME=$S/home/.local/state
OC=/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe
cd $S
$OC debug agent build --tool read --params '{"filePath":"a/notes.txt"}'   # exit 0
unshare -rn $OC debug agent build --tool read --params '{"filePath":"a/notes.txt"}'  # exit 0, same
```

Case contents: `a/AGENTS.md`; `b/CLAUDE.md`; `c/AGENTS.md`+`CLAUDE.md`; `d/AGENTS.md` and
`CLAUDE.md -> AGENTS.md`; each also `notes.txt` (`printf 'note a\n' > a/notes.txt`).

## 10. Remaining unknowns

- The always-on system-prompt file list for the four directories (needs a model request or a new
  upstream debug surface). [CODE] predicts the same winners for these flat cases, but it is not
  measured.
- Whether `Instruction.systemPaths` reads remote `instructions` entries unchanged across a redirect
  (OC-3b): not measured.
- Whether the read hook's per-message claims suppress a repeat load in a multi-read session: code
  says yes (dump 598311); not exercised because each debug invocation is a fresh session.
