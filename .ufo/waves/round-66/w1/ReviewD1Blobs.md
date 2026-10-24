# ReviewD1Blobs — r66 C2/D1 re-derived from committed bytes

Seat: reviewer (read-only). Assigned item: C2/D1 only — "each r65 registry path exists as a
nonempty JSON blob at the measured tip and is absent at pinned base. Report ancestry and exact
result; do not use the worktree."

- Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (round plan).
- Measured tip: `fc1b71e56fda86fefe672f2cae90a62318d34449` (the revision named by
  `receipts/C2-routed-after.txt:1,3` and `receipts/C2-integrity-after.txt:1`).
- Method: every byte below came from `git cat-file` / `git ls-tree` / `git show <rev>:<path>`
  against the lane object database. No worktree file was read for evidence. The only sandbox
  write was `/tmp/d1blobs.lp6HY2/counter.py` (a committed verifier extracted with
  `git cat-file blob 2a8eba5:verifiers/check_r66_routed_repairs.py`), run with `--root <lane>`.
  Nothing was written to the lane, its jj state, or its Git index.

## Exact result

| Path (as frozen in `verifiers/check_r66_routed_repairs.py:30-33`) | At `fc1b71e` (measured tip) | At `11385e04` (pinned base) |
|---|---|---|
| `.ufo/waves/round-65/w1/swarm-registry.json` | `git cat-file -e` rc=0; object `blob 362c9969e78fb2478ddb4f940747bb63b946dfb1`; 12,844 B; sha256 `a40abb1ac94e0d19fdf03cb383772985cb945d399a76c98da1fe629b5c5bcd30`; `json.loads` → dict, 6 keys (`schema, wave, createdAt, updatedAt, reportDir, members`), `bool(dict)`=True | `git cat-file -e` rc=128 → **absent**; no tree entry (see base listing below) |
| `.ufo/waves/round-65/w2/swarm-registry.json` | rc=0; `blob d2866536da7d671a3095b86e80c43ea9894ea896`; 11,755 B; sha256 `d71ffed342bdb4e657886ca28c20bee1666f8ab10eacdd9ab96931671d7e551b`; dict, 6 keys, nonempty | rc=128 → **absent**; no tree entry |

Both are `100644` stage-0 blobs, not trees/symlinks/executables (`git ls-tree -r -l`), and the two
documents are distinct (different blob ids, sizes, member key-sets). Non-recursive base tree of
`.ufo/waves/round-65` at `11385e04` contains only `census-after.txt, census-before.txt, controls/,
receipts/, snapshots/, w1-dispatch.err, w1-dispatch.json, w1-spec.json, w2-dispatch.err,
w2-dispatch.json, w2-spec.json` — no `w1/` or `w2/` entry of any kind, so base absence is not a
path-spelling artifact. (`git cat-file -t 11385e04:.ufo/waves/round-65/w1` → rc=128.)

Independent counter check, using the **committed frozen counter bytes** (SHA-256
`3129c0d7016467d93a3ea45a626dd1237bc92bd20d79bc09499c53c503293141`, identical at `e7d1d8c`,
`806b53b`, `fc1b71e`, `9e75e73`, `2a8eba5`, and equal to `controls/C2-counter-selftest.txt`), run
from `/tmp` with `--root` = lane:

```
$ python3 -B /tmp/d1blobs.lp6HY2/counter.py --root <lane> --rev fc1b71e56fda86fefe672f2cae90a62318d34449
control at 11385e04: 0 of 2
D1-r65-registries-committed: PASS
D2-corpus-integrity-reconciled: PASS
r66 routed defects closed 2 of 2      exit=0

$ ... --rev 11385e04e368c1e94ab1a5a89d7439033eb1f855
control at 11385e04: 0 of 2
D1-r65-registries-committed: FAIL
D2-corpus-integrity-reconciled: FAIL
r66 routed defects closed 0 of 2      exit=1
```

That counter's D1 reads only committed blobs (`show()` = `git show <rev>:<path>`,
`verifiers/check_r66_routed_repairs.py:59-75`), and its base gate refuses to certify anything
unless the pinned base itself scores 0 of 2 (`:126-130`). The verifier does not exist at the
pinned base (`git cat-file blob 11385e04:verifiers/check_r66_routed_repairs.py` fails); that is
irrelevant to the base score, which is computed from the base **tree**, not from a base copy of
the counter.

**Result: D1 re-derives true, exactly as claimed, at the measured tip and false at the pinned
base.**

## Ancestry

`git merge-base --is-ancestor 11385e04 fc1b71e` → true; 5 commits in `11385e04..fc1b71e`, a
linear chain, no merges:

```
11385e04 (base) -> e7d1d8c -> 806b53b -> daedcdf -> 4119647 -> fc1b71e (measured tip)
2a8eba5 (current git HEAD) -> parent 9e75e73 -> parent fc1b71e
98c994b0 (jj working-copy commit) -> parent 2a8eba5
```

- Introducing commit for both paths: `806b53b4491d6a52856ee856cd9c7c20a5472e27` "round-66: land
  G9 coupling and integrity fixes" (second commit after base). `git show --numstat` over the two
  paths: `329 0` and `329 0` — pure additions, no deletions elsewhere in `round-65/`.
- The blobs are unchanged through every later revision: `git ls-tree -r -l` yields the same two
  blob ids at `fc1b71e`, `9e75e73`, `2a8eba5` (HEAD) and `98c994b0` (jj working copy). No later
  commit modifies or deletes them.
- Freeze integrity: the counter bytes are bit-identical from the claim-freeze commit `e7d1d8c`
  through HEAD, so the "counter frozen before D1/D2 landing" claim in
  `controls/C2-counter-selftest.txt` holds against the committed history, not just the worktree.

## Provenance of the committed bytes (calibration, not required by the predicate)

- **Path identity:** at the pinned base, `w1-dispatch.json` / `w2-dispatch.json` already carry
  `registry.path` = exactly `.ufo/waves/round-65/w1/swarm-registry.json` /
  `.ufo/waves/round-65/w2/swarm-registry.json` (string-equal to the counter literals), plus
  `reportDir` and `schema` strings that the committed registries match.
- **Content identity:** the committed registries' `members` maps are exactly equal (32/32 parsed
  entries, object equality) to the `registry.members` maps committed **at the pinned base** inside
  those dispatch payloads. So the landed blobs are the r65 rendered registries, not new r66
  content.
- **State identity:** in both registries every member has `kind: "spawn"`, `agentId: null`, and
  `updatedAt == createdAt` (`.921Z` / `.947Z`, 26 ms apart). The generator's post-dispatch shape is
  visible in the older `round-47/build` registry, where `updatedAt` is later than `createdAt` and
  92 members have non-null `agentId`s. Null agent ids plus an unchanged `updatedAt` match a
  prepared-but-undispatched wave, consistent with r65's commit `484d325` ("prepared-but-undispatched
  L2 waves … dispatch payloads rendered").
- **Timestamp window:** `2026-10-24T06:15:11.921Z`/`.947Z` = `03:15:11-03:00`, 12 s before the r65
  prep commit `484d325` (`03:15:23-03:00`) and 41 min 38 s before the r66 landing commit `806b53b`
  (`03:56:49-03:00`). `schema: ufo-swarm-registry-v1` and the six top-level keys match the
  canonical registries of rounds 61, 63, 64 and 66.
- **No ignore exclusion:** the pinned base `.gitignore` contains only `.ufo/interactive-sessions/`,
  so the registries were not invisible to `git add` — the r65 defect was an uncommitted add, as
  routed.

## Findings

No finding invalidates D1 at the measured revisions. Ordered by severity:

1. **[Low] The frozen D1 predicate is presence-only; it does not check that the blob *is* the r65
   registry.** `tracked_nonempty_json` (`verifiers/check_r66_routed_repairs.py:63-71`) accepts any
   nonempty JSON *object* at either path, and the counter's only D1 kill fixture deletes a file
   (`:217-218`, `kill/D1-missing-registry`). A data-free `{"x":1}` blob, or a registry for a
   different wave, would also score PASS, so the claim's wording ("both generated r65
   swarm-registry.json blobs") is stronger than the predicate. At these revisions the claim is
   substantively true — the member maps are object-equal to the base-committed dispatch payloads
   (above) — so this is a predicate-strength risk to future re-measurement, not a false claim.
2. **[Info] Later revisions / tip precision.** The receipts measure `fc1b71e` ("final pre-report
   lane revision"); the lane is now at `2a8eba5` with a jj working-copy child `98c994b0`. D1 holds
   at all three with identical blob ids, so the claim is not tip-fragile. The plan text says
   `--rev <round-66-tip>`; the receipts' literal is `fc1b71e`, which is a strict ancestor of HEAD —
   worth keeping explicit in any closure text, but no contradiction.
3. **[Info] Added top-level metadata is self-asserted.** `wave`, `createdAt`, `updatedAt` are not
   derivable from the base-committed dispatch payloads (which embed only `schema, path, reportDir,
   members`). They match the canonical generator shape and the r65 prep window, but a timestamp is
   not proof against backdating; see residual risk.
4. **[Info] No D1→D2 count coupling to mis-attribute.** `corpus.index.tracked_files` counts
   `git ls-files corpus/` only (`verifiers/verify_corpus_integrity.py:6,606-611`); the two D1 blobs
   live under `.ufo/` and therefore do **not** contribute to the 116→118 tracked-file shift. Any
   seat attributing that delta to D1 would be wrong.
5. **[Info] No collateral caller.** No lane verifier walks `.ufo/waves/round-65/w1|w2` by default;
   the registries become the only entries in those directories, and `check_seat_counts.py` (the one
   gate that enumerates wave directories) requires explicit `--dir/--rev` and excludes
   `swarm-registry.json` by name (`verifiers/check_seat_counts.py:19-20,42-43`). Adding the two
   files changes no gate's default input set.

## Residual risk

- Whether the two files were physically present but untracked in the r65 working tree is **not
  provable from committed bytes**; untracked state is never recorded. Evidence consistent with it:
  base-embedded dispatch `members` equality, null agent ids, unchanged `updatedAt`, and the
  `03:15:11` timestamps relative to `484d325`. Evidence cannot exclude a deterministic
  re-render during r66.
- No pre-commit hash pair for the uncommitted artifacts exists in repo text (sibling scout reports
  the same gap), so byte-identity of the landed blobs to the r65-era working files rests on
  object-custody and the corroboration above.
- If a future revision regenerates the registries with the same shape but different rosters, D1
  will still PASS (finding 1).

## Verification gaps

- The registry generator is outside lane bytes: no lane `*.py` emits `ufo-swarm-registry-v1`
  (`grep` over lane Python: zero matches; only data files and `check_seat_counts.py`'s exclusion
  constant mention the registry name). Generator semantics were inferred from committed registry
  shapes (r47 vs r65) and cannot be re-executed here.
- `createdAt`/`updatedAt` cannot be validated beyond internal consistency with commit metadata.
- I did not re-run the corpus-integrity gate or any D2 check; those belong to the D2 seats.

## Tooling

No installs or upgrades were performed for this seat. No files were changed outside this report.
