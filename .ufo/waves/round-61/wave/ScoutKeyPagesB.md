# ScoutKeyPagesB — A4 blob introduction and forgeable commit dates

Seat: `kotoba-r61-wave-ScoutKeyPagesB`. Lane and fleet read-only. No git or jj write. No language server: the question is Git's command surface, not a repository symbol.

Question: documentation ground for arm A4 (how `git log` records blob introduction via `--diff-filter=A` and `--format` author vs committer dates), the exact commands the counter should run, and a `Not held` sentence that does not treat those dates as a wall clock.

Plan sentence (`plans/round-61.md:37-39`): the row's recorded sha256 equals the committed snapshot bytes, the quote occurs verbatim in them, and the earliest commit introducing those bytes is no older than the row's recorded open date. Declared limit in the same sentence: the arm authenticates internal consistency of committed bytes; it cannot authenticate wall-clock fetch time against author-forged commit dates.

Measured rev: `HEAD` `7827628a939b0333c89892dfcedc72e390ccfb60`, whose parent is the plan base `f3246d1493b60ea1c0d947a19c39f9e08e92f326` (`git cat-file -p HEAD`). Snapshot adds below are ancestors of that HEAD. Git 2.56.0 (`/usr/bin/git`). `diff.renames` is unset in this repo.

Confidence: high on the cited man sentences and on the commands whose output is pasted below. The merge-skip note for `--find-object` is marked inference. The empty `--max-count-oldest` + `--find-object` result is observed; the man page does not explain it.

## What Git actually records

`--diff-filter=A` does not mean "this blob's first appearance under any status." It selects the diff status letter Added.

`git-log(1)` / `git-diff(1)`, local `/usr/share/man/man1/git-log.1.gz`, footer `Git 2.56.0` / `2026-09-27`, section DIFF FORMATTING (same text is in `git-diff(1)`):

> `--diff-filter=[(A|C|D|M|R|T|U|X|B)...[*]]`
> Select only files that are Added (A), Copied (C), Deleted (D), Modified (M), Renamed (R), have their type changed (T), are Unmerged (U), are Unknown (X), or have had their pairing Broken (B).

Same section, immediately above the diff options:

> Note that unless one of `--diff-merges` variants (including short `-m`, `-c`, `--cc`, and `--dd` options) is explicitly given, merge commits will not show a diff, even if a diff format like `--patch` is selected, nor will they match search options like `-S`. The exception is when `--first-parent` is in use, in which case first-parent is the default format for merge commits.

`--find-object` is the blob identity switch. Same manual, DIFF FORMATTING:

> `--find-object=<object-id>`
> Look for differences that change the number of occurrences of the specified object. Similar to `-S`, just the argument is different in that it doesn't search for a specific string but for a specific object id.
> The object can be a blob or a submodule commit. It implies the `-t` option in `git-log` to also find trees.

[INFERENCE] Because the manual calls `--find-object` similar to `-S`, and the merge paragraph says merges do not match `-S` unless `-m` / `--diff-merges` / `--first-parent` is set, a blob added only by a merge is invisible without one of those. The recommended command passes `-m`. This lane's snapshot adds are ordinary commits; `-m` was not required to see them (measurement 2).

A pathspec is not blob identity. `git log -- <path>` "show[s] only commits that are enough to explain how the files that match the specified paths came to be" (DESCRIPTION, and History Simplification). Default mode "prunes some side branches if the end result is the same." `--full-history`: "Same as the default mode, but does not prune some history."

Author date and committer date are two stored fields, not one clock.

`git-commit-tree(1)`, `/usr/share/man/man1/git-commit-tree.1.gz`, COMMIT INFORMATION:

> A commit encapsulates:
> - all parent object ids
> - author name, email and date
> - committer name and email and the commit time.

`git-log(1)` PRETTY FORMATS, `raw`:

> The raw format shows the entire commit exactly as stored in the commit object.

`git-log(1)` PRETTY FORMATS, placeholders (the `--format` string reads these; it does not recompute them):

| placeholder | manual wording |
|---|---|
| `%ad` / `%cd` | author date / committer date (format respects `--date=`) |
| `%aI` / `%cI` | author date / committer date, strict ISO 8601 format |
| `%at` / `%ct` | author date / committer date, UNIX timestamp |
| `%ai` / `%ci` | author date / committer date, ISO 8601-like format |

`%aI` and `%cI` do not follow `--date=`. `%ad` and `%cd` do. The counter should print `%aI`/`%cI` and compare `%ct`, so a `log.date` or `--date=` config cannot move the predicate.

`git-log(1)` Commit Formatting:

> `--pretty[=<format>]`, `--format=<format>`
> When `<format>` is none of the built-in names, and has `%<placeholder>` in it, it acts as if `--pretty=tformat:<format>` were given.

`%xNN` is a literal byte (`%x09` is a tab). tformat terminates each commit with a newline, including the last.

`git-log(1)` Commit Ordering:

> By default, the commits are shown in reverse chronological order.
> `--date-order` — show commits in the commit timestamp order.
> `--author-date-order` — show commits in the author timestamp order.

The default order key is the commit timestamp, and the manual gives the author timestamp a separate switch. The predicate clock below is therefore `%ct` / `%cI`, not `%at` / `%aI`.

`git-log(1)` Commit Limiting (the `-1` trap):

> Note that these are applied before commit ordering and formatting options, such as `--reverse`.
> `--max-count=<number>` — Limit the output to the first `<number>` commits that would be shown.
> `--max-count-oldest=<number>` — Limit the output to the last `<number>` commits that would be shown.

So `git log --reverse -1` is still the newest matching commit. `--max-count-oldest=1` is the documented "oldest" limiter, but measurement 3 shows it must not be combined with `--find-object` on this Git.

How an author writes either date, `git-commit(1)`, `/usr/share/man/man1/git-commit.1.gz`:

> `--date=<date>` — Override the author date used in the commit.

COMMIT INFORMATION: author and committer information is taken from `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_AUTHOR_DATE`, `GIT_COMMITTER_NAME`, `GIT_COMMITTER_EMAIL`, `GIT_COMMITTER_DATE` if set. DATE FORMATS: those two date variables accept Git internal format `<unix-timestamp> <time-zone-offset>`, RFC 2822, and ISO 8601. "Fractional parts of a second will be ignored." `--date` additionally accepts human phrases such as "yesterday".

The manual does not say the words "forgeable" or "clock". What it says is that both timestamps are fields the committing process writes, that `--date` replaces the author date, and that either environment variable replaces its field with a parsed timestamp. [INFERENCE] Nothing in these pages checks the values against the host clock. A signature (`git commit-tree -S`) signs the commit object that already contains the chosen timestamps; it does not turn them into a clock reading. The plan's phrase "author-forged commit dates" matches this mechanism. It covers both fields: `--date` forges the author date only; `GIT_COMMITTER_DATE` forges the committer date, which is the field the arm compares.

Upstream manuals for this version, not re-fetched here: <https://git-scm.com/docs/git-log>, <https://git-scm.com/docs/git-commit>, <https://git-scm.com/docs/git-commit-tree>. The quotations above are from the local 2.56.0 man pages, not from those URLs.

## Commands the counter should run

Inputs already in v2: `<repo>`, `<rev>` (the measured revision, never `--all`), `<snapshot-path>` from `snapshot_path()` (`verifiers/check_scoped_rules.py:418-420`), and the opened cell `s[8]`, which v2 already requires to be in `OPENED = ("2026-10-23",)` (`check_scoped_rules.py:63`, `:254`, `:1047`). Use that cell. Do not parse the anchor's `Fetched …Z` prose.

Every invocation needs `--no-optional-locks` so a read-only measurement does not take `.git/index.lock`. Do not pass `-M`, `-C`, or `--find-renames`. Copy detection is what turns a second path with the same blob into status `C`, which `--diff-filter=A` then drops. With copy detection left off, that second path stays `A`.

### 1. Blob oid of the committed snapshot

This oid is the Git object id. It is not the sha256 printed in the SOURCES row. `--find-object` will not accept the sha256.

```sh
git --no-optional-locks -C <repo> rev-parse --verify '<rev>:<snapshot-path>'
```

The sha256 arm stays the v2 check: hash the bytes of `git show <rev>:<snapshot-path>` (or `git cat-file blob <oid>`) and compare to the row's first 64-hex sha256. Quote presence stays the v2 verbatim check on those same bytes. A4's date arm runs only after both of those hold.

### 2. Every commit that added that blob (the recycled-bytes walk)

No pathspec. A pathspec answers "when was this path added," which is a different question, and it misses the same blob added earlier under another path.

```sh
git --no-optional-locks -C <repo> log \
  --full-history \
  -m \
  --diff-filter=A \
  --find-object=<blob-oid> \
  --format='%H%x09%at%x09%ct%x09%aI%x09%cI' \
  <rev>
```

One line per matching commit, tab-separated: commit, author unix, committer unix, author strict ISO 8601, committer strict ISO 8601. The counter keeps every line and selects the minimum `%ct`. It does not pass `-1`, `--reverse -1`, or `--max-count-oldest`.

Empty stdout means no Added introduction of that blob is reachable from `<rev>`. Exit 0 with empty stdout is that outcome (measurement 3 and measurement 4). Fail closed: the row is not backed. Do not treat exit 0 as "found".

### 3. Path add, separately, only as a receipt

This confirms the snapshot path itself was added. It is not the recycled-bytes test.

```sh
git --no-optional-locks -C <repo> log \
  --diff-filter=A \
  --max-count-oldest=1 \
  --format='%H%x09%at%x09%ct%x09%aI%x09%cI' \
  <rev> -- <snapshot-path>
```

`--max-count-oldest=1` is safe on this path form (measurement 3 returned the add). It is not safe on the `--find-object` form.

### Predicate

- Take the minimum `%ct` from command 2.
- Convert that unix time to a UTC calendar date. Compare UTC, not the `-03:00` calendar day. `2026-10-22T22:00:00-03:00` is `2026-10-23T01:00:00Z` and is not older than opened `2026-10-23`. `2026-10-22T20:00:00-03:00` is `2026-10-22T23:00:00Z` and is older.
- Reject when that UTC date is strictly before the `opened` cell ("older than"). The same UTC day passes ("no older than").
- Record `%at` and `%aI` on the receipt. Do not compare them. On this repo's freeze commit they are 1100 seconds earlier than the committer fields (measurement 1) and still the same UTC day, so this particular commit would not false-reject either way. They are still a different field, and `git commit --date` writes only that field.
- A blob whose first appearance is status `M` (an existing path overwritten) is not selected by `--diff-filter=A`. Snapshot pages in this repo are Adds. That gap stays a limit, not a second walk, unless the arm spec is widened.

## Measurements

### 1. Commit object stores both timestamps — `date -u` `Fri 23 Oct 2026 07:11:24 PM UTC`

Command (exit 0). `git rev-parse HEAD` and `git cat-file -p HEAD | head -8`, then `git log -1 --format` re-read at `Fri 23 Oct 2026 07:12:39 PM UTC` (exit 0):

```text
7827628a939b0333c89892dfcedc72e390ccfb60
tree 0899776b86ff4c620e8bdf4eb0c95a723ca01ab6
parent f3246d1493b60ea1c0d947a19c39f9e08e92f326
author kotoba-shokunin <kotoba@shokunin.local> 1792781329 -0300
committer kotoba-shokunin <kotoba@shokunin.local> 1792782429 -0300

7827628a939b0333c89892dfcedc72e390ccfb60
1792781329 2026-10-23T15:48:49-03:00
1792782429 2026-10-23T16:07:09-03:00
```

Author UTC `2026-10-23T18:48:49+00:00`. Committer UTC `2026-10-23T19:07:09+00:00`. Delta 1100 seconds. Both are header bytes of the commit object.

### 2. Eligible snapshot blobs have one Added introduction, on the opened day — `date -u` `Fri 23 Oct 2026 07:11:24 PM UTC`

`git rev-parse HEAD:<path>` then `git cat-file blob <oid> | sha256sum` (exit 0). `git log --full-history -m --diff-filter=A --find-object=<oid> --format='%H%x09%aI%x09%cI' --name-status HEAD` (exit 0) for each:

| row | content sha256 | git blob | only Added commit | `%aI` and `%cI` |
|---|---|---|---|---|
| S103 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | `022dc3bab2728a6525b78e4a02365d396f3682be` | `7b80ae80cda69a95b6fc90879395113a99a57912` | `2026-10-23T09:28:13-03:00` both |
| S105 | `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f` | `0400f45312eb5e0381b2d8c857c06712e0d2f18d` | same commit | same |
| S106 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | `56a6ad07c0eec9583847973af7b903a34e4f143f` | same commit, path `.ufo/waves/round-60/snapshots/S106.page` | same |
| S108 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | `47c1554d6fb3be35e292f7dd525d3241fd2ff21e` | same commit, path `.ufo/waves/round-60/snapshots/S108.page` | same |

Path-only `git log --diff-filter=A --format=… HEAD -- .ufo/waves/round-60/snapshots/S106.page` returned that same single commit (exit 0). S106's content sha256 equals the digest recorded on the S048 row, and S108's equals S049, but neither blob exists under an earlier path in commits reachable from HEAD. A whole-history blob walk does not reject these four eligible rows: committer UTC day `2026-10-23` is not older than opened `2026-10-23`.

### 3. `--max-count-oldest` with `--find-object` prints nothing — `date -u` `Fri 23 Oct 2026 07:12:58 PM UTC`

Blob `56a6ad07c0eec9583847973af7b903a34e4f143f` (S106). All exit 0.

```text
git log --diff-filter=A --find-object=<blob> --format='%H %ct' HEAD
7b80ae80cda69a95b6fc90879395113a99a57912 1792758493

git log --diff-filter=A --find-object=<blob> --max-count-oldest=1 HEAD
(empty)

git log --full-history --diff-filter=A --find-object=<blob> --max-count-oldest=1 HEAD
(empty)

git log -m --diff-filter=A --find-object=<blob> --max-count-oldest=1 HEAD
(empty)

git log --diff-filter=A --max-count-oldest=1 --format='%H %ct' HEAD -- .ufo/waves/round-60/snapshots/S106.page
7b80ae80cda69a95b6fc90879395113a99a57912 1792758493

git log -1 --diff-filter=A --find-object=<blob> --format='%H %ct' HEAD
7b80ae80cda69a95b6fc90879395113a99a57912 1792758493
```

The `-1` result is the newest match, which happens to be the only match. It is the wrong flag once a second, older Add exists.

`--reverse -1` applied to `LOG.md` (same session, exit 0), where more than one commit touches the path:

```text
git log -1 --format='%H %cI' HEAD -- LOG.md
79cf263800552812ce6a45f4bb0313668b576749 2026-10-23T15:23:17-03:00

git log --reverse -1 --format='%H %cI' HEAD -- LOG.md
79cf263800552812ce6a45f4bb0313668b576749 2026-10-23T15:23:17-03:00

git log --max-count-oldest=1 --format='%H %cI' HEAD -- LOG.md
43e0c0224876da4a7ba0a86d852b6f621cfecd67 2026-09-28T15:29:47-03:00
```

`--reverse -1` did not return the oldest commit. That matches the manual: `--max-count` is applied before `--reverse`.

### 4. Round-53 scratch bytes are not a blob until some commit adds them — `date -u` `Fri 23 Oct 2026 07:13:23 PM UTC`

The W1 receipt names `/fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md` (`.ufo/waves/round-60/controls-v2/CtlReopenForged.md:127-129`, content sha256 `971d75bf…`). Read-only `git hash-object` (no `-w`):

```text
scratch oid bbb7d6f4e7350c51069f1f12bc0b26ec252e4a5b
git cat-file -t <oid>  →  fatal: git cat-file: could not get object info   exit 128
git log --diff-filter=A --find-object=<oid> --format='%H %cI' HEAD  →  (empty)  exit 0
```

Those bytes are not reachable from HEAD. Command 2 cannot reject them until a commit reachable from the measured revision Adds that blob. A world that puts the old bytes and `opened = 2026-10-23` into one commit dated that same UTC day does not fail this arm. A world that also has an earlier reachable commit Adding that blob, with committer UTC date before `opened`, does fail it. That earlier commit is what "recycled bytes" means to this command. Scratch that was never committed is outside the arm, which is the plan's declared limit, not a second detector.

## Not held wording

House shape is the list under `## Not held` in `corpus/knowledge/scoped-rules-round60.md:40-45`. Paste this as one bullet of the C1 entry. It does not say the arm knows when the page was fetched.

```markdown
- Wall-clock fetch time: not held. The check compares the row's `opened` day to the committer timestamp of the earliest commit, reachable from the measured revision, that added the snapshot blob (`git log --diff-filter=A --find-object=<blob-oid>`). That committer timestamp and the author timestamp beside it are fields the committing process wrote into the commit object (`GIT_COMMITTER_DATE` and `GIT_AUTHOR_DATE`; `git commit --date` overrides the author date only). Git stores them as bytes and does not check them against a clock, so either date can be written to fall on or after `opened` for bytes that were obtained earlier, or before `opened` for bytes that were obtained then. Bytes that no commit has added are invisible. The arm checks consistency of committed bytes, not the wall-clock time of the fetch.
```

Do not shorten this to "author dates are forgeable" alone. The compared field is the committer timestamp, and that one is set by `GIT_COMMITTER_DATE`, not by `--date`.

## Unknowns

- No merge in the measured snapshot history was shown to be the introducing commit. `-m` is included from the manual's `-S` paragraph plus the "similar to `-S`" sentence, not from a merge fixture.
- Why `--max-count-oldest=1` plus `--find-object` prints nothing on Git 2.56.0 is not stated in the man page. The effect is measured. The counter must not use that combination.
- A two-Add history (same blob, older path, then a new path) was not built. Building one would be a git write. The "minimum `%ct` of every line" rule is what the manual's status filter and commit ordering imply once more than one line is possible; it was not executed on two Adds.
- `diff.renames` unset does not by itself prove the compiled default. The command omits `-M`/`-C` so this repo's config cannot reclassify an Add as a copy.

installs: no installs

blockers: none

Attacked: A4's git mechanism (`--diff-filter=A`, `--find-object`, `%aI`/`%cI`/`%at`/`%ct`) against the 2.56.0 man pages and the committed S103/S105/S106/S108 blobs, including the empty `--max-count-oldest`+`--find-object` result and the round-53 scratch blob that is not in HEAD.
