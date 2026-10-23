# ExecInstancesA4 — E2c full-sha alias instances

**Axis:** depth. This report freezes concrete A4(iv) inputs and records the direct probe against the read-only r61 counter. No lane source, verifier, plan, fleet, state, or jj/git-index file was changed.

## Frozen instances and expected verdicts

These are the two required E2c rejects plus the two benign controls. Hashes are full lowercase SHA-256 values unless explicitly marked `sha256_prefix`.

```python
SHA_W1 = "971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff"
SHA_S110 = "c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8"
SHA_S106 = "00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980"
PREFIX_S048 = "00e45ea5"

# F-A4-7 / W1: full hash exists at base as S043; counted synthetic row S103
# carries the ordinary re-open teaches cell, not anchored supersedes.
BASE_ROWS_F_A4_7 = {
    "S043": {"sha256": SHA_W1},
}
REJECT_F_A4_7 = {
    "id": "S103",
    "sha256": SHA_W1,
    "teaches": "re-opens S043 — recycled bytes; no byte-identity declaration",
}
EXPECTED_F_A4_7 = (
    "REJECT",
    "already recorded by base row S043",
)

# F-A4-11 / condition (5): the alias is S043, but the anchored declaration
# names S048, whose actual base-row record has only the 8-hex prefix.
BASE_ROWS_F_A4_11 = {
    "S043": {"sha256": SHA_W1},
    "S048": {"sha256_prefix": PREFIX_S048},
}
REJECT_F_A4_11 = {
    "id": "S103",
    "sha256": SHA_W1,
    "teaches": "supersedes S048 — byte-identical declaration names prefix-only S048",
}
EXPECTED_F_A4_11 = (
    "REJECT",
    "declared row S048 does not record the aliased sha",
)

# Honest S110 precedent: the declaration names S096, whose base row has the
# same full digest; this is accepted byte-identity, not a fresh-fetch alias.
BASE_ROWS_S110 = {"S096": {"sha256": SHA_S110}}
ACCEPT_S110 = {
    "id": "S110",
    "sha256": SHA_S110,
    "teaches": "supersedes S096 — byte-identical correction of the S096 hook-event anchor",
}
EXPECTED_S110 = ("ACCEPT", [])

# Prefix control: S048 records only 00e45ea5; S106's complete digest must not
# collide with that prefix in A4(iv). (The S106 full digest is also recorded
# in current S106/S114 rows; those re-open rows are not a full-hash alias to
# S048 under this condition.)
BASE_ROWS_S106 = {"S048": {"sha256_prefix": PREFIX_S048}}
ACCEPT_S106_PREFIX = {
    "id": "S106",
    "sha256": SHA_S106,
    "teaches": "re-opens S048 — Copilot CLI's repository modular instruction files use the matching path key",
}
EXPECTED_S106_PREFIX = ("ACCEPT", [])
```

The two required attack verdicts and reason substrings are the **contract expectation**, not a claim that both pass against the pre-r62 primitive: F-A4-7 is rejected by the current primitive; F-A4-11 is accepted by it, as the scratch output below shows. Keep F-A4-11 as a separate condition-(5) kill; replacing it with a no-declaration example would not test target-row sha binding.

| Fixture | Expected verdict | Expected reason substring |
|---|---|---|
| F-A4-7 / full SHA recorded by S043; teaches does not start `supersedes S### —` | REJECT | `already recorded by base row S043` |
| F-A4-11 / anchored `supersedes S048 —`; S048 records only `00e45ea5` | REJECT | `declared row S048 does not record the aliased sha` |
| S110 / anchored declaration and matching full SHA | ACCEPT | empty reason list (`[]`) |
| S106 / S048's 8-hex prefix only | ACCEPT | empty reason list (`[]`) |

## Seven binding conditions frozen with the matrix

1. Build the base-table collision map from `BASE = 31092dc6`; S103–S111 are absent there and S043's full SHA is present. Exclude the counted row's own id unconditionally, even when a later selected base happens to contain it.
2. The fixture's base commit must actually contain S043 and its full SHA. A header-only base commit is vacuous and lets W1 pass.
3. Only a declaration anchored at the beginning of teaches (`supersedes S### —`) can establish byte identity. A row carrying that declaration is not a fresh eligible row and must not also carry a fresh-fetch claim. Appending `; supersedes S043` after `re-opens ...` must not exempt the alias.
4. Scan the measured commit's table as well as BASE, excluding the counted row itself; otherwise an alias introduced in the measured changeset is invisible.
5. Validate the named id against the base row's **recorded full 64-hex SHA**. F-A4-11 must reject because S048 has only `00e45ea5`, even though S043 holds the aliased full SHA.
6. Scan all 11 parsed SOURCES cells of a declared row for `fetched <ISO>`, not just teaches. A fetched assertion in anchor or scope invalidates byte-identity; such a row is barred from fresh-fetch claims.
7. Compare full 64-hex SHA strings only. An 8-hex prefix is not A4(iv) alias evidence; S048's `00e45ea5` must not reject S106's full digest.

## Supplemental probes for binding conditions (3) and (6)

Condition (3) appended-teaches input:

```python
sha = SHA_W1
base_shas = {SHA_W1: "S043"}
teaches = "re-opens S043 — Scope rules frontmatter; supersedes S043"
# Expected: REJECT; reason contains "teaches cell declares no supersedes".
```

Condition (6) uses the 11 parsed SOURCES cells in order `[id, source, kind, tier, scope, anchor, teaches, status, opened, recheck, used-by]`. The fetch assertion is deliberately in `anchor`, not teaches:

```python
CONDITION6_ROW = (
    "S103",
    "Claude Code — How Claude remembers your project — https://code.claude.com/docs/en/memory.md",
    "docs",
    "A",
    "Claude Code project rule files and frontmatter paths",
    "§ Path-specific rules (memory.md:194-200); fetched 2026-10-23T12:06:23Z, HTTP 200, 51,971 B, sha256 `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`",
    "supersedes S043 — byte-identical reuse of the S043 page bytes",
    "mined",
    "2026-10-23",
    "90d",
    "corpus/knowledge/scoped-rules-round60.md",
)
# Expected full-row verdict: REJECT; reason contains "fresh-fetch claim".
```

## Scratch probe: exact command, output, and result

Scratch source: `/fast/scratch/hyaku/kotoba-r62/KotobaR62.ExecInstancesA4/a4_instances.py` (not evidence). Its complete content is reproduced here so the report retains every literal input; the script imports the read-only counter and calls `alias_sha_why`/`SUPERSEDES_RE`.
```python
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

COUNTER_PATH = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py")
spec = spec_from_file_location("r61_check_scoped_rules_probe", COUNTER_PATH)
checker = module_from_spec(spec)
sys.modules[spec.name] = checker
spec.loader.exec_module(checker)

SHA_W1 = "971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff"
SHA_S110 = "c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8"
SHA_S106 = "00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980"
PREFIX_S048 = "00e45ea5"

print("SUPERSEDES_RE.pattern =", repr(checker.SUPERSEDES_RE.pattern))
for label, text in (
    ("anchored_S110", "supersedes S096 — byte-identical correction"),
    ("appended_S043", "re-opens S043 — Scope rules frontmatter; supersedes S043"),
    ("wrong_target_S048", "supersedes S048 — byte-identical declaration"),
):
    match = checker.SUPERSEDES_RE.match(text)
    print(f"SUPERSEDES_RE.match {label} ->", repr(match.group(1) if match else None))

cases = (
    (
        "reject_full_sha_no_anchored_declaration",
        SHA_W1,
        {SHA_W1: "S043"},
        "re-opens S043 — recycled round-53 bytes; no byte-identity declaration",
        "REJECT; reason contains 'already recorded by base row S043'",
    ),
    (
        "reject_condition5_wrong_named_prefix_row",
        SHA_W1,
        {SHA_W1: "S043", PREFIX_S048: "S048"},
        "supersedes S048 — byte-identical declaration names prefix-only S048",
        "REJECT; reason contains 'declared row S048 does not record the aliased sha'",
    ),
    (
        "accept_S110_honest_byte_identity",
        SHA_S110,
        {SHA_S110: "S096"},
        "supersedes S096 — byte-identical correction of the S096 hook-event anchor",
        "ACCEPT; reason []",
    ),
    (
        "accept_S106_full_sha_vs_S048_eight_hex_prefix",
        SHA_S106,
        {PREFIX_S048: "S048"},
        "re-opens S048 — Copilot CLI's repository modular instruction files use the matching path key",
        "ACCEPT; reason []",
    ),
    (
        "condition3_unanchored_appended_supersedes",
        SHA_W1,
        {SHA_W1: "S043"},
        "re-opens S043 — Scope rules frontmatter; supersedes S043",
        "REJECT; appended declaration must not satisfy anchored exemption",
    ),
)
for label, sha, base_shas, teaches, expected in cases:
    actual = checker.alias_sha_why(sha, base_shas, teaches)
    print(f"{label}: sha={sha!r}; base_shas={base_shas!r}; teaches={teaches!r}")
    print(f"  expected={expected}")
    print(f"  alias_sha_why={actual!r}")

# SOURCES row cells: [id, source, kind, tier, scope, anchor, teaches, status,
# opened, recheck, used-by].  The fetched assertion is intentionally in anchor,
# not teaches, matching MutA4's condition-6 anchor-cell seam.
condition6_row = (
    "S103",
    "Claude Code — How Claude remembers your project — https://code.claude.com/docs/en/memory.md",
    "docs",
    "A",
    "Claude Code project rule files and frontmatter paths",
    "§ Path-specific rules (memory.md:194-200); fetched 2026-10-23T12:06:23Z, HTTP 200, 51,971 B, sha256 `" + SHA_W1 + "`",
    "supersedes S043 — byte-identical reuse of the S043 page bytes",
    "mined",
    "2026-10-23",
    "90d",
    "corpus/knowledge/scoped-rules-round60.md",
)
fetch_in_anchor = "fetched 2026-10-23T12:06:23Z" in condition6_row[5]
fetch_in_teaches = "fetched 2026-10-23T12:06:23Z" in condition6_row[6]
condition6_actual = checker.alias_sha_why(SHA_W1, {SHA_W1: "S043"}, condition6_row[6])
print("condition6_row_cell_count =", len(condition6_row))
print("condition6_fetch_in_anchor =", fetch_in_anchor)
print("condition6_fetch_in_teaches =", fetch_in_teaches)
print("condition6_expected = REJECT; reason contains 'fresh-fetch claim'")
print("condition6_alias_sha_why (teaches-only API) =", repr(condition6_actual))
```

Command: `date -u && python3 -B /fast/scratch/hyaku/kotoba-r62/KotobaR62.ExecInstancesA4/a4_instances.py`

`date -u`: `Fri 23 Oct 2026 08:52:06 PM UTC`  
Exit code: `0`

Exact output:

```text
Fri 23 Oct 2026 08:52:06 PM UTC
SUPERSEDES_RE.pattern = '^supersedes\\s+(S\\d{3,})\\b'
SUPERSEDES_RE.match anchored_S110 -> 'S096'
SUPERSEDES_RE.match appended_S043 -> None
SUPERSEDES_RE.match wrong_target_S048 -> 'S048'
reject_full_sha_no_anchored_declaration: sha='971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff'; base_shas={'971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff': 'S043'}; teaches='re-opens S043 — recycled round-53 bytes; no byte-identity declaration'
  expected=REJECT; reason contains 'already recorded by base row S043'
  alias_sha_why=['A4: snapshot sha256 971d75bfce7a... is already recorded by base row S043 and the teaches cell declares no supersedes']
reject_condition5_wrong_named_prefix_row: sha='971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff'; base_shas={'971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff': 'S043', '00e45ea5': 'S048'}; teaches='supersedes S048 — byte-identical declaration names prefix-only S048'
  expected=REJECT; reason contains 'declared row S048 does not record the aliased sha'
  alias_sha_why=[]
accept_S110_honest_byte_identity: sha='c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8'; base_shas={'c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8': 'S096'}; teaches='supersedes S096 — byte-identical correction of the S096 hook-event anchor'
  expected=ACCEPT; reason []
  alias_sha_why=[]
accept_S106_full_sha_vs_S048_eight_hex_prefix: sha='00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980'; base_shas={'00e45ea5': 'S048'}; teaches="re-opens S048 — Copilot CLI's repository modular instruction files use the matching path key"
  expected=ACCEPT; reason []
  alias_sha_why=[]
condition3_unanchored_appended_supersedes: sha='971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff'; base_shas={'971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff': 'S043'}; teaches='re-opens S043 — Scope rules frontmatter; supersedes S043'
  expected=REJECT; appended declaration must not satisfy anchored exemption
  alias_sha_why=['A4: snapshot sha256 971d75bfce7a... is already recorded by base row S043 and the teaches cell declares no supersedes']
condition6_row_cell_count = 11
condition6_fetch_in_anchor = True
condition6_fetch_in_teaches = False
condition6_expected = REJECT; reason contains 'fresh-fetch claim'
condition6_alias_sha_why (teaches-only API) = []
```

## Evidence, risk, and blocker

- Source shapes are grounded in `plans/round-62.md` §C1; `plans/round-61.md` §E2c and its seven binding conditions; `.ufo/waves/round-61/wave/MutA4.md` F-A4-7/F-A4-11/F-A4-12 and alias-matrix receipts; and the committed S048/S096/S103/S106/S110/S114 rows in `corpus/SOURCES.md`.
- The existing frozen `alias_sha_why(sha, base_shas, teaches)` (read at `verifiers/check_scoped_rules.py:1186-1197`) accepts the anchored wrong-target F-A4-11 case because it checks only whether the regex matches; it cannot inspect the named row's recorded digest. It also cannot see condition (6)'s anchor-cell fetch assertion because that row cell is not an argument. Observed direct outputs are `[]` for both required row-level rejections. These are material integration risks: the r62 matrix must retain the expected rejections and must not report them as passing against this primitive.
- No builds, tests, linters, formatters, installs, git commands, or jj commands were run. The only execution was the explicitly requested scratch Python probe above.

Installs: no installs.  
Blockers: the read-only r61 primitive does not implement E2c conditions (5) and (6); this report freezes the required cases and exact observed misses for L1 integration.  
Produced: E2c's two full-sha rejection fixtures, S110 and prefix benign controls, and condition-(3)/(6) probes.
