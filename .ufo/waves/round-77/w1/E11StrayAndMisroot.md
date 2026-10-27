# E11StrayAndMisroot — R76-D1 stray path + fleet-root misroot sweep (round 77, w1)

Seat: executor, leaf. Scope: read-only determination plus one read-only sweep script.
No clone, no scratch dir, no lane/git/jj mutation, no helper run, no tool installs.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` @ `6523aced1ee0ebe07dca996213bdc645a6acbd1e`
(`round-77: freeze plan, base receipts (counters unchanged from r76 freeze)`), branch `master`
(`git config --get lane.branch` -> `master`; `git rev-parse refs/heads/master` -> `6523aced1ee0…` exp-tip).

## 1. Verified inventory (all commands read-only; every exit code is the command's own)

```
$ git ls-files | grep -i 'kotoba-shokukin'
kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md
kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md
$ find kotoba-shokukin -type f
kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md
kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md
```

Two tracked stray paths, not one. Sizes 3543 B / 1201 B (22 / 10 lines).

```
$ cmp .ufo/waves/round-76/w1/A18ScoutSnapshot.md kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md
$ echo $?            -> 0
$ sha256sum .ufo/waves/round-76/w1/A18ScoutSnapshot.md kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md
ae39b182e2bf4b95b7337f65fb6ceb4cb423e5b37fd4c0ffb9e49de9238118fb  .ufo/waves/round-76/w1/A18ScoutSnapshot.md
ae39b182e2bf4b95b7337f65fb6ceb4cb423e5b37fd4c0ffb9e49de9238118fb  kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md
```

Branch-tip membership (`git cat-file -e "refs/heads/master:<path>"`):

| path | in `refs/heads/master` |
|---|---|
| `kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` | **present** |
| `.ufo/waves/round-76/w1/A18ScoutSnapshot.md` (correct) | present |
| `kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md` | **present** |
| `.ufo/waves/round-75/w1/R75Facet48.md` (correct) | **ABSENT** |

Provenance (`git show --name-status --format='%h %s'`):

```
16c9ca2                     A  kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md
ac9f295 round-75: preserved  A  kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md
6ce2724 round-76: recovered  A  kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md
```

Both recovery commits **added a misrooted copy**; neither added the correct lane path.

Consequence, and the reason the two strays are not symmetric:

- **A18 stray is a pure duplicate** — the correct copy is committed and byte-identical (sha `ae39b182…8118fb`). Deletion loses nothing. This is R76-D1 as written.
- **R75Facet48 stray is the only copy.** `.ufo/waves/round-75/w1/` holds `R75Facet01…47` and `R75Facet49`; `R75Facet48` is missing there, and `R75Facet48` is a real seat (`grep` of `.ufo/waves/round-75/w1-spec.json` shows `{"name": "R75Facet48", "role": "scout", "axes": ["calibration","operability"] …}` and `w1-results.json:292` records its report path). Deleting it would destroy a real round-75 seat report. The recovery claim in `corpus/lessons/round-75.md:12` and `corpus/lessons/round-75-verifier-spotcheck.md:44` ("Copied byte-exact to the same relative lane path … then removed only the fleet-root copy") is **false at the tip**: the copy that git carries is `kotoba-shokukin/…`, i.e. exactly the typo prefix, and `refs/heads/master:.ufo/waves/round-75/w1/R75Facet48.md` does not exist. Same defect class as `corpus/lessons/round-76-verifier-spotcheck.md:25` (CD1), one round earlier and still open.

No gate reads either stray path: `git grep -n 'kotoba-shokukin/'` over the lane tree hits only prose/lesson/results text, and `grep -rn '\.ufo/waves' verifiers/` hits only docstring/fixture prose — no verifier globs `.ufo/waves/**`. Removing or moving these paths cannot move C1/C2 or any no-harm gate.

## 2. Mechanism, from `/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh`

`cmd_commit` canonicalizes each named path (line 630: `realpath -m --relative-to=. -- "$p"`), then routes it in a three-way branch (lines 632–647):

```
632   repo_path_allowed "$q" || exit 1
634   if [ -d "$q" ]; then
635     req+=("$q"); fs_dirs+=(root:"…"); fs_req+=(root:"…")
636   elif [ -e "$q" ] || [ -L "$q" ]; then            # still on disk
637     req+=("$q"); files+=("$q"); fs_files+=(root-file:"…"); fs_req+=(root-file:"…")
641   elif git cat-file -e "refs/heads/$branch:$q" 2>/dev/null; then
642     # Deleted or renamed-away path present in the branch tip: include it so
643     # the commit records the deletion.
644     req+=("$q"); fs_req+=("root-file:\"$(fileset_escape "$q")\"")
646     echo "warn: skipping missing path $p" >&2      # neither on disk nor in tip
```

`repo_path_allowed` (506–519) rejects `.git*`, `.jj*`, and the literals `.ufo`, `.ufo/state`, `.ufo/state/*`, `.ufo/watchdog.log`. A top-level `.ufo/waves/...` path and a `kotoba-shokukin/.ufo/...` path both fall to `*) return 0`, i.e. **allowed** — I re-evaluated that exact `case` block on the stray path and it prints `ALLOWED`. `realpath -m` on a non-existent path still normalizes (verified: `realpath -m --relative-to=. -- does/not/exist.md` -> `does/not/exist.md`), so a deleted path canonicalizes to the same repo-relative string.

Post-commit, `validate_change_scope` (522–567) re-reads the candidate tree as NUL-delimited `--no-renames` diff, requires each status in `A|M|D|T`, requires every changed path to sit under one named request path (549–553: otherwise `commit changed a path outside the request`), and enforces the phantom guard:

```
560   if [ "$status" = D ] && { [ -e "$cpath" ] || [ -L "$cpath" ]; }; then
561     err "commit would delete $cpath but it exists on disk (nested repo?) — refusing"
```

## 3. Answer: is a plain `rm` enough?

**Yes — and it is required.** Three facts from the code above:

1. With the working-tree file still present, line 636 wins: the path is `jj file track`ed and diffed as a *content* change. Identical bytes -> `jj diff --summary` is empty -> `nothing to commit`, exit 0 (line 675–678), stray survives. So the helper alone, without a prior `rm`, does **not** delete it.
2. With the working-tree file gone, `[ -e "$q" ]` fails and line 641 succeeds because the path is in `refs/heads/master` (verified above). The path is added to `req`/`fs_req`, `jj diff --summary` reports `D`, and the commit records the deletion. No `git add`, no `git rm`, no index write is needed anywhere.
3. The phantom guard is what makes `rm` *necessary* rather than optional: any route that records `D` while bytes remain on disk (`jj file untrack`, `git rm --cached`, an `mv` that leaves a copy) is refused at line 560–561 with `— refusing`, so the bookmark never advances. Deletion requires the bytes to be absent from the working tree first.

Ordering therefore matters: **`rm` first, helper second**, in the same working copy the helper will snapshot (`jj-lane.sh commit` `cd`s to the lane's physical path itself, so the helper invocation can be issued from any cwd provided the `-- <path>` is lane-relative).

## 4. Exact invocation for the L1

Minimal, single lane commit, R76-D1 only (A18 duplicate; correct copy already committed):

```
rm -f -- /home/vgpnk/Projects/shokunin/kotoba-shokunin/kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md

/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh commit \
  /home/vgpnk/Projects/shokunin/kotoba-shokunin \
  --as kotoba \
  -m "round-77: delete misrooted kotoba-shokukin/ duplicate of A18 seat report (R76-D1)" \
  -- kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md
```

`--as kotoba` is forced by the helper: `lane_id_jj` reads `user.name` (`jj --ignore-working-copy config get user.name` -> `kotoba-shokunin`) and strips the `-shokunin` suffix; `cmd_commit` accepts only `$lane_id` or `protocol` (line 621–623). Identity, branch, child-of-tip and conflict-free checks then run automatically.

Recommended single commit that also fixes the second stray without losing the only copy (restore + delete, 3 tree changes, all inside the named paths):

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
cp -- kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md .ufo/waves/round-75/w1/R75Facet48.md
cmp -- kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md .ufo/waves/round-75/w1/R75Facet48.md      # expect exit 0
rm -f -- kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md \
         kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md

/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh commit \
  /home/vgpnk/Projects/shokunin/kotoba-shokunin \
  --as kotoba \
  -m "round-77: un-misroot seat reports — restore R75Facet48 at its lane path, drop kotoba-shokukin/ duplicates (R76-D1)" \
  -- .ufo/waves/round-75/w1/R75Facet48.md \
     kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md \
     kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md
```

Expected candidate diff: `A .ufo/waves/round-75/w1/R75Facet48.md`, `D kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md`, `D kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` — every path matched by a named request, no `D`-with-bytes-on-disk, so `validate_change_scope` passes. The new file (3543 B) is under the 10 MiB cap, and line 636's branch `jj file track --include-ignored`s it, so the `A` is real.

Post-commit verification (read-only, on the hash the helper prints as `landed <hash>` — the helper's only citable line):

```
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r <landed> -- kotoba-shokukin | wc -l   # expect 0
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin cat-file -e <landed>:.ufo/waves/round-75/w1/R75Facet48.md   # expect 0
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin cat-file -e <landed>:.ufo/waves/round-76/w1/A18ScoutSnapshot.md  # expect 0
```

## 5. Operability hazards for the L1

- **Never name a directory.** Naming `kotoba-shokukin/` or `.ufo/waves/round-75/w1/` also sweeps every other working-copy change under it into the same commit (line 634 + the `root:"dir"` fileset). Name the three exact files.
- **Empty dirs.** After both deletions `kotoba-shokukin/` (and its subdirs) still exist on disk but are empty; git/jj do not track directories, so the commit is unaffected. `rmdir -p kotoba-shokukin/.ufo/waves/round-76/w1` afterwards is cosmetic and produces no tree change.
- **Exit codes.** 0 ok / nothing-to-do, 1 failure, 3 committed but push failed, 64 usage. Only `landed <hash>` is citable; on exit 3 the commit exists locally and must be pushed, not re-committed. The helper takes `$STATE/jj-<key>.lock` for up to 300 s — a concurrent lane commit blocks, it is not an error.
- **Ordering vs freeze.** This is pure hygiene; it touches no counter input (see §1) and can land either before or after the data commit, but must not be folded into a data commit — `validate_change_scope` would accept it, yet the r77 landing order (`plans/round-77.md` § Landing order) separates freeze, controls/wave-1 evidence and data.
- **Lesson correction owed.** `corpus/lessons/round-75.md:12` and `round-75-verifier-spotcheck.md:44` assert a recovery that the tip contradicts. If the L1 lands the restore in §4, those lines become half-true (the report is finally at the lane path) but the "copied … then removed the fleet-root copy" attribution still misdescribes what `ac9f295` did; the honest wording is "the recovery commit `ac9f295` added the report under the typo prefix `kotoba-shokukin/`; round 77 restored it at `.ufo/waves/round-75/w1/R75Facet48.md`". That edit is outside my write scope.

## 6. Fleet-root misroot sweep (deliverable script)

`.ufo/waves/round-77/build/E11StrayAndMisroot.misroot_sweep.sh` — read-only, one `git status` call, asserts `git rev-parse --show-toplevel` equals the fleet root, prints only untracked fleet-root paths matching `kotoba|round-77` (collapsed untracked dirs such as `?? kotoba-shokukin/` or `?? .ufo/waves/round-77/` still match on the directory name), exit 0 = clean, 1 = risk found, 2 = not a work tree. `--extra` additionally prints older `round-7x` spill as a diagnostic.

Run now:

```
$ git -C /home/vgpnk/Projects/shokunin rev-parse --show-toplevel
/home/vgpnk/Projects/shokunin
$ bash .ufo/waves/round-77/build/E11StrayAndMisroot.misroot_sweep.sh ; echo exit=$?
sweep: CLEAN — no untracked fleet-root path matching kotoba|round-77
exit=0
$ bash .ufo/waves/round-77/build/E11StrayAndMisroot.misroot_sweep.sh --extra ; echo exit=$?
sweep: CLEAN — no untracked fleet-root path matching kotoba|round-77
sweep: --extra — untracked fleet-root paths matching round-7 (diagnostic):
  .ufo/waves/round-75/
exit=0
$ bash -n .ufo/waves/round-77/build/E11StrayAndMisroot.misroot_sweep.sh ; echo exit=$?
exit=0
```

Fleet-root untracked set at sweep time (`git -C /home/vgpnk/Projects/shokunin status --porcelain`, 3 entries, `-uall` also 3): `.scratch/closure-mado-r50.json`, `.scratch/source-routing-queue.md`, `.ufo/waves/round-75/` (contains the single file `w1/RevEntryQuality.md`, 14330 B, untracked at the fleet root — an earlier-wave spill, **not** produced by round 77, and invisible to the required `kotoba|round-77` filter; hence the `--extra` mode). No `kotoba`-matching and no `round-77`-matching path exists at the fleet root right now, so wave-1 seats have not yet misrooted.

The script is a normal committable lane file, not ignored (`git check-ignore -v .ufo/waves/round-77/build/E11StrayAndMisroot.misroot_sweep.sh` -> exit 1, no pattern; the only `.ufo` line in `.gitignore` is `.ufo/interactive-sessions/`), and `.ufo/waves/round-76/build/` already carries 20 tracked drafts, so the L1 can name it in the wave-1 evidence commit like any other draft.

## 7. What I did not run, and known limits

- Did not run `jj-lane.sh` (any subcommand), `jj`, `git add/rm/commit/checkout/stash`, or any clone. Every git call above is `ls-files` / `show` / `log` / `cat-file` / `rev-parse` / `config --get` / `status` / `grep`.
- Did not clone to `/fast/scratch/hyaku/kotoba-r77/E11StrayAndMisroot/` because the determination needs only committed bytes in the lane; **no scratch dir was created**, so nothing to clean up.
- **[INFERENCE]** The one step I could not execute under the no-mutation rule is the end-to-end `rm` -> `jj diff --summary` -> `D` transition. It is grounded in the helper's own comment at line 642–643 ("include it so the commit records the deletion") and in jj 0.45.1 semantics that `snapshot.auto-track = "none()"` governs *new untracked files* only, while removal of a tracked file is always recorded by the working-copy snapshot. Two checks bound the risk: `git cat-file -e refs/heads/master:<stray>` returns 0 today (so line 641 fires), and `realpath -m` normalizes the absent path identically (so `req` and the diff fileset name the same string).
- **[INFERENCE]** `jj file untrack` would leave bytes on disk and therefore trip line 560–561. I did not test it; the conclusion follows from the guard reading, and the recommended command avoids that route entirely.
- No tool installs or upgrades were needed (jj 0.45.1 present, `bash`, `git`, `realpath` present). Nothing recorded under the operator tooling rule.

VERDICT: R76-D1's stray is a safe single-commit `rm` + `jj-lane.sh commit … --as kotoba -- kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md`; a second, earlier stray (`kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md`) is the only copy of a real r75 seat report and must be restored at `.ufo/waves/round-75/w1/` in the same commit, not deleted; fleet root currently clean of `kotoba|round-77` untracked paths.

DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/E11StrayAndMisroot.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E11StrayAndMisroot.misroot_sweep.sh
