# SentScope — round 67 wave 1

Snapshot: `2026-10-24T20:48:19-03:00` (final evidence rerun). Pinned lane base: `2a8eba56b3f9321b70c569fa2816d42237ca49a2`. Measured lane `HEAD`: `2a8eba56b3f9321b70c569fa2816d42237ca49a2`. Fleet-root `HEAD`: `7b7da895e373afe0b0fafbcb72fe3b2673f3af07`.
The lane `HEAD` is reported separately from the working-tree status below; no claim predicates were run by this sentinel.

## Findings

| ID | Severity | Observed finding | Impact | Smallest remediation |
|---|---|---|---|---|
| S1 — fleet-root scope | None observed on requested filter | `0` untracked, non-driver Git status paths outside the lane named `kotoba` or `round-67`. | No matching fleet-root scope signal in this snapshot. | No action for S1; retain the filter evidence below. |
| S2 — shokuknow recent mtimes | Review-required; attribution unknown | `577` files under `/home/vgpnk/Projects/shokuknow` matched the required 40-minute mtime scan. `0` of the separate hits under the assigned `merge/kotoba` package. | The wider shokuknow tree was not quiescent. These hits alone do not attribute a write to this wave or to any seat; the empty package-specific result does not establish who made the wider-tree changes. | L1/operator should attribute the recent-mtime hits before treating the wider tree as unchanged. This sentinel moved and deleted nothing. |
| S3 — lane non-w1 status | Review-required; attribution unknown | `199` expanded Git status paths were outside `.ufo/waves/round-67/w1/`; the full lines are below. They include paths from older rounds and round-67 driver/control paths, so presence is not proof of a seat violation. | A clean-lane or no-non-wave-change assertion is not supported by this snapshot. | L1 should reconcile only confirmed round-67 scope exceptions and leave historical/unrelated paths untouched; no automatic misroot sweep was performed here. |
| S4 — reports outside w1 | None observed in bounded scans | `0` candidate report paths from this wave's 32 declared seat names were found outside `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-67/w1` by the bounded recent-file scans. | No misrooted seat-report candidate was observed within the scanned locations. Arbitrary unsearched filesystem locations are not covered. | If a later integration check finds a candidate, L1 owns identification and any sweep. |

Exploit path: none tested; this was an observational scope audit. Evidence and exact outputs follow. The S4 result is bounded because an initial whole-fleet recent-file `find` exceeded the 120-second process bound and was killed; no whole-filesystem absence claim is made.

## S1 — fleet root

Requested command and observed stdout:
```console
$ git -C /home/vgpnk/Projects/shokunin status --porcelain
 M .ufo/state/chousa.report-baseline
 M .ufo/state/kagi.report-baseline
 M .ufo/state/kaidoku.report-baseline
 M .ufo/state/kake.report-baseline
 M .ufo/state/kama.report-baseline
 M .ufo/state/kengaku.report-baseline
 M .ufo/state/kumitate.report-baseline
 M .ufo/state/mado.report-baseline
 M .ufo/state/mori.report-baseline
 M .ufo/state/souji.report-baseline
 M .ufo/state/tameshi.report-baseline
 M .ufo/state/tsukuroi.report-baseline
 M .ufo/watchdog.log
?? .omp/mcp.json
?? .ufo/state/kotoba.report-baseline
?? .ufo/state/kotodama.report-baseline
?? .ufo/state/revenger.report-baseline
?? bm.json
?? live.html
?? live_s228.html
?? nama.html
?? s395.txt
?? scripts/hyaku/append-closure.py.bak-20261023T040735Z
?? scripts/hyaku/fleet-commit.sh.bak-20261023T040735Z
?? tf_bavelas.html
?? unblob.log
?? wb2.html
?? write
?? xc.xml
```
Exit code: `0`.
Stderr:

```text
<empty>
```

The expanded `-uall` rerun used to ensure every untracked path was visible:
```console
$ git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all
 M .ufo/state/chousa.report-baseline
 M .ufo/state/kagi.report-baseline
 M .ufo/state/kaidoku.report-baseline
 M .ufo/state/kake.report-baseline
 M .ufo/state/kama.report-baseline
 M .ufo/state/kengaku.report-baseline
 M .ufo/state/kumitate.report-baseline
 M .ufo/state/mado.report-baseline
 M .ufo/state/mori.report-baseline
 M .ufo/state/souji.report-baseline
 M .ufo/state/tameshi.report-baseline
 M .ufo/state/tsukuroi.report-baseline
 M .ufo/watchdog.log
?? .omp/mcp.json
?? .ufo/state/kotoba.report-baseline
?? .ufo/state/kotodama.report-baseline
?? .ufo/state/revenger.report-baseline
?? bm.json
?? live.html
?? live_s228.html
?? nama.html
?? s395.txt
?? scripts/hyaku/append-closure.py.bak-20261023T040735Z
?? scripts/hyaku/fleet-commit.sh.bak-20261023T040735Z
?? tf_bavelas.html
?? unblob.log
?? wb2.html
?? write
?? xc.xml
```
Exit code: `0`.
Stderr:

```text
<empty>
```

Filter applied to the expanded output: untracked paths only; exclude `.ufo/state/` and `.ufo/watchdog.log`; require `kotoba` or `round-67` in the path. Observed matching lines:

```text
<none>
```

## S2 — shokuknow

S2 evidence rerun at `2026-10-24T20:49:19-03:00`.

Required command and all observed stdout hits (not truncated in this report):
```console
$ find /home/vgpnk/Projects/shokuknow -newermt '-40 minutes' -type f
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/798dda31d8919c54ab82f2e4.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/798dda31d8919c54ab82f2e4.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/eb8db07d8c18a74f292c0ebc.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/eb8db07d8c18a74f292c0ebc.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/ae9511abf65efe4d0824ef1a.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/ae9511abf65efe4d0824ef1a.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/9fb472203129fd78ae818ce0.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/9fb472203129fd78ae818ce0.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/3e965c0cf1782dee6adf68c7.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/3e965c0cf1782dee6adf68c7.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/703d1c7aa1f1fd980a445ba0.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/703d1c7aa1f1fd980a445ba0.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/78491229df5cc4ccd077ab04.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/78491229df5cc4ccd077ab04.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/8dc0c34906c01a4b2d3e0c7e.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/8dc0c34906c01a4b2d3e0c7e.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/e6ed0970bcd1ff00a6b76a5b.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/e6ed0970bcd1ff00a6b76a5b.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/abd7513212eeb666fdfe5f56.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/abd7513212eeb666fdfe5f56.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/46872d17ba853ec79a53cec6.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/46872d17ba853ec79a53cec6.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/306fa33caaba3bf95b5d7154.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/31fae035abbfebb178b13913.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/f25602826878179b197462cc.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/31fae035abbfebb178b13913.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/19d963cced82515a57ed2ce7.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/f25602826878179b197462cc.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/306fa33caaba3bf95b5d7154.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/19d963cced82515a57ed2ce7.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/669d1f400c4fc71d73f5f62c.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/669d1f400c4fc71d73f5f62c.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/ce0c6a58a44234790b6b71df.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/d68390d39d4dcb4e36d3af81.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/b83f43497727b039ce549a02.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/7617d437b77cfaca690dd1d3.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/88b5859f0ab02d84aa168e33.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/0f80c99eefc2b70131701e9c.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/64e20710aec67a185df538d2.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/64e20710aec67a185df538d2.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/a623ae84bb829eeded4cd819.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/a623ae84bb829eeded4cd819.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/9411c5990196c0009b5953ee.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/d42eb7ee6cd3640328fbf74a.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/9411c5990196c0009b5953ee.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/13652a89d33041cf9ac8f9ab.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/50708c5cf8bc6de7b2d95367.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/f9c10a893188210d5d804b44.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/290f5665316725b0f8a2632d.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/290f5665316725b0f8a2632d.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/cc132c5ee2775fd7170d7f7d.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/cc132c5ee2775fd7170d7f7d.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/fd3f9e23229fb44030d80c3f.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/fd3f9e23229fb44030d80c3f.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/def404b0f0ef0d3f13b8536a.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/def404b0f0ef0d3f13b8536a.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/9644ee2dea335a364b3119f7.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/9644ee2dea335a364b3119f7.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/015352e29c644496d018ca20.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/015352e29c644496d018ca20.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/d7302a02a577499858035b4b.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/d7302a02a577499858035b4b.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/42a7d6cb18f9ce1b964c3138.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/114dc6a442161054dc851700.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/114dc6a442161054dc851700.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/266be2cf636dd42886880e68.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/88a92b4aff5312329fc9551e.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/1a2b63a0720661d58686c523.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/3086e06060b7bfb9553d35e5.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/9e6585382f72813b6ab958fa.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/d56e45e3d52be4f4ad8eb936.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/ee38dc2e08391c5b9ef406a9.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/3e7f35dd03e1fa8dd8fd1fce.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/53f61993f59552de6777a335.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/143d44de279cc35dbb9637c5.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/0b2df9b5e8b348dec2cfc225.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/0b2df9b5e8b348dec2cfc225.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/ad3ed0669aba0fb1c2827da5.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/3e5863d83bbadd3a6d9a499f.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/3e5863d83bbadd3a6d9a499f.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/143d44de279cc35dbb9637c5.pdf
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/143d44de279cc35dbb9637c5.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/b68b30300b5affe7c0f2591e.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/b68b30300b5affe7c0f2591e.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/03b37ed8c4323554b117b0ff.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/03b37ed8c4323554b117b0ff.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/be13f94fb77dc006a3d2b57b.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/be13f94fb77dc006a3d2b57b.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/ee6110d61ca6363d8b946dde.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/ee6110d61ca6363d8b946dde.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/209d430b2e9791544e9edc78.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/209d430b2e9791544e9edc78.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/5817f489f6e5faa900b446af.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/7bb66eabbfc017f60e7f6606.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/7bb66eabbfc017f60e7f6606.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/f8d76237eabdd32bf16b46c9.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/f8d76237eabdd32bf16b46c9.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/3805de50a98e855cbe6bec14.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/b251dcd95d2985e25f0f1e2d.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/b251dcd95d2985e25f0f1e2d.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/02093d300a0c64077ebe5abc.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/9fec3f89709c73856cfa7b4a.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/f9a3ddf07408f8c10367dde5.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/f9a3ddf07408f8c10367dde5.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/e46b7f1f695c11ea2879d231.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/693e1e75c06ee45ca29fff00.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/e46b7f1f695c11ea2879d231.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/693e1e75c06ee45ca29fff00.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/f72bb196393c13c709e17768.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/d404004de74bf2e09e2d1f2f.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/1edc43ecd19e2094001a096f.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/7e09e9dfbccc281aa7e254e0.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/53ec88ada82023af022af3d5.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/53ec88ada82023af022af3d5.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/2a54001dc202fb5c41bee094.fail
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/1d9f3c397e1de762f91cd2b8.raw
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/1d9f3c397e1de762f91cd2b8.pdf
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/1d9f3c397e1de762f91cd2b8.txt
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/round13-handles.json
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutKaidoku.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutMori.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutKake.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutSouji.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutKagi.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutKotoba.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutGameDev3d.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutKasegi.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutKotodama.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutMado.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutKumitate.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutKama.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutChousa.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutLore.md
/home/vgpnk/Projects/shokuknow/.ufo/scopes/corpus-expansion-15/ScoutTameshi.md
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/.deepresearch/20261024_202225_quoting-paper-and-journal-abstracts/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v1i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v1i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v2i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v2i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v3i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v3i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v4i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v4i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v5i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v5i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v6i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v6i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v7i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v7i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v8i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v8i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v9i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v9i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v10i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v10i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v11i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v11i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v12i1.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/fns/v12i2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/ia.json
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/trial_conf.pdf
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/trial_v1.pdf
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/ia2.json
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/trial_conf.txt
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/we329.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/we334.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/we292.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/erp_index.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/ol_in_epistemic+transition+systems.json
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/ol_in_knowledge+and+time+Dixon+Nalon+Ramanujam.json
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/gal.xml
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/erp_root.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/erp_pub.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/erp_book.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/erp_index2.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/erp_public.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/neohelicon.pdf
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/neohelicon.txt
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/wb.json
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_250.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_251.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_252.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_253.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_254.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_255.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_256.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_257.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_258.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_259.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_260.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_261.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_262.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_263.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_264.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_265.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_266.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_267.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_268.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_269.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_270.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_271.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_272.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_273.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_274.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_275.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_276.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_277.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_278.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_279.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_280.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_281.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_282.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/fetch/p_283.html
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/gate-census.sh
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/gate-census-raw.txt
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/gate-census.txt
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/route-probe.txt
/home/vgpnk/Projects/shokuknow/lanes/lore/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/.deepresearch/20261024_200044_gd3d_r15/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/measurements/godot/project.godot
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/measurements/godot/cap.tscn
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/measurements/godot/cap.gd
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/measurements/godot/godot_1.png
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/measurements/godot/godot_2.png
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/measurements/round15_measurements.txt
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/measurements/gate.py
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/measurements/compare.py
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/measurements/__pycache__/compare.cpython-314.pyc
/home/vgpnk/Projects/shokuknow/lanes/game-dev-3d/round15/measurements/chal.html
/home/vgpnk/Projects/shokuknow/lanes/kagi/round15/.deepresearch/20261024_200032_kagi-corpus-expansion/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/kagi/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/kagi/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/kagi/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kagi/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/kagi/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/kagi/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/mori/round15/.deepresearch/20261024_200039_mori-round15/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/kotodama/round15/.deepresearch/20261024_200046_kotodama-r15/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/kotodama/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/kotodama/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/kotodama/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kotodama/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kotodama/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/kotodama/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/kotodama/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/kasegi/round15/evidence/plan_json.html
/home/vgpnk/Projects/shokuknow/lanes/kasegi/round15/evidence/rmfyalk_request_shape_probe.txt
/home/vgpnk/Projects/shokuknow/lanes/kasegi/round15/.deepresearch/20261024_200104_round15-queue-closure/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/kasegi/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/kasegi/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/kasegi/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kasegi/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kasegi/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/kasegi/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/kasegi/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cman-dir.raw.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-cman-prefix.json.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/live-people80.raw.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/live-people.raw.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-root.raw.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-zh.raw.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/live-people80.raw.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-cman-prefix.json.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-root.raw.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-zh.raw.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/live-people.raw.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cman-dir.raw.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-root.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-zh.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/live-people80.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/live-people.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cman-dir.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-cman-prefix.json
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-cman-prefix2.json.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-people.json.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-uncheck.json.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-es.raw.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-people.raw.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-it.raw.code
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-uncheck.json.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-it.raw.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-cman-prefix2.json.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-es.raw.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-people.json.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-people.raw.hdr
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-it.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-es.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-people.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-uncheck.json
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-cman-prefix2.json
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cdx-people.json
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-uncheck.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cmpp-perpage-log-capture.txt
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-people-409.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-people-laser.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-people-meaculpa.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-people-mhss.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-people-xuming.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-pl.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-ru.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mp-tr.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-meaculpa-untrans.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-meaculpa-trans.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-xuming-checked.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/wb-mhss-checking.raw
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/cmpp-translator-lists-capture.txt
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/captures/mirror-siblings-capture.txt
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/tsukuroi/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/tabi/round8/.work/ratelimit-series.tsv
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/commit.json
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/openreplay-zh.html
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/devtools-zhtw.html
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/ot-blog-zhcn.html
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/model_context_tool.idl.b64
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/model_context_supplement.idl.b64
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/model_context.idl.b64
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/juejin-zh.html
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/model_context_tool.idl
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/model_context.idl
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/model_context_supplement.idl
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/extract.py
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/juejin-zh.txt
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/openreplay-zh.txt
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/devtools-zhtw.txt
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/ot-blog-zhcn.txt
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/st.json
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/model_context_tool_invocation.cc.b64
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/model_context.cc.b64
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/model_context.cc
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/model_context_tool_invocation.cc
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/html.json
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/forms.json
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/form_mcp_schema.cc.b64
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/html_form_element.cc.b64
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/form_mcp_schema.cc
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/html_form_element.cc
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/write_s239.py
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/write_s240.py
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/write_s241.py
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/write_s242.py
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/chromium-attr-sweep-r15.txt
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/.work/write_s243.py
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/tabi/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/.deepresearch/20261024_200054_souji-r15-leads/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/gitscm-gc-2520.html
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/gitscm-worktree-2520.html
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/qiita-yagrush-ja.html
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/liginc-ja.html
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/qiita-yagrush-ja.txt
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/liginc-ja.txt
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/gitscm-worktree-zh.html
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/cnblogs-worktree-zh.html
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/gitscm-worktree-zh.txt
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/cnblogs-worktree-zh.txt
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/qiita-yagrush-wayback.html
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/evidence/r35-fleet-expire-selection.out
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/fixtures/r35-fleet-expire-selection.sh
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/fixtures/append-entry.py
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/souji/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/kama/round15/.deepresearch/20261024_200607_kama_r15_leads/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/kama/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/kama/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/kama/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kama/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kama/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/kama/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/kama/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/kengaku/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/kengaku/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kengaku/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kengaku/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/kengaku/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/kengaku/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/kengaku/round15/arxiv-2608-29463-source-preprint.tex
/home/vgpnk/Projects/shokuknow/lanes/kengaku/round15/osf-disclosure-audit-manifest-v1.4.txt
/home/vgpnk/Projects/shokuknow/lanes/kengaku/round15/osf-disclosure-audit-codebook-v1.4.md
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/.deepresearch/20261024_200051_kake-r15-queue/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/.evidence/lane_sweeps_r15.sh
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/.evidence/baidu_series_sweep_r15.txt
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/.evidence/carrier_map_r15.txt
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/.evidence/cos_11424_r15.txt
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/.evidence/crux_nokey_r15.json
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/.evidence/urls_r15.txt
/home/vgpnk/Projects/shokuknow/lanes/kake/round15/.evidence/fetch_manifest_r15.txt
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/voices_games.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/plusmusic.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/mirelo.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/v_blog.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/v_press.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/p_blog.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/p_ent.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/sony_ai2.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/mirelo.txt
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/p_api.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/p_price.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/mirelo_price.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/sony_blog.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/v_wb.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/p_wb.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/mirelo_company.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/mirelo_blog.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/mirelo_api.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/p_wb2.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/mirelo_sfx2.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/mirelo_price2.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/mirelo_blog.txt
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/mirelo_price.txt
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/mirelo_sfx2.txt
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/v_g2.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/v_sitemap.xml
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/p_en.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/p_sitemap.xml
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/p_wb3.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/sony_wb.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/nc_alt.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/vm_games.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/evidence/tc_mirelo.html
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/audio/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/ipsj-index.html
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/ipsj-pdf.html
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/jstage-ipsjcss.html
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/ipsjjip-article.html
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/ipsjjip-pdf.pdf
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/cdx-ipsj2024-prefix.json
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/cdx-ipsjjip-pdf.json
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/ipsjjip-pdf.txt
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/ipsj-css47-pdf.pdf
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/cdx-ipsj-css47.json
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/cdx-ipsj-2024-all.json
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/ixsq-record.json
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/jstage-ipsjcss-browse.html
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/cinii-css-articles.json
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/ipsj-css2024026.pdf
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/ixsq-item.html
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/v1-file.pdf
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/v2-file.pdf
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/v3-record.html
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/measurements/v4-oai.xml
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/revenger/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/kumitate/round15/.deepresearch/20261024_200041_kumitate_r15/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/kumitate/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/kumitate/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/kumitate/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kumitate/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kumitate/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/kumitate/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/kumitate/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/kumitate/round15/ada253611-report-text-2026-10-24.txt
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/evidence/f2-corpus-flakiness.py
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/evidence/f2-corpus-flakiness.txt
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/evidence/f3-kit-dryrun.py
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/evidence/surface-census.sh
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/evidence/f3-kit-dryrun.txt
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/evidence/f4-two-level-chain.py
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/evidence/f4-two-level-chain.txt
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/evidence/xiao-faculty.html
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/evidence/xiao-faculty-ja.html
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/.deepresearch/20261024_200036_tameshi-r15/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/tameshi/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/.deepresearch/notes/leaderboard-gap-round15.txt
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/.deepresearch/notes/owner-enumeration-diff-round15.txt
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/.deepresearch/notes/registry-statements-round15.txt
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/.deepresearch/notes/japanese-client-census-round15.txt
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/.deepresearch/notes/client-provenance-round15.txt
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/.deepresearch/20261024_200050_kotoba_r15/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/kotoba/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/.deepresearch/20261024_200619_chousa-r15-prisma/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/evidence/jebm-26-4-issue-listing.html
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/evidence/jebm-priority-publication.html
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/evidence/jebm-current-issue-listing.html
/home/vgpnk/Projects/shokuknow/lanes/chousa/round15/evidence/SHA256SUMS
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/.deepresearch/20261024_200048_mado-round15-ledger-leads/final_turn_001.md
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/fetch/host-focus-grab-client-sweep.txt
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/fetch/corpus-round24-artifacts-sweep.txt
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/fetch/host-waybar-dated-backups-sweep.txt
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/fetch/host-webarchive-snapshot-sweep.txt
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/fetch/omarchy-menu.sh
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/fetch/host-omarchy-toggles-state-sweep.txt
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/mado/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/probes/harness/mechanism_check.py
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/probes/harness/census_rendered.py
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/probes/out/clear_colour_mechanism_check.txt
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/probes/out/class_reference_residue.txt
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/probes/out/round11_capture_census.txt
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/probes/src/mesa-26.2.5/lp_setup.c
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/probes/src/mesa-26.2.5/u_math.h
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/probes/src/mesa-26.2.5/u_pack_color.h
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/probes/src/mesa-26.2.5/u_format_pack.py
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/probes/src/mesa-26.2.5/PROVENANCE.txt
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/DOMAIN.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/CHANNELS.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/SOURCES-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/KNOWLEDGE-PROPOSED.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/SEARCH-LOG.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/REJECTIONS.md
/home/vgpnk/Projects/shokuknow/lanes/game-dev-2d/round15/CANNOT-ANSWER.md
/home/vgpnk/Projects/shokuknow/.git/index
/home/vgpnk/Projects/shokuknow/.video_agent/plugin_root
/home/vgpnk/Projects/shokuknow/.zcode/workflow-drafts/Shokunin-corpus-three-swarm-loops.dwf.ts
/home/vgpnk/Projects/shokuknow/.zcode/workflow-runs/dwfrun-19047d0b-a215-4835-9943-76e77109b9c9.mjs
/home/vgpnk/Projects/shokuknow/.zcode/workflow-runs/dwfrun-4c910a99-cf59-48b9-96f6-8084b42cfa3f.mjs
/home/vgpnk/Projects/shokuknow/.zcode/workflow-runs/dwfrun-957d7a42-b8c6-4c81-b5ca-55c12a3e5efa.mjs
```
Exit code: `0`.
Stderr:

```text
<empty>
```

Derived from that captured stdout: **577 hits**. Top-level grouping (a summary only; the complete list is above):

```text
   437 lanes
   134 .ufo
     4 .zcode
     1 .git
     1 .video_agent
```

Package-specific read-only check:
```console
$ find /home/vgpnk/Projects/shokuknow/merge/kotoba -newermt '-40 minutes' -type f -print
<empty>
```
Exit code: `0`.
Stderr:

```text
<empty>
```

Observed package-specific hit count: **0**.

## S3 — lane Git status outside the wave

Requested command and observed stdout:
```console
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain
 M .ufo/waves/round-65/w1/swarm-registry.json
 M .ufo/waves/round-66/w1/swarm-registry.json
 M corpus/README.md
 M corpus/SOURCES.md
?? .ufo/waves/round-65/w1/ConnSibling2.md
?? .ufo/waves/round-65/w1/CriticFrontier.md
?? .ufo/waves/round-65/w1/CriticPlanFreeze.md
?? .ufo/waves/round-65/w1/ExecFloorsProbe.md
?? .ufo/waves/round-65/w1/ExecGovProbe.md
?? .ufo/waves/round-65/w1/ExecKillReverify.md
?? .ufo/waves/round-65/w1/MutGovArms.md
?? .ufo/waves/round-65/w1/MutNewLanes.md
?? .ufo/waves/round-65/w1/RevC2Mechanism.md
?? .ufo/waves/round-65/w1/RevNoHarm.md
?? .ufo/waves/round-65/w1/RevReceiptRevs.md
?? .ufo/waves/round-65/w1/ScoutLessonBacklog.md
?? .ufo/waves/round-65/w1/ScoutQualityDebt3.md
?? .ufo/waves/round-65/w1/ScoutReceiptSweep.md
?? .ufo/waves/round-65/w1/ScoutS049Recheck.md
?? .ufo/waves/round-65/w1/ScoutS121Reopen.md
?? .ufo/waves/round-65/w1/ScribeCensusCheck.md
?? .ufo/waves/round-65/w1/ScribeDispositions.md
?? .ufo/waves/round-65/w1/ScribeEntryCheck.md
?? .ufo/waves/round-65/w1/ScribeSHONEN2.md
?? .ufo/waves/round-65/w1/ScribeSourcesRow2.md
?? .ufo/waves/round-65/w1/SentWaveSpecs.md
?? .ufo/waves/round-66/w1/CriticBaselineFitting.md
?? .ufo/waves/round-66/w1/CriticCodeSpanBoundary.md
?? .ufo/waves/round-66/w1/CriticDoNothingTarget.md
?? .ufo/waves/round-66/w1/CriticFleetOveraccept.md
?? .ufo/waves/round-66/w1/ExecC1Selftest.md
?? .ufo/waves/round-66/w1/ExecIntegrityNoBaseline.md
?? .ufo/waves/round-66/w1/ExecRoutedCounter.md
?? .ufo/waves/round-66/w1/MutC1Exemption.md
?? .ufo/waves/round-66/w1/MutC1Uncoupled.md
?? .ufo/waves/round-66/w1/MutC1WitnessDeletion.md
?? .ufo/waves/round-66/w1/MutC2CodeSpan.md
?? .ufo/waves/round-66/w1/MutC2NoFleetHop.md
?? .ufo/waves/round-66/w1/ReviewC1Control.md
?? .ufo/waves/round-66/w1/ReviewC1DoNothing.md
?? .ufo/waves/round-66/w1/ReviewC1ExistingWorlds.md
?? .ufo/waves/round-66/w1/ReviewC1Witness.md
?? .ufo/waves/round-66/w1/ReviewCensus.md
?? .ufo/waves/round-66/w1/ReviewCorpusIndex.md
?? .ufo/waves/round-66/w1/ReviewD1Blobs.md
?? .ufo/waves/round-66/w1/ReviewD2Baseline.md
?? .ufo/waves/round-66/w1/ReviewD2FleetRoot.md
?? .ufo/waves/round-66/w1/ReviewNoHarmC1.md
?? .ufo/waves/round-66/w1/ReviewS122Fit.md
?? .ufo/waves/round-66/w1/ScoutClaimDataWalk.md
?? .ufo/waves/round-66/w1/ScoutCorpusCount.md
?? .ufo/waves/round-66/w1/ScoutIndexRows.md
?? .ufo/waves/round-66/w1/ScoutIntegrityContext.md
?? .ufo/waves/round-66/w1/ScoutR65Registries.md
?? .ufo/waves/round-66/w1/ScoutS122Reopen.md
?? .ufo/waves/round-66/w1/ScoutSiblingOverlap.md
?? .ufo/waves/round-66/w1/ScribeLessonGate.md
?? .ufo/waves/round-66/w1/ScribeMistakeQ61.md
?? .ufo/waves/round-66/w1/ScribePlanPredicate.md
?? .ufo/waves/round-66/w1/ScribeReportContract.md
?? .ufo/waves/round-66/w1/ScribeSOURCES.md
?? .ufo/waves/round-67/
?? corpus/knowledge/instruction-authority-ladder-round67.md
?? corpus/lessons/round-67.md
?? corpus/live.md
?? plans/round-67.md
```
Exit code: `0`.
Stderr:

```text
<empty>
```

Expanded `-uall` rerun, used so directory collapsing could not hide individual paths:
```console
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain --untracked-files=all
 M .ufo/waves/round-65/w1/swarm-registry.json
 M .ufo/waves/round-66/w1/swarm-registry.json
 M corpus/README.md
 M corpus/SOURCES.md
?? .ufo/waves/round-65/w1/ConnSibling2.md
?? .ufo/waves/round-65/w1/CriticFrontier.md
?? .ufo/waves/round-65/w1/CriticPlanFreeze.md
?? .ufo/waves/round-65/w1/ExecFloorsProbe.md
?? .ufo/waves/round-65/w1/ExecGovProbe.md
?? .ufo/waves/round-65/w1/ExecKillReverify.md
?? .ufo/waves/round-65/w1/MutGovArms.md
?? .ufo/waves/round-65/w1/MutNewLanes.md
?? .ufo/waves/round-65/w1/RevC2Mechanism.md
?? .ufo/waves/round-65/w1/RevNoHarm.md
?? .ufo/waves/round-65/w1/RevReceiptRevs.md
?? .ufo/waves/round-65/w1/ScoutLessonBacklog.md
?? .ufo/waves/round-65/w1/ScoutQualityDebt3.md
?? .ufo/waves/round-65/w1/ScoutReceiptSweep.md
?? .ufo/waves/round-65/w1/ScoutS049Recheck.md
?? .ufo/waves/round-65/w1/ScoutS121Reopen.md
?? .ufo/waves/round-65/w1/ScribeCensusCheck.md
?? .ufo/waves/round-65/w1/ScribeDispositions.md
?? .ufo/waves/round-65/w1/ScribeEntryCheck.md
?? .ufo/waves/round-65/w1/ScribeSHONEN2.md
?? .ufo/waves/round-65/w1/ScribeSourcesRow2.md
?? .ufo/waves/round-65/w1/SentWaveSpecs.md
?? .ufo/waves/round-66/w1/CriticBaselineFitting.md
?? .ufo/waves/round-66/w1/CriticCodeSpanBoundary.md
?? .ufo/waves/round-66/w1/CriticDoNothingTarget.md
?? .ufo/waves/round-66/w1/CriticFleetOveraccept.md
?? .ufo/waves/round-66/w1/ExecC1Selftest.md
?? .ufo/waves/round-66/w1/ExecIntegrityNoBaseline.md
?? .ufo/waves/round-66/w1/ExecRoutedCounter.md
?? .ufo/waves/round-66/w1/MutC1Exemption.md
?? .ufo/waves/round-66/w1/MutC1Uncoupled.md
?? .ufo/waves/round-66/w1/MutC1WitnessDeletion.md
?? .ufo/waves/round-66/w1/MutC2CodeSpan.md
?? .ufo/waves/round-66/w1/MutC2NoFleetHop.md
?? .ufo/waves/round-66/w1/ReviewC1Control.md
?? .ufo/waves/round-66/w1/ReviewC1DoNothing.md
?? .ufo/waves/round-66/w1/ReviewC1ExistingWorlds.md
?? .ufo/waves/round-66/w1/ReviewC1Witness.md
?? .ufo/waves/round-66/w1/ReviewCensus.md
?? .ufo/waves/round-66/w1/ReviewCorpusIndex.md
?? .ufo/waves/round-66/w1/ReviewD1Blobs.md
?? .ufo/waves/round-66/w1/ReviewD2Baseline.md
?? .ufo/waves/round-66/w1/ReviewD2FleetRoot.md
?? .ufo/waves/round-66/w1/ReviewNoHarmC1.md
?? .ufo/waves/round-66/w1/ReviewS122Fit.md
?? .ufo/waves/round-66/w1/ScoutClaimDataWalk.md
?? .ufo/waves/round-66/w1/ScoutCorpusCount.md
?? .ufo/waves/round-66/w1/ScoutIndexRows.md
?? .ufo/waves/round-66/w1/ScoutIntegrityContext.md
?? .ufo/waves/round-66/w1/ScoutR65Registries.md
?? .ufo/waves/round-66/w1/ScoutS122Reopen.md
?? .ufo/waves/round-66/w1/ScoutSiblingOverlap.md
?? .ufo/waves/round-66/w1/ScribeLessonGate.md
?? .ufo/waves/round-66/w1/ScribeMistakeQ61.md
?? .ufo/waves/round-66/w1/ScribePlanPredicate.md
?? .ufo/waves/round-66/w1/ScribeReportContract.md
?? .ufo/waves/round-66/w1/ScribeSOURCES.md
?? .ufo/waves/round-67/census-before.txt
?? .ufo/waves/round-67/controls/SOURCES.append.r67.md
?? .ufo/waves/round-67/controls/census-validate-append.txt
?? .ufo/waves/round-67/controls/collisions
?? .ufo/waves/round-67/controls/reg-ids
?? .ufo/waves/round-67/controls/staged-ids
?? .ufo/waves/round-67/controls/validate/LOG.md
?? .ufo/waves/round-67/controls/validate/PROVINCE.md
?? .ufo/waves/round-67/controls/validate/SCORECARD.md
?? .ufo/waves/round-67/controls/validate/SKILL.md
?? .ufo/waves/round-67/controls/validate/corpus/QUALITY.md
?? .ufo/waves/round-67/controls/validate/corpus/README.md
?? .ufo/waves/round-67/controls/validate/corpus/SOURCES.append.r67.md
?? .ufo/waves/round-67/controls/validate/corpus/SOURCES.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/agent-def-audit-round6.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/agent-definition-files-round56.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/agent-defs-commands-and-round-prompts.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/agents-md-and-dispatch-surfaces.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/alwayson-checklist-round7.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/alwayson-rule-files-round53.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/anatomy-and-compression.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/checklist-execution-round15.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/checklist-execution-round16.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/checklist-execution-round17.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/claim-census-round12.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/claim-scope-audit-round9.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/claude-md-surface.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/cold-run-round11.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/command-files-round58.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/compound-clause-citation-round63.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/corpus-integrity-round11.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/dispatch-prompt-audit-round7.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/erratum-absorption-round62.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/explicit-invocation-round55.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/fail-closed-and-anti-patterns.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/fleet-commit-resolution-round66.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/fleet-skill-audit-round5.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/frontmatter-rule-authorities-round48.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/frontmatter-trigger-surface.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/g7-span-closure-round65.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/g7-span-pinning-round64.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/harness-independent-round37.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/harness-independent-round41-census.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/harness-router-models-round9.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/harness-system-prompt.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/harness-verifier-round10.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/hook-files-round59.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/independent-verification-round12.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/instruction-authority-ladder-round67.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/instruction-surface-census-round13.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/instruction-surface-remeasure-round13.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/mcp-server-instructions-round52.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/opencode-extraction-round14.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/opencode-offer-trace-round8.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/plugin-manifests-round57.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/render-mechanism-round7.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/scoped-rules-counter-round61.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/scoped-rules-round60.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/sibling-citation-routing-round16.json
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/sibling-citation-routing-round16.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/sibling-citation-routing-round21.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/sibling-description-rewrites-round8.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/sibling-overlap-census-round49.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/skill-activation-telemetry.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/skill-listing-thresholds-round54.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/skill-overlap-levers-round51.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/skill-selection-rules-round50.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/substrate-pin-guard-round23.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/trigger-miss-proxy-round6.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/writing-revision-calibration-round61.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-1-aggregator-audit.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-1.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-10.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-11.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-12.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-16.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-19-recensus.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-3.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-4-aggregator-audit.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-4.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-46-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-46.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-47-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-47.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-48-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-48.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-49-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-49.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-5-aggregator-audit.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-5.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-50-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-50.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-51-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-51.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-52-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-52.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-53-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-53.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-54-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-54.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-55-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-55.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-56-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-56.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-57-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-57.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-58-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-58.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-59-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-59.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-6-aggregator-audit.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-6.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-60-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-60.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-61-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-61.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-62-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-62.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-63-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-63.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-64-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-64.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-65-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-65.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-66-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-66.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-67.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-7.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-8-aggregator-box3-coldrun.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-8.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-9-aggregator-corpus-verdict.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-9.md
?? .ufo/waves/round-67/controls/validate/corpus/live.md
?? .ufo/waves/round-67/w1-spec.json
?? .ufo/waves/round-67/w1/ExecC1BaseControl.md
?? .ufo/waves/round-67/w1/ExecC1HalfControls.md
?? .ufo/waves/round-67/w1/ExecC2JunkControl.md
?? .ufo/waves/round-67/w1/ExecCollision.md
?? .ufo/waves/round-67/w1/MutC1Index.md
?? .ufo/waves/round-67/w1/ScribeReadmeIndex.md
?? .ufo/waves/round-67/w1/controls/C1-base.txt
?? .ufo/waves/round-67/w1/controls/C1-half-controls.txt
?? .ufo/waves/round-67/w1/controls/C1-mutants.txt
?? .ufo/waves/round-67/w1/controls/C2-junk-control.txt
?? .ufo/waves/round-67/w1/controls/collision-count
?? .ufo/waves/round-67/w1/controls/collisions
?? .ufo/waves/round-67/w1/controls/junk-world/
?? .ufo/waves/round-67/w1/controls/reg-ids
?? .ufo/waves/round-67/w1/controls/staged-ids
?? .ufo/waves/round-67/w1/controls/validate/corpus/QUALITY.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/README.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/SOURCES.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/agent-def-audit-round6.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/agent-definition-files-round56.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/agent-defs-commands-and-round-prompts.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/agents-md-and-dispatch-surfaces.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/alwayson-checklist-round7.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/alwayson-rule-files-round53.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/anatomy-and-compression.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/checklist-execution-round15.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/checklist-execution-round16.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/checklist-execution-round17.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/claim-census-round12.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/claim-scope-audit-round9.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/claude-md-surface.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/cold-run-round11.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/command-files-round58.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/compound-clause-citation-round63.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/corpus-integrity-round11.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/dispatch-prompt-audit-round7.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/erratum-absorption-round62.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/explicit-invocation-round55.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/fail-closed-and-anti-patterns.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/fleet-commit-resolution-round66.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/fleet-skill-audit-round5.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/frontmatter-rule-authorities-round48.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/frontmatter-trigger-surface.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/g7-span-closure-round65.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/g7-span-pinning-round64.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/harness-independent-round37.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/harness-independent-round41-census.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/harness-router-models-round9.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/harness-system-prompt.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/harness-verifier-round10.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/hook-files-round59.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/independent-verification-round12.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/instruction-authority-ladder-round67.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/instruction-surface-census-round13.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/instruction-surface-remeasure-round13.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/mcp-server-instructions-round52.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/opencode-extraction-round14.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/opencode-offer-trace-round8.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/plugin-manifests-round57.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/render-mechanism-round7.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/scoped-rules-counter-round61.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/scoped-rules-round60.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/sibling-citation-routing-round16.json
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/sibling-citation-routing-round16.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/sibling-citation-routing-round21.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/sibling-description-rewrites-round8.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/sibling-overlap-census-round49.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/skill-activation-telemetry.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/skill-listing-thresholds-round54.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/skill-overlap-levers-round51.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/skill-selection-rules-round50.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/substrate-pin-guard-round23.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/trigger-miss-proxy-round6.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/knowledge/writing-revision-calibration-round61.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-1-aggregator-audit.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-1.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-10.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-11.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-12.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-16.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-19-recensus.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-3.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-4-aggregator-audit.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-4.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-46-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-46.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-47-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-47.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-48-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-48.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-49-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-49.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-5-aggregator-audit.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-5.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-50-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-50.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-51-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-51.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-52-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-52.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-53-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-53.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-54-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-54.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-55-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-55.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-56-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-56.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-57-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-57.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-58-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-58.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-59-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-59.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-6-aggregator-audit.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-6.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-60-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-60.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-61-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-61.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-62-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-62.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-63-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-63.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-64-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-64.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-65-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-65.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-66-verifier-spotcheck.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-66.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-7.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-8-aggregator-box3-coldrun.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-8.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-9-aggregator-corpus-verdict.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/lessons/round-9.md
?? .ufo/waves/round-67/w1/controls/validate/corpus/live.md
?? .ufo/waves/round-67/w1/dispatch.log
?? .ufo/waves/round-67/w1/drafts/README-index-rows.r67.md
?? .ufo/waves/round-67/w1/drafts/SOURCES.append.r67.md
?? .ufo/waves/round-67/w1/logs/ConnSibling.log
?? .ufo/waves/round-67/w1/logs/CriticC1.log
?? .ufo/waves/round-67/w1/logs/CriticC2.log
?? .ufo/waves/round-67/w1/logs/CriticProvenance.log
?? .ufo/waves/round-67/w1/logs/ExecC1BaseControl.log
?? .ufo/waves/round-67/w1/logs/ExecC1HalfControls.log
?? .ufo/waves/round-67/w1/logs/ExecC2Counter.log
?? .ufo/waves/round-67/w1/logs/ExecC2JunkControl.log
?? .ufo/waves/round-67/w1/logs/ExecCollision.log
?? .ufo/waves/round-67/w1/logs/ExecQualityBar.log
?? .ufo/waves/round-67/w1/logs/ExecTransform.log
?? .ufo/waves/round-67/w1/logs/MutC1Index.log
?? .ufo/waves/round-67/w1/logs/MutC2Counter.log
?? .ufo/waves/round-67/w1/logs/RevFabrication.log
?? .ufo/waves/round-67/w1/logs/ReviewAppendOnly.log
?? .ufo/waves/round-67/w1/logs/ReviewC1Repair.log
?? .ufo/waves/round-67/w1/logs/ReviewCounter.log
?? .ufo/waves/round-67/w1/logs/ReviewEntry.log
?? .ufo/waves/round-67/w1/logs/ReviewSources.log
?? .ufo/waves/round-67/w1/logs/ScoutArxiv.log
?? .ufo/waves/round-67/w1/logs/ScoutBaselineShape.log
?? .ufo/waves/round-67/w1/logs/ScoutConsiderthese.log
?? .ufo/waves/round-67/w1/logs/ScoutIndexShape.log
?? .ufo/waves/round-67/w1/logs/ScoutModelSpec.log
?? .ufo/waves/round-67/w1/logs/ScoutQwen.log
?? .ufo/waves/round-67/w1/logs/ScoutSkillCreator.log
?? .ufo/waves/round-67/w1/logs/ScribeEntry.log
?? .ufo/waves/round-67/w1/logs/ScribeLesson.log
?? .ufo/waves/round-67/w1/logs/ScribeReadmeIndex.log
?? .ufo/waves/round-67/w1/logs/ScribeReport.log
?? .ufo/waves/round-67/w1/logs/ScribeSources.log
?? .ufo/waves/round-67/w1/logs/SentScope.log
?? .ufo/waves/round-67/w1/seat-results.json
?? .ufo/waves/round-67/w1/swarm-registry.json
?? corpus/knowledge/instruction-authority-ladder-round67.md
?? corpus/lessons/round-67.md
?? corpus/live.md
?? plans/round-67.md
```
Exit code: `0`.
Stderr:

```text
<empty>
```

Every expanded status line whose path is outside `.ufo/waves/round-67/w1/`:

```text
 M .ufo/waves/round-65/w1/swarm-registry.json
 M .ufo/waves/round-66/w1/swarm-registry.json
 M corpus/README.md
 M corpus/SOURCES.md
?? .ufo/waves/round-65/w1/ConnSibling2.md
?? .ufo/waves/round-65/w1/CriticFrontier.md
?? .ufo/waves/round-65/w1/CriticPlanFreeze.md
?? .ufo/waves/round-65/w1/ExecFloorsProbe.md
?? .ufo/waves/round-65/w1/ExecGovProbe.md
?? .ufo/waves/round-65/w1/ExecKillReverify.md
?? .ufo/waves/round-65/w1/MutGovArms.md
?? .ufo/waves/round-65/w1/MutNewLanes.md
?? .ufo/waves/round-65/w1/RevC2Mechanism.md
?? .ufo/waves/round-65/w1/RevNoHarm.md
?? .ufo/waves/round-65/w1/RevReceiptRevs.md
?? .ufo/waves/round-65/w1/ScoutLessonBacklog.md
?? .ufo/waves/round-65/w1/ScoutQualityDebt3.md
?? .ufo/waves/round-65/w1/ScoutReceiptSweep.md
?? .ufo/waves/round-65/w1/ScoutS049Recheck.md
?? .ufo/waves/round-65/w1/ScoutS121Reopen.md
?? .ufo/waves/round-65/w1/ScribeCensusCheck.md
?? .ufo/waves/round-65/w1/ScribeDispositions.md
?? .ufo/waves/round-65/w1/ScribeEntryCheck.md
?? .ufo/waves/round-65/w1/ScribeSHONEN2.md
?? .ufo/waves/round-65/w1/ScribeSourcesRow2.md
?? .ufo/waves/round-65/w1/SentWaveSpecs.md
?? .ufo/waves/round-66/w1/CriticBaselineFitting.md
?? .ufo/waves/round-66/w1/CriticCodeSpanBoundary.md
?? .ufo/waves/round-66/w1/CriticDoNothingTarget.md
?? .ufo/waves/round-66/w1/CriticFleetOveraccept.md
?? .ufo/waves/round-66/w1/ExecC1Selftest.md
?? .ufo/waves/round-66/w1/ExecIntegrityNoBaseline.md
?? .ufo/waves/round-66/w1/ExecRoutedCounter.md
?? .ufo/waves/round-66/w1/MutC1Exemption.md
?? .ufo/waves/round-66/w1/MutC1Uncoupled.md
?? .ufo/waves/round-66/w1/MutC1WitnessDeletion.md
?? .ufo/waves/round-66/w1/MutC2CodeSpan.md
?? .ufo/waves/round-66/w1/MutC2NoFleetHop.md
?? .ufo/waves/round-66/w1/ReviewC1Control.md
?? .ufo/waves/round-66/w1/ReviewC1DoNothing.md
?? .ufo/waves/round-66/w1/ReviewC1ExistingWorlds.md
?? .ufo/waves/round-66/w1/ReviewC1Witness.md
?? .ufo/waves/round-66/w1/ReviewCensus.md
?? .ufo/waves/round-66/w1/ReviewCorpusIndex.md
?? .ufo/waves/round-66/w1/ReviewD1Blobs.md
?? .ufo/waves/round-66/w1/ReviewD2Baseline.md
?? .ufo/waves/round-66/w1/ReviewD2FleetRoot.md
?? .ufo/waves/round-66/w1/ReviewNoHarmC1.md
?? .ufo/waves/round-66/w1/ReviewS122Fit.md
?? .ufo/waves/round-66/w1/ScoutClaimDataWalk.md
?? .ufo/waves/round-66/w1/ScoutCorpusCount.md
?? .ufo/waves/round-66/w1/ScoutIndexRows.md
?? .ufo/waves/round-66/w1/ScoutIntegrityContext.md
?? .ufo/waves/round-66/w1/ScoutR65Registries.md
?? .ufo/waves/round-66/w1/ScoutS122Reopen.md
?? .ufo/waves/round-66/w1/ScoutSiblingOverlap.md
?? .ufo/waves/round-66/w1/ScribeLessonGate.md
?? .ufo/waves/round-66/w1/ScribeMistakeQ61.md
?? .ufo/waves/round-66/w1/ScribePlanPredicate.md
?? .ufo/waves/round-66/w1/ScribeReportContract.md
?? .ufo/waves/round-66/w1/ScribeSOURCES.md
?? .ufo/waves/round-67/census-before.txt
?? .ufo/waves/round-67/controls/SOURCES.append.r67.md
?? .ufo/waves/round-67/controls/census-validate-append.txt
?? .ufo/waves/round-67/controls/collisions
?? .ufo/waves/round-67/controls/reg-ids
?? .ufo/waves/round-67/controls/staged-ids
?? .ufo/waves/round-67/controls/validate/LOG.md
?? .ufo/waves/round-67/controls/validate/PROVINCE.md
?? .ufo/waves/round-67/controls/validate/SCORECARD.md
?? .ufo/waves/round-67/controls/validate/SKILL.md
?? .ufo/waves/round-67/controls/validate/corpus/QUALITY.md
?? .ufo/waves/round-67/controls/validate/corpus/README.md
?? .ufo/waves/round-67/controls/validate/corpus/SOURCES.append.r67.md
?? .ufo/waves/round-67/controls/validate/corpus/SOURCES.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/agent-def-audit-round6.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/agent-definition-files-round56.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/agent-defs-commands-and-round-prompts.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/agents-md-and-dispatch-surfaces.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/alwayson-checklist-round7.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/alwayson-rule-files-round53.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/anatomy-and-compression.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/checklist-execution-round15.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/checklist-execution-round16.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/checklist-execution-round17.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/claim-census-round12.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/claim-scope-audit-round9.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/claude-md-surface.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/cold-run-round11.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/command-files-round58.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/compound-clause-citation-round63.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/corpus-integrity-round11.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/dispatch-prompt-audit-round7.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/erratum-absorption-round62.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/explicit-invocation-round55.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/fail-closed-and-anti-patterns.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/fleet-commit-resolution-round66.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/fleet-skill-audit-round5.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/frontmatter-rule-authorities-round48.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/frontmatter-trigger-surface.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/g7-span-closure-round65.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/g7-span-pinning-round64.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/harness-independent-round37.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/harness-independent-round41-census.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/harness-router-models-round9.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/harness-system-prompt.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/harness-verifier-round10.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/hook-files-round59.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/independent-verification-round12.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/instruction-authority-ladder-round67.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/instruction-surface-census-round13.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/instruction-surface-remeasure-round13.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/mcp-server-instructions-round52.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/opencode-extraction-round14.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/opencode-offer-trace-round8.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/plugin-manifests-round57.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/render-mechanism-round7.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/scoped-rules-counter-round61.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/scoped-rules-round60.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/sibling-citation-routing-round16.json
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/sibling-citation-routing-round16.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/sibling-citation-routing-round21.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/sibling-description-rewrites-round8.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/sibling-overlap-census-round49.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/skill-activation-telemetry.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/skill-listing-thresholds-round54.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/skill-overlap-levers-round51.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/skill-selection-rules-round50.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/substrate-pin-guard-round23.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/trigger-miss-proxy-round6.md
?? .ufo/waves/round-67/controls/validate/corpus/knowledge/writing-revision-calibration-round61.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-1-aggregator-audit.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-1.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-10.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-11.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-12.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-16.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-19-recensus.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-3.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-4-aggregator-audit.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-4.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-46-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-46.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-47-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-47.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-48-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-48.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-49-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-49.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-5-aggregator-audit.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-5.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-50-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-50.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-51-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-51.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-52-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-52.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-53-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-53.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-54-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-54.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-55-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-55.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-56-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-56.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-57-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-57.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-58-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-58.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-59-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-59.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-6-aggregator-audit.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-6.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-60-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-60.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-61-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-61.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-62-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-62.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-63-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-63.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-64-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-64.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-65-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-65.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-66-verifier-spotcheck.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-66.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-67.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-7.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-8-aggregator-box3-coldrun.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-8.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-9-aggregator-corpus-verdict.md
?? .ufo/waves/round-67/controls/validate/corpus/lessons/round-9.md
?? .ufo/waves/round-67/controls/validate/corpus/live.md
?? .ufo/waves/round-67/w1-spec.json
?? corpus/knowledge/instruction-authority-ladder-round67.md
?? corpus/lessons/round-67.md
?? corpus/live.md
?? plans/round-67.md
```

This is the requested Git-status evidence, not independent proof that no `.jj` metadata changed. No `jj` command or Git write command was run.

## S4 — misrooted report checks

The candidate names came from the 32 declared items in `.ufo/waves/round-67/w1-spec.json`. The scans excluded the allowed w1 tree and only inspected recent Markdown files in the lane plus direct fleet/lane `round-67` wave directories.

Bounded direct-round-67 scan:
```console
$ names='ExecC2Counter.md ExecC1BaseControl.md ExecC1HalfControls.md ExecC2JunkControl.md ExecCollision.md ExecTransform.md ExecQualityBar.md ScoutModelSpec.md ScoutSkillCreator.md ScoutArxiv.md ScoutQwen.md ScoutIndexShape.md ScoutBaselineShape.md ScoutConsiderthese.md ScribeEntry.md ScribeSources.md ScribeLesson.md ScribeReadmeIndex.md ScribeReport.md ReviewEntry.md ReviewSources.md ReviewCounter.md ReviewC1Repair.md ReviewAppendOnly.md CriticC1.md CriticC2.md CriticProvenance.md ConnSibling.md MutC2Counter.md MutC1Index.md SentScope.md RevFabrication.md'; for d in /home/vgpnk/Projects/shokunin/.ufo/waves/round-67 /home/vgpnk/Projects/shokunin/*/.ufo/waves/round-67; do if [ -d "$d" ]; then while IFS= read -r p; do b=${p##*/}; case " $names " in *" $b "*) case "$p" in /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-67/w1/*) ;; *) echo "$p" ;; esac ;; esac; done < <(find "$d" -type f -newermt '-40 minutes' -name '*.md' -print); fi; done
<empty>
```
Exit code: `0`.
Stderr:

```text
<empty>
```

Bounded whole-lane recent-Markdown scan:
```console
$ names='ExecC2Counter.md ExecC1BaseControl.md ExecC1HalfControls.md ExecC2JunkControl.md ExecCollision.md ExecTransform.md ExecQualityBar.md ScoutModelSpec.md ScoutSkillCreator.md ScoutArxiv.md ScoutQwen.md ScoutIndexShape.md ScoutBaselineShape.md ScoutConsiderthese.md ScribeEntry.md ScribeSources.md ScribeLesson.md ScribeReadmeIndex.md ScribeReport.md ReviewEntry.md ReviewSources.md ReviewCounter.md ReviewC1Repair.md ReviewAppendOnly.md CriticC1.md CriticC2.md CriticProvenance.md ConnSibling.md MutC2Counter.md MutC1Index.md SentScope.md RevFabrication.md'; while IFS= read -r p; do b=${p##*/}; case " $names " in *" $b "*) case "$p" in /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-67/w1/*) ;; *) echo "$p" ;; esac ;; esac; done < <(find /home/vgpnk/Projects/shokunin/kotoba-shokunin -newermt '-40 minutes' -type f -name '*.md' -print)
<empty>
```
Exit code: `0`.
Stderr:

```text
<empty>
```

Common fleet-root misroot locations:
```console
$ for p in /home/vgpnk/Projects/shokunin/.ufo/waves/round-67 /home/vgpnk/Projects/shokunin/round-67 /home/vgpnk/Projects/shokunin/kotoba; do if [ -e "$p" ]; then find "$p" -type f -print | sort; else echo "ABSENT: $p"; fi; done
ABSENT: /home/vgpnk/Projects/shokunin/.ufo/waves/round-67
ABSENT: /home/vgpnk/Projects/shokunin/round-67
ABSENT: /home/vgpnk/Projects/shokunin/kotoba
```
Exit code: `0`.
Stderr:

```text
<empty>
```
Initial broad scan limitation:

```console
$ find /home/vgpnk/Projects/shokunin -newermt '-40 minutes' -type f -path '*/.ufo/waves/round-67/*' -not -path '/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-67/w1/*' -print | sort
```
Observed outcome: killed by the tool after `120.012 seconds`; no result was used as evidence.

Final candidate list from the two bounded S4 scans:

```text
<none>
```

No files were moved, deleted, installed, committed, or otherwise remediated by this seat. Its sole lane write is this report.

Report: .ufo/waves/round-67/w1/SentScope.md
