Result: DONE — Added self-test arms and killed all 17 single-point mutants; the sandbox source was restored exactly to the target commit.

## Detector and restoration

All code execution was in `/fast/scratch/hyaku/kotoba-r54/MutGateRegistry`, checked out at `e33715486a45a4a857b64c30e6b695f7995858b8`.

- Detector: `python3 -B verifiers/check_gate_registry.py --self-test`.
- Pristine target bytes, SHA-256 `86c003952f9b5fda2593ede55607dab06d772328753648e1c37775fdd873e6f0`: `self-test: 0 failure(s) over 22 assertions`; exit 0.
- With the added self-test arms, the common pre-mutation bytes had SHA-256 `b9ba4b9d4a0235a5a85f57ca954ac34309ca89dca0174c0054e3d84e7db105cb`; detector output ended `self-test: 0 failure(s) over 30 assertions`; exit 0.
- Each mutant was made from those same expanded baseline bytes. After each run, the file was copied back from the saved baseline; every restoration hash was `b9ba4b9d4a0235a5a85f57ca954ac34309ca89dca0174c0054e3d84e7db105cb`.
- Final restore to target commit bytes: `git checkout -- verifiers/check_gate_registry.py`; SHA-256 returned to `86c003952f9b5fda2593ede55607dab06d772328753648e1c37775fdd873e6f0`. Re-running the detector printed `self-test: 0 failure(s) over 22 assertions`; exit 0.

## Mutants

For each row, the listed hash is the mutated file's SHA-256. The detector was run on each mutant; every run exited 1 with the recorded failing self-test case(s). No mutant survived and none was inconclusive.

| Mutant | Mutated SHA-256 | Actual detector result |
|---|---|---|
| Universe extension filter (`.sh` omitted) | `572d83b3a26098093318706cc9c3ce0495ef88f008622197a04d26ae6be7ffe2` | `FAIL universe includes only .py and .sh blobs`; 1 failure / 30 assertions |
| Blob-only filter removed | `1d2938cd7b81ab79691ce4739c51c4bbcf90f837671c1894e1d83617aee0b832` | `FAIL universe includes only .py and .sh blobs`; 1 / 30 |
| Extra `tool` kind allowed | `1b6497c764b0be2004b29c5db375faf69e575d7747c9d8a0d0310d31fc57ad4b` | `FAIL bad kind`; 1 / 30 |
| Entry-command path check disabled | `b02bf80042b977df4895f5a0c455ea8138fde1dd5891d1716bacc17b3ca206cc` | `FAIL entry command not naming file`; 1 / 30 |
| `->` and `→` pair syntax removed | `e05b3732d61822b981f1be7cffbfe944c3ab3568c28542cbee1085dc029e8ad8` | `FAIL arrow form accepted`; 1 / 30 |
| Duplicate-code check disabled | `1f898128aec47f2982b60484e1832019eae4faa2c9e0075614f030acc9ed8ada` | `FAIL code declared twice`; 1 / 30 |
| Gate 0/1 pair requirement disabled | `a82e4b0751e848ac597446f97d62a85851c3a1272e6cad3005e25411942d025b` | `FAIL gate lacking 1=failed`, `FAIL gate mapping 1 to clean`, and `FAIL gate lacking 0=clean`; 3 / 30 |
| Self-test literal check disabled | `a20c34e4c7a16f08607f43644f328a175bdda7909ff8be9c2280d6eb457e4483` | `FAIL self-test flag absent from file`; 1 / 30 |
| Pinned-path existence check disabled | `addb7e4e51043ac5698c27c12a8bb4d641914a0353b50c6a3408c0a9090f8e34` | `FAIL pinned path missing`; 1 / 30 |
| `..` guard removed | `999bef609dc8a42c150a3caba7acccc4405eb59b4aac16ab2936b400063ee04b` | `FAIL pinned path climbing out when it exists`; 1 / 30 |
| Absolute-path guard removed | `08e68ac0ea831ab0d34fc9e34cecfa25871ce463a37670cfe8c0068ea146ae58` | `FAIL absolute pinned path rejected when it exists`; 1 / 30 |
| Write-scope check disabled | `60e32167558d0319fa4b172db222e36874f8c32f91594a0bb02d3844bec77c0e` | Two `FAIL empty write scope` assertions (empty and dash/em-dash inputs); 2 / 30 |
| Owner check disabled | `b53aeb69cbb2addfa6c7fcbdea7390c2217cae067430b371684d04d1e60de8e2` | `FAIL wrong owner`; 1 / 30 |
| Phantom detection disabled | `3b5e3f7333aa85b8041ce6f4b516d939e9657398421a1499f045fdcd8dcabc87` | `FAIL phantom row counted when inside the table` and `FAIL CLI exits one when a phantom row exists`; 2 / 30 |
| Heading anchor changed | `2e321c4429519fcf883d5cd0050e53b8571436faed6cb3082da73e0798ed2378` | `FAIL table under another heading not read`; 26 failures / 30 |
| Header anchor disabled | `5a0753d23b92435f6f3712b1c1031d895942f01f7210ae61d7e916d3c0ec397e` | `FAIL wrong header not read`; 1 / 30 |
| CLI exit rule changed to always 0 | `f3bffea58c1510b868a885f643e7179357e79132cd2d72ad39707bd5099e8def` | `FAIL CLI exits one when a row is missing` and `FAIL CLI exits one when a phantom row exists`; 2 / 30 |

Survivors: none. Thus there is no surviving mutant requiring a proposed kill case.

## Deliverables and scope

- Patch: `.ufo/waves/round-54/build/MutGateRegistry.patch`. It adds only self-test arms; no judging logic was changed.
- No lane source file was edited. The sandbox source ends at the exact target bytes/hash above.
- Tool installs or updates: none.
