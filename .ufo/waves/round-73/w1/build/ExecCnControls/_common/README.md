# `_common` — the honest scaffold, not a candidate submission

This tree is applied first by worlds 2-6. It is the baseline the shortcut
worlds perturb: one entry at the frozen path, six `mined` registry rows, six
sha256-pinned page snapshots and their manifest. It reads **4 of 4** (exit 0)
under both `own-reading.py` and the wave-1 counter draft, and its registry is
census-clean (exit 0, the 20 pre-existing W04 warnings only) — so each world's
failure is attributable to that world's defect.

The lane's real entry is the Scribe's to write; the text here exists only to
give the worlds a satisfying baseline. Nothing in the lane was edited.

## Files

    tree/corpus/knowledge/chinese-vendor-skill-surfaces-round73.md
    tree/corpus/SOURCES.md                        (base + six rows under ## Registry)
    tree/.ufo/waves/round-73/snapshots/S217.page … S222.page
    tree/.ufo/waves/round-73/snapshots/MANIFEST.sha256

## Snapshot provenance (byte copies; sha256 of the committed bytes)

| commit id | copied from (wave-1 build artifact) | bytes | sha256 |
|---|---|---|---|
| S217 | `ExecSrcTrae/snapshot.md` | 13351 | `3126996917f9e14f81beec94c98f4fc19c6f52819a94776a1b3912ac314aa28b` |
| S218 | `ExecSrcCodebuddyIde/snapshot.md` | 3887 | `a8aa1e094eb638f3437c12aab9f9d7608739836132ad0a9a7c8e427562213453` |
| S219 | `ExecSrcCodebuddyCli/snapshot.md` | 25241 | `88468f4f5f80055a86c5107eb87d530485bc8003313a742a214c55a4cfe4f784` |
| S220 | `ExecSrcKimiEn/snapshot.md` | 13528 | `5a18c3384e8e91be4cb99570a83b62a046aeddb434d6bed403bab72592b43c52` |
| S221 | `ScoutCnCensus/snap/kimicom.txt` | 8370 | `fb4a3c44755510c92dc53c24c390f499bfabfa7e5331d5f2a93906fb3fdc2486` |
| S222 | `ExecSrcZhipu/snapshot.md` | 7381 | `b20e45c7ff0bb09bd0164e5148162a9cda8e9ccd8f5140c8bb1578fb24961618` |

The copied artifacts are those seats' own fetches of this wave; this scaffold
does not re-fetch anything and makes no claim about the pages. S221 is the
scout's text extraction (HTML shell included), so its quote sits further into
the file than the other five.

## Manifest convention (an assumption a reviewer must check)

`MANIFEST.sha256` lines are `<sha256>  <bare filename>` and the files sit under
`.ufo/waves/round-73/snapshots/` (the round-59/round-60 `<S###>.page`
convention). The counter draft resolves a cited id by that filename prefix; a
manifest that pinned repo-root-relative paths would need both changed together.
