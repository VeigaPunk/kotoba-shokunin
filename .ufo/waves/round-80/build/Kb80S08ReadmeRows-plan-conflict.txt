# Plan-vs-measurement conflict (recorded by seat Kb80S08ReadmeRows)

Not part of this seat's README item. Recorded because a conflict between the frozen plan text and
the gates' own findings must be reported verbatim for the canonical judge, not smoothed over. No lane
file was modified to address it; nothing here changes the coverage rows.

## Plan text (verbatim, `plans/round-80.md` § C1)

> The two `commit_unresolvable` tokens are `owner/repo@<hex>` citations of THIRD repositories
> (`google-gemini/gemini-cli@451a02ff`, `zed-industries/zed@cfb894a5`); both objects are absent from
> lane and fleet (`git cat-file -t` → fatal, both repos, receipts). One lives in a
> `spotcheck-identity`-pinned file and cannot be edited; the other is lesson evidence of a recorded
> breach (M45) and must not be rewritten.

## Measured at base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`

The two gate subjects (read from committed receipts, not re-run by me):

```
$ grep -n 'commit_unresolvable' .ufo/waves/round-80/build/Kb80E11Receipts.txt | head
175:           commit_unresolvable: corpus/SOURCES.md:171: 7bb48f213ac677f943d5c791199ed3dddf302f00
176:           commit_unresolvable: corpus/SOURCES.md:172: 7bb48f213ac677f943d5c791199ed3dddf302f00

$ sed -n '273,280p' .ufo/waves/round-80/build/Kb80E11Receipts.txt
      "commit_unresolvable": 2,
      "commit_unresolvable_detail": [
        "corpus/SOURCES.md:171: 7bb48f213ac677f943d5c791199ed3dddf302f00",
        "corpus/SOURCES.md:172: 7bb48f213ac677f943d5c791199ed3dddf302f00"
      ],
```

The plan's named tokens are **not** the gate's subjects. My own read-only sweep at the base:

```
$ git grep -n '451a02ff' 398cbe1 -- corpus/ SKILL.md PROVINCE.md
corpus/SOURCES.md:59 (S046), :70 (S057), :73 (S060) — explicit google-gemini/gemini-cli@<hex> citations
corpus/knowledge/skill-listing-thresholds-round54.md:29
corpus/lessons/round-53.md:26; round-54-verifier-spotcheck.md:37,147,148,223; round-54.md:30; round-55.md:54,57; round-56.md:76

$ git grep -n 'cfb894a5' 398cbe1 -- corpus/ SKILL.md PROVINCE.md
corpus/SOURCES.md:63 (S050), :74 (S061) — explicit zed-industries/zed@<hex> citations
corpus/knowledge/alwayson-rule-files-round53.md:32
corpus/lessons/round-53.md:44; round-54.md:13 (M45), :52
```

Every hit is an explicit `owner/repo@<hex>` form. The gates do not list any of them under
`commit_unresolvable`; round-53/54 converted them to that grammar precisely so the gates could read
them. So the plan's parenthetical names the wrong objects, and its "one lives in a
spotcheck-identity-pinned file / the other is M45 lesson evidence" narrative attaches to citations
that are not the blockers.

## The two real subjects

- `corpus/SOURCES.md:171` (S230, pi-mono), anchor cell: `page revision \`main\` resolved to
  \`badlogic/pi-mono\` commit \`7bb48f213ac677f943d5c791199ed3dddf302f00\`` — a **bare-hex**
  token; the third-repo name sits outside the token on the same line.
- `corpus/SOURCES.md:172` (S231, Mistral Vibe), anchor cell: `served commit
  \`7bb48f213ac677f943d5c791199ed3dddf302f00\`` — **the same hex as S230**. A
  `raw.githubusercontent.com/mistralai/mistral-vibe` page cannot be served from a `badlogic/pi-mono`
  commit, so one of the two cells carries the other's hash. The row was written in round 79 and may
  not be rewritten in place (M45: only `status`, `recheck`, `used-by` may change). I flag the
  impossibility; I do not claim which cell is wrong or how it happened.

## Consequences for repair 5 (C1)

1. A grammar class keyed only on in-token `owner/repo@<hex>` **cannot** clear either token — they are
   bare hex, with the repo name separate. The plan's own "(or otherwise an explicit third-repository
   citation)" clause at line scope is required, exactly as Kb80V03Instruments reported.
2. A line-scope INFO class would also classify S231's impossible hash as an external citation and
   stop flagging it. That converts a row-data defect into silence. If repair 5 lands, the closure
   still owes a separate decision on S231's anchor hash — an appended correction row (the lane's
   practice), never a classification change used as the correction.
3. The plan's premise is therefore wrong in two ways at once (wrong subjects, and a repair that would
   not have cleared the real ones). Anything the report says about "the two third-repo citations"
   must be corrected to the measured subjects above, or the round will record a claim its own gates
   contradict.

## Limits

- I did not run `verify_corpus_integrity.py` or `verify_corpus_independent.py` myself; the finding
  lines and the JSON detail are read from `Kb80E11Receipts.txt` (same lines in
  `Kb80S06Shonen-receipt-corpint-lane.txt:15-16`), both committed under `.ufo/waves/round-80/build/`.
  The two `git grep` sweeps above are mine, read-only, at the base commit.
- No `corpus/SOURCES.md` row, no verifier and no lane file was touched.

## Resolution (appended after reading the fetch records; supersedes the "either cell" hedge above)

The impossibility is one-sided and attributable, so the earlier "I do not claim which cell is wrong"
no longer applies:

- `S231.fetch.json`: "`main` resolved to commit `7bb48f213ac677f943d5c791199ed3dddf302f00` by git
  ls-remote … and the commit-pinned raw URL served the same 77634 B / same sha256". The round-80
  re-open (`Kb80R03ReopenSix-S231.fetch.json`) repeats `git ls-remote …/mistralai/mistral-vibe
  refs/heads/main` → `7bb48f21…`, unchanged.
- `S230.fetch.json`: pi-mono `main` at the r79 fetch = `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923`,
  the last commit touching the docs path = `25cc5c7bf4cbc76b2e134c729eb8d57d521ed749`, and the body
  blob `19d2bf28910ce49caaaf4dde86d1e96330ca7b31` equals the GitHub contents-API sha for that path
  at `ref=main`. The round-80 re-open (`Kb80R03ReopenSix-S230.fetch.json`) shows the branch has moved
  to `85c2ee3e761e4fc4f901ff0ed584fb2465aa552e` with byte-identical content.

So `7bb48f21…` is the **mistral-vibe** commit. `corpus/SOURCES.md:172` (S231) cites it correctly;
`corpus/SOURCES.md:171` (S230) attributes it to `badlogic/pi-mono` — that cell is **wrong**, not merely
outside the lane/fleet resolution set. M45 forbids rewriting the row, so the lane's practice is an
appended correction row (the round-57 S086–S088 precedent) naming the measured head `bb65e3e4…` /
`85c2ee3e…` and the docs commit `25cc5c7bf…`. A grammar class can then classify the frozen token as
external INFO *without* that classification standing in for the correction.

Entry update observed while checking: `.ufo/waves/round-80/build/allowed-tools-surfaces-round80.md`
(mtime 2026-10-27 20:31:50) no longer contains any of these full hexes on its pi-mono / mistral-vibe
lines — E10's hazard (3) was measured against an earlier revision of that file and should be re-read
before it is acted on.
