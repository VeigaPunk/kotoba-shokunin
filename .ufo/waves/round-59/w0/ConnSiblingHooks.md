# ConnSiblingHooks — sibling-overlap scan for the C1 surface (hook configuration files by client)

Seat: `KotobaR59.ConnSiblingHooks` (W0, pre-freeze). Lane: kotoba-shokunin (read-only). Base `a975cbbf00534443c49bf02e29c813a3db0bf0f8`; plan draft `a3e70a303bab75671272498156099a65fe9b688e`. Scan date 2026-10-23 (UTC). Method: for every `/home/vgpnk/Projects/shokunin/*-shokunin` except kotoba-shokunin, read SKILL.md description (where present) and PROVINCE.md Core/Refuses, and `grep -ril 'hook'` over `corpus/ SKILL.md PROVINCE.md` (head). Commit cited via `git -C <lane> rev-parse HEAD` (read-only).

Surface under test: "where each client documents its hook config file and events, and when a rule belongs in a hook instead of a prompt" (C1, `### Hook files by client` beside `### Custom command files by client`).

## Census

| lane | relation | quote | commit |
|---|---|---|---|
| audio | none | "Owns: game audio production — SFX (UI, impacts, movement, ambience) and" (`PROVINCE.md:3`) | `7a2fcd4f08831154686e4e323031f41fffdb077f` |
| chousa | adjacent | "Deep-research method (調査) — question framing, source hierarchy, citation chaining, claim-vs-source verification." (`SKILL.md:3` description) | `0fb300b5c27900ab8bb3abeb5f54776d71e04beb` |
| game-dev-2d | none | "Owns: 2D game production verified by executable headless fixtures — loop, input, physics, scenes, camera, UI, levels, juice, export readiness." (`PROVINCE.md:3`) | `7753d49b16674e122ed134403e7a9b301f2cbf7e` |
| game-dev-3d | none | "Domain specialist — 3D game production verified by executable headless fixtures — spatial queries, camera/frustum, transforms, scene structure," (`SKILL.md:3` description) | `89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080` |
| kagi | adjacent | "Domain specialist — secrets & vault ops — the-janitor flows, credential hygiene evidence, vault lifecycle. Rank: shonen." (`SKILL.md:3` description) | `899c50b42634a3a4ad0b28ab7509786315e2fc2b` |
| kaidoku | none | "Domain specialist — reverse engineering of shipped artifacts with REA on this Linux host — native ELF/PE through the Ghidra 12.1.4 provider," (`SKILL.md:3` description) | `e58ed21be0e72e76e5374fea894dd5cf14a0cfda` |
| kake | adjacent | "Domain specialist — web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys. Rank: shonen." (`SKILL.md:3` description) | `6d5cd54a54d5098978f0e80eca510aa8f1c0b099` |
| kama | adjacent | "**Refuses:** model quality/eval (kengaku), credential material & auth flows (kagi), dispatch/route mechanism (kumitate), remote web surfaces (kake)." (`PROVINCE.md:40`) | `e49b4cf77046024551ba83d490ef83d9dee061ed` |
| kasegi | adjacent | "Domain specialist — bounty & security research — scopes ~/Projects/bounties, program rules, claim packages. Rank: shonen." (`SKILL.md:3` description) | `1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a` |
| kengaku | adjacent | "Sibling arbitration: kotoba owns prompt and skill craft (kengaku keeps only measured capability effects);" (`SKILL.md:3` description) | `1f3b0f1ec41ec297130e8944ff97968d32324632` |
| kotodama | adjacent | "Anti-trigger: NOT world-bible canon recording … NOT prompt/skill craft (kotoba-shokunin)," (`SKILL.md:3` description) | `78ad4b176695e9fcd490ab607cb8218e2ce62738` |
| kumitate | adjacent | "Prompt and skill craft → kotoba." (`PROVINCE.md:27`) | `980a16afc7caafe4e924ef117692248fdc7acbd6` |
| lore | none | "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification and sourced inspiration." (`PROVINCE.md:3`) | `380ef3abc7c7af11d7f23e9f9c82bb1937e1f695` |
| mado | none | "Domain specialist — desktop & compositor craft. Rank: shonen (probation)." (`SKILL.md:3` description) | `05319e0fed2ce25cf0a883380af2763a85fd4936` |
| mori | none | "Fleet & host observability (森) — detect and report fleet liveness, wave settlement, kill/OOM events and resource runway." (`SKILL.md:3` description) | `721040a908103817fe2025b5edd4614f96d791d2` |
| revenger | none | "Owns: reverse engineering of shipped artifacts — native binaries, managed" (`PROVINCE.md:3`) | `876630dbb4d630e016d7d8c32a19ea04c646cbae` |
| souji | none | "Fleet repo & workspace hygiene (掃除). Triggers: 'clean', 'prune', 'sweep', 'stale artifacts', …" (`SKILL.md:3` description) | `4edb25dfe262515d0da63224bbba71e02e36cba5` |
| tabi | none | "Domain specialist — browser & web-interaction craft. Rank: shonen (probation)." (`SKILL.md:3` description) | `e3cf4e0d30bb835532ff44b118c5ad52e09eb76d` |
| tameshi | adjacent | "Verification-fixture craft for 'hermetic suites', 'mutation testing', and 'gate fixtures'." (`SKILL.md:3` description) | `c111dab58b0a8d55e991bbd2efe3aad56717b95a` |
| tsukuroi | none | "Domain specialist — host operability & system repair. Rank: shonen (probation)." (`SKILL.md:3` description) | `15c9ac0e1b02917f43c0bc016d6060f888cb603a` |

Notes on hook-adjacent lanes that are NOT this surface:
- `mado-shokunin` mentions host-side omarchy hooks (`hooks/**` bodies, `*.d` hook dirs) and surveys the omarchy SKILL.md frontmatter, but those are compositor/host hooks, not client AI hook-config files. Census classification for mado is `none`; no ownership of the C1 surface.
- `tsukuroi-shokunin` owns pacman/ALPM host hooks (`walker-restart.hook`, `90-mkinitcpio-install.hook`) and initramfs hooks — host operability, not client AI hook-config files.
- `game-dev-3d-shokunin` mentions a `SessionStart` hook, but that is the Unreal MCP upstream hook, not a client hook-config-file location.
- `kumitate-shokunin` mentions a shutdown hook readiness predicate (`assertShutdownHookReady`), runtime orchestration, not client hook-config files.

No lane is classified `owns` for this surface: no sibling's SKILL.md description or PROVINCE.md Core/Refuses names client hook-config-file locations or the instruction-vs-hook decision. The nine `adjacent` lanes share a boundary with kotoba on prompt/skill craft or instruction surfaces and defer that craft to kotoba; none claims the client hook-config surface itself.

## Province fit

Verdict: **FITS**.

Reasons:
1. Kotoba's province is "prompt & skill craft" (`PROVINCE.md` Domain line: "prompt & skill craft — scopes SKILL.md/AGENTS.md quality, trigger fidelity"). The C1 surface is an instruction surface: where clients document their hook-config files and events, plus the craft decision of when a rule belongs in a hook instead of a prompt. This is the same family as the existing `### Agent-definition files by client`, `### Plugin manifests by client`, and `### Custom command files by client` subsections.
2. It belongs under the existing heading `## Instruction surfaces — pick the file before the fix` in `SKILL.md`, as a new subsection `### Hook files by client` placed beside `### Custom command files by client` (per the plan draft `a3e70a30`).
3. Kotoba already governs the instruction-vs-prompt placement decision for other surfaces (`### MCP server instructions`, `### Custom command files by client`), so adding the hook case keeps one authoritative home per fact (compression rule) rather than a second convention.
4. No sibling owns the surface (no `owns` rows above), so there is no boundary conflict; the nine `adjacent` lanes defer prompt/skill craft to kotoba.

Wording the `### Hook files by client` section MUST carry to stay in scope:
- The instruction-vs-hook decision: a rule that must hold every time (deterministic, lifecycle-bound) belongs in a hook, not in prompt text the model may ignore; prompt/always-on text stays for advisory/flexible guidance. State this as the action cell / craft rule for each client row, mirroring the `### Custom command files by client` table's "Action" column.
- A boundary sentence for siblings: "Host-side hooks (omarchy/compositor hooks, pacman/ALPM hooks, initramfs hooks, runtime shutdown hooks) are owned by their lanes (mado, tsukuroi, kumitate); this section documents only client AI hook-config files and the craft decision of when to move a rule out of a prompt." Plus the existing kotoba adjacent-lane deferral already in SKILL.md descriptions.

Result: DONE — no sibling lane owns the client hook-config surface; it fits kotoba under `## Instruction surfaces` as `### Hook files by client`, with the instruction-vs-hook decision and a host-hook boundary sentence required.
