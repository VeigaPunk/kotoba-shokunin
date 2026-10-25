# ExecCollision — round 68, wave 1, item 10 (id-collision check in scratch)

Executor seat, scoped findings only. All paths relative to the lane repo
`kotoba-shokunin/`. No production file was touched; everything below was
computed in scratch under `.ufo/waves/round-68/w1/assimilation/`.

## The frozen check — printed numbers

Command run verbatim from the round prompt, output as printed by `wc -l`:

```
128 .ufo/waves/round-68/w1/assimilation/reg-ids
174 .ufo/waves/round-68/w1/assimilation/staged-ids
  5 .ufo/waves/round-68/w1/assimilation/collisions
307 total
```

- registry ids extracted: **128** (`corpus/SOURCES.md`)
- staged ids extracted: **174** (`/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md`, read-only)
- collisions: **5**

## `collisions` is NOT empty

`cat collisions` prints exactly:

```
S198
S199
S200
S201
S202
```

These are the **five C1 client trust-gate rows** (vtcode / parallelworks /
kilo.ai / agent-framework / mistral-vibe — S198–S202). Both sides located:

| id | in staged block (line of `SOURCES.append.md`) | already in registry (line of `corpus/SOURCES.md`) |
|---|---|---|
| S198 | 75 | 139 |
| S199 | 76 | 140 |
| S200 | 77 | 141 |
| S201 | 78 | 142 |
| S202 | 79 | 143 |

Reading: the registry already carries S198–S202 (appended for C1 this round;
registry ids now run to S202). The staged append block — which was built
including those same five rows — re-offers them. The other **169** staged rows
(S130–S197, S203–S303) are collision-free against the registry as it stands.

## Guard non-vacuousness — proved on scratch

Full transcript: `.ufo/waves/round-68/w1/assimilation/guard-proof.txt`
(fixture: `fixture-registry.md`, built in scratch with a two-leading-space row
whose id `S130` collides with a staged id).

- 0–3-space census pattern `^ {0,3}\|[[:space:]]*S[0-9]{3,}` → **catches** the
  indented colliding row (`4:  | S130 | an INDENTED colliding row …`).
- column-zero-only pattern `^\|[[:space:]]*S[0-9]{3,}` → **misses** it; returns
  only the column-zero `S001` row.

So the naive pattern would compute a falsely-empty collision set here; the
frozen check's pattern has discriminating power exactly where the naive one
fails. Guard proved non-vacuous.

## What this hands the L1 (no judgment executed here)

- The append must not re-add S198–S202: those five staged rows should be
  **dropped from the append set** (their ground is already registered), fixed in
  scratch only, per the plan's rule "a nonempty collision file is fixed in
  scratch only, and every adopted citation is re-pointed **by document**, never
  by arithmetic".
- Any knowledge entry drafted against staged ids S198–S202 should cite the
  **registered** rows at `corpus/SOURCES.md:139–143` (same documents: the five
  C1 client URLs), not renumbered staged arithmetic.
- The 169 remaining staged rows collide with nothing as measured today; if the
  L1 appends any of them, re-run this exact check after the append since the
  registry's id space will have moved.

## Evidence pointers

- Frozen check stdout: the `wc -l` block above (command + output).
- `collisions` content: `.ufo/waves/round-68/w1/assimilation/collisions`
- Id lists: `.ufo/waves/round-68/w1/assimilation/reg-ids`,
  `.ufo/waves/round-68/w1/assimilation/staged-ids`
- Guard proof: `.ufo/waves/round-68/w1/assimilation/guard-proof.txt`
- Both-side line numbers: produced by `grep -n "^| <id> "` against each file in
  this session's tool log.
