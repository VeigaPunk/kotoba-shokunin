# ExecC2JunkControl — Round 67 wave 1

## Outcome

Built the C2 junk control world and left it ready at
`.ufo/waves/round-67/w1/controls/junk-world/`.

**Blocker:** the assigned drafted counter,
`.ufo/waves/round-67/w1/drafts/check_instruction_authority.py`, was absent on the
initial read, absent again after world construction, and absent from a final
lane-wide exact-basename glob. I did not wait in a loop and did not claim a
counter rejection. The required counter run remains pending until that file
appears.

## Files changed

- `.ufo/waves/round-67/w1/controls/junk-world/` — scratch mirror of the committed
  base, with the junk knowledge entry and the scratch LOG evidence note.
- `.ufo/waves/round-67/w1/controls/C2-junk-control.txt` — ready-to-run command,
  unavailable-counter status, and verbatim static preflight output.
- `.ufo/waves/round-67/w1/ExecC2JunkControl.md` — this report.

No production file was changed. No git or jj write command was run. The scratch
revision's loose objects were constructed directly in the copied scratch object
database; the lane's HEAD, refs, index, and jj state were not mutated.

## World and behavior

- Pinned/measured base: `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (the lane
  HEAD also remained this revision).
- Junk revision: `429ca66fd28ad58fc0347679b799ed2af3b0ece6`, whose parent is the
  pinned base. It is a dangling commit in the scratch mirror, addressed directly
  by `--rev`; no ref was moved.
- `corpus/knowledge/instruction-authority-ladder-round67.md` has 693 real bytes
  and a superficial knowledge-entry shape, but:
  1. its only `source:` identifier is `S999`, which has no row in the revision's
     `corpus/SOURCES.md`;
  2. it has zero `verified-at:` lines;
  3. `corpus/README.md` has zero mentions of its path.
- `corpus/SOURCES.md` and `corpus/README.md` are byte-identical to base. The only
  base-to-junk paths are the added entry and `LOG.md` (the mirror's required
  evidence note).

## Exact evidence

Committed-world preflight printed:

```text
entry_bytes=693
source_ids=S999
unresolved_source_ids=S999
verified_at_lines=0
coverage_index_mentions=0
```

Independent byte comparisons printed:

```text
corpus/README.md_byte_identical_to_base=True
corpus/SOURCES.md_byte_identical_to_base=True
```

`git -C <junk-world> diff --name-status <base> <junk-rev>` printed:

```text
M	LOG.md
A	corpus/knowledge/instruction-authority-ladder-round67.md
```

`git -C <junk-world> diff --check <base> <junk-rev>` exited 0. The junk commit's
subject is `Round 67 C2 junk do-nothing control`; `git cat-file -e <junk-rev>^{commit}`
succeeded in the junk world.

## Ready counter command

After copying the drafted counter to the junk mirror's
`verifiers/check_instruction_authority.py`, run:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-67/w1/controls/junk-world/verifiers/check_instruction_authority.py --rev 429ca66fd28ad58fc0347679b799ed2af3b0ece6
```

This path form deliberately assumes only the planned `--rev` interface: the
counter's parent-derived lane root will be the junk world. Required verdict: it
must not print `authority ladder grounded 1 of 1`, and it must exit nonzero.
Verbatim counter output and exit code are **N/A** because the counter was absent;
see `controls/C2-junk-control.txt`.

## Remaining risks / blockers

- The sole blocker is the missing drafted counter; its behavioral rejection of
  the prepared world is unmeasured.
- The static preflight establishes the three required junk properties, not the
  counter's verdict. No depth-axis judgment is made here.
