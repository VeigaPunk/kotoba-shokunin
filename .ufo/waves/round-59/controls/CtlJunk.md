Result: DONE — CtlJunk: S 0 of 7; F 0 of 7; G 0; exit 1; predicate NOT MET

## Control and frozen contract

Control: `CtlJunk`. Measured commit: sandbox b75bdf760b8b98009c2b5cc98b661923c7deef5e (/fast/scratch/hyaku/kotoba-r59/CtlJunk). This is one control-world commit on freeze `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`, retained by sandbox branch `ctl-junk-control`; no lane code was edited.

Axes: sandbox isolation, frozen-detector fidelity, reproducible junk rejection.

The constants were read from the committed counter at freeze: `verifiers/check_hook_files.py:253-254`, `TARGET = 4`, `NEW_TARGET = 5`. The row rule/census/predicate were read from `plans/round-59.md:22-83`. Its freeze addendum at `plans/round-59.md:93-98` limits Events to printed identifiers: it does not establish that a printed identifier is a hook event; semantic checks remain separately routed.

Expected detector: the unmodified frozen CLI must not accept this junk world. With `--fetch`, require exit 1, F=0, G=0 rather than meeting F>=4 and G>=5. Without `--fetch`, the contract always returns 1 and G=0; it is not the predicate.

### Counter identity

Lane read-only committed-byte hash command (exit 0):

```text
env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE timeout 30 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 67b68e0f9a0c48e5aa5ced63e6117cfca69da491:verifiers/check_hook_files.py | sha256sum
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  -
```

From `/fast/scratch/hyaku/kotoba-r59/CtlJunk` (exit 0):

```text
$ timeout 10 sha256sum verifiers/check_hook_files.py
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
```

## Mutant world

Mutation: add seven client rows in both required table shapes, with invented dot-led path tokens, two invented backticked identifier spans per Events cell, and five-word nonsense actions. Add new S096–S102 rows with random non-pinned `.invalid` hosts and junk metadata (`kind=zunvek`, `tier=Q`, `status=pirnaq`, `opened=xolvem`). Quotes are six nonsense words including the matching path token, with no hook/hooks word. Every quote is in `## Gate`; every invented snapshot carries that quote and both event strings; each exact snapshot SHA-256 is written into its SOURCES row. Required headers, client identities, source IDs, SHA labels and digests are structural, not claims of genuine evidence.

Sandbox commit evidence locations: `SKILL.md:599-609`; `corpus/knowledge/hook-files-round59.md:3-11`; `corpus/SOURCES.md:108-114`; `corpus/lessons/round-59.md:3-13`; `.ufo/waves/round-59/snapshots/S096.page:1` through `S102.page:1`. The world builder reused the counter's CLIENTS, snapshot_path and cells helpers; it extracted and reused the self-test's page_for and src_row builders (`verifiers/check_hook_files.py:1844-1890`) without running the self-test or altering any counter globals/bytes.

| Client | Source | Invented token | Invented Events |
|---|---|---|---|
| Claude Code | S096 | `.zz/qq.json` | `Qelvok`, `Marnix` |
| Codex | S097 | `.vx/mb.toml` | `Tuvrel`, `Pasken` |
| VS Code | S098 | `.jp/nu.json` | `Ziflor`, `Bemnaq` |
| Copilot CLI | S099 | `.ra/tx.conf` | `Nuvdex`, `Kolmir` |
| Gemini CLI | S100 | `.qm/vb.yaml` | `Ravpoq`, `Xendul` |
| Cursor | S101 | `.nk/ud.json` | `Fiznem`, `Worpak` |
| opencode | S102 | `.wf/ez.toml` | `Dalqim`, `Suvret` |

### Synthetic snapshot pins (not fetched pages)

| Source | Invented URL | Bytes | SHA-256 written into row |
|---|---|---|---|
| S096 | https://vydokq.invalid/velmor | 99 | `99c14d8543d0135f1ca340c8d9f23fee86e614b23b82f43ca8ae4c6af46bc3f0` |
| S097 | https://xenqup.invalid/zavrik | 98 | `3a39471acf3c4aec7108b9244b42c1c706515a95ed4fc43549c310f26acb8899` |
| S098 | https://fumrak.invalid/torvex | 99 | `426e3e46cbf1723a5cf001417572e4d60d7431c38f09ccab1dd3996d4f2cb5ec` |
| S099 | https://qavton.invalid/bexnal | 99 | `cdd25e5fee26b0a27e7973c1084dee484e755573b932e2c73a081b58a341a8e9` |
| S100 | https://nulpix.invalid/ximvar | 99 | `94c1ed53c33f7df2ec5be4af58cd0116fc7ae2598fd999373526bb84debb1d83` |
| S101 | https://jivqem.invalid/kalvex | 99 | `41eddc565b2670d371b55c43cb221f2a148632143e2c5365384c7383b46ecdc0` |
| S102 | https://bemzar.invalid/pernul | 99 | `983a89e2dc456fbd1fb563c6e5eb64c42b8d6373a2d7879436399c93d9d137f2` |

No synthetic content is claimed to be a vendor quote or an opened source. [INFERENCE from S=0 and `verifiers/check_hook_files.py:2383-2397`] the fetch loop has no backed clients and contacts none of these URLs. No HTTP status or source-access time is claimed. The date lines below are actual `date -u` invocation timestamps.

## Bounded detector receipts

All six commands ran from the sandbox, with GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE removed from the environment. Each uses the same frozen counter and `timeout 900`. Full stdout and exit code follow; stderr was empty in every case.

### Pristine — without --fetch

```text
Fri Oct 23 09:22:31 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
hook files backed on committed snapshots 0 of 0; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
stderr: (empty)
exit code: 1
```

### Pristine — with --fetch

```text
Fri Oct 23 09:22:32 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491 --fetch
hook files backed on committed snapshots 0 of 0; found on the live page 0 of 0; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
stderr: (empty)
exit code: 1
```

### Mutated — without --fetch

```text
Fri Oct 23 09:25:20 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev b75bdf760b8b98009c2b5cc98b661923c7deef5e
hook files backed on committed snapshots 0 of 7; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev b75bdf760b8b98009c2b5cc98b661923c7deef5e
reject Claude Code: entry row S096: quote holds no hook/hooks word outside the token; S096 kind 'zunvek' (need docs); S096 tier 'Q'; S096 status 'pirnaq'; S096 opened 'xolvem'; S096 URL 'https://vydokq.invalid/velmor' is not on a pinned host
reject Codex: entry row S097: quote holds no hook/hooks word outside the token; S097 kind 'zunvek' (need docs); S097 tier 'Q'; S097 status 'pirnaq'; S097 opened 'xolvem'; S097 URL 'https://xenqup.invalid/zavrik' is not on a pinned host
reject VS Code: entry row S098: quote holds no hook/hooks word outside the token; S098 kind 'zunvek' (need docs); S098 tier 'Q'; S098 status 'pirnaq'; S098 opened 'xolvem'; S098 URL 'https://fumrak.invalid/torvex' is not on a pinned host
reject Copilot CLI: entry row S099: quote holds no hook/hooks word outside the token; S099 kind 'zunvek' (need docs); S099 tier 'Q'; S099 status 'pirnaq'; S099 opened 'xolvem'; S099 URL 'https://qavton.invalid/bexnal' is not on a pinned host
reject Gemini CLI: entry row S100: quote holds no hook/hooks word outside the token; S100 kind 'zunvek' (need docs); S100 tier 'Q'; S100 status 'pirnaq'; S100 opened 'xolvem'; S100 URL 'https://nulpix.invalid/ximvar' is not on a pinned host
reject Cursor: entry row S101: quote holds no hook/hooks word outside the token; S101 kind 'zunvek' (need docs); S101 tier 'Q'; S101 status 'pirnaq'; S101 opened 'xolvem'; S101 URL 'https://jivqem.invalid/kalvex' is not on a pinned host
reject opencode: entry row S102: quote holds no hook/hooks word outside the token; S102 kind 'zunvek' (need docs); S102 tier 'Q'; S102 status 'pirnaq'; S102 opened 'xolvem'; S102 URL 'https://bemzar.invalid/pernul' is not on a pinned host
stderr: (empty)
exit code: 1
```

### Mutated — with --fetch

```text
Fri Oct 23 09:25:20 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev b75bdf760b8b98009c2b5cc98b661923c7deef5e --fetch
hook files backed on committed snapshots 0 of 7; found on the live page 0 of 7; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev b75bdf760b8b98009c2b5cc98b661923c7deef5e
reject Claude Code: entry row S096: quote holds no hook/hooks word outside the token; S096 kind 'zunvek' (need docs); S096 tier 'Q'; S096 status 'pirnaq'; S096 opened 'xolvem'; S096 URL 'https://vydokq.invalid/velmor' is not on a pinned host
reject Codex: entry row S097: quote holds no hook/hooks word outside the token; S097 kind 'zunvek' (need docs); S097 tier 'Q'; S097 status 'pirnaq'; S097 opened 'xolvem'; S097 URL 'https://xenqup.invalid/zavrik' is not on a pinned host
reject VS Code: entry row S098: quote holds no hook/hooks word outside the token; S098 kind 'zunvek' (need docs); S098 tier 'Q'; S098 status 'pirnaq'; S098 opened 'xolvem'; S098 URL 'https://fumrak.invalid/torvex' is not on a pinned host
reject Copilot CLI: entry row S099: quote holds no hook/hooks word outside the token; S099 kind 'zunvek' (need docs); S099 tier 'Q'; S099 status 'pirnaq'; S099 opened 'xolvem'; S099 URL 'https://qavton.invalid/bexnal' is not on a pinned host
reject Gemini CLI: entry row S100: quote holds no hook/hooks word outside the token; S100 kind 'zunvek' (need docs); S100 tier 'Q'; S100 status 'pirnaq'; S100 opened 'xolvem'; S100 URL 'https://nulpix.invalid/ximvar' is not on a pinned host
reject Cursor: entry row S101: quote holds no hook/hooks word outside the token; S101 kind 'zunvek' (need docs); S101 tier 'Q'; S101 status 'pirnaq'; S101 opened 'xolvem'; S101 URL 'https://jivqem.invalid/kalvex' is not on a pinned host
reject opencode: entry row S102: quote holds no hook/hooks word outside the token; S102 kind 'zunvek' (need docs); S102 tier 'Q'; S102 status 'pirnaq'; S102 opened 'xolvem'; S102 URL 'https://bemzar.invalid/pernul' is not on a pinned host
stderr: (empty)
exit code: 1
```

### Restored — without --fetch

```text
Fri Oct 23 09:25:20 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
hook files backed on committed snapshots 0 of 0; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
stderr: (empty)
exit code: 1
```

### Restored — with --fetch

```text
Fri Oct 23 09:25:20 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491 --fetch
hook files backed on committed snapshots 0 of 0; found on the live page 0 of 0; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
stderr: (empty)
exit code: 1
```

C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) — NOT MET

## Verdict and limits

The junk control was rejected: S=0 of K=7, F=0 of K=7, G=0, exit 1. All seven tokens entered K, so the table/row/token shapes were not merely ignored. Each rejection names the missing hook/hooks word, junk kind/tier/status/opened fields, and the off-pin host. No rejection names a snapshot digest mismatch or missing snapshot/event/quote.

Mutation-test verdict: **INCONCLUSIVE**, not killed and not survived. The pristine frozen world already exits 1 with 0 of 0, so this is a completed negative-control receipt, not a pass-to-fail mutation kill. No satisfying baseline was invented, no predicate was weakened, and no semantic Events guarantee is claimed.

## Exact restoration

The mutation probe used a finally block. Restore command (exit 0):

```text
$ timeout 30 git checkout -q 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
```

SHA-256 was measured before mutation, at the sandbox control commit, and after restoration. `ABSENT` means the added path did not exist. All original bytes match after restoration; all nine added world paths are absent again. The counter SHA-256 is identical in all three states.

| Path | Pristine SHA-256 | Mutated SHA-256 | Restored SHA-256 |
|---|---|---|---|
| `verifiers/check_hook_files.py` | `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` | `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` | `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` |
| `SKILL.md` | `2af0a1a9c09fd241ce0c146976f4996f08714f2413b55f283ef8fdf5a1111e07` | `299e4f600e1441802f307617ee3c306e6dfbf8ac8b089fd87e309de6317cdd5e` | `2af0a1a9c09fd241ce0c146976f4996f08714f2413b55f283ef8fdf5a1111e07` |
| `corpus/knowledge/hook-files-round59.md` | `ABSENT` | `900ae68a1368125af2c1547fe4b98132c4d4486635e5ad61bf6b51536d9d5bf4` | `ABSENT` |
| `corpus/SOURCES.md` | `9656d5d9d882d24b3b71f5ce63f96a4fd2a1732d90576b56fd5763350374d150` | `fa5349fa0b63f724537ce77c8eca8e79e40681606fa29115116a35057e5acba8` | `9656d5d9d882d24b3b71f5ce63f96a4fd2a1732d90576b56fd5763350374d150` |
| `corpus/lessons/round-59.md` | `ABSENT` | `91b85c71b1676f08e597b5256e449fca6b593ad677fbfff4ec2f4a8899d30983` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S096.page` | `ABSENT` | `99c14d8543d0135f1ca340c8d9f23fee86e614b23b82f43ca8ae4c6af46bc3f0` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S097.page` | `ABSENT` | `3a39471acf3c4aec7108b9244b42c1c706515a95ed4fc43549c310f26acb8899` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S098.page` | `ABSENT` | `426e3e46cbf1723a5cf001417572e4d60d7431c38f09ccab1dd3996d4f2cb5ec` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S099.page` | `ABSENT` | `cdd25e5fee26b0a27e7973c1084dee484e755573b932e2c73a081b58a341a8e9` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S100.page` | `ABSENT` | `94c1ed53c33f7df2ec5be4af58cd0116fc7ae2598fd999373526bb84debb1d83` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S101.page` | `ABSENT` | `41eddc565b2670d371b55c43cb221f2a148632143e2c5365384c7383b46ecdc0` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S102.page` | `ABSENT` | `983a89e2dc456fbd1fb563c6e5eb64c42b8d6373a2d7879436399c93d9d137f2` | `ABSENT` |

The restored no-fetch receipt exactly equals the pristine no-fetch stdout/stderr/exit; the restored fetch receipt exactly equals the pristine fetch stdout/stderr/exit. The working checkout is back at freeze; the control commit remains available by `ctl-junk-control`. Scratch-only receipt records are in `ctl-junk-receipts/` (the six detector JSON records, world manifest, command records, and three hash manifests). Generated import bytecode was removed before the control commit.

Tools installed or updated: none. No task spawns, model/client calls, pushes, lane Git writes, fleet-root writes or other orchestration runtime invocations were performed. Only this requested report was written in the lane.

Report: .ufo/waves/round-59/controls/CtlJunk.md
