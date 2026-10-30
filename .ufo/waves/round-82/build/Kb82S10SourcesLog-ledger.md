# Round-82 mutable SOURCES transitions — integration draft

Axes: freshness; operability.
Named base: `47dbe8781657de563ff867caca6244d28e3db504`.
This draft records evidence, not an applied production edit or a passing gate.

## Proposed round lesson insertion

**2026-10-30 — S248 reopened before admission.** Opened `https://code.claude.com/docs/en/agent-sdk/skills.md` at 2026-10-30T14:39:20Z (fetch start): HTTP 200, curl exit 0, 28395 bytes, sha256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`. Fresh bytes are retained in `.ufo/waves/round-82/build/Kb82S10SourcesLog-sdk.md`; they compare equal to `.ufo/waves/round-81/snapshots/S249.md` (cmp exit 0). This is a new fetch, not inherited access evidence. Freshly read lines 344–350 and 385–391 locate the pre-approval/managed-override paragraph and the exact quote “The list pre-approves the named tools rather than restricting the others.”

| Source | Mutable cell | Frozen base old value | Round-82 proposed value | Disposition/evidence |
|---|---|---|---|---|
| S248 | status | queued | mined | Eligible after the fresh fetch above and direct read of its located spans. Current working row was already `mined` when this seat inspected it; this seat neither applied nor establishes the chronology of that edit. |
| S248 | recheck | 90d | 90d | No transition. Preserve. |
| S248 | used-by | corpus/knowledge/allowed-tools-sdk-round81.md | corpus/knowledge/allowed-tools-sdk-round81.md | No transition. Existing target resolves at base and working tree; target line 2 explicitly begins `source: S248`. |

Only `status`, `recheck`, and `used-by` may change in place, per `verifiers/check_sources_append_only.py:5–7,30`. The `opened` cell is protected: retain `2026-10-27`; today's re-open belongs in this lesson ledger and access receipt, not an in-place rewrite. Preserve all other protected cells, including the historical anchor and teaches text. No source-row append or newly counted expansion is proposed here.

## Explicit limits and conflicts

- Exact frozen status tail: `| queued | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-sdk-round81.md |`.
- Exact observed working status tail: `| mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-sdk-round81.md |`.
- Fresh access now supports admission, but cannot prove the already-observed edit happened after source opening. L1 must preserve actual chronology, not backdate this receipt.
- The protected teaches cell still says “a documented surface outside the frozen six, held queued”. That historical wording is not edited in place by this draft.
- The first inherited S248 located quote crosses a Markdown link and is not a literal contiguous raw span. The resolving used-by entry already records this defect in its Limits section. This report does not silently normalize, replace, or claim validation of that inherited quote; the second quote was directly located in the fresh source.
- S249 uses the same URL and snapshot; this fetch reopens their shared document, but no S249 mutable-cell change is proposed.
- S251 has not been opened by this seat. Its reserved loader source remains outside this ledger's admission evidence.

## Sources actually opened during this seat

1. Current registry S248/S249 shared SDK Markdown URL: new HTTP 200 fetch, raw spans read, digest and cmp above. Relevant current access evidence.
2. Historical staged round-72 `S248` Vercel artifact: opened and checksum-verified (`d9c8dbd5cd080dab56554be7069eeecb8c7d357e2d7366a1ed9add10f91464dc`, sha256sum -c exit 0); also fetched its Vercel URL, HTTP 200, 899272 bytes, digest `ebf0ad3812912f397963d57c519dc002ca1360b82bc150a424e8e7ff71bf42f6`. This was an initial identifier collision during discovery, NOT current registry S248. The fetched HTML's claims were not validated, and it supplies no evidence for the SDK transition.
3. Local contextual records read: round-82 plan, current SOURCES header/row, round-81 reopen report, base and current `allowed-tools-sdk-round81.md`, and append-only verifier rule text. Reading these is not re-executing their reported checks or reopening all their cited sources.

VERDICT: SDK source freshly opened and existing used-by resolved; S248 status-only ledger drafted, with working-tree chronology and inherited quote defects explicitly retained.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S10SourcesLog-ledger.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S10SourcesLog-sdk.md
