# Kb82S10SourcesLog — mutable SOURCES ledger

Axes: freshness; operability. Base: `47dbe8781657de563ff867caca6244d28e3db504`.

## Behavior and findings

Drafted a lesson-ready mutable-cell ledger in `build/Kb82S10SourcesLog-ledger.md`. Current registry S248 is the Claude Agent SDK skills page, not the round-72 staged Vercel source with the same identifier. Freshly fetched the correct SDK document this round, read its pre-approval and grant-note spans, and resolved its existing used-by file, including explicit `source: S248` on line 2 at both the named base and current tree.

The frozen base row is `queued`; the working row was already `mined` when inspected. This seat did not mutate that row and cannot attest that the existing edit followed the fresh access. Preserve this chronology conflict rather than upgrading the new receipt into evidence for an earlier action.

Only proposed mutable transition: **S248.status queued → mined**. `recheck=90d` and `used-by=corpus/knowledge/allowed-tools-sdk-round81.md` stay unchanged. `opened=2026-10-27` is protected and must not be updated in place. The ledger retains the historical teaches phrase “held queued” and the inherited first quote's Markdown-link discontinuity; neither is silently repaired.

## Commands and observed outcomes

Fresh access command (executed from this seat's scratch, TMPDIR set):

```sh
export TMPDIR=/fast/scratch/hyaku/kotoba-r82/Kb82S10SourcesLog/tmp
date -u '+%Y-%m-%dT%H:%M:%SZ'
curl -sS -L -A Mozilla/5.0 --max-time 60 -o /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S10SourcesLog-sdk.md -w 'http=%{http_code} bytes=%{size_download} effective=%{url_effective}\n' https://code.claude.com/docs/en/agent-sdk/skills.md
printf 'curl_exit=%s\n' "$?"
sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S10SourcesLog-sdk.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/snapshots/S249.md
printf 'sha_exit=%s\n' "$?"
cmp /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S10SourcesLog-sdk.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/snapshots/S249.md
printf 'cmp_exit=%s\n' "$?"
```

Exact output:

```text
2026-10-30T14:39:20Z
http=200 bytes=28395 effective=https://code.claude.com/docs/en/agent-sdk/skills.md
curl_exit=0
ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S10SourcesLog-sdk.md
ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/snapshots/S249.md
sha_exit=0
cmp_exit=0
```

Read fresh source lines 344–350 and 385–391 directly. Exact located quote: “The list pre-approves the named tools rather than restricting the others.” No SDK runtime was invoked.

Frozen provenance commands:

```sh
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -n -F '| S248 |' 47dbe8781657de563ff867caca6244d28e3db504 -- corpus/SOURCES.md
printf 'exit=%s\n' "$?"
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 47dbe8781657de563ff867caca6244d28e3db504:corpus/knowledge/allowed-tools-sdk-round81.md
printf 'exit=%s\n' "$?"
sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/knowledge/allowed-tools-sdk-round81.md
printf 'sha_exit=%s\n' "$?"
```

Both git commands exit 0. Exact frozen row is retained in transcript artifact `artifact://32667:raw:1-2`; its tail is `| queued | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-sdk-round81.md |`. Working row tail read directly: `| mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-sdk-round81.md |`.
Observed working-file digests (not immutable production pins): SOURCES `c48d3340ad833b2df752d878157cf8cbe5d31b3acc3f0a06dbdd1b8fdf78a5af`; consumer `fe57322c535b281a7c60ddf89f31812ebff26ec4739b8daa3b9b3a8d3eecb8be`; sha_exit=0.

## Other opened material and discovery detour

Read plan, tooling rules, godspeed skill, registry schema, prior reopen report, current/base consumer, and append-only verifier rule text. No historical receipt was treated as present access.

Initial broad discovery conflated historical staged S248 with the current ID. Opened `.ufo/waves/round-72/snapshots/S248-vercel-agents-md.md`: `sha256sum -c S248.sha256` returned `S248-vercel-agents-md.md: OK`, sha_exit=0; digest `d9c8dbd5cd080dab56554be7069eeecb8c7d357e2d7366a1ed9add10f91464dc`, 11843 bytes. Also ran a curl fetch of `https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals` into this seat's scratch: curl_exit=0, http_code=200, 899272 bytes, sha256 `ebf0ad3812912f397963d57c519dc002ca1360b82bc150a424e8e7ff71bf42f6`. Its claims were not validated. This detour is excluded from current S248 admission evidence; temporary HTML was removed with scratch.

## Gates, touched surfaces, limits

No production gate, self-test, C1/C2 after-value, score, census, or tip battery was run or claimed. Main/L1 owns integration and any append-only round-range check. This draft does not certify all round-82 source openings; it lists this seat's actual accesses. S251 was not opened by this seat and receives no admission evidence here.

Only writes: this report, the ledger draft, fresh SDK snapshot, and this seat's removed scratch. No product/code/registry/plan changes; no commits, pushes, index/jj mutations, tool installs/upgrades, pacman transactions, or SDK invocation.

Disk guard command `bash /home/vgpnk/Projects/shokunin/scripts/hyaku/disk-guard.sh status 2>&1; echo "exit=$?"` exited 0: root 25% / 96.8G free; scratch 47% / 429.4G free. No heavy gate performed. Three initial finite commands were inadvertently submitted as named supervised services (`diskguard`, `snapcheck`, `livefetch`); all exited 0, none remains running, and none was polled repeatedly. Their completed outputs were read once; this exception is reported rather than hidden.

Cleanup command `rm -r -- /fast/scratch/hyaku/kotoba-r82/Kb82S10SourcesLog; printf 'cleanup_exit=%s\n' "$?"` returned cleanup_exit=0.

Report: .ufo/waves/round-82/w1/Kb82S10SourcesLog.md
VERDICT: Fresh SDK access and used-by resolution established; status-only integration ledger complete, with pre-existing working edit chronology unproven and inherited quote defect retained.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82S10SourcesLog.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S10SourcesLog-ledger.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S10SourcesLog-sdk.md
