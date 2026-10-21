verdict: PARTIAL — the verifier's *machinery* holds (7/7 PASS, self-test 99/99, exit 0 on the frozen 18.12.5/1.19.3 dumps), but its **docstring and OC comments contain 12 false or stale statements** about rules, fixtures, callee generations and limits; the highest-severity is `verifiers/verify_surfaces.py:102` ("runs rules OC-1..OC-4" — the code runs seven rules) and the exit-code contract at `:109-112` (an OS-level baseline read error exits **1 with an uncaught traceback**, not the documented 2).

Lane: `KotobaR47-2.W2SurfDocstring-2` (leaf, no subagents). Tip reviewed: **`7ad7fadfc09354b74fb66605dfb0c1182c115a2f`**.
Target: `verifiers/verify_surfaces.py` (1225 lines, sha256 `e44bf34b1a52c0e5e4cd320b8f90a20c10c0a997bc225e9b36bf90ccf173be4e`).
Scratch clone: `/fast/scratch/kotoba-r47/w2/W2SurfDocstring/kotoba-shokunin` (detached at 7ad7fad; `diff` vs the lane tree: IDENTICAL).
Read-only substrate: `/fast/scratch/kotoba-r47/shared/` — `sha256sum -c SHA256SUMS` → **exit 0, 4/4 OK**.

**Nothing in the lane tree was mutated.** The only writes are this report and `W2SurfDocstring.evidence.json` under `.ufo/waves/round-47/falsify/`. No git/jj mutating command was run in `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. The `~/.local/bin/opencode` wrapper was never executed. **No tools were installed or upgraded** (python3 + coreutils only; `uv`/`pacman` not invoked).

---

## What I attacked

Every prose assertion in the module docstring (`:1-113`) and in the OC comment blocks (`:138-150`, `:336-427`) was checked against (a) the code at 7ad7fad, (b) the frozen `omp-18.12.5.strings` / `opencode-1.19.3.strings` dumps, (c) `verifiers/surfaces-baseline.json`, (d) `corpus/knowledge/instruction-surface-census-round13.md`, (e) `verifiers/fixtures/surfaces/`.

**Baseline runs (these hold):**

```
$ python3 -B verifiers/verify_surfaces.py --self-test
0 failure(s) over 99 assertions
exit=0

$ python3 -B verifiers/verify_surfaces.py \
    --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
    --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings \
    --baseline verifiers/surfaces-baseline.json \
    --inventory corpus/knowledge/instruction-surface-census-round13.md
PASS surfaces.literal_present: 42 loader-kind entries verified against the dumps
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
exit=0
```

Note the verifier's own stdout already contradicts its docstring: **7/7 rules**, not "OC-1..OC-4".

---

## Findings by severity

### HIGH

#### H1 — `:102` — "This check runs rules OC-1..OC-4" is false; the code runs **seven** rules

`verifiers/verify_surfaces.py:101-102`:
```
   OC-1..OC-4 over the opencode dump instead and requires TWO-WAY parity: every
```

Code (`verifiers/verify_surfaces.py:454`, `:464`, `:471`, `:475`, `:482`, `:490`, `:497`) declares **seven** rules:

| rule | line | owns |
|---|---|---|
| OC-1 | :454 | `opencode:instructions/{AGENTS,CLAUDE,CONTEXT}.md` |
| OC-2 | :464 | `opencode:config/AGENTS.md`, `opencode:claude-home/CLAUDE.md` |
| OC-3a | :471 | `opencode:config/instructions` |
| OC-3b | :475 | `opencode:config/instructions-remote` |
| OC-4 | :482 | `opencode:read-hook/instructions` |
| OC-5 | :490 | (no id — shape witness) |
| OC-6 | :497 | `opencode:instruction-context/AGENTS.md` |

Repro (exit 0, stdout quoted above): `... from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)`.

The module's own section header `verifiers/verify_surfaces.py:337` says `rules OC-1..OC-6`; the comment at `:147` says `OC-1..OC-6`; `corpus/knowledge/instruction-surface-census-round13.md:212` is `### B′. opencode — instruction model (re-derived 2026-10-21 for 1.19.3, round 47)` and its prose says "Rules OC-1..OC-6 in `verifiers/verify_surfaces.py` were re-measured anchor by anchor on the dump". **Only the docstring is stale** — it was not updated with the round-47 re-derivation, and it under-reports the rule count by three (it misses OC-3b's split from OC-3, and all of OC-5/OC-6).

Calibration impact: a reader auditing "how many rules must match" from the docstring gets 4; the self-test matrix (`verifiers/verify_surfaces.py:1036-1043`) actually exercises **seven** drop-one fixtures (`strings-opencode-drop-oc1/oc2/oc3a/oc3b/oc4/oc5/oc6.txt`). The docstring's "every rule matches" therefore covers a materially smaller surface than the code.

#### H2 — `:109-112` — the exit-code contract is false for an OS-level baseline read error (documented 2, actual 1 + traceback)

`verifiers/verify_surfaces.py:109-111`:
```
Exit: 0 all checks pass | 1 any FAIL | 2 environment unreadable (binary, dump
file, strings tool, inventory file, or an OS-level baseline read error — never
a pass) | 3 baseline missing or unparseable ...
```

`load_baseline` raises **`EnvError`** on a non-`FileNotFoundError` `OSError` (`verifiers/verify_surfaces.py:242-243`):
```python
    except OSError as exc:
        raise EnvError("baseline unreadable: %s (%s)" % (path, exc))
```
but `main` catches **only `BaselineError`** around that call (`verifiers/verify_surfaces.py:1163-1170`), and the `except EnvError` arm (`:1190`) sits in a *later* try-block that covers only the dumps and the inventory. `EnvError` therefore escapes `main` uncaught.

Repro A (baseline path is a directory):
```
$ python3 -B verifiers/verify_surfaces.py --baseline verifiers/fixtures \
    --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
    --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings
Traceback (most recent call last):
  ...
  File ".../verifiers/verify_surfaces.py", line 1225, in <module>
    sys.exit(main())
  File ".../verifiers/verify_surfaces.py", line 1164, in main
    entries = load_baseline(baseline_path)
  File ".../verifiers/verify_surfaces.py", line 243, in load_baseline
    raise EnvError("baseline unreadable: %s (%s)" % (path, exc))
EnvError: baseline unreadable: verifiers/fixtures ([Errno 21] Is a directory: 'verifiers/fixtures')
exit=1
```
Repro B (unreadable file): `cp verifiers/surfaces-baseline.json /tmp/bl.json && chmod 000 /tmp/bl.json` → **exit=1** (same path).

The documented contract says exit **2**. Actual: exit **1**, an uncaught traceback on stderr, and — under `--json` — **no JSON payload at all** (the `emit_json([], 2, …)` arm at `:1190-1192` is never reached, because the baseline load happens before it). Exit 1 is the documented code for "a check FAILed", so a caller that distinguishes "FAIL" from "environment unreadable" mis-classifies this as a check failure. The "never a pass" half of the sentence does hold (1 ≠ 0).

This is the docstring's exit table being wrong in exactly the place a machine caller depends on. It is *not* caught by the self-test: `verifiers/verify_surfaces.py:1091-1096` covers a missing **inventory** file (→ 2, correct, because that path raises `EnvError` inside the covered try-block) and `:1098-1103` covers a missing **baseline** file (→ 3, correct) — but never an *unreadable* baseline. The nearest related case, a missing **dump** file (`:1028-1033`), is also exit 2 and correct.

---

### MEDIUM

#### M1 — `:16-19`, `:150`, `:165-166` — every example call shape in the docstring/comments is absent from the current substrate; the var-bound group names are one generation stale

`verifiers/verify_surfaces.py:13-19`:
```
1. Loader-class extraction.  ``strings -n 4`` dumps of the binaries are
   scanned for the registration-call shapes the bundles use::

       Id(e, "gemini", "GEMINI.md")              Cl(e, "github", "copilot-instructions.md")
       jDe(e, Pqr, "AGENTS.md")  with  var Pqr = "agents-md"
       I5(d, d$, "AGENTS.md")  with  var d$ = "agents-md"
       Gl(d, "gemini", "GEMINI.md")              Mo(d, "gemini", "GEMINI.md")
```

Occurrence counts in the frozen `omp-18.12.5.strings` (the pinned substrate of C1):

| docstring example | occurrences in 18.12.5 |
|---|---|
| `Id(e,"gemini","GEMINI.md")` | **0** |
| `Cl(e,"github","copilot-instructions.md")` | **0** |
| `jDe(e,Pqr,"AGENTS.md")` | **0** |
| `I5(d,d$,"AGENTS.md")` | **0** |
| `Gl(d,"gemini","GEMINI.md")` | **0** |
| `Mo(d,"gemini","GEMINI.md")` | **0** |
| `Cl(e,"cursor","rules")` (from `:64`) | **0** |
| `s(Cl(` (from `:150`) | **0** |
| `var Pqr` (from `:165`) | **0** |
| `, Zou = "AGENTS.md"` (from `:165-166`) | **0** |

The **actual** `.md` registration-call shapes in omp 18.12.5 — the full set, extracted with `OMP_CALL_RE` (`:156-160`) — are:
```
lq(u, f$, "AGENTS.md"        lq(u, m$, "CLAUDE.md"
Xl(u, "gemini", "GEMINI.md"  Fo(u, "gemini", "GEMINI.md"
Fo(u, "gemini", "SYSTEM_TEMPLATE.md"   Fo(u, "gemini", "system.md"
Xl(u, "gemini", "SYSTEM_TEMPLATE.md"   Xl(u, "gemini", "system.md"
Xl(u, "opencode", "AGENTS.md"          Fo(u, "github", "copilot-instructions.md"
Xl(u, "windsurf", "memories/global_rules.md"
```
i.e. **only three callees carry the whole extraction**: `lq`, `Xl`, `Fo`. The var-bound group names are `f$` → `"agents-md"` and `m$` → `"claude-md"` (verified: `f$` and `m$` are the only two `…$` bindings in 18.12.5; `Pqr` and `d$` bind to nothing).

Note the docstring is **internally inconsistent**: the inline allowlist at `:21` *does* include `lq|Xl|Fo` (added by round 47), but the illustrative example block above it — which the prose presents as "the registration-call shapes **the bundles use**" — shows only the retired 2026-09-28/2026-10-18 generations. A reader auditing the docstring against a live dump concludes the allowlist is dead.

The same staleness is visible in `corpus/knowledge/instruction-surface-census-round13.md:73-80` (§ A's evidence column still cites `jDe(e,Pqr,"AGENTS.md")`, `Id(e,"opencode","AGENTS.md")`, `Id(e,"gemini","GEMINI.md")`, `Cl(e,"github","copilot-instructions.md")`) and in `verifiers/fixtures/surfaces/baseline-clean.json:2` (`"omp:cursor/rules is Cl(e,\"cursor\",\"rules\")"`). That is the census/fixture lane's scope, but it is the source the docstring copied, so the docstring's examples should have moved with the round-47 re-pin and did not.

#### M2 — `:145-147` — the opencode allowlist rationale ("historical names only … full of single-letter callees that must not feed this extractor") is false on both of its factual claims

`verifiers/verify_surfaces.py:145-147`:
```
#   opencode: historical names only — its live bundle is full of single-letter
#             callees that must not feed this extractor; opencode's loaders
#             are list/join shapes governed by the OC-1..OC-6 rules instead
```

Two separate falsifications:

1. **"single-letter callees"** — the opencode allowlist is `CALL_RE` (`:151-155`), whose callee set is `Id | Cl | jDe | jDf | Tl | dr | GW`. **None is a single letter**; the shortest are two characters (`Id`, `Cl`, `Tl`, `GW`, `dr`). `CALLEE_SHAPES["opencode"]` (`:163`) confirms the same five-name set.
2. **"must not feed this extractor" / "full of"** — I broadened the callee alternation to *any* identifier and re-scanned the live opencode 1.19.3 dump for the same `(v, group, "file.md")` shape:
   ```
   broadened (any-callee) .md call shapes in opencode 1.19.3: 0
   CALL_RE (opencode) hits: 0
   ```
   The live opencode bundle contains **no** `.md` registration-call shape from **any** callee. So there is no "full of single-letter callees" hazard to keep out, and the opencode allowlist entry is inert either way. The real reason the opencode extractor yields nothing is stated correctly at `:99-101` ("opencode's loaders are JS list/join/filter shapes") — the comment at `:145-147` gives a different, wrong reason.

Additionally the label **"historical names only"** does not describe anything real for opencode: `Id|Cl|jD[ef]|Tl|dr|GW` are *omp's* 2026-09-28 and 2026-10-14 generations (`:142`), and opencode has never had a registration-call loader at all. The per-harness separation the comment advertises at `:139-141` ("a name harmless in one bundle over-matches the other") is, for opencode, **no separation at all** — `CALL_RE` is byte-identical to the first five alternatives of `OMP_CALL_RE`.

#### M3 — `:342-344` — the OC section header mis-describes which rules DERIVE ids and how many ids are witnesses

`verifiers/verify_surfaces.py:342-344`:
```
# the shape carries the name (OC-1, OC-2) and WITNESS the two ids whose identity
# is a behaviour rather than a literal (OC-3's two entries, OC-4).  Every rule is
```

- **OC-6 derives an id**, it does not witness one: `OC_V2_TARGETS = 'targets:["AGENTS.md"]'` (`:418`) is a literal-carrying shape, and `rule("OC-6", ["opencode:instruction-context/AGENTS.md"], v2, …)` (`:497-498`) turns that literal into a class id. By the header's own criterion ("the shape carries the name"), OC-6 is a derivation rule and is missing from the `(OC-1, OC-2)` list.
- **"the two ids"** is not two: the witness set is `opencode:config/instructions` (OC-3a), `opencode:config/instructions-remote` (OC-3b), `opencode:read-hook/instructions` (OC-4) — **three** ids, plus OC-5 which owns no id at all (`:485-492`, and the code's own wording "owns no class id; witnesses the path").

Round 47 changed this and the header was not updated. The census agrees with the code, not the header: `corpus/knowledge/instruction-surface-census-round13.md:257` (the OC-6 row, `opencode:instruction-context/AGENTS.md`, literal `AGENTS.md`).

#### M4 — `:361-362` — the GENERATION NOTE points at the **superseded** census section

`verifiers/verify_surfaces.py:360-362`:
```
# The rules were re-measured anchor by anchor on that dump (counts and dump lines in
# `corpus/knowledge/instruction-surface-census-round13.md` § B, round 47); the
```

The anchor-by-anchor counts and dump lines for 1.19.3 live in **`§ B′`** (`corpus/knowledge/instruction-surface-census-round13.md:212`, `### B′. opencode — instruction model (re-derived 2026-10-21 for 1.19.3, round 47)`), whose rows carry `(OC-1; dump 443993)`, `(OC-4; dump 443995 / 444228)`, `(OC-6; dump 445481-445487)` etc.

`§ B` (`:162`) is the **v2.0.26** section. Its own round-47 errata (`:164-168`) says so and redirects the reader:
> "this subsection describes the v2.0.26 binary, which is no longer on the host. … the live opencode classes are in § B′."

So the note's locator points a reader at the superseded model for the very evidence (counts, dump lines) it promises. This is the round-47 C1 locator that the assignment's own claim summary calls "§ B′"; the code still says "§ B".

#### M5 — `:363-364` — "the retired v2.0.26 rule set survives **only** as the must-fail generation fixture" is false inside the verifier's own fixture directory

`verifiers/verify_surfaces.py:363-364`:
```
# retired v2.0.26 rule set survives only as the must-fail generation fixture
# `fixtures/surfaces/strings-opencode-v2.0.26.txt`.
```

The v2.0.26 rule set is still described verbatim in four fixture baselines that the same self-test drives:
- `verifiers/fixtures/surfaces/baseline-clean.json:2`
- `verifiers/fixtures/surfaces/baseline-excluded-noreason.json:2`
- `verifiers/fixtures/surfaces/baseline-rekind-doc.json:2`
- `verifiers/fixtures/surfaces/baseline-rekind-partial.json:2`

all ending:
> "Round 18: opencode half re-derived for the v2.0.26 rule set (OC-1..OC-6 over ConfigInstructionPlugin/ReadTool/API anchors)."

But those fixtures now carry the **1.19.3** ids — I dumped `baseline-clean.json`: `opencode:instructions/{AGENTS,CLAUDE,CONTEXT}.md`, `opencode:config/instructions`, `opencode:config/instructions-remote`, `opencode:read-hook/instructions`, `opencode:instruction-context/AGENTS.md` — and the v2.0.26 rule set owned `opencode:api-entries/instructions` (round-18 code, `git show 02302c5:verifiers/verify_surfaces.py:426`), which is not present. The fixture prose therefore contradicts the fixture content it describes.

(The `must-fail` half of the claim does hold: `verifiers/verify_surfaces.py:1056-1063` drives `strings-opencode-v2.0.26.txt` and asserts exit 1 + `OC-1 (owns`; my run of `--self-test` confirms it — 0 failures / 99 assertions, exit 0.)

#### M6 — `:36-39` — the DOCUMENTED LIMITS bullet enumerates the wrong baseline kinds for the loaders it names

`verifiers/verify_surfaces.py:36-39`:
```
   - loaders that are not ``(group, literal)``-shaped calls (e.g. opencode's
     ``InstructionContext.observe`` up-walk and ``instructions`` config array)
     are invisible to the extractor — baseline ``loader-config``/``prompt-text``
     entries cover them by declaration only;
```

The two named loaders are covered by **loader-literal** entries, not `loader-config`/`prompt-text`:
- `opencode:instruction-context/AGENTS.md` (the `InstructionContext.observe` up-walk) — `verifiers/surfaces-baseline.json`: `context_kind: "loader-literal"`, `verdict: "governed"`.
- `opencode:instructions/{AGENTS,CLAUDE,CONTEXT}.md` (the name-priority array) — also `loader-literal`.

`prompt-text` appears in no opencode baseline entry at all (all 9 opencode entries are `loader-literal` ×5 and `loader-config` ×4). The docstring's own `loader-literal` paragraph at `:61-67` defines the kind correctly; the LIMITS bullet just never learned that the round-47 re-derivation re-kinded the priority-array ids.

#### M7 — `:32-35` — the DOCUMENTED LIMITS bullet names two **non-existent** class ids and mis-states the verdict of the third

`verifiers/verify_surfaces.py:32-35`:
```
   - only ``.md``-suffixed registrations are extracted; non-``.md`` discovery
     registrations the dump actually contains (``omp:cursor/rules``,
     ``omp:gemini/settings.json``, ``omp:vscode/mcp.json``, …) are outside the
     set and must be declared by hand in the census as excluded;
```

- `omp:gemini/settings.json` — **0** occurrences in `corpus/knowledge/instruction-surface-census-round13.md` and **0** in `verifiers/surfaces-baseline.json`. The real ids are `omp:discovery/settings` and `omp:discovery/mcp-configs` (both `loader-config`, `verdict: "excluded"`).
- `omp:vscode/mcp.json` — likewise **0**/0. Not a class id.
- `omp:cursor/rules` — a real id, but `verdict: "governed"`, not excluded (`verifiers/surfaces-baseline.json`; census § A row at `corpus/knowledge/instruction-surface-census-round13.md:88`). Under the corpus's technical sense of "excluded" (`verdict: "excluded"` with a reason, cf. the census § C table), the sentence's "must be declared by hand in the census as **excluded**" is false for the very first example it names.

(The `settings.json` / `mcp.json` *literals* do exist in the omp dump — 41 and 69 occurrences — so the bullet's underlying point about non-`.md` discovery registrations is sound; only the class ids and the verdict are wrong.)

#### M8 — `:100` — the quoted extractor in the `opencode_extract` description is not the code's opencode extractor

`verifiers/verify_surfaces.py:100`:
```
   ``no_uncovered_class``'s ``(Id|Cl|jD[ef])(<v>, <group>, "<file>.md")``
```
The opencode pattern is `CALL_RE` (`:151-155`): `(Id|Cl|jD[ef]|Tl|dr|GW)` — five alternatives, not three. `CALLEE_SHAPES["opencode"]` (`:163`) carries the correct five. The *conclusion* the sentence draws ("finds nothing there by construction") is **true** — measured 0 hits on 1.19.3 — but it is reached via a regex that no longer exists in the file. `Tl|dr|GW` were added to the omp list on 2026-10-14 and into `CALL_RE` with them, and the docstring was never updated.

---

### LOW

#### L1 — `:49-53` and `:55-59` — the "A class id is …" paragraph is duplicated verbatim

```
49|A class id is ``<harness>:<group-or-kind>/<literal-or-key>``; each baseline
50|entry declares ``class_id``, ``harness``, ``literal``, ``context_kind``
51|(``loader-group`` | ``loader-config`` | ``loader-literal`` | ``prompt-text`` | ``template-list`` |
52|``doc``), ``verdict`` (``governed`` | ``excluded``), and — for excluded entries
53|only — ``reason``.
54|
55|A class id is ``<harness>:<group-or-kind>/<literal-or-key>``; each baseline
56|entry declares ``class_id``, ``harness``, ``literal``, ``context_kind``
57|(``loader-group`` | ``loader-config`` | ``loader-literal`` | ``prompt-text`` |
58|``template-list`` | ``doc``), ``verdict`` (``governed`` | ``excluded``), and —
59|for excluded entries only — ``reason``.
```
Five lines duplicated back-to-back (the `|`-wrapping differs only by where the line breaks land). Cosmetic, but it is dead weight in the file the lane's own contract says must stay maintainable.

#### L2 — `:68-107` — the documented check list omits `surfaces.no_uncovered_class`

The docstring documents six check ids: `surfaces.literal_present` (`:69`), `surfaces.table_parity` (`:75`), `surfaces.excluded_reason` (`:81`), `surfaces.literal_parity` (`:84`), `surfaces.kind_parity` (`:94`), `surfaces.opencode_extract` (`:98`).

`CHECK_IDS` (`:175-183`) has **seven** — the missing one is `surfaces.no_uncovered_class` (`:177`). It is a real, independently-runnable check with its own guard arms (vacuity at `:636-643`, extractor-blindness at `:644-655`, kind-laundering at `:656-665`); it is only *mentioned* in passing inside the `opencode_extract` description at `:100`. Repro (exit 0):
```
$ python3 -B verifiers/verify_surfaces.py --check surfaces.no_uncovered_class \
    --omp-strings <omp> --opencode-strings <oc> \
    --baseline verifiers/surfaces-baseline.json --inventory corpus/knowledge/instruction-surface-census-round13.md
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
exit=0
```

#### L3 — `:165-166` — the `ASSIGN_RE` comment's example identifiers are gone from the substrate

```
165|# Identifier -> string bindings anywhere in the dump (`var Pqr = "agents-md"`,
166|# second declarators like `, Zou = "AGENTS.md"`, plain `X = "..."`).
```
`var Pqr` → 0 occurrences and `, Zou = "AGENTS.md"` → 0 occurrences in `omp-18.12.5.strings`. The *mechanism* the comment describes is real and still works (`f$`/`m$` resolve fine), but the named examples are round-13-era. Fold into M1's fix.

---

## Claims I attacked that **HOLD** (findings in their own right — they survived)

Recording these because the contract asks for it: a claim that survives the attack is also a finding.

| claim | where | verdict |
|---|---|---|
| Every OC comment's quoted dump line number | `:366` (OC-1, dump 443993), `:374` (OC-2, 443993), `:384` (OC-3, 443993), `:403` (OC-5, 443993), `:421-424` (OC-4, 443995 / 444228), `:410-412` (OC-6, 445481-445487) | **HOLD.** Independently re-located in the frozen dump: `fn("Instruction.resolve")` → 443995; `fn("ReadTool.execute")` → 444228; `Key.make("core/instructions")` → 445481; `InstructionContext.observe` and `targets:["AGENTS.md"]` → 445482; `system-context-builtins` → 445487; the priority array, both `.join(...config/home...)`, `for(let O of T.instructions)` and both `globUp(...)` → all on 443993. |
| Every OC comment's quoted code snippet | `:367` `y=["AGENTS.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]`; `:375` `X.join(r.config,"AGENTS.md")` / `X.join(r.home,".claude","CLAUDE.md")`; `:386` `for(let O of T.instructions){if(O.startsWith("https://")…`; `:389` `(T.instructions??[]).filter((q)=>q.startsWith("https://")||q.startsWith("http://"))`; `:404-406` the `OPENCODE_DISABLE_PROJECT_CONFIG` / `globUp` switch; `:413` `jX(L.config,"AGENTS.md")` | **HOLD** — every one reproduced byte-exact by regex against `opencode-1.19.3.strings`. |
| "`<system-reminder>` alone is a generic token (18 hits on 1.19.3)" | `:425-426` | **HOLD** — 18 occurrences (`grep -o -F | wc -l`), on 15 distinct lines. (An occurrence count, not a line count — correct as written.) |
| "the round-14 pattern also matched a's loop (2 hits on 1.19.3)" | `:391-392` | **HOLD** — the round-14 regex `\.instructions.{0,40}?startsWith\("https://"\).{0,40}?startsWith\("http://"\)` (from `git show 29c17be:verifiers/verify_surfaces.py`) matches **2** times on 1.19.3, once on OC-3a's `for(let O of T.instructions)` loop and once on the real `.filter(`; the tightened round-47 regex (`:396-399`) matches **1**. |
| The six v2.0.26 anchors occur 0 times on 1.19.3 | `:357-360` | **HOLD** — `ConfigInstructionPlugin` 0, `ReadTool.Plugin` 0, `SessionInstructions` 0, `session.instructions.entry.put` 0, `j5(r.config` 0, `InstructionDiscovery` 0. |
| The generation note's sha `179ca421…` and "npm opencode-ai 1.19.3" | `:355-356` | **HOLD** — `SHA256SUMS` line `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9  bin/opencode-1.19.3`; `sha256sum -c` exit 0. |
| "the retired v2.0.26 rule set … must-fail generation fixture" (the *must-fail* half) | `:363-364`, `:1056-1063` | **HOLD** — the self-test asserts exit 1 and `"OC-1 (owns"` on `strings-opencode-v2.0.26.txt`, and my `--self-test` run (0 failures / 99 assertions) exercises it. |
| The `loader-literal` examples | `:64-66` | **PARTIALLY HOLD** — the *class ids* and *literals* are correct against `verifiers/surfaces-baseline.json`: `omp:cursor/rules` literal `rules` kind `loader-literal` ✓, `opencode:read-hook/instructions` literal `<system-reminder>` ✓. Only the quoted shape `Cl(e,"cursor","rules")` is stale (0 occurrences in 18.12.5 — folded into M1). |
| "Probed like ``loader-config``: literal must occur in the dump; no call-shape requirement" | `:66-67` | **HOLD** — `check_literal_present` (`:563-591`) applies the call-shape requirement only to `loader-group` (`:580-587`). |
| `surfaces.literal_present` / `table_parity` / `excluded_reason` / `literal_parity` / `kind_parity` / `opencode_extract` descriptions | `:69-107` | **HOLD** as behaviour descriptions — I traced each against its implementation (`check_literal_present` `:563-591`, `check_table_parity` `:658-678`, `check_excluded_reason` `:801-820`, `check_literal_parity` `:680-725`, `check_kind_parity` `:763-798`, `check_opencode_extract` `:727-761`) and the self-test's own assertions; the only defects are the ones listed above (rule count, extractor regex, omitted check id). |
| `CONTEXT.md` occurs once in the 1.19.3 dump (census § B′) | census `:251` | **HOLD** — `grep -o -F 'CONTEXT.md' \| wc -l` → 1. |

---

## Residual risk

1. **The docstring is the only place a reader learns the rule count and the exit-code contract.** The code is correct on both counts; the prose is what a downstream consumer (a caller, a re-derivation lane, an auditor) would copy. H1 and H2 are therefore calibration defects in the artifact that the round-47 lane itself claims to have re-derived.
2. **H2 is a live behavioural defect, not only prose.** `verifiers/verify_surfaces.py:242-243` raises `EnvError` where `main` (`:1163-1170`) only catches `BaselineError`. Any future caller that adds a `--baseline` on a network/permission-restricted path gets exit 1 + a traceback instead of the documented exit 2 + a JSON error payload. It is a one-line fix (catch `EnvError` alongside `BaselineError` at `:1165`) and it would also let `--json` emit `{"error": ...}`.
3. **M1's stale examples are load-bearing for a future re-pin.** The docstring's example block is what a minification bump would be re-derived *against*; leaving the 2026-09-28 shapes there while the allowlist has moved three generations invites the next bump to be re-pinned against shapes the binary no longer contains — exactly the failure mode the allowlist comment at `:140-141` ("the callee name is minification-volatile — the FIRST thing to re-pin on a binary bump") warns about.
4. **M4/M5 show the round-47 append-only errata discipline was applied to the census but not to the verifier's own locator and fixture prose.** Both are append-only-fixable without touching the code.
5. **Scope boundary:** the census § A evidence column (`corpus/knowledge/instruction-surface-census-round13.md:73-80`) and the four fixture-baseline `$comment`s carry the same stale generation as M1/M5. I did not modify them (other lanes own them) but flag them for the integrator: fixing the verifier's prose alone would leave the two artifacts telling different stories about the same substrate.

---

## Verification gaps — what I did **NOT** check

- **I did not re-derive the census rows themselves** (literals, kinds, verdicts, reasons, the § A/§ B′/§ C table contents) against the dumps beyond the specific rows I cite above; a full census re-derivation is not my lane.
- **I did not verify omp 18.12.2 / 18.11.1 / 18.12.0 dumps** — only 18.12.5 and 1.19.3 are frozen. The generation dates asserted at `:142-144` (2026-09-28 / 2026-10-14 / 2026-10-16 18.11.1 / 2026-10-18 18.12.2) are therefore **unverifiable** here and are reported as neither confirmed nor refuted. I only established that on 18.12.5 the callees `Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo` still *exist as identifiers* in the binary (6–1465 occurrences each) but contribute **zero** `.md` registration-call shapes — all 11 come from `lq`/`Xl`/`Fo`.
- **I did not check the runtime behaviour of either harness** (no omp session, no opencode run, no `~/.local/bin/opencode` invocation) — out of contract and out of lane.
- **I did not verify `verifiers/check_substrate_pins.py`, `verifiers/baseline.json`'s pins, `verify_skill_checklist.py`, or the fault harness** — other lanes own those; my scope was the surfaces verifier's prose.
- **I did not audit the census § "Honest ceiling" or § "Superseded class rows and the round-47 opencode ledger"** (`:287-322`) for prose accuracy, nor `corpus/knowledge/opencode-extraction-round14.md`.
- **I did not mutate the verifier** to prove each prose defect is *observable* by a caller — the defects are prose-level by construction, so I demonstrated each by direct measurement (occurrence counts, exit codes, rule reports) rather than by mutation. The only mutation-style checks I ran were the two exit-code repros (H2), which required no source change.
- **The `strings` tool version is whatever the host provides**; I used the frozen `.strings` dumps rather than re-running `strings -n 4`, so my counts are the frozen artefacts' counts, not a fresh re-derivation from the binaries. The frozen dumps' digests match `SHA256SUMS` (exit 0, 4/4 OK), so they are the pinned bytes.
- I did **not** check `verifiers/fixtures/surfaces/inventory-*.md` or the other 32 fixture files' prose, nor the `--repo` default-path resolution (`DEFAULT_REPO = Path(__file__).resolve().parent.parent`, `:122`) against the lane's canonical layout.
