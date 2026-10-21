verdict: PARTIAL — 1.19.3's version literal, byte identity and round-14 loader generation hold on the frozen dump and on the published npm tarball; but the supporting "different channel / not on this registry" story is falsified: v2.0.26 IS on npm as `@opencode/cli(-linux-x64)@2.0.26` (exact sha `d9123b9b…`), and the live 2.x head 2.1.2 still carries the v2.0.26 instruction model.

# Scope
Attack of C1's opencode half at 7ad7fadfc09354b74fb66605dfb0c1182c115a2f (BASE c61a973b): the claim that npm `opencode-ai` 1.19.3 is "a different channel, not v2.0.26's successor", specifically the checks the ticket names — `var n="1.19.3"`, absence of `2.0.26` and of the six v2.0.26 anchors, npm metadata for `opencode-ai`, and whether any 2.x is on npm under another package. Working clone: `/fast/scratch/kotoba-r47/w2/W2OcLineage-2/kotoba-shokunin` (canonical layout, clean `git status`, HEAD 7ad7fad). Frozen snapshot digests verified first.

## 1. What survives the attack (observed, not inferred)

### 1.1 The frozen bytes and the dump are the npm 1.19.3 artifact
- `cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS` → **exit 0**, 4/4 OK (`bin/opencode-1.19.3` = `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`).
- `strings -n 4 bin/opencode-1.19.3 | sha256sum` → `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3` = the frozen dump's sha (SHA256SUMS line 4), **exit 0**. The dump is exactly `strings -n 4` of the binary, not hand-assembled.
- Downloaded the published platform tarball `https://registry.npmjs.org/opencode-linux-x64/-/opencode-linux-x64-1.19.3.tgz` (60,356,012 B; sha512 matches `dist.integrity` `sha512-wz+kXi7ZkvLW…`): `package/bin/opencode` sha256 = `179ca421…`, **exit 0**. The frozen binary is byte-identical to the published npm artifact.
- The `opencode-ai@1.19.3` npm metadata (`npm view opencode-ai@1.19.3 --json`, exit 0) is version 1.19.3, bin `opencode` → `bin/opencode.exe`; its tarball (3,046 B, integrity matches) contains a 479-byte "postinstall not run" shim at that path; `postinstall.mjs` links the real ELF from `opencode-linux-x64@1.19.3` into it. On the host both paths are the same inode (43795736, link count 2; 186,013,824 B), which is why the census path is true of the host.

### 1.2 Version self-report
- `grep -c 'var n="1\.19\.3"' opencode-1.19.3.strings` → **1**; dump line **447186** is `var n="1.19.3",t="latest",l=!1;` — a version+channel constant chunk (`export{n as vA,t as wA,l as xA}`).
- Same literal in the binary at byte offset 105,438,847, count 1 (mmap search).
- Corroborating: dump line 749118 carries `--user-agent=opencode/1.19.3`. The npm package version is also 1.19.3.
- **No execution** was used: `~/.local/bin/opencode` was read, never run.

### 1.3 `2.0.26` absent; six v2.0.26 anchors absent
- `grep -c '2\.0\.26' opencode-1.19.3.strings` → **0** (grep exit 1); same count 0 in `bin/opencode-1.19.3` (grep -a, exit 1).
- Six anchors, counted in dump and binary with `grep -c -F`:
  `ConfigInstructionPlugin` 0, `ReadTool.Plugin` 0, `SessionInstructions` 0, `session.instructions.entry.put` 0, `j5(r.config,` 0, `InstructionDiscovery` 0 — in **both** the dump and the binary.
- Positive controls on real artifacts, not the fixture: the real 2.0.26 npm binary (tarball proven in §2.1) has `ConfigInstructionPlugin` 2, `ReadTool.Plugin` 2, `SessionInstructions` 3, `session.instructions.entry.put` 4, `j5(r.config,` 1, `InstructionDiscovery` 3, and zero round-14 anchors (`["AGENTS.md",` 0, `disableClaudeCodePrompt` 0, `CONTEXT.md` 0, `Instruction.resolve` 0, `InstructionContext.observe` 0).
- Round-14 anchors present in 1.19.3 (dump counts): `y=["AGENTS.md"` 1 (line 443993, the census's cited line — verified inside that huge line at byte 10,893,160), `.join(r.config,"AGENTS.md")` 1, `.join(r.home,".claude","CLAUDE.md")` 1, `disableClaudeCodePrompt` 2, `CONTEXT.md` 1, `Instruction.resolve` 1, `InstructionContext.observe` 1, `system-context-builtins` 1, `@opencode/Instruction` 1. The "round-14 loader lineage" half of C1 is correct.

### 1.4 The generation separation is real on real binaries (stronger than the committed fixture)
`verifiers/fixtures/surfaces/strings-opencode-v2.0.26.txt:1-3` labels itself synthetic and contains only anchor shapes (5 of the 6 v2.0.26 anchors; `InstructionDiscovery` is not in it), so the committed `oc-gen` test (`verifiers/verify_surfaces.py:1056-1063`) is a fixture test. I ran the same 1.19.3 rules against the actual published binaries:
- `python3 -B verifiers/verify_surfaces.py --opencode-binary /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe --json` → **exit 0, 7/7**.
- `... --opencode-binary /tmp/oc1/package/bin/opencode` (published `opencode-linux-x64@1.19.3`) → **exit 0, 7/7**, detail `9/9 declared class(es) from 7/7 rules`.
- `... --opencode-binary /tmp/oc2/package/bin/opencode` (real `@opencode/cli-linux-x64@2.0.26`) → **exit 1, pass 5/fail 2**: `FAIL surfaces.opencode_extract | vacuity: extraction produced 0 class(es) from 7 rule(s)…`.
- `... --opencode-binary /tmp/oc212/package/bin/opencode` (`@opencode/cli-linux-x64@2.1.2`) → **exit 1, pass 5/fail 2**, same vacuity.

So the substantive line "1.19.3's rules do not accept v2.0.26 bytes" is true and now proven on the real artifact, not just the synthetic fixture.

### 1.5 The default-resolution gate values
- `python3 -B verifiers/verify_surfaces.py --json` (default paths; live `~/.local/bin/omp` + npx-cache opencode) → **exit 0, pass 7 / fail 0** (`surfaces.opencode_extract`: "9/9 declared class(es) from 7/7 rules").
- `python3 -B verifiers/check_substrate_pins.py` → **exit 0, OK 3/3 pins hold** (opencode sha `179ca421…`).
- Before values are consistent with the missing old path: `ls /home/vgpnk/.opencode/bin/` → **exit 2**, and `.ufo/waves/round-47/before/SUMMARY.md:3-5` records surfaces exit 2 / pins exit 2 DRIFT 3/3.

## 2. Counterexamples (the channel claim)

### 2.1 v2.0.26 IS on npm — exact byte match
`.ufo/waves/round-47/build/KnowSubstrateRecensus.md:26` states: *"the round-18 `2.0.26` line is not on this registry"*. That is false. `@opencode/cli` is an npm package whose 2.0.26 release contains the exact round-18 binary:
- `npm view '@opencode/cli' versions --json` → 1,226 versions, **`2.0.26` present**, latest `2.1.2`; no 1.x versions at all.
- `npm view '@opencode/cli@2.0.26'` (exit 0): repository `git+https://github.com/anomalyco/opencode.git`; bin `opencode`/`opencode2`; optionalDependencies `@opencode/cli-linux-x64: 2.0.26`; publish time `2026-10-08T19:43:12.373Z` (six days **before** round 18's 2026-10-14 re-census).
- `curl https://registry.npmjs.org/@opencode/cli-linux-x64/-/cli-linux-x64-2.0.26.tgz` (97,566,348 B; sha512 matches `dist.integrity` `sha512-UIA2/1Ik8HaN54…`) → `package/bin/opencode` sha256 = **`d9123b9bcdb0a31f7ab9fe9812b58a9dc1768ad6d97e7b276dff1181813218c9`**, exactly the full round-18 sha recorded at `corpus/knowledge/instruction-surface-census-round13.md:23`.
- `npm view opencode-ai@2.0.26 version` → **exit 1**, `E404` — true only for the `opencode-ai` package, not "this registry".
- Same maintainer on both lines: `npm view opencode-ai maintainers --json` and `npm view '@opencode/cli' maintainers --json` both return `thdxr <d@ironbay.co>`.

Consequence: `KnowSubstrateRecensus.md:50`'s `[INFERENCE] the 2.x binary came from a different channel (the ~/.opencode/bin installer path)` is refuted. `~/.opencode/bin` is an install **location**; the bytes are the published npm package's bin (`@opencode/cli-linux-x64@2.0.26`). Both the 1.x and 2.x lines are npm packages using the same wrapper/postinstall/platform-binary pattern (`@opencode/cli@2.0.26` has the same 229-byte shim + `postinstall.mjs` shape as `opencode-ai@1.19.3`). "Different distribution channel" is true only as "different npm package line", which is not what the report's registry inference says.

Production wording is imprecise rather than false on this point: `corpus/knowledge/instruction-surface-census-round13.md:217-219` ("different distribution channel from v2.0.26 (`~/.opencode/bin`, removed 2026-10-20), not its successor"), `corpus/SOURCES.md:28` ("the opencode path moved channel (2.0.26 → npm 1.19.3)"), and `verifiers/verify_surfaces.py:355-357` ("opencode moved channel … a different lineage") are all defensible if "channel" means package line, but none says both lines are npm; the only explicit registry claim is the build report's, and it is false.

### 2.2 The "retired / superseded" verdicts are host-scoped but written as universal — and the 2.x line is live
`corpus/knowledge/instruction-surface-census-round13.md:287` heads the moved rows **"Superseded class rows"**, and the ledger at :310-313 marks three ids **"retired"** solely from counts on the 1.19.3 dump. `verifiers/verify_surfaces.py:363-364` says the *"retired v2.0.26 rule set survives only as the must-fail generation fixture"*. Against the current 2.x head:
- `npm view '@opencode/cli' dist-tags.latest` → **`2.1.2`**, published `2026-10-21T03:39:33.353Z` (≈13 h before the after battery at `2026-10-21T13:46:38-03:00`, i.e. `16:46Z`).
- `@opencode/cli-linux-x64@2.1.2` tarball (99,002,353 B; integrity matches) `package/bin/opencode` sha256 `cf5841e6666aeb469abec8b39ca494cef07a637756454a34a742b2f4996e1675`; endpoint UA `opencode/latest/2.1.2/cli`.
- Anchor counts in that binary: `ConfigInstructionPlugin` 2 (including `ConfigInstructionPlugin.{read,globalSource,projectSource,match,configuredSource}`), `ReadTool.Plugin` 2, `SessionInstructions` 3, `session.instructions.entry.put` 4, `InstructionDiscovery` 3, and — inside `ConfigInstructionPlugin.projectSource` — `yield*r.up({targets:["AGENTS.md"],start:T,stop:C,type:"file"})` plus the global `r.resolve(nx(l.config,"AGENTS.md"))`. (`j5(r.config,` is 0 because the helper was re-minified to `nx`; the semantic shape survives.)
- Zero round-14 anchors in 2.1.2 (`disableClaudeCodePrompt`, `CONTEXT.md`, `Instruction.resolve`, `InstructionContext.observe` all 0), so this is the same generation as 2.0.26, not a v1 build.

So the three "retired" ids are retired **only on the host's 1.x line**; they are live in the project's current release. § B's errata prose is host-scoped ("no longer on the host", census:164-166), but the heading, the ledger's unqualified "retired", and the verifier's "survives only as the must-fail fixture" are not — a craft reader can't tell that the v2.0.26 model is still the upstream model. This is a calibration defect, not a byte/test failure: the 1.19.3 gate is correct for the host, and our exit-1 runs above show the 1.19.3 rule set would loudly reject either 2.x binary if the host moved.

### 2.3 Minor: substrate citation names the wrapper package's path as the ELF
`corpus/knowledge/instruction-surface-census-round13.md:214-215` cites `.../opencode-ai/bin/opencode.exe` sha `179ca421…`. That is true **on this host** (postinstall hardlinked the platform ELF into the wrapper), but in the published `opencode-ai@1.19.3` tarball that path is the 479-byte error shim; the artifact with sha `179ca421…` is `opencode-linux-x64@1.19.3` (`package/bin/opencode`). The pin is on the right bytes; only the package attribution is conflated. Also, `opencode-ai` carries no `repository`/`homepage` metadata at 1.19.3, so npm metadata alone cannot tie the 1.x line to `sst/opencode` (the round-8 doc's upstream citation); `@opencode/cli` does carry `github.com/anomalyco/opencode`.

## 3. Reproduction (all in /tmp; nothing copied into the repo)
```
cd /fast/scratch/kotoba-r47/shared
sha256sum -c SHA256SUMS                                   # exit 0, 4/4 OK
strings -n 4 bin/opencode-1.19.3 | sha256sum              # f4d8f34a… == dump
grep -c 'var n="1\.19\.3"' opencode-1.19.3.strings        # 1 (line 447186)
grep -c '2\.0\.26' opencode-1.19.3.strings                # 0 (exit 1)

cd /tmp && mkdir -p oc2 && cd oc2
curl -sSL -o v2.tgz https://registry.npmjs.org/@opencode/cli-linux-x64/-/cli-linux-x64-2.0.26.tgz
tar -xzf v2.tgz && sha256sum package/bin/opencode          # d9123b9b… (round-18 sha)
curl -sSL -o v212.tgz https://registry.npmjs.org/@opencode/cli-linux-x64/-/cli-linux-x64-2.1.2.tgz
# same for opencode-linux-x64@1.19.3 → package/bin/opencode = 179ca421…

npm view opencode-ai versions --json        # 12,253 versions, 2.x = []
npm view opencode-ai@2.0.26 version         # exit 1, E404 (opencode-ai only)
npm view @opencode/cli versions --json      # 1,226, 2.0.26 present, latest 2.1.2
npm view @opencode/cli@2.0.26 --json        # repo anomalyco/opencode, 2.0.26
npm view @opencode/cli time.2.0.26          # 2026-10-08T19:43:12Z
npm view @opencode/cli time.2.1.2           # 2026-10-21T03:39:33Z

cd <clone>
python3 -B verifiers/verify_surfaces.py --json                                   # exit 0, 7/7
python3 -B verifiers/check_substrate_pins.py                                     # exit 0, 3/3
python3 -B verifiers/verify_surfaces.py --opencode-binary /tmp/oc1/package/bin/opencode --json  # exit 0, 7/7
python3 -B verifiers/verify_surfaces.py --opencode-binary /tmp/oc2/package/bin/opencode --json  # exit 1, 0 classes/7 rules
python3 -B verifiers/verify_surfaces.py --opencode-binary /tmp/oc212/package/bin/opencode --json # exit 1, 0 classes/7 rules
```
Tarball integrity was checked against `dist.integrity` for all four downloads (`opencode-ai@1.19.3`, `opencode-linux-x64@1.19.3`, `@opencode/cli-linux-x64@2.0.26`, `@opencode/cli-linux-x64@2.1.2`) — **all match** (sha512).

## 4. Adjacent observation (outside the lineage claim, disclosed)
`.ufo/waves/round-47/after/SUMMARY.md:8` (untracked in the fleet root; `git ls-files .ufo/waves/round-47/after` at 7ad7fad is empty) records `harness claims exit=1`. Its output shows 7 DRIFTs, including an opencode-side row `oc.roots.names_plus_builtin: observed=11 expected=7` — the host skill-root population grew after the round-47 pin. This is not part of C1's "surfaces 7/7 + pins 3/3" claim, which reproduces, but the after battery as a whole is not all-green.

## 5. What I did NOT check
- No opencode binary was executed, including the frozen snapshots and the 2.0.26/2.1.2 tarball binaries; all version/anchor claims are static (strings/byte search). Runtime loader firing remains undecided.
- No GitHub release artifacts or installer-script internals were fetched; the channel finding is npm-registry-only.
- No sigstore/provenance verification beyond npm `dist.integrity` (sha512) and the maintainer field.
- Other platforms' package hashes (`darwin`, `windows`, `musl`, `baseline`) were not downloaded; only linux-x64.
- The host's removal history of `~/.opencode` was not reconstructed; only current absence (`ls` exit 2) and the round-18/census records were used.
- I did not re-run the C2/C3 gates (checklist, corpus integrity/independent, fault harness) or the full harness gate; only the two C1 gates in my lane plus the binary-level probes above.
- No tools were installed or upgraded; `curl`/`npm pack` downloads went to `/tmp` only.

## 6. Bottom line
The falsifiable core of the ticket holds: `var n="1.19.3"` (once), no `2.0.26` in the dump or binary, all six v2.0.26 anchors absent in both, `opencode-ai` has no 2.x in its published metadata (12,253 versions; no unpublish markers), and the 1.19.3 rules accept the published 1.19.3 ELF while rejecting the real 2.0.26 and 2.1.2 ELFs. What breaks is the **reason given for "different channel"**: v2.0.26 is an npm artifact (`@opencode/cli-linux-x64@2.0.26`, sha `d9123b9b…`), both lines share the maintainer and the same wrapper/platform-binary packaging, and the 2.x line is alive at 2.1.2 today with the v2.0.26 instruction model intact. The production wording should say "different npm package line (`opencode-ai` 1.x vs `@opencode/cli` 2.x), not the successor of 2.0.26", and the "retired/superseded" verdicts need a host-scope qualifier plus a note that the 2.x model remains upstream.
