# ReviewErrata69 — round 70 wave 1 (read-only reviewer)

**Verdict: PASS on every claim.** One low-severity finding about a citation path; no defect changes C1 or C2.

Repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, HEAD `16b212a390c7ce68b6bce49b2c3766b154fbcbae`. Working tree is clean for `corpus/lessons/round-69.md`, `corpus/lessons/round-70.md` and `corpus/SOURCES.md` (`git status --porcelain` printed nothing for them).

Revisions resolved (`git rev-parse a5f7459 9ce102b 7d51253 a02ba7e`):
`a5f7459f99bb27bf697e9438362e75ac5833eca8`, `9ce102b9e3f8896d5ed3f050ee896ca90d693a38`, `7d51253f99906b8551b6a0a108761eedac00de74`, `a02ba7e42e230bf6bb4de902e91d6346aee93bfe`.

## Claim 1 — `a02ba7e` changed S201's anchor: PASS

`git log -S'(14 words)' --oneline -- corpus/SOURCES.md` printed exactly one commit:

```
a02ba7e round 69: skill name-collision precedence; close R68-1..R68-8
```

`git log --oneline a5f7459..9ce102b -- corpus/SOURCES.md` lists `278b9dc` and `a02ba7e`. `278b9dc` changed only the S207 row: `git show 278b9dc -- corpus/SOURCES.md | grep -E '^[-+]\|'` shows only the `-| S207 |` and `+| S207 |` lines. A sha256 of the `| S201 |` line at each revision:

```
a5f7459 6b225f47193e2bd6
a02ba7e 1555c7f962b4a49b
278b9dc 1555c7f962b4a49b
9ce102b 1555c7f962b4a49b
7d51253 1555c7f962b4a49b
HEAD    1555c7f962b4a49b
```

So the S201 row changed in `a02ba7e` and nowhere else. It has not changed in round 70 either: `git diff 7d51253 HEAD -- corpus/SOURCES.md` only adds `+| S209`, `+| S210` and `+| S211`.

## Claim 2 — old `(13 words)`, new `(14 words)`, no other S201 cell changed: PASS

I split the S201 row on ` | ` at `a5f7459` and at `9ce102b` with a Python script and compared the cells pairwise:

```
cells 11 11
DIFF cell 5
  old: the "Security best practices" subsection; quote "Agent Skills should be treated like any third-party code you bring into your project." (13 words)
  new: the "Security best practices" subsection; quote "Agent Skills should be treated like any third-party code you bring into your project." (14 words)
```

Only the anchor cell differs, and within it only the word count. The quoted sentence is unchanged. `git diff a5f7459 9ce102b -- corpus/SOURCES.md` shows the same thing: one `-`/`+` pair for S201, and the rest are added rows S203 to S208.

The new count is correct: `len(q.split())` returns **14**. It would be 15 if "third-party" were split at the hyphen. The lane counts whitespace-separated words, and both the spot-check and round 70 use that rule.

The cell sits outside the in-place rule. Fleet `CORPUS.md:116` reads: "2. **Append-only.** Only `status`, `recheck` and `used-by` change in place, and each change…". This matches round-70.md:157, which says the cell is outside "the three cells CORPUS.md rule 2 lets change in place".

## Claim 3 — the round-70 § Status changes S201 line is accurate: PASS

`corpus/lessons/round-70.md:155-158` says: changed in place in `a02ba7e`, `(13 words)` → `(14 words)` (old → new), the new count is true, the change was outside the rule-2 cells, this line is the required old→new log (K69-9), and no other S201 cell changed (with the `git diff a5f7459 9ce102b` command). All of this agrees with Claims 1 and 2. It also does what the routed defect asked: `corpus/lessons/round-69-verifier-spotcheck.md:197-202` says "log the change old→new in round 70's lesson".

## Claim 4 — erratum K69-9 (`round-69.md:173`): PASS

The erratum says the r69 line "No prior row's `status`, `recheck` or `used-by` was changed" is true for those three cells but leaves out S201's in-place anchor edit `(13 words)`→`(14 words)` in `a02ba7e`, and that the old→new log is in round-70 § Status changes. Every part checks out against Claims 1–3.

## Claim 5 — erratum K69-10 (`round-69.md:172`): PASS (see the low finding)

- The filed text still has the stale tally: `grep -n "18 assertions"` on the 7d51253 copy gives `24:(18 assertions).` This matches the spot-check's pointer `round-69.md:24`.
- I re-ran the counter at the r69 tip in a `git clone --shared` sandbox (`git checkout 9ce102b9…`, then `python3 -B verifiers/check_skill_precedence.py --self-test`). It printed 22 PASS lines and `self-test: 0 failure(s) over 22 assertions`, with `exit=0`.
- `.ufo/waves/round-70/receipts/r69-tip-defense.txt:10` reads `self-test: 0 failure(s) over 22 assertions`.
- `.ufo/waves/round-69/controls/postfreeze-receipt.txt:4` reads `selftest: self-test: 0 failure(s) over 22 assertions`. That receipt's `measured-rev` is `54f4b6c`, not `9ce102b`, but the counter is byte-identical at both revisions: `git show <rev>:verifiers/check_skill_precedence.py | sha256sum` gives `dc9f1507…6c245` for both, and that hash matches the receipt's own line 3. `54f4b6c` is an ancestor of `9ce102b` (`git merge-base --is-ancestor`). So the erratum is right to cite that receipt for the r69-tip count.

## Claim 6 — the filed text above the errata is byte-identical to `git show 7d51253:corpus/lessons/round-69.md` (append-only): PASS

- `git show 7d51253:corpus/lessons/round-69.md` is 11713 bytes. The current file is 12624 bytes.
- `head -c 11713 corpus/lessons/round-69.md | cmp - base.md` printed nothing and exited 0, so the first 11713 bytes are identical.
- The base file ends in `\n`. The appended bytes start `\n## Errata (appended in round 70; the text above is not edited)\n\n- Erratum (K69-10)…` (from `od -c`), so the old final line was not touched.
- The base sha256 is `d139e8ff…1463aad`, and `git show 9ce102b:corpus/lessons/round-69.md` has the same hash. The file did not change between the r69 tip and the round-70 base.
- `git log --oneline 7d51253..HEAD -- corpus/lessons/round-69.md` shows only `8edeb49`. `git diff --stat 7d51253 HEAD` reports `5 insertions(+)`, and the diff has 0 `-` lines.

## Findings by severity

**Low — the K69-10 erratum gives an incomplete path (`corpus/lessons/round-69.md:172`).** It cites `controls/postfreeze-receipt.txt`. There is no such path from the repo root (`grep: controls/postfreeze-receipt.txt: No such file or directory`). The only tracked copy is `.ufo/waves/round-69/controls/postfreeze-receipt.txt` (`git ls-files | grep postfreeze-receipt`). You can work it out from the filed text (`round-69.md:14` names the receipts directory `.ufo/waves/round-69/controls/`), and the spot-check uses the same short name. But the other citation in the same sentence is a full repo path (`.ufo/waves/round-70/receipts/r69-tip-defense.txt`), so the two are inconsistent. This does not affect C1: the erratum's facts are all correct. Because round-69.md is append-only, any fix would have to be appended.

No medium, high or critical findings.

## Residual risk and verification gaps

- I did not fetch the Microsoft page, so I have not checked that the quoted sentence is still verbatim upstream. S201's quote text did not change between revisions, so this does not affect the K69-9 claims.
- I did not run the C1 counter `verifiers/check_r69_routed_repairs.py`. My scope was the errata and the S201 line, not the counter's tally.
- Tools installed or updated: none. Scratch directory `/tmp/k70w1-ReviewErrata69.9InR` (which held the shared clone) has been deleted; `ls -d /tmp/k70w1-ReviewErrata69.*` printed "No such file or directory".
