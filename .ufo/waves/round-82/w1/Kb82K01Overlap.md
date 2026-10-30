# Kb82K01 — host ELF drift × scoped loader extraction: the re-pin boundary (round 82, w1)

Axes: freshness (C1), operability (C2). Seat kind: connector/boundary scan with live host measurement. This is not the C1 counter run, not a claim score, and not a production after-value: every measurement below is a read-only extraction recon on the live host binaries, authorized as control/recon evidence. Base named by assignment: `47dbe8781657de563ff867caca6244d28e3db504`; lane HEAD at measurement `006a834cee43` (one committed round-82 freeze commit; `git diff --stat 47dbe878..HEAD -- verifiers/ corpus/` is empty, so the instruments and baseline I exercised are the base instruments; working tree additionally carries an uncommitted sibling edit to `corpus/SOURCES.md`, read as data only).

## 1. Host ELF drift, measured (freshness substrate)

| fact | value | command-owned evidence |
|---|---|---|
| installed omp | `/home/vgpnk/.local/bin/omp`, ELF 64-bit x86-64, **not stripped**, BuildID `588d7307f333…` | `file`, exit 0 |
| version | `omp/18.14.0` | `--version`, exit 0 |
| sha256 | `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f` | `sha256sum`, exit 0 |
| size / mtime | 276,244,656 B / 2026-10-29 23:19:46.168359786 −03:00 | `stat`, exit 0; matches sibling receipt `receipts/host-open.json` (mtime_ns 1793326786168359786) |
| `omp.real` | **absent** | `ls`, exit 2 |
| strings dump | 47,434,077 B, sha256 `81277d35…` (1.1 s) | `strings -n 4`, exit 0 |
| opencode dump | sha256 `020fb253…` — **byte-identical** to `verifiers/census-removals.json` `measured_against.dump_sha256` | `strings -n 4`, exit 0 |
| embedded changelog | window 18.13.0 (2026-10-26) … 18.14.0 (2026-10-29) present in the binary | awk extract, exit 0 |

Drift shape: round 72 re-pinned by *path* (`omp` → shell wrapper → `omp.real`, bytes identical to the round-51 pin `85d9daf3…` v18.12.6). The wrapper and `omp.real` are now **both gone**, replaced by a new ELF lineage (18.12.6 → 18.14.0, skipping 18.13.x in pin terms but embedding those releases' changes). The `before-pins.txt` receipt records the consequence: omp sha256/mtime rows UNREADABLE, 1 PASS / 2 UNREADABLE, exit 2. The opencode half of the substrate did not move: its dump hash equals the round-72 ledger measurement, so the opencode pin (`ca9b3ee2…`) and the three removal-ledger anchors are anchored to unchanged bytes.

## 2. Scoped loader extraction under the drift, measured

Ran the **unchanged** round-72 `verifiers/verify_surfaces.py` against the 18.14.0 dump + live opencode dump (`--omp-strings`/`--opencode-strings` fixture hooks only; receipt 13):

- **7/7 checks PASS** on the new binary: `literal_present` (39 loader-kind entries), `no_uncovered_class` (all 8 extracted omp loader classes declared), `opencode_extract` 6/6 (+3 ledgered removals, 7/7 OC rules), table/literal/kind parity 42 ids, excluded_reason 8/8.
- Extraction comparison via the verifier's own `extract_classes` (receipt 14, payload `build/Kb82K01Overlap-extraction.json`):

| | 18.12.6 (fixture `strings-omp-18.12.6.txt`) | 18.14.0 (live dump) |
|---|---|---|
| extracted (group, file) pairs | 8 | **same 8** |
| admitted callees (round-52 declared-admission rule) | Ho (4 calls), Kl (5) | **Ac (5), ts (4)** — rotated again |
| ident-group calls | 2 | 2 |
| module markers `^//…\.[jt]sx?$` | 8 (trimmed fixture) | 3,261 |
| `@bun` chunk markers | 0 (fixture) | 3,147 |
| historical allowlist `OMP_CALL_RE` extraction | — | **0 pairs** |

Three consequences, all bounded:

1. **The callee names rotated a seventh time** (Id/Cl → Tl/dr/GW → Co/Dl/Hj → I5/Gl/Mo → lq/Xl/Fo → Kl/Ho/bq → **Ac/ts**). The round-52 callee-rename-robust rule absorbs this: extraction is unchanged. The round-72 docstring already named callee rotation as "the FIRST thing to re-pin on a binary bump" — for an *allowlist* extractor. On the current rule the rotation is a non-event for extraction, and remains an event **only** for the pins (sha256/mtime/default path).
2. **A naive historical-allowlist re-pin would silently extract nothing** on 18.14.0 (0 pairs measured; the self-test vacuity guard catches it, but only because the guard exists). The round-52 declared-admission rule is what makes the unchanged 7/7 meaningful; this is a method robustness fact, not a claim enlargement.
3. **The module-scope substrate survives** (3,261 source-path comment lines, 3,147 `@bun` chunk separators): the round-51 scoped-resolution rule keeps its input. The documented residual stands — the source-path comment is a *proxy* for a variable scope, not a proof of one (round-51 falsify `CriticC1Landed`, carried in the instrument docstring).

## 3. Corpus limitations the drift touches (freshness ↔ corpus connection)

The census's own documented LIMITs (`verify_surfaces.py` docstring) are: only `.md`-suffixed registration calls are extracted; non-`(group, literal)`-shaped loaders are invisible; **"a compiled-in call shape proves the loader path exists in the binary, not that it fires at runtime or reaches a prompt."** The 18.12.6→18.14.0 drift window ships four concrete instances of those limits:

1. **`--no-context-files`** (18.13.0): start a session *without* `AGENTS.md`/`CLAUDE.md` — a runtime switch that suppresses loader firing. Static extraction cannot see it; the governed literals stay in the dump regardless.
2. **task-subagent `AGENTS.md` fix** (18.13.1): "Fixed task subagents receiving `AGENTS.md` files, including the user-level `~/.omp/agent/AGENTS.md`, when the session has additional workspace roots" — *dispatch semantics* of a governed literal changed while the literal and call shape are byte-stable.
3. **Custom tool loaders breaking change** (18.14.0): "constructors take cwd as their first argument instead of a pi namespace." Tool loaders are outside the census surface entirely (the census covers *instruction* surfaces); a behavioral breaking change in the same drift is invisible to the counter by construction.
4. **`task.file=true`** (18.14.0): "subagent instructions … loaded from an absolute UTF-8 file path or local:// URL with the submitted path and SHA-256 recorded" — a new instruction-ingestion path whose targets are user-supplied arbitrary paths, not enumerable literals. The dump shows `task.file` ×5, `local://` ×90, "subagent instructions" ×3 (receipt 15). No census row can or should declare it: it is exactly the "loaders that are not (group, literal)-shaped calls are invisible" class, now with a live instance.
5. **`managed-skills` symlink guard fix** (18.13.3): behavior around an already-excluded class (`omp:unknown/managed-skills`) changed; exclusion rows carry a reason, not a behavioral contract, so no pin moves — correctly.

The corpus knowledge layer already encodes the same boundary shape: `corpus/knowledge/resident-index-and-rungs-round72.md` (round-72) states of its three vendor sources: "**No page says a client refuses a mis-runged instruction, and no client's loading behaviour was observed.**" The re-pin claim inherits that honesty: presence/parity, not behavior.

## 4. Does the re-pin claim overreach runtime behavior? — No, if the plan's own bound is kept

The plan (round-82.md §C1) already bounds the claim: "host-bound extraction/parity and pin freshness, **not proof of exhaustive runtime discovery or prompt effectiveness**." Measured against the drift, that bound is exactly right, and the drift shows why it must not be widened:

- **IN the claim** (supported by the unchanged counter + this recon): sha256/mtime freshness of the installed omp; default-path repair (`omp.real` → `omp`); set parity of loader-call shapes and instruction literals between the pinned baseline and the live dump (same 8 pairs, 39 loader-kind literals present); opencode dump identity with the ledger's measured bytes; removal-ledger anchors absent from the live opencode dump; module-scope resolution parity (proxy-based, fail-loud).
- **OUT of the claim** (nothing in the counter measures these): whether any loader fires — the 18.13.0/18.13.1 changelog entries prove firing semantics moved while statics stood still; whether instruction bytes reach a prompt; the new `task.file` ingestion path; tool-loader constructor semantics (18.14.0 breaking); anything requiring executing the binary; "exhaustive runtime discovery" in any form.

**Exact boundary sentence**: the re-pin claim certifies that *the bytes now installed at `~/.local/bin/omp` contain the same declared loader-call shapes and instruction literals the census governs, in a dump whose extraction the unchanged round-72 rules validate (7/7), and names those bytes (sha256/mtime) — and certifies nothing about whether, when, or to what prompt any of those loaders deliver.* A stronger sentence overreaches; a weaker one is unnecessary (the 7/7 on unchanged instruments is measured, receipt 13).

## 5. Does it overreach the kaidoku method? — No; the methods agree on the boundary

The sibling kaidoku lane (domain: "reverse engineering of shipped artifacts with REA on this Linux host") states the same epistemic boundary for static reads of binaries: `SKILL.md:1504` "**The bit does not prove execution**" (of an IMAGE_SCN_MEM_EXECUTE range); `SKILL.md:1545` "**Error patterns are local-reader findings, not host-loader verdicts**"; its gate registry runs a 3-valued ladder where "2 is never a pass" and could-not-evaluate is "never native judgment" (`:596`, `:819`). Kotoba's counter is the same method family applied to Bun bundles: printable-run extraction, declared-pair admission, fail-closed unevaluable classes, a frozen removal ledger judged against the live bytes. The kaidoku c1 census (scope-table locus census over its own records) and kotoba's substrate census answer different questions, but neither converts a static read into a runtime verdict, and the round-82 re-pin claim does not ask the kaidoku method to do so. No overreach — *provided* the S251 knowledge entry (sibling draft `Kb82S02Source-S251-draft.md`, present and read) keeps its own pending-anchor discipline: derivation receipt, located quote, and measured revision before admission, which the draft already states.

## 6. Where a re-pin claim WOULD overreach (failure modes to keep named)

1. Reporting `pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3` as *behavioral* freshness ("the new omp loads instructions the same way") — contradicted in-window by 18.13.0/18.13.1/18.14.0 changelog entries.
2. Claiming the census is *complete* over the new binary — non-`.md` discovery, `task.file`, and tool loaders are documented-invisible; `no_uncovered_class` is set parity over the declared extraction, never existential completeness (docstring, verbatim).
3. Claiming callee stability — measured rotation to Ac/ts falsifies it; only the round-52 rule makes this harmless.
4. Silent ledger widening: the plan's "never silently delete a census class" applies in reverse — the new in-window surfaces (task.file, --no-context-files) must not be quietly added as governed classes to make the census look drift-complete; they are outside the extractor's set by design.
5. C2-adjacent: the hermetic selftest repair must not remap the failing governance arm to green or reduce N below 1863; the live `governance.citation_resolves` red (before receipt: `1 failure(s) over 1863 assertions`, exit 1, reading live SCORECARD) is debt that must stay nameable while the fixture arm goes isolated. That is the same boundary shape: fixture/parity evidence, never live-corpus cleanliness.

## 7. Absorbed / changed

- Absorbed from siblings or shokuknow: nothing.
- Lane files changed: none by this seat. Writes: this report, `build/Kb82K01Overlap-surfaces-18140.json`, `build/Kb82K01Overlap-extraction.json`, `build/Kb82K01Overlap-receipts.txt`.
- Tools installed or upgraded: none (none needed; no pacman).
- Scratch: `/fast/scratch/hyaku/kotoba-r82/Kb82K01Overlap/` — dumps and changelog extract deleted on exit after receipt copy; TMPDIR respected.
- Dependencies on absent peers: none required; sibling files I read (`Kb82S02Source-S251-draft.md`, `receipts/host-open.json`) were present. Live peers' C1 re-derivation receipts were not polled and are not assumed.

VERDICT: Host ELF drift is real and bounded: `omp.real` and its wrapper are gone; the installed omp is a new ELF lineage (18.14.0, sha256 e7dd2b60…, 2026-10-29 23:19:46.168359786 −03:00) whose strings dump the UNCHANGED round-72 extraction rules validate 7/7, with the same 8 loader pairs and callee names rotated a seventh time (Ac/ts) — absorbed by the round-52 declared-admission rule; the opencode half is byte-stable (dump sha256 equals the round-72 ledger measurement). The re-pin claim does NOT overreach runtime behavior or the kaidoku method as long as it stays the plan's own sentence: extraction/parity + pin freshness on named bytes, never firing, delivery, or exhaustive discovery; the exact boundary is stated in §4, and the drift window's own changelog (--no-context-files 18.13.0, task-subagent AGENTS.md fix 18.13.1, tool-loader breaking change and task.file ingestion 18.14.0) supplies four live proofs of why the boundary must hold. Corpus limitation connection: all four entries are instances of the census's three documented invisibilities (non-.md registrations, non-call-shaped loaders, presence-not-firing).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82K01Overlap.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82K01Overlap-surfaces-18140.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82K01Overlap-extraction.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82K01Overlap-receipts.txt
