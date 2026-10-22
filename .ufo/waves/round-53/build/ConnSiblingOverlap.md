Result: DONE — The committed-scope scan finds one direct shared always-on file, three distinct omp binary consumers, and one bounded evidence-only proposal; ownership disputes remain unresolved.

# Scope and evidence basis

Assignment: round-53 §3 sibling-overlap scan, judged on adjacency. This is a connector report, not an admission, gate verdict, integration, or ownership ruling.

- Read `plans/round-53.md` first. C1 is the opencode 1.19.4 extraction/re-pin claim (`:22-36`); C2 executes only `alwayson.04` and `alwayson.07` on the frozen cases (`:38-54`). Their counting cases/tables remain frozen at `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`.
- Pinned every sibling below at its local committed HEAD at **2026-10-22T20:04:55Z**. Read/search scope is each commit's `PROVINCE.md`, `SKILL.md`, and `corpus/README.md`; the three absent skills are explicitly recorded. Worktree edits are not substituted for committed scope.
- Snapshot commands, with Git environment overrides removed: `git -C /home/vgpnk/Projects/shokunin/<lane>-shokunin rev-parse HEAD` and `git -C /home/vgpnk/Projects/shokunin/<lane>-shokunin archive --format=tar --output=/fast/scratch/hyaku/kotoba-r53/ConnSiblingOverlap/scope-<lane>.tar <commit> -- PROVINCE.md SKILL.md corpus/README.md`. Omit `SKILL.md` only for the absent cases. **Every rev-parse and archive exited 0**; rev-parse stdout is the commit column; archive stdout/stderr were empty.
- Local source locators are `file:///home/vgpnk/Projects/shokunin/<lane>-shokunin/<path>` **at the recorded commit**, not HTTP sources. HTTP status: **not applicable**; no external URL was fetched. Snapshot byte counts/digests are in the appendix. Quoted locations below are original member-file line numbers at those commits, not tar offsets. Every quote is at most 25 words.
- The immutable read copies are `/fast/scratch/hyaku/kotoba-r53/ConnSiblingOverlap/{scope,detail}-<lane>.tar:<member>`. Detail archives use the same sibling commits, captured **2026-10-22T20:06:41Z**. No live global AGENTS file, installed client binary, credential source, or client session was read or executed.

## Committed scope inventory

In this table, “no named target overlap” means none located in the three searched scope surfaces, not proof about every file in a sibling repository.

| Sibling | Commit read | Bounded finding |
|---|---|---|
| audio | `7a2fcd4f08831154686e4e323031f41fffdb077f` | No named target overlap; SKILL absent. |
| chousa | `6c5eb1466f2b8abbd3de576389037f435016d07b` | Research method; client/route mentions, not a target binary pin. |
| game-dev-2d | `7753d49b16674e122ed134403e7a9b301f2cbf7e` | No named target overlap; SKILL absent. |
| game-dev-3d | `89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080` | No named target overlap. |
| kagi | `899c50b42634a3a4ad0b28ab7509786315e2fc2b` | Shared global AGENTS shape pin; opencode config/state; binary pin explicitly excluded. |
| kaidoku | `dbd87cfa09eb89306c4e07d3171a4556eb732024` | Broad shipped-artifact RE; REA client registrations, not a named omp/opencode binary parser. |
| kake | `b1752a2480aa86fc27536dd6e7d27a91b52bed12` | No named target overlap. |
| kama | `1560e4d83f42b04f40336357de6f9637eafa0f4b` | omp fallback declaration read by endpoint-consumer resolver. |
| kasegi | `1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a` | Historical routing/provider policy; not a target binary parser. |
| kengaku | `1f3b0f1ec41ec297130e8944ff97968d32324632` | Historical opencode request-envelope measurements; not a binary pin. |
| kotodama | `662239d2c8fcb9a2b7f9ac297ca2283f36397c14` | opencode appears in historical report directory names only. |
| kumitate | `a0a07bae9236311314f12e3cec8d3666049d0dbc` | omp launch attestation; Kimi skill/agent discovery; prompt craft routed to kotoba. |
| lore | `380ef3abc7c7af11d7f23e9f9c82bb1937e1f695` | No named target overlap. |
| mado | `8e5d93691e2f7baa3d4a0a61c9428e5acb5d2122` | Omarchy SKILL pin and own AGENTS obligation; OMP transcript reader, not binary parser. |
| mori | `69349c2a874438e070ea5e1cc74b18f5f68fafcf` | Installed omp byte-pattern parser and digest receipt for background-job capacity. |
| revenger | `876630dbb4d630e016d7d8c32a19ea04c646cbae` | Broad shipped-artifact RE; SKILL absent; no named target parser. |
| souji | `4edb25dfe262515d0da63224bbba71e02e36cba5` | Duplicate-config/removal-receipt boundary, not an always-on authoring gate. |
| tabi | `e3cf4e0d30bb835532ff44b118c5ad52e09eb76d` | No named target overlap. |
| tameshi | `367ec0f1d79cb9b67d724f2962e7554a0841b1fc` | Verification method and sibling-gate mutation work, not target product ownership. |
| tsukuroi | `3c94d7308e561832a0df0981cbc39dda270e32d8` | Own AGENTS obligations; OS/package state, not named omp/opencode binary parsing. |

Absence evidence: `git -C <lane-repo> cat-file -e <recorded-commit>:SKILL.md` for **audio, game-dev-2d, revenger** each exited **128**, stdout empty, stderr `fatal: path 'SKILL.md' does not exist in '<recorded-commit>'`.

# Surface 1 — always-on instruction files

**Direct same-file overlap: kagi.** Its scope explicitly names `$HOME/.agents/AGENTS.md`. No sibling scope file in this sweep names a CLAUDE.md authoring/canonical-name gate. The named neighbours below must nevertheless remain distinct from C2.

| Sibling and surface | Sibling's own words and location | Would C2 duplicate or contradict its gate? |
|---|---|---|
| **kagi — global `~/.agents/AGENTS.md`** | “kagi pins its bytes; kotoba owns the checklist/shape reading” — `kagi-shokunin/corpus/README.md:97`. Its actual policy says “pinned by **mode + line count only**” — `SKILL.md:224`. | **Not duplicate predicates.** Kagi checks stored shape/link integrity; C2 checks dated/transient content and root rule-file/redirect topology. Different findings can coexist. Its private-file no-hash policy must not be replaced with a shared content digest. |
| **tsukuroi — its own AGENTS obligations** | “**Secrets shape-only**” — `tsukuroi-shokunin/SKILL.md:169`, citing `AGENTS.md:4-5`; `:182` identifies AGENTS evidence/read-only/secrets obligations. | **No matching C2 gate located.** This is consumption of local instructions, not a check for dates or canonical filenames. A C2 finding grants no package, unit, or host repair authority (`PROVINCE.md:25-28`). |
| **mado — Omarchy SKILL and own AGENTS obligation** | “The omarchy skill (`~/.agents/skills/omarchy/`) is documentation surface,” — `mado-shokunin/PROVINCE.md:10`; “read-only.” — `:11`. `SKILL.md:909-910` pins the skill leaf and link topology; `:990` cites its own AGENTS LOG obligation. | **Adjacent class, not C2 duplication.** A SKILL.md documentation-byte pin is not an AGENTS.md/CLAUDE.md authoring check. Expanding C2 to mado's skill bytes would be an additional claim, not the frozen C2. |
| **kumitate — prompt/agent/skill runtime** | “Prompt and skill craft → kotoba.” — `kumitate-shokunin/PROVINCE.md:27`. Its Kimi skill-resolution inventory is `corpus/README.md:70-74`. | **No same authoring gate located.** Runtime discovery/dispatch and Kimi member enumeration do not test the two C2 boxes. `SKILL.md:577` uses “always-on” for root enumeration, not an instruction-file checklist. |
| **souji — duplicate configurations and removal receipts** | “duplicate configs, stale generated” — `souji-shokunin/PROVINCE.md:12`; “F3 duplicate verdicts — byte-identical copies” — `:69`; “class would be a taxonomy change (operator decision).” — `:70`. | **No duplicate check located for C2's predicates.** A canonical-name FAIL is not a duplicate-removal receipt. Souji's deletion certification is OFF (`SKILL.md:13-17`); C2 cannot be used to delete or quarantine either instruction file. |
| **tameshi — verification-fixture method** | “every lane's gate remains its own” — `tameshi-shokunin/PROVINCE.md:14`; “owns only the reusable craft” — `:15`. | **Complementary, not a second product gate.** It can review the discriminating method without taking over the always-on rule. A mutation kill is sensitivity evidence, not product-policy truth (`SKILL.md:879-881`). |

## Important contradiction: “pins bytes” is not this file's implemented pin

Kagi's `corpus/README.md:97` and kotoba's carried `PROVINCE.md:46` say kagi pins the file's bytes. At kagi's recorded commit:

- `corpus/drift-baseline.tsv:14` is `$HOME/.agents/AGENTS.md<TAB>600<TAB>75<TAB>-`.
- `corpus/drift-pins.sh:70-77` includes that path in `NOHASH`; `:93-101` computes mode/line count without a hash for no-hash files; `:143-156` requires the stored sha to be `-` and compares those fields.
- `SKILL.md:224-228` explicitly admits that content drift is invisible under this policy.

**Contradiction stated, not resolved:** “pins its bytes” overstates the implemented AGENTS content guarantee. This is not evidence that the live file currently has mode 600 or 75 lines: those are the committed expected values. [INFERENCE] A same-line-count date insertion could change C2's answer without changing kagi's shape answer. That would not be two gates contradicting the same proposition.

There is a second topology distinction: kagi rejects a symlink at its pinned **AGENTS.md** path (`drift-pins.sh:130-132`). C2's frozen PASS is a **CLAUDE.md → AGENTS.md** symlink (`check_alwayson_boxes.py:82`). These are different paths and are **not a demonstrated gate conflict**. Turning the pinned AGENTS file itself into a link is not authorized by that PASS case.

C2 also deliberately accepts an import redirect with additional Claude-specific rules (`check_alwayson_boxes.py:79-81`); “one canonical rule-file name” must not be reported as byte identity or as a claim that every client loads exactly the same full rule stack.

# Surface 2 — substrate pins and opencode/omp binaries

**Named omp binary consumers: kumitate, kama, mori.** They attest or inspect different things. No named sibling **opencode executable-byte pin/parser** was located in the searched scope files. Kagi explicitly excludes the historical opencode executable; its opencode configuration/state gates are not executable pins.

| Sibling | Own words and evidence at its commit | Relationship to kotoba C1/C2 |
|---|---|---|
| **kumitate — omp launch identity** | “ATTESTED binary” — `kumitate-shokunin/SKILL.md:233`; “host attestation = realpath'd+sha256'd omp binary,” — `corpus/knowledge/native-trial-launch.md:108`. | Records the identity of the binary a launcher spawns; not kotoba's loader extraction or C2 authoring predicate. `PROVINCE.md:19` keeps the OMP harness contract on its frontier. Its docs note explicitly says “its implementation was not inspected” (`corpus/knowledge/omp-task-contract.md:205`); the dated omp/18.12.3 observation is not a current claim about 18.12.6. No launch was run here. |
| **kama — omp builtin endpoint fallback** | “`~/.local/bin/omp` carries a builtin llama-cpp fallback of 8080” — `kama-shokunin/SKILL.md:117`; “The registry row attests that fallback shape only.” — `:118`. | Actual binary **text-pattern reader**, not a whole-binary hash baseline: `registry/endpoint-consumers.tsv:35` targets `~/.local/bin/omp` with `grep:LLAMA_CPP_BASE_URL`; `tools/kama-probe.sh:640-650` reads the match. A bare env-symbol match is `inherited`, and its declaration may be reused (`SKILL.md:117-120`, registry `:35`). A C1 pin does not establish the environment-selected endpoint, endpoint health, or model identity. C2 does not test any of these. |
| **mori — omp background-job capacity** | “located by pattern over” — `mori-shokunin/PROVINCE.md:298`; “no DRIFT verdict, no baseline re-pin.” — `:316`. | Actual installed-binary **byte-pattern parser**, plus a digest in its receipt. `tools/mori-job-runway.py:113-117` declares clamp/default patterns; `:474-486` evaluates them and emits `binary_sha256`; `:616-620` resolves the real path of omp on PATH. C1's hash/mtime gate and loader rules neither duplicate nor certify this resource-cap interpretation. Mori reports a cap, never current job count (`PROVINCE.md:307-313`), and leaves mechanism semantics to kumitate (`:335-344`). C2 is unrelated. |
| **kagi — opencode config/state, executable exclusion** | “are not lane-owned bytes” — `kagi-shokunin/SKILL.md:233`, referring to package-managed host binaries including `~/.opencode/bin/opencode`. | Its pins cover the handler's opencode overlay/config/agent/plugin and runtime shape (`PROVINCE.md:22-34`), not the executable. That historical path is also not kotoba C1's npm-cache `opencode.exe` (`check_substrate_pins.py:40-46,64-67`). Config custody cannot substitute for executable identity. |
| **tsukuroi — OS/package provenance** | “state and” / “health*, not internals” — `tsukuroi-shokunin/PROVINCE.md:26-27` (the emphasis spans the line break). | Its declared package/boot scope is adjacent to how software reached the host, not a named omp/opencode loader parser. No exact executable pin was located in its three scope files. A successful C1 re-pin is not host update clearance. |
| **kaidoku and revenger — general shipped-artifact RE** | “reverse engineering of shipped artifacts with REA” — `kaidoku-shokunin/PROVINCE.md:3`; “Owns: reverse engineering of shipped artifacts” — `revenger-shokunin/PROVINCE.md:3`. | Both broadly claim the method/domain that could inspect these executables; neither required scope set names an omp/opencode binary parser. Kaidoku's OMP pins at `PROVINCE.md:8-24` are **REA MCP package requests**, not omp executable pins. This scan does not choose a general RE owner or extend kotoba's loader claim into general binary analysis. |

No whole-file executable identity test was located in kama's named resolver or mori's named parser: kama checks its declared endpoint read; mori emits the digest but has no baseline re-pin by its own scope. Kumitate's attestation is launch-specific, not a sibling-wide promise that kotoba's current binary is the one it launched. [INFERENCE] The same pathname may therefore underlie independently valid, differently scoped receipts without providing a shared measurement instant.

## Contested scope — left open

1. **`$HOME/.config/opencode` group ownership:** kagi's `corpus/README.md:96` still says “no fleet artifact names a single owner” and marks it `unresolved`; kotoba's carried `PROVINCE.md:46` also leaves it with the integrator. This report does not assign the group or authorize config changes.
2. **General shipped-artifact RE:** both kaidoku and revenger claim it; tsukuroi explicitly records “kaidoku/revenger ownership unresolved” (`PROVINCE.md:51`). Loader-specific interpretation needed for C1 must not be presented as an adjudication of that broader boundary.
3. **No new ownership ruling follows from shared reads.** Mori already distinguishes its capacity observation from kumitate's mechanism; the authoring/custody split for the global AGENTS file is stated by kagi. The observed wording contradiction about pin strength is not a license to change either lane's contract.

# One bounded proposed move

**Add question-qualified overlap annotations to this round's existing evidence report, not another gate or shared pin baseline.** For each relevant observation, state:

`surface | predicate/question | instrument owner and commit | identity strength | observed result or not run`

The useful split is:

- Global AGENTS: **kagi shape/custody** (mode/line count, content hash withheld) beside **kotoba authoring** (`alwayson.04`/`.07`). Keep separate results; do not reproduce or digest the private file to join them.
- omp: **kotoba loader/binary identity**, **kumitate launch attestation**, **kama endpoint fallback**, and **mori capacity clamp/default**. Join executable observations only when the available receipts actually establish the same path/digest and measurement context; otherwise label identity unjoined. No new sibling probes are required for this annotation.

This is one evidence-presentation change only: no counter/case expansion, no rerouting, no sibling edit, no gate consolidation, no file rename/deletion, no host mutation. The present report supplies the pinned overlap evidence; the L1 can attach actual measured C1/C2 results without turning these unrun sibling checks into passes.

## Affected axes and second-order effects

- **Adjacency:** [INFERENCE] improves by attaching an exact question and sibling-owned evidence to a shared path instead of treating all readers as rival owners.
- **Freshness and calibration:** [INFERENCE] improves the interpretation of substrate receipts by distinguishing executable identity, historical versions, declarations and live behaviour. It does **not** move either frozen claim's count.
- **Operability/consistency:** [INFERENCE] no harm expected from an evidence-only annotation; the C2 instrument interface and fixed cases remain untouched. No claim that this report makes the instrument runnable.
- **Runtime:** no extra executable/model call, startup check, or hot-path work; a rule-file diagnostic cannot become a cleanup action or service remediation.
- **Contract:** C2 stays a two-box fixture-discrimination claim. An import with client-specific additions remains a pinned PASS, and sibling checks remain independent propositions. Tameshi's method is not absorbed as a new kotoba-owned service.
- **Substrate:** no shared auto-repin, and no replacement of kagi's no-hash policy. C1 still measures its declared opencode executable rather than a wrapper or an obsolete opencode path.
- **Verification:** preserve raw outputs and separate fields; never collapse differing gate propositions into one “healthy” score. Loader semantic alignment remains reviewer work (`plans/round-53.md:35-36`), not something an identity join proves.

## Risks and verification

**Observed research, not executed product verification:** metadata/archive commands above succeeded; `read`/`grep` supplied the quoted evidence. Neither round counter, any sibling gate, a self-test, a mutation suite, nor a live C2 population run was executed by this seat. The supplied before-values were not rerun.

Bounded negative-sweep method: `functions.grep` over each pinned archive's required scope members, with `gitignore:false`, using `(?i)(AGENTS\.md|CLAUDE\.md|always[- ]on|instruction[- ]file|rule[- ]file)` and `(?i)(opencode|\bomp\b)`. All returned matches were classified; generic “always on” wording, client/provider mentions, transcript readers and report-directory names are not executable pin claims. Relevant sections were opened with `read`. This is not a client-documentation silence claim or an all-repository absence claim.

**Main-agent verification recommendations, unrun here:**

1. Reproduce any cited line from `git show <recorded-commit>:<path>` before using it as an ownership premise. If a sibling later commits, give the later observation a new pin; do not rewrite this capture time.
2. When attaching the delivered C1/C2 measurements, retain each exact command, measured revision, substrate identity and exit code. Keep the frozen plan counters unchanged. The annotations must not claim sibling-gate execution unless a real receipt is available.
3. Review the result against the two concrete conflations above: kagi's shape pin must not become “content unchanged”; C2's CLAUDE symlink PASS must not become permission to replace the pinned AGENTS file or to delete a second file.
4. Keep config-owner and general-RE disputes explicitly unresolved. Annotations may cite stated splits; they cannot create an arbitration ruling.

Limitations: sibling HEADs can advance after the capture; scope-file absence does not prove tool-code absence elsewhere; the C2 implementation was not evaluated. No live shared-file contents were inspected, so this report establishes no current cleanliness or drift result for them. No tools were installed or updated.

# Snapshot integrity appendix

All snapshot outputs reside only in this seat's sandbox. Scope archives contain the three required files, except the three absent skills; detail archives contain only the named additional gate/knowledge files described above. Digests below are of **local committed-source tar bytes**, not of a private AGENTS file or an installed client binary.

Scope captures: 2026-10-22T20:04:55Z; HTTP status not applicable.

| Snapshot | Bytes | SHA-256 |
|---|---:|---|
| `scope-audio.tar` | 20480 | `0235e0793bc4ab8caa7a0e7c2651f9fdc3f934206df90afe542a01d85f73b8ee` |
| `scope-chousa.tar` | 174080 | `d3ebbd12a02f5b6561c89b385692ad4bae55748eb5e749bf6e557afdb493dd3f` |
| `scope-game-dev-2d.tar` | 20480 | `ad02bb203ffc8938e247b37e066643c3a7a6f0a5de86922aa884b6695bcf91be` |
| `scope-game-dev-3d.tar` | 61440 | `84812af7001792c76401d560ce4713931c40f88c8282dcf581f0af8cb4c43a3e` |
| `scope-kagi.tar` | 133120 | `cc3e6af978053b81464c834bb9eb4d7fa1e568535a78a69bbeeaab4a7bdb944f` |
| `scope-kaidoku.tar` | 225280 | `cb8bb23545fffb76fdd9c1d5884f9a4e09b27a9e634f3fec90bc53ecd910b359` |
| `scope-kake.tar` | 143360 | `edb04785c0dd6b5d4f0e9c03784b6c3bbfb6b71bc156ac484ae6664afb547338` |
| `scope-kama.tar` | 143360 | `62d0dd75a717e84b5c6289c9b2ab8ce9af9f6fbf827ed8c13841abfd3eaad6c8` |
| `scope-kasegi.tar` | 112640 | `d4fc3741a31b6d003b2f31893e3b2708374999360b34037195d93444c98e5eb6` |
| `scope-kengaku.tar` | 143360 | `659f6d84ef306b814bd5db00f9a9f8160d0e59280d62e412583f8aa432888321` |
| `scope-kotodama.tar` | 256000 | `65eb5e280b453ed64398e740ce33a5ecb60f442c486d173ebf7d9f6e4b6a58bd` |
| `scope-kumitate.tar` | 122880 | `23ba2aaa3b7669c177707e92bcf64e81604671039ca4ec8955beb6e59b8bcde6` |
| `scope-lore.tar` | 61440 | `5677b698319a616cf7b2a45f9f498073528ba5febfce362ea9288e2d2571e95f` |
| `scope-mado.tar` | 225280 | `252ea76fbcf363e2d91e866a777297b3bd00dca3dbe5ca226bd7a782afc06e69` |
| `scope-mori.tar` | 204800 | `21bf48aabfbd68a6c16fb2ead03570db667e6cda03d5dc86d2aef05c862e23c8` |
| `scope-revenger.tar` | 20480 | `b5887171e22fbd7c35e3a26d0534e4247144789a94179298ac6131b1d61d696d` |
| `scope-souji.tar` | 102400 | `5e9fc53db61711efbde1ad4ba22841058888efb17cdfa0dd2de2f2770199ab32` |
| `scope-tabi.tar` | 286720 | `aa0fa51dbc43ff3d6757e5b4baf35e785b55d1d7a1e064c6841477f1fc0f449b` |
| `scope-tameshi.tar` | 225280 | `7ce647a145d692e602364bed4e16dc42825f900ef5b943ac072bf6852ee802cb` |
| `scope-tsukuroi.tar` | 409600 | `2771634cea45d69efef2819ec5aada440c280e7f2ad2d9295ef49d6e7766733f` |

Detail captures: 2026-10-22T20:06:41Z; `git archive` exit 0 for each, no stdout/stderr; same pinned commits as the scope table.

| Snapshot | Bytes | SHA-256 |
|---|---:|---|
| `detail-kagi.tar` | 30720 | `fb1af659da53e213b0c7860f1d555db4066054e72dd2cb45f359d9e0363f5acc` |
| `detail-kama.tar` | 61440 | `62272ec0542352920bfc7c65c00874312e76a91ab7417a21ccd03085aca33b3f` |
| `detail-mori.tar` | 71680 | `b690155a6cb7533c85ce0a6a1162ee0b4dc579f1cd70495aae1212f53e74eac6` |
| `detail-kumitate.tar` | 61440 | `940f2c81ba3f0d68e9406edd998b007038e9b752c6c25d67005b8373dde1b6c1` |
