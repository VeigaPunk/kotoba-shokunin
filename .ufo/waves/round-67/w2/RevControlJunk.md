# RevControlJunk — round 67 wave 2

## Scoped attack and verdict

**Attack target:** C2's do-nothing/junk-entry control: real entry bytes at the required path, an unresolvable `S###` citation, no `verified-at:` line, and no coverage-map index row must not satisfy the landed counter.

**Verdict: the control survives this attack.** The landed counter refused both the rebuilt committed revision and the rebuilt direct-file world with `authority ladder grounded 0 of 1` and exit 1. No actionable correctness finding remains in this scoped control test.

The **first failing conjunct in evaluation/report order is (3), source-ID resolution**, specifically its no-registry-row branch: `S999: no row in corpus/SOURCES.md`. Conjunct (2) does not reject this world because `source: S999 ...` is syntactically valid. The implementation accumulates findings rather than short-circuiting on conjunct (3); its final `if findings` return rejects the world after the later checks.

## Identity and evidence locations

- Landed content tip and counter identity: `da86c03e482a6aef433c34d733726b37c7cf6607`.
- Counter executed: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_instruction_authority.py`. `git diff --exit-code da86c03e482a6aef433c34d733726b37c7cf6607 -- verifiers/check_instruction_authority.py` exited 0, so the executed file matched the landed bytes.
- Pinned base used for `corpus/SOURCES.md` and `corpus/README.md`: `2a8eba56b3f9321b70c569fa2816d42237ca49a2`.
- Junk revision used for the entry bytes: `429ca66fd28ad58fc0347679b799ed2af3b0ece6`, parent `2a8eba56b3f9321b70c569fa2816d42237ca49a2`.
- Independent rebuild: `/tmp/k67-rev-control-junk.x3K8j6`.
- The dispatcher's `.ufo/waves/round-67/controls/junk-world/` path is absent. The actual committed control is `.ufo/waves/round-67/w1/controls/junk-world/`, with receipt `.ufo/waves/round-67/w1/controls/C2-junk-control.txt`. That historical receipt says `NOT RUN` because the counter was then unavailable; it does not claim a rejection. This report supplies a new execution without editing that receipt.

## Rebuild and preflight

I created a fresh `/tmp` directory, copied the scratch object's Git metadata there, materialized the 693-byte entry from junk revision `429ca66f`, and materialized the registry and coverage map from pinned base `2a8eba56`. Thus the canonical `--rev` run and a direct run over the actual rebuilt files could be made in the same sandbox. No Git or jj write command was run.

The independent preflight read the rebuilt files and asserted the required junk properties. Its verbatim output was:

```text
world=/tmp/k67-rev-control-junk.x3K8j6
entry_bytes=693
entry_sha256=410b263fe99ad4522722b9ea72468c353280b3864af5f198c92c3501d12e9487
source_ids=S999
unresolved_source_ids=S999
verified_at_lines=0
coverage_index_mentions=0
sources_sha256=02d643dacd4259626dac595577cb3421d43b485e39fd5e1d9ba64ebc3bcd752a
readme_sha256=19d303b059be9611d1f20c5ac4e37f988f63d38df8b45355732e68c9887f53c2
```

This establishes real nonempty bytes, one syntactically cited but unresolvable ID (`S999`), zero `verified-at:` lines, and zero coverage-map mentions of the entry path.

## Landed-counter runs

Canonical committed-bytes invocation:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_instruction_authority.py   --repo /tmp/k67-rev-control-junk.x3K8j6   --rev 429ca66fd28ad58fc0347679b799ed2af3b0ece6
```

Direct rebuilt-world invocation:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_instruction_authority.py   --repo /tmp/k67-rev-control-junk.x3K8j6
```

Their combined verbatim counter output and wrapper-recorded exit codes were:

```text
authority ladder grounded 0 of 1
  - S999: no row in corpus/SOURCES.md
  - no `verified-at: 2026-10-24` line
  - the entry has no coverage-map index row in corpus/README.md
authority ladder grounded 0 of 1
  - S999: no row in corpus/SOURCES.md
  - no `verified-at: 2026-10-24` line
  - the entry has no coverage-map index row in corpus/README.md
canonical_rev_exit=1
direct_world_exit=1
```

Both required refusal modes therefore agree: committed revision exit 1 and direct world exit 1; neither prints `grounded 1 of 1`.

## Why conjunct (3) is first

The landed code establishes this order:

1. **(1) Entry existence passes** (`verifiers/check_instruction_authority.py:136-139`).
2. **(2) Source-line shape passes** (`:147-150`): `_entry_source_lines` recognizes `S999`; there is no early `no source:` return.
3. **(3) ID resolution fails first** (`:159-164`): `rows.get("S999")` returns no row, appending `S999: no row in corpus/SOURCES.md`. The mined-status half of conjunct (3) is never reached.
4. The `continue` at `:164` skips conjuncts (4) and (6) for `S999`; their source-cell and anchor-quote checks are not what rejects this world.
5. **(5) adds the later missing-`verified-at` finding** (`:183-185`). The entry does have `recheck: 90d`, so no missing-recheck finding appears.
6. **(7) adds the later coverage-map finding** (`:189-191`). Finally, `:193-195` returns grounded count 0 because findings exist, and `:292-295` prints them in accumulation order.

## Residual risk and verification gaps

- This is evidence only for the scoped junk-entry control, not for the truth of the admitted entry's prose or the overall C2/depth claim. The plan expressly bounds the counter to admission shape and citation resolution.
- The test does not show that every possible malformed entry is rejected; it shows that the exact required three-defect junk world is rejected, with the expected first failure and two later independent findings.
- No requested verification remains open: both the canonical `--rev` path and direct rebuilt files were measured. C1, the separate base/tip C2 predicate runs, and source/prose review were outside this seat and were not retested.
