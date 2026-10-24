# CriticFleetOveraccept — round-66 w1 (godspeed, leaf critic)

**Scope attacked:** the commit-citation fleet-root fallback landed for C2 —
`commit_resolves()` in `verifiers/verify_corpus_integrity.py:591` and its
independent twin `analyse_commits()` in `verifiers/verify_corpus_independent.py:471`
(`_git(fleet_root, "cat-file", "-e", "<tok>^{commit}")` at :487-491, and the
pointer analogue `report_pointer_exists` at :263-268). Base observed:
`11385e04e368c1e94ab1a5a89d7439033eb1f855`; measured tip `2a8eba56`. All
fixtures below ran in `/tmp/fleetover.sqgRBL` (temporary sandbox; no lane or
fleet bytes touched).

## Counterexamples

### A — token resolves only in a wrong repository (CONFIRMED, both implementations)

`commit_resolves` guards the hop with `fleet_root.is_dir()` only; the
independent path guards it not at all. When `fleet_root` exists but is not a
repository, `git -C <fleet_root>` walks **upward** to the nearest enclosing
repository and `cat-file -e` resolves there. The docstring claims "a
fleet_root that is missing or is not a git repository reads False" — it reads
False only by accident of where the directory happens to sit.

Sandbox (`enclosing/` is a repo; `enclosing/subdir/notarepo` is not):

- `commit_resolves(ENC_SHA, lane, enclosing/subdir/notarepo)` → **True**
  (enclosing repo's commit accepted as a "fleet object"). Q61's declared
  resolution set is {lane repo, declared fleet root}; the enclosing repo is
  in neither.
- Independent path: `_git("…/subdir/notarepo", "cat-file", "-e",
  "<enc>^{commit}")` → exit 0 — same accept.
- `commit_resolves(FLEET_SHA, lane, enclosing/subdir/notarepo)` → False
  (fleet-only token correctly absent there) — i.e. the failure direction
  flips depending on which repo sits above.

**Live stakes, honestly bounded:** the real `FLEET_ROOT
/home/vgpnk/Projects/shokunin` is a git repo today, and the three fleet-only
citations (`7b370d54…`, `def4b9ff…`, `1154d57a…`) do **not** resolve in the
enclosing `/home/vgpnk` repository — so on this host a `.git` loss under the
fleet root degrades to visible DRIFT, not a silent pass. The over-accept is
real but conditional on the ancestor object store containing the token; it is
a fail-open in exactly the misconfiguration the docstring claims to handle.
Also note `/home/vgpnk` itself is a repo, so *every* non-repo directory under
it is subject to upward resolution.

### B — a blob/tree rather than commit (CONFIRMED for tag objects; blob/tree rejected)

`cat-file -e <tok>^{commit}` accepts **annotated-tag object SHAs**: the
`^{commit}` peel dereferences the tag to its target. Sandbox in the fleet
repo: `commit_resolves(TAG_SHA, lane, fleetrepo)` → **True** for
`c57b0a9a…` whose `cat-file -t` is `tag`. The gate's own spec says the token
"must … name a commit object"; a tag object is not a commit. Blob SHA
`6a69f920…` and tree SHA `6a0d993e…` are correctly rejected by the same
expression. The lane-first probe uses the identical expression, so a lane tag
SHA cited as `commit \`<tag>\`` is likewise accepted — the flaw is in the
peel arg, not only in the hop.

### C — invalid fleet root (CONFIRMED as covered-by-accident; D distinguishes)

- Missing dir: primary guarded (`is_dir` → False); independent correctly
  returns nonzero (`git -C` refuses). Clean.
- Non-repo dir **not** inside any repo: rejected — this is the only arm the
  existing self-tests cover (`commit-hop/fleet-not-a-repo`, `fleet_com`
  fixture), and it is satisfied *by git's failure to find any repo*, not by
  an explicit probe. It does not distinguish "declared root is a repo" from
  "no enclosing repo happened to exist" — the A fixture is the missing arm.
- `fleet_root` = a file: independent → nonzero (rejected, clean); primary →
  `is_dir()` False (clean).

### D — object absent everywhere (CONFIRMED correctly rejected)

`commit_resolves("f"*40, lane, fleetrepo)` → False; raw `cat-file -e
f…f^{commit}` nonzero in both stores. This arm is already honestly covered by
`commit-hop/neither` and the `big`/`genuinely absent` self-test fixtures.

### E — secondary, environmental: `GIT_DIR` leaks through `subprocess.run`

Neither `_git`/`git_ok` filters `GIT_*` env vars. With
`GIT_DIR=/tmp/fleetover.sqgRBL/lane/.git` exported, `git -C <fleetrepo>
cat-file -e <lane_sha>^{commit}` → exit 0: the fallback resolves in an
**arbitrary** repo named by the caller's environment, defeating `-C` entirely
(`GIT_OBJECT_DIRECTORY`/`GIT_ALTERNATE_OBJECT_DIRECTORIES` widen it further).
Environmental rather than corpus-injected, but a one-line `env` scrub makes
the declared set airtight.

## Impacted axes

- **Depth (C1 claim area): none** — the attack lives entirely in C2 territory.
- **Consistency/calibration (C2): yes.** Q61's criterion requires resolution
  against "the declared fleet root"; A resolves against an undeclared
  ancestor repository, and B admits a non-commit object under a commit
  citation — both are false accepts inside the very hop the claim measures.
- **Verifier falsifiability:** the D2 counter
  (`check_r66_routed_repairs.py::check_d2`) is text-presence only — its own
  "honest" fixture is `def commit_resolves(hex_id): pass`. No counter arm
  distinguishes a correct hop from an always-true or enclosing-repo hop; the
  over-accepts would survive counter evaluation undetected. (Fixable, and
  noted for the mutation seat rather than judged fatal here.)

## Minimal test (what to add, nothing more)

`verify_corpus_integrity.py` self-test, inside the existing `TemporaryDirectory`
block — two arms next to `commit-hop/fleet-not-a-repo`:

```python
enc = root / "enclosing"; enc_sub = enc / "sub"
_one_commit_repo(enc, "enclosing seed\n")          # enc IS a repo
enc_sha = subprocess.run(["git","-C",str(enc),"rev-parse","HEAD"],
                        capture_output=True,text=True,check=True).stdout.strip()
enc_sub.mkdir()                                     # enc_sub is NOT a repo
eq("commit-hop/fleet-nonrepo-under-repo",
   commit_resolves(enc_sha, lane_git, enc_sub), False)
enc_git = root / "enc-git"; _one_commit_repo(enc_git, "enc\n")
subprocess.run(["git","-C",str(enc_git),"tag","-a","-m","m","v9",
                subprocess.run(["git","-C",str(enc_git),"rev-parse","HEAD"],
                capture_output=True,text=True,check=True).stdout.strip()],check=True)
tag_sha = subprocess.run(["git","-C",str(enc_git),"rev-parse","v9"],
                        capture_output=True,text=True,check=True).stdout.strip()
eq("commit-hop/tag-object-not-a-commit",
   commit_resolves(tag_sha, lane_git, enc_git), False)
```

Mirrored arm for `verify_corpus_independent.py` (`analyse_commits` with a
non-repo `fleet_root` under a repo; a tag SHA in the lane repo cited as
``commit `<tagsha>` `` → must land in `commit_unresolvable`).

## Smallest safe correction

1. `git_ok(fleet_root, "cat-file", "-t", hex_id) == "commit"` (replace the
   `^{commit}` peel for both lane and fleet lookups; run `-t` output against
   `== "commit"`). Rejects tag/blob/tree/absent uniformly; ref-name tokens
   still resolve honestly to their type.
2. Before the fleet query, probe repo-ness of the *root itself*, e.g.
   `git -C fleet_root rev-parse --show-toplevel` compared realpath-equal to
   `fleet_root` (or `rev-parse --absolute-git-dir` contained under
   `fleet_root`). A non-repo inside any ancestor then reads False as the
   docstring already claims. Same probe in the independent path, which today
   has no guard at all.
3. (Secondary) strip `GIT_DIR`, `GIT_WORK_TREE`, `GIT_OBJECT_DIRECTORY`,
   `GIT_ALTERNATE_OBJECT_DIRECTORIES` from the subprocess env in `git_ok`/`_git`.

## Does it change the intended scope? — No.

- **Frozen predicates:** `check_d2` requires only the `COMMIT_HOP_MARKER`
  literal, `def commit_resolves(`, `inside_code_span`, and the
  `commit_resolves(hex_id` signature — all untouched by tightening the body.
- **Measured counts:** all 38 live corpus citations verified `cat-file -t
  == commit` in lane or fleet (3 fleet-only, the r62/r65/r66 closure
  spot-check citations) — the fix accepts exactly the current accepted set;
  `commit_total`/`unresolvable`/`nonhash` pins unchanged, so the frozen 2-of-2
  predicate and the `commit_total 37`/`0` baseline pins still hold.
- **Self-test counts:** the +2/+2 assertion arms are additive; no frozen
  predicate pins those totals (receipts record 161/103 today).
- **Net effect:** narrows false accepts (enclosing-repo resolution, tag
  objects) without refusing any citation the corpus actually makes. This is
  a fixable defect inside the claim's own Q61 semantics, not a tradeoff the
  judge should eat.

No installs performed; no lane/fleet files mutated (sandbox only).
