verdict: PARTIAL — corpus/knowledge's present-tense substrate layer is partly falsified at 7ad7fad: the live § A evidence/method still describes the 2026-09-28 omp bundle (`jDe`/`Id`/`Cl`; `Tl|dr|GW` in the errata), and two indexed host-fact files still assert removed paths, a moved byte offset and a dead sqlite recipe; § B′, the class set, and both gates hold.

# W2KnowledgeStale — present-tense substrate claims vs round-47 substrate

Swept: `corpus/knowledge/*.md` at `7ad7fad` — 34 files (6430 newline-terminated lines). Method: token sweep
(`~/.opencode`, `.opencode/bin`, `pi_natives`, `2.0.26`, `1.19`, `18.12`, callee names
`Id|Cl|jDe|jDf|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo|lq|Xl|Fo`, `sha256|pin`, `<skills>|available_skills`),
then read only the 7 files with substrate hits plus the tokens' surrounding sections; the
other 27 files have no present-tense substrate claim in the swept token classes.
Only **one** knowledge file changed in round 47 (`git diff --stat c61a973b..7ad7fad -- corpus/knowledge`
→ `instruction-surface-census-round13.md` +88/−5); the findings below outside the census were untouched.

Classification rule applied (stated so it can be attacked): a claim is **dated** when its
section names a source date/round and describes that epoch ("Sourced 2026-09-28 (round 8)",
"Binaries (2026-09-28)", "Falsifiers, run on the landed tree (2026-09-28)"), and a reader is told
so; a claim is **present-tense** when it cites an unversioned live path, sits in the live
inventory/craft tables the skill cites as authority, or asserts equality with a live repo file,
with no epoch marker on the claim. Findings below are present-tense claims whose test now fails.

Substrate used (all read-only; no opencode execution):
`/fast/scratch/kotoba-r47/shared/bin/omp-18.12.5` sha256 `fdbc8136…` = live `/home/vgpnk/.local/bin/omp`
and `…/opencode-1.19.3` sha256 `179ca421…` = live npx ELF (both `sha256sum`, exit 0);
`omp --version` → `omp/18.12.5`.

---

## K1 [HIGH] census § A — the live inventory's evidence and method describe the 2026-09-28 bundle; one cited callee is now a different function

`corpus/knowledge/instruction-surface-census-round13.md`

- `:12-14` (round-18 errata) — "**§ A stays live** — the same `.md` registration shapes persist
  under renamed callees (`Id|Cl|jD[ef]` → `Tl|dr|GW`, allowlist re-pinned in the verifier)".
  Test: on `bin/omp-18.12.5`, registration shapes for `Tl`, `dr`, `GW` are **0**, as they are for
  `Id`, `Cl`, `jDe`, `jDf`, `Co`, `Dl`, `Hj`, `I5`, `Gl`, `Mo`. Only `lq` (2 ident-group),
  `Xl` (5 quoted-group) and `Fo` (4 quoted-group) produce `(<v>, <group>, "<file>.md")` shapes.
  The verifier's own comment records the full lineage it has absorbed
  (`verifiers/verify_surfaces.py:142-144`: `Co/Dl/Hj` 2026-10-16, `I5/Gl/Mo` 2026-10-18,
  `lq/Xl/Fo` 2026-10-21). The census's "renamed callees" statement is three renames stale.
- `:73-80` — all eight machine-extracted rows' **evidence cells** cite shapes with 0 occurrences
  in the live binary (exact-substring, `python3` over the frozen bytes):
  `jDe(e,Pqr` 0, `jDe(e,BWr` 0, `Id(e,"opencode","AGENTS.md")` 0, `Cl(e,"gemini","GEMINI.md")` 0,
  `Id(e,"gemini","system.md")` 0, `Cl(e,"gemini","SYSTEM_TEMPLATE.md")` 0,
  `Cl(e,"github","copilot-instructions.md")` 0, `Id(e,"windsurf","memories/global_rules.md")` 0.
  Live replacements (1 each, quoted from the bytes):
  `lq(u, f$, "AGENTS.md")`, `lq(u, m$, "CLAUDE.md")`, `Xl(u, "gemini", "GEMINI.md")`,
  `Fo(u, "gemini", "GEMINI.md")`, `Xl(u, "gemini", "system.md")`,
  `Xl(u, "gemini", "SYSTEM_TEMPLATE.md")`, `Fo(u, "github", "copilot-instructions.md")`,
  `Xl(u, "windsurf", "memories/global_rules.md")`. The group bindings also moved: live is
  `var f$ = "agents-md"` / `var m$ = "claude-md"`; `Pqr`/`BWr` no longer name groups.
- **False witness:** `jDe` still exists in 18.12.5, but as an unrelated function —
  `function jDe(e, t, g, B = $9) { const s = NA(g); …` (string/template formatter, called by
  `qDe` and `terminal.write`). A reader grepping the census's `jDe(e,Pqr,"AGENTS.md")` today finds
  a formatter, not a loader — the exact failure mode the verifier comment calls
  "minification-volatile … the FIRST thing to re-pin on a binary bump".
- `:47` — Method 1's documented reproducible command, callee set `(Id|Cl|jDe|jDf|n4|o4|CTt)`,
  returns **0 registration pairs** on the live binary. The table presents this as *the*
  extraction command with no round-47 replacement.
- `:92` — `omp:omp-dir/RULES.md` row: "literal 6 hits in the omp bytes" → live count **4**.
- `:360` — "`Id/Cl/jDe` prove file discovery" → all three are 0 registration shapes at 18.12.5
  (the argument is callee-agnostic, so the *claim* survives; the *proof tokens* do not).
- `:365` — extraction ceiling "group names passed as variables other than the two resolved
  (`Pqr`, `BWr`)" → live group variables are `f$`/`m$`; the named pair no longer exists.
- `:439` (round-22 byte-preserved block) — AGENTS.md craft row cites
  ``jDe(e,Pqr,"AGENTS.md")`` as live loader code. Lower severity: the block has a provenance
  note (`:409-413`) and a round-24 erratum, but the erratum corrects only the "seven" count, not
  the callee.

Disclosure that bounds this finding: the census already says the `evidence` column has **no
machine counterpart** (`:402-406`), and the gate proves id/literal/kind parity (7/7 PASS). So K1
is *disclosed-unchecked prose gone wrong*, not a hole in the checked set. Round 47 re-pinned the
allowlist in code and gave the opencode side a § B′ errata, but appended no omp-side errata; under
the file's own append-only-errata convention that omission is the gap.

Repro (frozen bytes, exit 0):
```
cd /fast/scratch/kotoba-r47/shared
python3 -c 'd=open("bin/omp-18.12.5","rb").read();
[print(s, d.count(s)) for s in (b"jDe(e,Pqr", b"Id(e,\"opencode\",\"AGENTS.md\")", b"lq(u, f$, \"AGENTS.md\")", b"Xl(u, \"opencode\", \"AGENTS.md\")")]'
→ b'jDe(e,Pqr' 0 · b'Id(e,"opencode","AGENTS.md")' 0 · b'lq(u, f$, "AGENTS.md")' 1 · b'Xl(u, "opencode", "AGENTS.md")' 1
```

## K2 [MED] claude-md-surface — dead binary path and two wrong counts, presented as current host evidence

`corpus/knowledge/claude-md-surface.md:8-11` — "**Loader exists in both harnesses.** …
`~/.opencode/bin/opencode` → 9 occurrences, `~/.local/bin/omp` → 17; `AGENTS.md` 30/35
respectively, `CONTEXT.md` 1. So CLAUDE.md is a *recognized* rules-file name on this host."

- `ls -la ~/.opencode/bin` → **exit 2** ("No such file or directory"); the census itself records
  the removal (`instruction-surface-census-round13.md:218`, "removed 2026-10-20").
- Same method (`grep -oa` on the binaries), current bytes: `CLAUDE.md` omp **15** (not 17),
  opencode **9**; `AGENTS.md` omp **37** (not 35), opencode **30**; `CONTEXT.md` omp **0**,
  opencode **1**.
- The *substance* survives: CLAUDE.md is still a loader class in both live harnesses
  (`lq(u, m$, "CLAUDE.md")` in omp; `y[1]` + `disableClaudeCodePrompt` in 1.19.3).
- Method defect: this is the reference-count proof the census expressly adjudicated away
  (`instruction-surface-census-round13.md:333-340` — "a reference count cannot separate a loader
  from prompt text"). The file is the census's own 7th-class companion and README row 18; it
  keeps a ROUND-7 DRIFT note for the file inventory (`:20-23`) but none for its loader evidence.

## K3 [MED] skill-activation-telemetry — stale byte offset in the omp ELF, plus the removed opencode path

`corpus/knowledge/skill-activation-telemetry.md:17-21` — "The template is embedded plaintext in
the omp ELF (`~/.local/bin/omp`, byte offset 283082932, found via `grep -abo '<skills>'`) …
Not found in `~/.opencode/bin/opencode` or `pi_natives` — the prompt is omp's."

- `grep -abo '<skills>' bin/omp-18.12.5` → **253192800** (claim 283082932; Δ 29,890,132 B).
- Template bytes themselves still present at 253192750:
  `<skills>\n{{#each skills}}\n- {{name}}: {{description}}\n{{/each}}\n</skills>` and the
  directive `` you MUST read `skill://<name>` before proceeding `` immediately precedes it — so the mechanism
  claim holds; only the offset (and the dead opencode path) is wrong. Offsets are exactly what
  the census bans as anchors (`instruction-surface-census-round13.md:59-62`).
- The substantive negative holds: `grep -oa '<skills>' bin/opencode-1.19.3` → **0**.

## K4 [MED] skill-activation-telemetry — the per-call activation recipe no longer runs; the live db has no `part` table

`corpus/knowledge/skill-activation-telemetry.md:52-56,69-71` — "Primary store:
`~/.local/share/opencode/opencode.db` … Per-call activation = `part` rows where
`json_extract(data,'$.tool')='skill'` … Query recipe (read-only): `sqlite3 -readonly opencode.db
"select … from part where …"`."

- `sqlite3 -readonly ~/.local/share/opencode/opencode.db ".tables"` (exit 0) → `session_v2`,
  `instruction_blob`, `instruction_entry`, `instruction_state`, `session_message`, … — **no
  `part`, no `message`**.
- `sqlite3 -readonly … "select count(*) from part"` → **exit 1**, `no such table: part`.
- `:74` — "**Loader collisions**: 1898 `duplicate skill name` WARNs in opencode.log" → the live
  log is 922,614 B (mtime 2026-10-20 07:52) with **0** occurrences of that literal; the 9.49 MB
  log the round-8/9 counts came from is gone.
- README row 16 carries a round-27 note that the `part` table is gone from opencode v2.x
  (`corpus/README.md:16`); the knowledge file itself carries no such note, and README row 77
  points readers here for per-render attribution. The histogram table (`:61-66`) *is* windowed
  ("2026-08-28 → 2026-09-28") and is fine; the recipe above it is not.

## K5 [MED] opencode-extraction-round14 — the errata's "current rule set" pointer is the v2.0.26 set that 1.19.3 falsified

`corpus/knowledge/opencode-extraction-round14.md:3-11` — the round-18 append-only errata says:
"The current rule set — OC-1…OC-6 over `ConfigInstructionPlugin.projectSource`, `ReadTool.Plugin`,
the API-managed instruction entries and an env-gate — is the round-18 re-derivation recorded in
`instruction-surface-census-round13.md` § B (errata block)."

- On the 1.19.3 dump: `ConfigInstructionPlugin` **0**, `ReadTool.Plugin` **0**,
  `SessionInstructions` **0**, `session.instructions.entry.put` **0**; § B itself now opens with
  "this subsection describes the v2.0.26 binary, **which is no longer on the host**"
  (`instruction-surface-census-round13.md:164-167`) and points to § B′.
- So the one sentence in this file that states what is *current* names a dead model and a dead
  section. The file is README row 39 ("opencode extraction rules") and is cited by the preserved
  SKILL.md block (`instruction-surface-census-round13.md:427-429`) as the rule-set/falsifier
  reference. Its *body* is correctly historical; the top errata link is not.
- The later `:94` "Falsifiers, run on the landed tree (2026-09-28)" row `7/7 PASS, exit 0` still
  reproduces (`verify_surfaces.py` 7/7, exit 0), so that row is not stale.

## K6 [LOW, pre-existing] opencode-extraction-round14 — a live-file equality that is false

`corpus/knowledge/opencode-extraction-round14.md:96-97` — "Binary `sha256 f9dab322…` (equal to
`verifiers/baseline.json` `measured_against.opencode_binary_sha256`)". At HEAD the pin is
`179ca421…` (`verifiers/baseline.json:9`). The section header dates the run (2026-09-28), and the
falsification predates round 47 (the pin moved at round 18); round 47 re-pinned and kept the
equality false. Not introduced here; recorded so the next reader does not use it as provenance.

## K7 [LOW, precision] harness-verifier-round10 — the vacuity holds; its stated cause is no longer the cause

`corpus/knowledge/harness-verifier-round10.md:215-219` — "6 of the 11 opencode-side checks are
vacuous on this host — the v2.0.26 log grammar no longer prints `init count=` /
`evaluated permission=skill` / `duplicate skill name`, so those counters read 0".

- Present-tense effect holds: before-battery `init_count_max=0  skill_perm=0/0`; live log 0/0/0.
- Causal attribution does not: the live 1.19.3 dump contains **0** `init count=`, **0**
  `evaluated permission=skill` and **1** `duplicate skill name`, i.e. the missing grammar is not a
  v2.0.26-era property that a channel change would reverse; and one of the three literals still
  exists. A reader diagnosing a future green would look for a v2 regression that is not there.

## K8 [LOW] substrate-pin-guard-round23 — cited script digest and self-test count are stale

`corpus/knowledge/substrate-pin-guard-round23.md:11-12` — "`verifiers/check_substrate_pins.py`
(round 23 …; file sha256 `fafe88d881eb…`) enforces them"; `:34` — "`--self-test` → `0 failure(s)
over 51 assertions`".

- `sha256sum verifiers/check_substrate_pins.py` → `9615d547…`, and `--self-test` → `0 failure(s)
  over 62 assertions`, exit 0. Round 47 changed the file (default opencode path move,
  `git diff c61a973b..7ad7fad -- verifiers/check_substrate_pins.py`), and appended no note.
- This is a round-23 landing record, so the counts are legitimately dated; the digest is the
  problem: it is attached to a present-tense mechanism sentence, and the doc's own rule
  (`:66-68`) is that a moved substrate is re-recorded with a mechanism note. The baseline itself
  did get one — `verifiers/baseline.json` `round47_note` records the pin move, the channel move
  and `lq/Xl/Fo` — so the discipline held where the gate reads and lapsed where only prose reads.

## K9 [LOW] instruction-surface-remeasure-round13 — reproduction counts no longer reproduce (dated record; do not cite as current)

`corpus/knowledge/instruction-surface-remeasure-round13.md:15` — "the L1 reproduced the
load-bearing literals by an independent byte scan (`omp` `RULES.md` 6 hits, `enabledProviders` 4,
`disabledProviders` 21 …)". At 18.12.5: RULES.md **4**, `enabledProviders` **3**,
`disabledProviders` **23**. The file is round-13-scoped, so this is a dated record; it is listed
because the same `RULES.md 6` count is repeated in the *live* inventory row at
`instruction-surface-census-round13.md:92` (K1).

---

## Dated records checked and correctly scoped (not findings)

- `instruction-surface-census-round13.md:53-57` (binaries 2026-09-28), `:162-207` (§ B v2.0.26 with
  the round-47 errata), `:287-303` (superseded rows moved outside `## Class inventory`).
- `opencode-offer-trace-round8.md:3-8` (names opencode ELF, size, mtime, BuildID, db versions).
- `harness-independent-round37.md:66` (join-driver digest `bb8dcecd…`, superseded by the round-41
  erratum on the next line; HEAD digest `778b367e…`).
- `harness-independent-round41-census.md`, `claim-census-round12.md`, `cold-run-round11.md`,
  `render-mechanism-round7.md`, `harness-router-models-round9.md`,
  `harness-system-prompt.md` (epoch-scoped or observed-not-owned; swept tokens found no
  present-tense live-path/version claim that fails).
- `substrate-pin-guard-round23.md:32-33` ("live: … OK 3/3 pins hold, omp mtime delta 0 ns") —
  landing record; reproduces today (3/3, delta 0 ns, exit 0).

## Claims that survived the attack (findings too, not padding)

- **§ B′ (census `:212-321`) is accurate on the frozen 1.19.3 bytes**, anchor for anchor:
  `y=["AGENTS.md",` 1, `globUp(T,d.directory,d.worktree)` 1,
  `!t.disableClaudeCodePrompt?["CLAUDE.md"]:[]` 1, `"CONTEXT.md"]` 1,
  `n=[X.join(r.config,"AGENTS.md")` 1, `X.join(r.home,".claude","CLAUDE.md")` 1,
  `for(let O of T.instructions)` 1, https filter 1, `{concurrency:4}` 1,
  `fn("Instruction.resolve")` 1, `fn("ReadTool.execute")` 1,
  `while(G.startsWith(N)&&G!==N)` 1, `InstructionContext.observe` 1, `system-context-builtins` 1,
  `instructions:{entry:{list:` 1, `var n="1.19.3"` 1; and all seven retired anchors 0
  (`ConfigInstructionPlugin`, `ReadTool.Plugin`, `SessionInstructions`,
  `session.instructions.entry.put`, `j5(r.config,…)`, `InstructionDiscovery`, `2.0.26`).
- **Channel/path claims**: `~/.opencode/bin` absent (exit 2); the `~/.local/bin/opencode` wrapper is
  the 1460 B npx launcher for `opencode-ai` (read, not executed); the resolved ELF hash equals the
  frozen copy. Census `:214-219` holds.
- **Gates at 7ad7fad**: `verify_surfaces.py` 7/7 PASS exit 0 (42 ids, 8/8 omp classes, 9/9
  opencode classes from 7/7 rules); `check_substrate_pins.py` 3/3 exit 0, mtime delta 0 ns.
- **Round-47 pin discipline where it is machine-read**: `verifiers/baseline.json` gained a
  `round47_note` naming the pin move, the removed channel and `lq/Xl/Fo`.

## What I did NOT check

- Host-log/session counts in `skill-activation-telemetry.md` (`32` http-400 captures, `3837`
  session records, `5609` jsonl, histograms) — host state, not round-47 substrate; not re-derived.
- § A2 provider priorities and § A3 wire probe (explicitly single-lane/unconfirmed in the file).
- `instruction-surface-remeasure-round13.md:63` (`.opencode/AGENTS.md` "no read path"): live bytes
  show only user-scope `Xl(u,"opencode","AGENTS.md")` and no `Fo(…,"opencode",…)` project
  registration — [INFERENCE] support, not proof.
- `corpus/README.md` rows 16/31/33/76 (outside the assigned `corpus/knowledge` set), even though
  row 16's round-27 note and row 76's round-47 freshness row carry adjacent version claims.
- C2 (`trigger.no_xml_tag`, SKILL.md description) and C3 (LOG erratum, corpus index,
  corpus-baseline, fault harness) — peers' lanes.
- Did not execute opencode or any omp session; did not read `~/.omp/logs` or session jsonl.
