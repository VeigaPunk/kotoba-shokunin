# ExecReceiptRevs — receipt revision resolution

Axes: revision identity correctness, scratch-world separation, read-only operation.

One executable production file in the patch: `verifiers/fixtures/round-93/check-receipt-revs.sh` (bash, set -u, embedded Python stdlib). No production lane file edited. Patch base: `6d7eee0570912d9f3b9d3e3d0137f3c755451233`.

Scans regular files recursively; counts occurrences, not unique hashes. Resolves G1 12-hex prefixes with git rev-parse --verify -q <prefix>^{commit}, then checks commits using git -C REPO cat-file -e <hex>^{commit}. Extracts every full 40-hex token on the specified header lines, including a base token if present. Scratch declarations are line-local and case-insensitive; never counted as resolved. Symlink files are excluded. Scratch count precedes the exact requested final summary. No network or repository writes inside checker.

Exit ladder: 0 for at least one resolved occurrence and no misses; 1 for unresolved occurrences; 2 for no candidates, missing directory, unreadable input or bad usage.

## Four assigned probes (verbatim)

### round92

```text
$ bash /fast/scratch/hyaku/kotoba-r93/ExecReceiptRevs/repo/verifiers/fixtures/round-93/check-receipt-revs.sh /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-92/receipts/landing /home/vgpnk/Projects/shokunin/kotoba-shokunin
UNRESOLVED cd355c4796fa165ff2b7d822401b4027da29e4d0 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-92/receipts/landing/controls-run.stderr:23
UNRESOLVED cd355c4796fa165ff2b7d822401b4027da29e4d0 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-92/receipts/landing/controls-run.stderr:52
UNRESOLVED cd355c4796fa165ff2b7d822401b4027da29e4d0 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-92/receipts/landing/landing-rev.txt:1
UNRESOLVED cd355c4796fa165ff2b7d822401b4027da29e4d0 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-92/receipts/landing/tip-battery.txt:1
3 scratch-declared
receipt revisions: 1 resolved, 4 unresolved over 18 files
exit=1
```

### round93

```text
$ bash /fast/scratch/hyaku/kotoba-r93/ExecReceiptRevs/repo/verifiers/fixtures/round-93/check-receipt-revs.sh /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-93/receipts /home/vgpnk/Projects/shokunin/kotoba-shokunin
2 scratch-declared
receipt revisions: 2 resolved, 0 unresolved over 5 files
exit=0
```

### fabricated

```text
$ bash /fast/scratch/hyaku/kotoba-r93/ExecReceiptRevs/repo/verifiers/fixtures/round-93/check-receipt-revs.sh /fast/scratch/hyaku/kotoba-r93/ExecReceiptRevs/fake /home/vgpnk/Projects/shokunin/kotoba-shokunin
UNRESOLVED 1111111111111111111111111111111111111111 /fast/scratch/hyaku/kotoba-r93/ExecReceiptRevs/fake/rev.txt:1
0 scratch-declared
receipt revisions: 0 resolved, 1 unresolved over 1 files
exit=1
```

### real

```text
$ bash /fast/scratch/hyaku/kotoba-r93/ExecReceiptRevs/repo/verifiers/fixtures/round-93/check-receipt-revs.sh /fast/scratch/hyaku/kotoba-r93/ExecReceiptRevs/real /home/vgpnk/Projects/shokunin/kotoba-shokunin
0 scratch-declared
receipt revisions: 1 resolved, 0 unresolved over 1 files
exit=0
```

## Findings

- Round-92 landing fails at four occurrences of cd355c4796fa165ff2b7d822401b4027da29e4d0, including landing-rev.txt:1. The one resolved occurrence is the base commit on tip-battery.txt:1, not the landing identity.
- Round-92 G1 text includes scratch, so its prefix is scratch-declared as required. The two world rev declarations provide the other two scratch occurrences.
- Round-93 pre-data passes with two lane-base occurrences; two forgery headers contain scratch paths and count separately. This is not a claim about future landing receipts.
- Fabricated hash rejected; real-only fixture passes.

## Patch handoff

fresh freeze clone: git apply --check PASS
exit=0

Patch SHA-256: `e172509b5695b2ada2f4859b28d4d85b6e9953f032856d9c489dd0ae48954ab3`.
Fresh second clone checked out at freeze; git apply --check exited 0. Scratch clones and fixtures removed by EXIT trap after retaining evidence. No commits created. No tools installed or upgraded.

## Risks and limits

Scratch classification honors any line containing world rev, scratch or forgery; this is a declaration rule, not proof of provenance. Resolution cannot certify that a receipt names the desired landing revision. Prefix and empty-input arms implemented but not separately exercised. Only four assigned checker probes and patch applicability run. LSP unavailable in this seat tool inventory; no symbol service used for the new shell entry point.

Self-evaluation: accuracy 4 (four probes observed; other arms unexercised), completeness 4 (implementation and patch protocol complete, broader gates not claimed), clarity 4 (literal evidence retained, repeated paths), actionability 5 (single-file patch, hash, apply proof), conciseness 4 (verbatim evidence repeats paths). Overall 4.2. Parent should integrate and check actual committed landing receipts.
