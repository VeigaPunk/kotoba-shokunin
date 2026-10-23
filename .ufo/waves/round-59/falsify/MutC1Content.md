Result: MIXED — Six content mutations change the frozen counter's row signal; d and f are invisible, and only b fails its unchanged exit predicate.

# Scope and fixed detector

Attacked: what C1's counter measures on the committed round-59 data world, not the overall round verdict. Axes: depth (field-level falsifiability), calibration (row signal versus acceptance), and byte integrity/no-harm.

Data revision: `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`. All execution and Git writes were confined to `/fast/scratch/hyaku/kotoba-r59/MutC1Content`. No lane content, index, jj state, sibling copy, or fleet-root file was changed; the sole lane write is this report. No subagents, client hooks, client model calls, UFO runtime, builds, or unrelated tests were invoked. No tools were installed or updated.

Frozen detector: `verifiers/check_hook_files.py`, SHA256 `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`. Its bytes were identical in every receipt. Read the committed assignments at `verifiers/check_hook_files.py:253-254`: TARGET=4, NEW_TARGET=5. No rule, counter, target, or predicate was edited.

Every measured command was `timeout 600 python3 -B verifiers/check_hook_files.py --rev <full commit> --fetch`, with the same transparent logging environment. `probe/bin/curl` forwarded the exact frozen arguments to `/usr/bin/curl`, retained its original stdout/stderr and exit, and returned them unchanged. It did not replace, cache, or synthesize page content. Per-fetch bodies, full curl output/trailer, stderr, actual `date -u` output, HTTP status, URL, size and SHA256 are retained in the receipt directories below.

Receipts and harness: `/fast/scratch/hyaku/kotoba-r59/MutC1Content/probe/`. Each run is `receipts/<label>/receipt.json`, with exact `counter.stdout`, `counter.stderr`, and `fetch-NN.{body,stdout,stderr,json}`. The outer launcher was `timeout 650 python3 -B probe/run_probe.py <label>`; it completed with exit 0 for all labels because it records, rather than overwrites, the detector's separately reported exit. Git add/commit commands were bounded by 20/30 seconds, respectively. The detector's actual exits are below.

# Baseline, mutants, and after-column

S = backed rows, F = live-found rows, G = distinct new tokens, K = well-formed lead-token population. Expected S/F/G/exit was fixed from the frozen row rule and targets before each edit. 'Signal killed' means the predicted row rejection/count reduction appeared; 'predicate killed' means the real frozen exit changed from baseline 0 to 1. This distinction is necessary: one rejected row still leaves G=5, meeting the frozen floor.

| Mutant | Expected S/F/G; K; exit | Observed S/F/G; K; exit | Signal verdict | Frozen-predicate verdict | Restored after-column |
|---|---|---|---|---|---|
| a: Drop the Claude Code SKILL row | 5/5/5; 5; 0 | 5/5/5; 5; 0 | KILLED (row signal) | SURVIVED | 6/6/6; K=6; exit 0; exact tree/hash restoration |
| b: Swap only Claude Code and Codex's lead Hook config tokens | 4/4/4; 6; 1 | 4/4/4; 6; 1 | KILLED (row signal) | KILLED | 6/6/6; K=6; exit 0; exact tree/hash restoration |
| c: Replace Claude Code's `PreToolUse` Events span with `InventedLifecycleEventR59` | 5/5/5; 6; 0 | 5/5/5; 6; 0 | KILLED (row signal) | SURVIVED | 6/6/6; K=6; exit 0; exact tree/hash restoration |
| d: Replace the same span with real same-page tool identifier `Bash` | 6/6/6; 6; 0 | 6/6/6; 6; 0 | SURVIVED (no signal change) | SURVIVED | 6/6/6; K=6; exit 0; exact tree/hash restoration |
| e: Change S096 snapshot byte offset 0 from `>` (0x3e) to `!` (0x21), without repinning | 5/5/5; 6; 0 | 5/5/5; 6; 0 | KILLED (row signal) | SURVIVED | 6/6/6; K=6; exit 0; exact tree/hash restoration |
| f: Replace all seven Action cells, including opencode's, with `amber pebble orbit` | 6/6/6; 6; 0 | 6/6/6; 6; 0 | SURVIVED (no signal change) | SURVIVED | 6/6/6; K=6; exit 0; exact tree/hash restoration |
| g: Remove only S096's Gate quotation, retaining its URL/access/digest/line metadata | 5/5/5; 6; 0 | 5/5/5; 6; 0 | KILLED (row signal) | SURVIVED | 6/6/6; K=6; exit 0; exact tree/hash restoration |
| h: Change the Claude Code entry Source cell from S096 to the Codex row's S097 | 5/5/5; 6; 0 | 5/5/5; 6; 0 | KILLED (row signal) | SURVIVED | 6/6/6; K=6; exit 0; exact tree/hash restoration |

Pristine: S/F/G=6/6/6, K=6, exit 0. Every restored run independently returned the same values. There is no baseline failure and no inconclusive mutant. All detector stderr streams were empty.

**HOLDS — row/source/integrity conjuncts exercised by a, b, c, e, g, h.** a rejects the missing client; b rejects both foreign client tokens plus entry/quote/page mismatches; c rejects the invented event on the committed snapshot; e rejects the snapshot digest before treating its content as evidence; g rejects the missing Gate quote; h rejects the foreign pinned host and the snapshot quote. Relevant implementation: `verifiers/check_hook_files.py:786-866,887-929`.

**BREAKS — an interpretation that 6/6 certifies hook-event semantics or meaningful Actions.** d and f both retain S/F/G=6/6/6 and exit 0. The only output change is the measured revision's bookkeeping hash; neither adds a rejection. This is the expected semantic coverage gap, not permission to alter the frozen contract.

- d: `Bash` is printed on S096 but names a tool, not an event. Ordinary live fetch https://code.claude.com/docs/en/hooks.md, retained as `probe/receipts/pristine/fetch-01.body:195`, says verbatim (no Markdown bytes stripped; 12 words):

> The matcher `"Bash"` matches the tool name, so this hook group activates.

  The same fetched bytes distinguish event `PreToolUse` at line 78 from matcher `Bash` at line 80. Source access record is pasted below. `verifiers/check_hook_files.py:705-763` checks identifier syntax and boundary-preserving page presence, not identifier role. This exactly exercises the limit declared at `plans/round-59.md:93-98`, which routes semantics to cell reviewers.
- f: all useful Action instructions, including review/trust/cloud-agent conditions, can disappear while each cell still meets the three-word minimum. `verifiers/check_hook_files.py:912-914` reads only its word count; `plans/round-59.md:35-37` states that minimum. The counter therefore does not establish the Actions' usefulness, factuality, or connection to the cited source.

**HOLDS — the frozen threshold is not an all-rows-valid gate.** a, c, e, g and h are visibly rejected but still exit 0; b alone reduces G to 4, below NEW_TARGET=5, while F=4 still meets TARGET. Do not describe the five one-row mutants as invisible or as exit-killed. Exact interpretation correction: report S/F/G and rejection output separately from predicate acceptance; leave the frozen rule/targets unchanged.

# Exact mutation points and inverse corrections

- **a** — data-world `SKILL.md:127`: Drop the Claude Code SKILL row. Inverse correction applied: Restore the exact Claude Code row at line 127.
- **b** — data-world `SKILL.md:127-128`: Swap only Claude Code and Codex's lead Hook config tokens. Inverse correction applied: Claude Code leads with `.claude/settings.json`; Codex leads with `~/.codex/hooks.json`.
- **c** — data-world `SKILL.md:127`: Replace Claude Code's `PreToolUse` Events span with `InventedLifecycleEventR59`. Inverse correction applied: Replace `InventedLifecycleEventR59` with `PreToolUse` in that Events cell.
- **d** — data-world `SKILL.md:127`: Replace the same span with real same-page tool identifier `Bash`. Inverse correction applied: Replace `Bash` with `PreToolUse` in that Events cell.
- **e** — data-world `.ufo/waves/round-59/snapshots/S096.page:1`: Change S096 snapshot byte offset 0 from `>` (0x3e) to `!` (0x21), without repinning. Inverse correction applied: Restore byte offset 0 to `>` (0x3e); do not change the SOURCES digest.
- **f** — data-world `SKILL.md:127-133`: Replace all seven Action cells, including opencode's, with `amber pebble orbit`. Inverse correction applied: Restore all seven original Action cells from the data commit; the full-file original SHA256 below fixes the exact bytes.
- **g** — data-world `corpus/lessons/round-59.md:10`: Remove only S096's Gate quotation, retaining its URL/access/digest/line metadata. Inverse correction applied: Restore the original S096 quotation after the retained `hooks.md:910` metadata.
- **h** — data-world `corpus/knowledge/hook-files-round59.md:23`: Change the Claude Code entry Source cell from S096 to the Codex row's S097. Inverse correction applied: Change that entry Source cell from S097 back to S096.

# Hashes and restoration evidence

Original tracked tree: `909b6685757c1a6feb3d73c63d6e492a2cb50a07`. Every restored commit has this exact tree ID, so every tracked byte and tree mode is restored, not merely the touched cell. All 11 measured file SHA256 lines also equal pristine after every restore. Scratch-only receipt/harness files were never added to a commit.

Original and every restored file SHA256 (`timeout 10 sha256sum ...`, exit 0 in each receipt):

```text
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
f2bde4090fa4bcb71ed6b84e02066e8eb670c54b4eedbcfcc504aeb42ccfca9e  SKILL.md
4ad65c1b1d8532506e961fdc468a3afef001763658237861ccac41379ae8540b  corpus/knowledge/hook-files-round59.md
0e6cc77600200a213a68baa26cfc9d788995baae0fa5522e796e017e769fea84  corpus/lessons/round-59.md
3f63a11ffeedccf710aa872d08fd4b159ca8a52e89e0c11b3576c456c973779a  corpus/SOURCES.md
c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8  .ufo/waves/round-59/snapshots/S096.page
57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92  .ufo/waves/round-59/snapshots/S097.page
98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08  .ufo/waves/round-59/snapshots/S098.page
23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4  .ufo/waves/round-59/snapshots/S099.page
fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc  .ufo/waves/round-59/snapshots/S100.page
8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d  .ufo/waves/round-59/snapshots/S101.page
```

Changed file SHA256 (before and restored values resolve to the exact original row above):

| Mutant | File | Before SHA256 | Mutated SHA256 | Restored SHA256 |
|---|---|---|---|---|
| a | `SKILL.md` | `f2bde4090fa4bcb71ed6b84e02066e8eb670c54b4eedbcfcc504aeb42ccfca9e` | `133b59cf0c9b8afe77d42983cc69751a040d94e01f8ae8bdbadadacec3042b25` | `f2bde4090fa4bcb71ed6b84e02066e8eb670c54b4eedbcfcc504aeb42ccfca9e` |
| b | `SKILL.md` | `f2bde4090fa4bcb71ed6b84e02066e8eb670c54b4eedbcfcc504aeb42ccfca9e` | `c01f065162e6f10ecac84ef737079442656f514d6982e5cc748c348711ec9bf4` | `f2bde4090fa4bcb71ed6b84e02066e8eb670c54b4eedbcfcc504aeb42ccfca9e` |
| c | `SKILL.md` | `f2bde4090fa4bcb71ed6b84e02066e8eb670c54b4eedbcfcc504aeb42ccfca9e` | `59a2ce0d112e86cab983c56456ec89762789a5e3d4916525e2f207ae558efb5d` | `f2bde4090fa4bcb71ed6b84e02066e8eb670c54b4eedbcfcc504aeb42ccfca9e` |
| d | `SKILL.md` | `f2bde4090fa4bcb71ed6b84e02066e8eb670c54b4eedbcfcc504aeb42ccfca9e` | `ca36a00a6ef54cc70f6e52b1ee8135b8343e6d557c199a1f17bb04059331df0b` | `f2bde4090fa4bcb71ed6b84e02066e8eb670c54b4eedbcfcc504aeb42ccfca9e` |
| e | `.ufo/waves/round-59/snapshots/S096.page` | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` | `95587b0278544371559be827fab4bab6b94d34f4429ab63562d19e3c7238142c` | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` |
| f | `SKILL.md` | `f2bde4090fa4bcb71ed6b84e02066e8eb670c54b4eedbcfcc504aeb42ccfca9e` | `0d16cb2d5a58f95e8c4446e4267a3706dcd27c2e879451591cc7adc6e8093162` | `f2bde4090fa4bcb71ed6b84e02066e8eb670c54b4eedbcfcc504aeb42ccfca9e` |
| g | `corpus/lessons/round-59.md` | `0e6cc77600200a213a68baa26cfc9d788995baae0fa5522e796e017e769fea84` | `6dc305285ea87ddd7f7ea751461afb640a93757550c5dc5eedb61e156d28f542` | `0e6cc77600200a213a68baa26cfc9d788995baae0fa5522e796e017e769fea84` |
| h | `corpus/knowledge/hook-files-round59.md` | `4ad65c1b1d8532506e961fdc468a3afef001763658237861ccac41379ae8540b` | `dd426109ffedbdf4a48458b4197eddfd2034275e860bbbd4d9236ca1047e2626` | `4ad65c1b1d8532506e961fdc468a3afef001763658237861ccac41379ae8540b` |

Sandbox commit provenance (these are local scratch commits, never lane commits; never pushed):

| Mutant | Mutated revision | Restored revision | Restored tree |
|---|---|---|---|
| a | sandbox f3d772ba58096cfd969e1368c1f4737cf194d0dd (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | sandbox f3e8a3d9bfad222e1a1214da646d5e5b83dfc8e6 (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | `909b6685757c1a6feb3d73c63d6e492a2cb50a07` |
| b | sandbox 719e40b1e39a79d7a43d28ee5d64d7365c08e10a (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | sandbox 6272da9f663afc34ef42ad3349dd58143bdd3eeb (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | `909b6685757c1a6feb3d73c63d6e492a2cb50a07` |
| c | sandbox 4a9545e8a6ea49761037c7cf70b5a0f5733b664c (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | sandbox 442ef42a5704a87850fc7c573908f56cd2fa2fc4 (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | `909b6685757c1a6feb3d73c63d6e492a2cb50a07` |
| d | sandbox b8eb74e9c8529c7a808fe55c4cbdaa3383d2f81a (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | sandbox 73ad58bf491e28abba05dc3c0eac08bce4ac7f5c (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | `909b6685757c1a6feb3d73c63d6e492a2cb50a07` |
| e | sandbox 1f8051221d661a28a5749a53f7d9ddbe934c3066 (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | sandbox 61f0ba050f05dcd289a3a6b8e17c6290300d2174 (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | `909b6685757c1a6feb3d73c63d6e492a2cb50a07` |
| f | sandbox f6c0212793cd17234d5316a3e92f3f4b0179abb2 (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | sandbox c6deec78ba58084e595a6b1b490d61ab47f1e4f7 (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | `909b6685757c1a6feb3d73c63d6e492a2cb50a07` |
| g | sandbox 5214e00f00b14c17a7c9359e967671df7f51a96d (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | sandbox d8b8d3d3edf27d8a402052784162ef2549b8b2db (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | `909b6685757c1a6feb3d73c63d6e492a2cb50a07` |
| h | sandbox b3c400a262e134637ebf02c5cf6485b46bf3e736 (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | sandbox a9282245dccd76ffa1c99d87e0cac8e2f2629fd5 (/fast/scratch/hyaku/kotoba-r59/MutC1Content) | `909b6685757c1a6feb3d73c63d6e492a2cb50a07` |

# Actual detector commands and outputs

All commands below ran with cwd at the sandbox root and the same logger PATH. No output is inferred or reconstructed from a hypothetical run. The measured revision line is retained verbatim.

## pristine

Revision: data revision c63ccc6823e1f6a8577acbb43d19551eadbbee9a.

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a --fetch
$ date -u (start)
Fri Oct 23 09:54:39 AM UTC 2026
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:54:40 AM UTC 2026
```

## a-mutated

Revision: sandbox f3d772ba58096cfd969e1368c1f4737cf194d0dd (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev f3d772ba58096cfd969e1368c1f4737cf194d0dd --fetch
$ date -u (start)
Fri Oct 23 09:54:57 AM UTC 2026
hook files backed on committed snapshots 5 of 5; found on the live page 5 of 5; new ground 5
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev f3d772ba58096cfd969e1368c1f4737cf194d0dd
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); entry row S096: snapshot .ufo/waves/round-59/snapshots/S096.page: no hook token to find on the page
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:54:58 AM UTC 2026
```

## a-restored

Revision: sandbox f3e8a3d9bfad222e1a1214da646d5e5b83dfc8e6 (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev f3e8a3d9bfad222e1a1214da646d5e5b83dfc8e6 --fetch
$ date -u (start)
Fri Oct 23 09:55:16 AM UTC 2026
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev f3e8a3d9bfad222e1a1214da646d5e5b83dfc8e6
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:55:17 AM UTC 2026
```

## b-mutated

Revision: sandbox 719e40b1e39a79d7a43d28ee5d64d7365c08e10a (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev 719e40b1e39a79d7a43d28ee5d64d7365c08e10a --fetch
$ date -u (start)
Fri Oct 23 09:55:38 AM UTC 2026
hook files backed on committed snapshots 4 of 6; found on the live page 4 of 6; new ground 4
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 719e40b1e39a79d7a43d28ee5d64d7365c08e10a
reject Claude Code: SKILL.md hook token '~/.codex/hooks.json' carries Codex's marker 'codex'; entry row S096: entry Hook config cell '`.claude/settings.json`' is not the SKILL.md token '~/.codex/hooks.json'; quote does not hold the hook token '~/.codex/hooks.json' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S096.page: the token '~/.codex/hooks.json' is not on the page
reject Codex: SKILL.md hook token '.claude/settings.json' carries Claude Code's marker 'claude'; entry row S097: entry Hook config cell '`~/.codex/hooks.json`' is not the SKILL.md token '.claude/settings.json'; quote does not hold the hook token '.claude/settings.json' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S097.page: the token '.claude/settings.json' is not on the page
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 1
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:55:38 AM UTC 2026
```

## b-restored

Revision: sandbox 6272da9f663afc34ef42ad3349dd58143bdd3eeb (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev 6272da9f663afc34ef42ad3349dd58143bdd3eeb --fetch
$ date -u (start)
Fri Oct 23 09:56:01 AM UTC 2026
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 6272da9f663afc34ef42ad3349dd58143bdd3eeb
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:56:03 AM UTC 2026
```

## c-mutated

Revision: sandbox 4a9545e8a6ea49761037c7cf70b5a0f5733b664c (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev 4a9545e8a6ea49761037c7cf70b5a0f5733b664c --fetch
$ date -u (start)
Fri Oct 23 09:56:25 AM UTC 2026
hook files backed on committed snapshots 5 of 6; found on the live page 5 of 6; new ground 5
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 4a9545e8a6ea49761037c7cf70b5a0f5733b664c
reject Claude Code: entry row S096: snapshot .ufo/waves/round-59/snapshots/S096.page: event 'InventedLifecycleEventR59' is not on the page
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:56:26 AM UTC 2026
```

## c-restored

Revision: sandbox 442ef42a5704a87850fc7c573908f56cd2fa2fc4 (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev 442ef42a5704a87850fc7c573908f56cd2fa2fc4 --fetch
$ date -u (start)
Fri Oct 23 09:56:45 AM UTC 2026
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 442ef42a5704a87850fc7c573908f56cd2fa2fc4
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:56:46 AM UTC 2026
```

## d-mutated

Revision: sandbox b8eb74e9c8529c7a808fe55c4cbdaa3383d2f81a (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev b8eb74e9c8529c7a808fe55c4cbdaa3383d2f81a --fetch
$ date -u (start)
Fri Oct 23 09:57:18 AM UTC 2026
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev b8eb74e9c8529c7a808fe55c4cbdaa3383d2f81a
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:57:19 AM UTC 2026
```

## d-restored

Revision: sandbox 73ad58bf491e28abba05dc3c0eac08bce4ac7f5c (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev 73ad58bf491e28abba05dc3c0eac08bce4ac7f5c --fetch
$ date -u (start)
Fri Oct 23 09:57:35 AM UTC 2026
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 73ad58bf491e28abba05dc3c0eac08bce4ac7f5c
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:57:36 AM UTC 2026
```

## e-mutated

Revision: sandbox 1f8051221d661a28a5749a53f7d9ddbe934c3066 (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev 1f8051221d661a28a5749a53f7d9ddbe934c3066 --fetch
$ date -u (start)
Fri Oct 23 09:57:53 AM UTC 2026
hook files backed on committed snapshots 5 of 6; found on the live page 5 of 6; new ground 5
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 1f8051221d661a28a5749a53f7d9ddbe934c3066
reject Claude Code: entry row S096: snapshot .ufo/waves/round-59/snapshots/S096.page sha256 95587b027854... does not equal the SOURCES row sha256 c6ef9d211e8c...
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:57:54 AM UTC 2026
```

## e-restored

Revision: sandbox 61f0ba050f05dcd289a3a6b8e17c6290300d2174 (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev 61f0ba050f05dcd289a3a6b8e17c6290300d2174 --fetch
$ date -u (start)
Fri Oct 23 09:58:16 AM UTC 2026
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 61f0ba050f05dcd289a3a6b8e17c6290300d2174
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:58:17 AM UTC 2026
```

## f-mutated

Revision: sandbox f6c0212793cd17234d5316a3e92f3f4b0179abb2 (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev f6c0212793cd17234d5316a3e92f3f4b0179abb2 --fetch
$ date -u (start)
Fri Oct 23 09:58:48 AM UTC 2026
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev f6c0212793cd17234d5316a3e92f3f4b0179abb2
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:58:50 AM UTC 2026
```

## f-restored

Revision: sandbox c6deec78ba58084e595a6b1b490d61ab47f1e4f7 (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev c6deec78ba58084e595a6b1b490d61ab47f1e4f7 --fetch
$ date -u (start)
Fri Oct 23 09:59:33 AM UTC 2026
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev c6deec78ba58084e595a6b1b490d61ab47f1e4f7
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:59:34 AM UTC 2026
```

## g-mutated

Revision: sandbox 5214e00f00b14c17a7c9359e967671df7f51a96d (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev 5214e00f00b14c17a7c9359e967671df7f51a96d --fetch
$ date -u (start)
Fri Oct 23 09:59:56 AM UTC 2026
hook files backed on committed snapshots 5 of 6; found on the live page 5 of 6; new ground 5
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 5214e00f00b14c17a7c9359e967671df7f51a96d
reject Claude Code: entry row S096: round-59 Gate does not record this quote
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 09:59:57 AM UTC 2026
```

## g-restored

Revision: sandbox d8b8d3d3edf27d8a402052784162ef2549b8b2db (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev d8b8d3d3edf27d8a402052784162ef2549b8b2db --fetch
$ date -u (start)
Fri Oct 23 10:00:16 AM UTC 2026
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev d8b8d3d3edf27d8a402052784162ef2549b8b2db
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 10:00:17 AM UTC 2026
```

## h-mutated

Revision: sandbox b3c400a262e134637ebf02c5cf6485b46bf3e736 (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev b3c400a262e134637ebf02c5cf6485b46bf3e736 --fetch
$ date -u (start)
Fri Oct 23 10:00:39 AM UTC 2026
hook files backed on committed snapshots 5 of 6; found on the live page 5 of 6; new ground 5
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev b3c400a262e134637ebf02c5cf6485b46bf3e736
reject Claude Code: entry row S097: S097 URL 'https://learn.chatgpt.com/docs/hooks.md' is not on a pinned host; snapshot .ufo/waves/round-59/snapshots/S097.page: the quote is not on the page
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 10:00:40 AM UTC 2026
```

## h-restored

Revision: sandbox a9282245dccd76ffa1c99d87e0cac8e2f2629fd5 (/fast/scratch/hyaku/kotoba-r59/MutC1Content).

```text
$ timeout 600 python3 -B verifiers/check_hook_files.py --rev a9282245dccd76ffa1c99d87e0cac8e2f2629fd5 --fetch
$ date -u (start)
Fri Oct 23 10:01:06 AM UTC 2026
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev a9282245dccd76ffa1c99d87e0cac8e2f2629fd5
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
exit 0
stderr: <empty>
$ date -u (end)
Fri Oct 23 10:01:10 AM UTC 2026
```

# Fetch access evidence

95 ordinary curl fetches were actually made across the 17 detector runs. All returned HTTP 200 with curl exit 0; each requested URL equaled its effective URL. Every URL had exactly one observed size/digest pair over all its fetches, listed here. The following per-fetch table pastes every actual UTC `date -u` line and ties it to the URL/byte-count/hash record; no status or hash was borrowed from an earlier run. Raw body hashes also match the committed snapshots on this world (except the deliberately mutated committed snapshot in e).

Frozen curl arguments, passed unchanged by the recorder:

```text
/usr/bin/curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '
%{http_code} %{url_effective}' <URL>
```

| Source key | Requested = effective URL | HTTP / curl exit | Body bytes | SHA256 |
|---|---|---|---|---|
| S096 | https://code.claude.com/docs/en/hooks.md | 200 / 0 | 274129 | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` |
| S097 | https://learn.chatgpt.com/docs/hooks.md | 200 / 0 | 47133 | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` |
| S098 | https://code.visualstudio.com/docs/agent-customization/hooks.md | 200 / 0 | 15152 | `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` |
| S099 | https://docs.github.com/en/copilot/concepts/customizations/hooks.md | 200 / 0 | 8428 | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` |
| S100 | https://geminicli.com/docs/hooks/best-practices.md | 200 / 0 | 17650 | `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` |
| S101 | https://cursor.com/docs/hooks | 200 / 0 | 69145 | `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` |

Each row's `fetch-NN.json` lives under `probe/receipts/<run>/`; its full recorded curl argv, URL, status, body length, digest, date, and exit are preserved. The matching `.body` file supplies byte-exact quotation line numbers.

| Run | Fetch receipt | Source metadata above | Actual `date -u` output |
|---|---|---|---|
| pristine | `fetch-01.json` | S096 | `Fri Oct 23 09:54:39 AM UTC 2026` |
| pristine | `fetch-02.json` | S097 | `Fri Oct 23 09:54:39 AM UTC 2026` |
| pristine | `fetch-03.json` | S098 | `Fri Oct 23 09:54:40 AM UTC 2026` |
| pristine | `fetch-04.json` | S099 | `Fri Oct 23 09:54:40 AM UTC 2026` |
| pristine | `fetch-05.json` | S100 | `Fri Oct 23 09:54:40 AM UTC 2026` |
| pristine | `fetch-06.json` | S101 | `Fri Oct 23 09:54:40 AM UTC 2026` |
| a-mutated | `fetch-01.json` | S097 | `Fri Oct 23 09:54:57 AM UTC 2026` |
| a-mutated | `fetch-02.json` | S098 | `Fri Oct 23 09:54:58 AM UTC 2026` |
| a-mutated | `fetch-03.json` | S099 | `Fri Oct 23 09:54:58 AM UTC 2026` |
| a-mutated | `fetch-04.json` | S100 | `Fri Oct 23 09:54:58 AM UTC 2026` |
| a-mutated | `fetch-05.json` | S101 | `Fri Oct 23 09:54:58 AM UTC 2026` |
| a-restored | `fetch-01.json` | S096 | `Fri Oct 23 09:55:16 AM UTC 2026` |
| a-restored | `fetch-02.json` | S097 | `Fri Oct 23 09:55:17 AM UTC 2026` |
| a-restored | `fetch-03.json` | S098 | `Fri Oct 23 09:55:17 AM UTC 2026` |
| a-restored | `fetch-04.json` | S099 | `Fri Oct 23 09:55:17 AM UTC 2026` |
| a-restored | `fetch-05.json` | S100 | `Fri Oct 23 09:55:17 AM UTC 2026` |
| a-restored | `fetch-06.json` | S101 | `Fri Oct 23 09:55:17 AM UTC 2026` |
| b-mutated | `fetch-01.json` | S098 | `Fri Oct 23 09:55:38 AM UTC 2026` |
| b-mutated | `fetch-02.json` | S099 | `Fri Oct 23 09:55:38 AM UTC 2026` |
| b-mutated | `fetch-03.json` | S100 | `Fri Oct 23 09:55:38 AM UTC 2026` |
| b-mutated | `fetch-04.json` | S101 | `Fri Oct 23 09:55:38 AM UTC 2026` |
| b-restored | `fetch-01.json` | S096 | `Fri Oct 23 09:56:02 AM UTC 2026` |
| b-restored | `fetch-02.json` | S097 | `Fri Oct 23 09:56:02 AM UTC 2026` |
| b-restored | `fetch-03.json` | S098 | `Fri Oct 23 09:56:02 AM UTC 2026` |
| b-restored | `fetch-04.json` | S099 | `Fri Oct 23 09:56:02 AM UTC 2026` |
| b-restored | `fetch-05.json` | S100 | `Fri Oct 23 09:56:02 AM UTC 2026` |
| b-restored | `fetch-06.json` | S101 | `Fri Oct 23 09:56:02 AM UTC 2026` |
| c-mutated | `fetch-01.json` | S097 | `Fri Oct 23 09:56:25 AM UTC 2026` |
| c-mutated | `fetch-02.json` | S098 | `Fri Oct 23 09:56:25 AM UTC 2026` |
| c-mutated | `fetch-03.json` | S099 | `Fri Oct 23 09:56:25 AM UTC 2026` |
| c-mutated | `fetch-04.json` | S100 | `Fri Oct 23 09:56:25 AM UTC 2026` |
| c-mutated | `fetch-05.json` | S101 | `Fri Oct 23 09:56:25 AM UTC 2026` |
| c-restored | `fetch-01.json` | S096 | `Fri Oct 23 09:56:45 AM UTC 2026` |
| c-restored | `fetch-02.json` | S097 | `Fri Oct 23 09:56:45 AM UTC 2026` |
| c-restored | `fetch-03.json` | S098 | `Fri Oct 23 09:56:46 AM UTC 2026` |
| c-restored | `fetch-04.json` | S099 | `Fri Oct 23 09:56:46 AM UTC 2026` |
| c-restored | `fetch-05.json` | S100 | `Fri Oct 23 09:56:46 AM UTC 2026` |
| c-restored | `fetch-06.json` | S101 | `Fri Oct 23 09:56:46 AM UTC 2026` |
| d-mutated | `fetch-01.json` | S096 | `Fri Oct 23 09:57:18 AM UTC 2026` |
| d-mutated | `fetch-02.json` | S097 | `Fri Oct 23 09:57:18 AM UTC 2026` |
| d-mutated | `fetch-03.json` | S098 | `Fri Oct 23 09:57:18 AM UTC 2026` |
| d-mutated | `fetch-04.json` | S099 | `Fri Oct 23 09:57:18 AM UTC 2026` |
| d-mutated | `fetch-05.json` | S100 | `Fri Oct 23 09:57:19 AM UTC 2026` |
| d-mutated | `fetch-06.json` | S101 | `Fri Oct 23 09:57:19 AM UTC 2026` |
| d-restored | `fetch-01.json` | S096 | `Fri Oct 23 09:57:35 AM UTC 2026` |
| d-restored | `fetch-02.json` | S097 | `Fri Oct 23 09:57:35 AM UTC 2026` |
| d-restored | `fetch-03.json` | S098 | `Fri Oct 23 09:57:36 AM UTC 2026` |
| d-restored | `fetch-04.json` | S099 | `Fri Oct 23 09:57:36 AM UTC 2026` |
| d-restored | `fetch-05.json` | S100 | `Fri Oct 23 09:57:36 AM UTC 2026` |
| d-restored | `fetch-06.json` | S101 | `Fri Oct 23 09:57:36 AM UTC 2026` |
| e-mutated | `fetch-01.json` | S097 | `Fri Oct 23 09:57:53 AM UTC 2026` |
| e-mutated | `fetch-02.json` | S098 | `Fri Oct 23 09:57:54 AM UTC 2026` |
| e-mutated | `fetch-03.json` | S099 | `Fri Oct 23 09:57:54 AM UTC 2026` |
| e-mutated | `fetch-04.json` | S100 | `Fri Oct 23 09:57:54 AM UTC 2026` |
| e-mutated | `fetch-05.json` | S101 | `Fri Oct 23 09:57:54 AM UTC 2026` |
| e-restored | `fetch-01.json` | S096 | `Fri Oct 23 09:58:16 AM UTC 2026` |
| e-restored | `fetch-02.json` | S097 | `Fri Oct 23 09:58:17 AM UTC 2026` |
| e-restored | `fetch-03.json` | S098 | `Fri Oct 23 09:58:17 AM UTC 2026` |
| e-restored | `fetch-04.json` | S099 | `Fri Oct 23 09:58:17 AM UTC 2026` |
| e-restored | `fetch-05.json` | S100 | `Fri Oct 23 09:58:17 AM UTC 2026` |
| e-restored | `fetch-06.json` | S101 | `Fri Oct 23 09:58:17 AM UTC 2026` |
| f-mutated | `fetch-01.json` | S096 | `Fri Oct 23 09:58:49 AM UTC 2026` |
| f-mutated | `fetch-02.json` | S097 | `Fri Oct 23 09:58:49 AM UTC 2026` |
| f-mutated | `fetch-03.json` | S098 | `Fri Oct 23 09:58:49 AM UTC 2026` |
| f-mutated | `fetch-04.json` | S099 | `Fri Oct 23 09:58:49 AM UTC 2026` |
| f-mutated | `fetch-05.json` | S100 | `Fri Oct 23 09:58:49 AM UTC 2026` |
| f-mutated | `fetch-06.json` | S101 | `Fri Oct 23 09:58:50 AM UTC 2026` |
| f-restored | `fetch-01.json` | S096 | `Fri Oct 23 09:59:33 AM UTC 2026` |
| f-restored | `fetch-02.json` | S097 | `Fri Oct 23 09:59:34 AM UTC 2026` |
| f-restored | `fetch-03.json` | S098 | `Fri Oct 23 09:59:34 AM UTC 2026` |
| f-restored | `fetch-04.json` | S099 | `Fri Oct 23 09:59:34 AM UTC 2026` |
| f-restored | `fetch-05.json` | S100 | `Fri Oct 23 09:59:34 AM UTC 2026` |
| f-restored | `fetch-06.json` | S101 | `Fri Oct 23 09:59:34 AM UTC 2026` |
| g-mutated | `fetch-01.json` | S097 | `Fri Oct 23 09:59:56 AM UTC 2026` |
| g-mutated | `fetch-02.json` | S098 | `Fri Oct 23 09:59:56 AM UTC 2026` |
| g-mutated | `fetch-03.json` | S099 | `Fri Oct 23 09:59:56 AM UTC 2026` |
| g-mutated | `fetch-04.json` | S100 | `Fri Oct 23 09:59:56 AM UTC 2026` |
| g-mutated | `fetch-05.json` | S101 | `Fri Oct 23 09:59:56 AM UTC 2026` |
| g-restored | `fetch-01.json` | S096 | `Fri Oct 23 10:00:16 AM UTC 2026` |
| g-restored | `fetch-02.json` | S097 | `Fri Oct 23 10:00:16 AM UTC 2026` |
| g-restored | `fetch-03.json` | S098 | `Fri Oct 23 10:00:17 AM UTC 2026` |
| g-restored | `fetch-04.json` | S099 | `Fri Oct 23 10:00:17 AM UTC 2026` |
| g-restored | `fetch-05.json` | S100 | `Fri Oct 23 10:00:17 AM UTC 2026` |
| g-restored | `fetch-06.json` | S101 | `Fri Oct 23 10:00:17 AM UTC 2026` |
| h-mutated | `fetch-01.json` | S097 | `Fri Oct 23 10:00:39 AM UTC 2026` |
| h-mutated | `fetch-02.json` | S098 | `Fri Oct 23 10:00:39 AM UTC 2026` |
| h-mutated | `fetch-03.json` | S099 | `Fri Oct 23 10:00:39 AM UTC 2026` |
| h-mutated | `fetch-04.json` | S100 | `Fri Oct 23 10:00:39 AM UTC 2026` |
| h-mutated | `fetch-05.json` | S101 | `Fri Oct 23 10:00:39 AM UTC 2026` |
| h-restored | `fetch-01.json` | S096 | `Fri Oct 23 10:01:06 AM UTC 2026` |
| h-restored | `fetch-02.json` | S097 | `Fri Oct 23 10:01:07 AM UTC 2026` |
| h-restored | `fetch-03.json` | S098 | `Fri Oct 23 10:01:07 AM UTC 2026` |
| h-restored | `fetch-04.json` | S099 | `Fri Oct 23 10:01:10 AM UTC 2026` |
| h-restored | `fetch-05.json` | S100 | `Fri Oct 23 10:01:10 AM UTC 2026` |
| h-restored | `fetch-06.json` | S101 | `Fri Oct 23 10:01:10 AM UTC 2026` |

# Scope close

All eight assigned probes completed; exact tracked bytes were restored after each probe, including the final h restore. The bounded detector was run on pristine, each isolated mutant, and every restored world. This report makes no overall round-admission judgment and proposes no change to the counter, row rule, or targets. The L1's other semantic review seats, not these counts alone, cover the remaining content claim.

Report: .ufo/waves/round-59/falsify/MutC1Content.md
