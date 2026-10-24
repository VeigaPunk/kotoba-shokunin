# ExecCollision — round 67 wave 1

**Axis:** calibration / assimilation consistency.

**Measured inputs:** the current working-tree `corpus/SOURCES.md` and the read-only staged file `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md`. `git rev-parse master` printed `2a8eba56b3f9321b70c569fa2816d42237ca49a2`; the extraction read the working-tree file, not a historical checkout.

## Result

- **Collision count: 0.** `controls/collisions` is empty and `controls/collision-count` contains `0`.
- Readback counted **120 registry ids** (`S001`–`S115`, then `S117`–`S122`) and **164 staged ids** (`S123`–`S286`). Their intersection is empty.
- Because the collision set is empty, **no renumber map is required and nothing was renumbered**. No registry, staged-package, citation, or knowledge file was edited.

## Exact check evidence

The assigned commands were run with `A=/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-67/w1/controls`:

```sh
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md | grep -oE 'S[0-9]+' | sort > "$A/reg-ids"
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md | grep -oE 'S[0-9]+' | sort > "$A/staged-ids"
comm -12 "$A/reg-ids" "$A/staged-ids" > "$A/collisions"
wc -l < "$A/collisions" > "$A/collision-count"
```

The command batch exited 0. Output readback: `reg-ids` 120 lines, `staged-ids` 164 lines, `collisions` 0 lines, `collision-count` `0`.

## Non-vacuous guard

Scratch input `/tmp/kotoba-r67-exec-collision-guard-2a8eba56/registry.md` contained exactly `  | S002 |` (two leading spaces).

- The same 0–3-leading-space extraction pipeline exited 0 and produced `S002`.
- The column-zero-only variant using `^\|[[:space:]]*S[0-9]{3,}` exited 1 and produced 0 bytes.
- Assertions for caught output, column-zero rejection, and their expected exit statuses exited 0.

Observed guard receipt:

```text
caught_pipeline_exit=0
caught_output=S002
column_zero_pipeline_exit=1
column_zero_output_bytes=0
guard_assertions_exit=0
```

## Seat-written lane files

- `.ufo/waves/round-67/w1/controls/reg-ids`
- `.ufo/waves/round-67/w1/controls/staged-ids`
- `.ufo/waves/round-67/w1/controls/collisions`
- `.ufo/waves/round-67/w1/controls/collision-count`
- `.ufo/waves/round-67/w1/ExecCollision.md`

**Remaining risks:** this assigned check proves the literal id intersection only; document-level URL/anchor review would become necessary only for adopted citations in a nonempty-collision renumbering case. No such case occurred here.

**Blockers:** none.
