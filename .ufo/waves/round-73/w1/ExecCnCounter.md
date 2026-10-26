# ExecCnCounter — C1 frozen counter `check_cn_vendor_surfaces.py` (round 73, wave 1)

**Verdict.** The counter is built to the frozen § C1 predicate, its 47-world `--self-test` reads
**0 failures over 139 assertions**, and the do-nothing control reads exactly the figure the plan froze:
`vendor skill surfaces backed 0 of 4`, `held at base: 0`, **exit 1** at `072048f`. Two rulings the plan left
to the counter are now frozen in its docstring (the manifest→row pin and the source-line/row-URL binding);
one residual hole in (c)/(d) cannot be closed without network at measurement and is named in § A6. Nothing in
the lane was modified, no lane gate was executed, no tool was installed, scratch removed.

Draft: `.ufo/waves/round-73/w1/build/ExecCnCounter/check_cn_vendor_surfaces.py`, 1,303 lines / 56,766 B,
`sha256 051d3e2dca9ef34c44f27d1f8e11f2ca264814e641430fb6ba96baa346df22ce`, blanked self-sha
`b4ca05cf3c0a45d239995b4e726caa47903d37d42a503d276e0c7b3d8b2e3573`.
Evidence transcript (self-test + base run + unknown-rev run, verbatim): `.ufo/waves/round-73/w1/build/ExecCnCounter/evidence.txt`.

---

## F0 — the frozen predicate, reproduced verbatim in the draft's docstring and printed by the run

```
$ python3 -B .ufo/waves/round-73/w1/build/ExecCnCounter/check_cn_vendor_surfaces.py \
      --rev 072048fa8e8a52c707d25f7079772fa317244eb7          # lane root cwd
measured-rev: 072048fa8e8a52c707d25f7079772fa317244eb7
vendor skill surfaces backed 0 of 4
held at base: 0
  entry corpus/knowledge/chinese-vendor-skill-surfaces-round73.md absent at 072048fa8e8a52c707d25f7079772fa317244eb7 (the frozen path is the entry's only home)
exit 1
```

```
$ python3 -B ... --rev 0000000000000000000000000000000000000000
environment error: --rev 0000000000000000000000000000000000000000 is not a commit
exit 2
```

`held at base` is read at the frozen `BASE_REV = 072048fa…` (a module constant, no CLI flag can move it),
never at `--rev`: it is the do-nothing figure, not a property of the measured revision. Independent
re-derivation of the same zero (so the counter's zero is not self-certified):

```
$ git show 072048fa8e8a52c707d25f7079772fa317244eb7:corpus/SOURCES.md \
    | grep -cEi 'docs\.trae\.cn|codebuddy\.ai|kimi\.com|bigmodel\.cn|moonshot|kimi-cli'
0
$ git show 072048fa8e8a52c707d25f7079772fa317244eb7:corpus/SOURCES.md \
    | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
142
```

## F1 — the self-test: 47 worlds, 139 assertions, 0 failures

```
$ python3 -B .ufo/waves/round-73/w1/build/ExecCnCounter/check_cn_vendor_surfaces.py --self-test | tail -1
self-test: 0 failure(s) over 139 assertions
$ ... --self-test | grep -c '^PASS'
47
```

Each world is an isolated `git init` repo under a fresh `mktemp -d` with **two** commits (a base commit for
`held at base`, then the measured tip); the toplevel is asserted equal to the temp dir before the first
commit and the tree is deleted in a `finally`. No lane, fleet repo, sibling lane or cargo index is touched.
Worlds, in order (`PASS <label>: exit N`):

honest/base: 1 honest `4 of 4` exit 0 · 2 base world (entry absent) `0 of 4` exit 1 · 3 vendor hosts in the
base registry `held at base: 4` · 4 one TRAE host in base `held at base: 1` · 5 (d) quote wrapped across a
line break still found (proves whitespace collapse is the only shaping).

(a): 6 row hidden in an HTML comment · 7 row hidden in a fenced block · 8 two rows name one vendor ·
9 no `verified-at:` · 10 no `recheck:` · 11 cited id absent from the `source:` lines · 12 entry outside
`corpus/knowledge/` · 13 no vendor table · 14 token-stuffed row (`.stuffed/root`, `ztuff`, `ytuff`) ·
15 invented root `.trae/plugins/` · 16 root that occurs only in a page the row does not cite ·
17 three keys, no root · 18 only two tokens · 19 row named `Kimi Codex` (does not name `Kimi Code`) ·
20 key occurring only inside a longer word (`filename`, `descriptions`) · 21 CJK abutting a root is a
boundary (positive arm).

(b): 22 pin of a different page on the same vendor host · 23 status `queued` · 24 tier `C` · 25 12 cells ·
26 `used-by` omits the entry · 27 URL off the vendor host · 28 URL on the *other* vendor's host · 29 no
registry rows · 30 staged campaign-schema rows appended as-is (4 cells) · 31 two rows for one id · 32 cited
id absent from the registry · 33 `github.com/evil/kimi-cli` fails Kimi's path-pinned host.

(c): 34 tampered snapshot with the manifest hash left → exit 2 `snapshot_tampered` · 35 no manifest → exit 2 ·
36 malformed manifest line → exit 2 · 37 `../S999-x.md` escape → exit 2 · 38 two pinned snapshots begin with
one cited id → exit 2 `ambiguous` · 39 entry names an uncommitted snapshot → exit 2 `not committed`.

(d): 40 quote 4 words · 41 quote 26 words · 42 quote absent from its snapshot · 43 two distinct located
quotes for one id · 44 backticked code span absent from the page (proves no backtick stripping).

cannot-evaluate: 45 unknown revision · 46 registry absent at the revision · 47 base registry unreadable.

## F2 — falsifiers I ran on the draft itself (not part of the world table)

Drift guard (the frozen-counter rule, copied from `check_author_rules.py`):

```
$ cp check_cn_vendor_surfaces.py $S/drift.py && echo "# a reviewer's hand edit" >> $S/drift.py
$ python3 -B $S/drift.py --rev 072048fa… --repo <lane>
environment error: counter drifted — the running file is not the frozen counter
exit 2
```

Committed bytes only (an uncommitted entry on disk must not count):

```
$ git clone --shared -q <lane> $D && git -C $D checkout -q 072048fa… \
  && printf 'source: S217 — x\nverified-at: …\n| TRAE | `.trae/skills/` |\n' \
       > $D/corpus/knowledge/chinese-vendor-skill-surfaces-round73.md
$ git -C $D status --porcelain | head -3
?? corpus/knowledge/chinese-vendor-skill-surfaces-round73.md
$ python3 -B … --rev HEAD --repo $D
vendor skill surfaces backed 0 of 4
  entry corpus/knowledge/chinese-vendor-skill-surfaces-round73.md absent at HEAD (the frozen path is the entry's only home)
exit 1
```

No tracked lane file touched by any of my runs: `git status --porcelain -uno | wc -l` → `0` (HEAD
`ac8fc59523c2e41dbd46e0c2787e94949aa3cec0`, unchanged; only the untracked `.ufo/waves/round-73/w1/` tree
exists). Optional second evidence, off the verdict path:

```
$ python3 -B … --rev 072048fa… --census-check
… census validate: conformant      (exit 1 overall: N = 0, as frozen)
```

## F3 — the contract the entry and the manifest must meet (freeze-2 inputs for the L1)

Everything reads `git show <rev>:<path>`; no network, no execution of lane gates. The counter froze these
readings because § C1 names the conjuncts but not their shape; each is in the draft's docstring with the
reason so a reviewer attacks it rather than discovers it.

1. **Entry** `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` (rendered: HTML comments and fenced
   blocks stripped). It must open with one `source: S### — … — <URL> — … — located quote "<5-25 words>"
   (snapshot `<file>`)` line per cited id, then `verified-at:`, then `recheck:`. A source line's ids are
   those before its first `located quote`; an id glued to a slug (`S217-trae-ide.md`) is a file name, not a
   citation.
2. **Vendor table**: any markdown table of the entry; a vendor row's first cell must begin with the vendor's
   frozen name (`TRAE`, `CodeBuddy`, `Kimi Code`, `Zhipu`) — `| Kimi Codex |` does not name `Kimi Code`;
   exactly one row per vendor. Counted tokens are the backticked spans after that first cell: ≥ 3 total,
   ≥ 1 containing `/` or starting `.`/`~`/`$`, ≥ 2 matching `^[A-Za-z][A-Za-z0-9_:-]*$` (no dot:
   `SKILL.md` is not a key). Every token must occur in the snapshot(s) of the pages the row cites, and the
   entry's `source:` line for each cited id must carry a URL equal (host + path, trailing `/` ignored) to
   that row's first registry URL — the pin is bound to the cited page.
3. **Snapshot pinning**: `MANIFEST.sha256` lines `<sha256>  <file>` (two spaces or a tab; `*` binary marker
   tolerated), `<file>` relative to `.ufo/waves/round-73/snapshots/`, no absolute path, no `..`, no
   conflicting duplicate. A cited id resolves to the single file the entry names on a line citing it whose
   basename is a manifest key (the round-72 `(snapshot `S262-…md:106-114`)` convention), else to the single
   manifest file whose basename begins with the id + a non-digit. Zero candidates, two candidates, a
   missing file or a digest mismatch is **exit 2** — so the manifest must land in the same freeze as the
   entry; a partially pinned tree cannot be scored at all.
4. **Hosts** are exact: `www.codebuddy.ai` (a row written on `codebuddy.ai` fails), `docs.trae.cn`,
   `docs.bigmodel.cn`, and for Kimi `github.com/moonshotai/kimi-cli` (host **and** path prefix,
   case-insensitive) or `www.kimi.com`.

## F4 — token reachability in the wave-1 seat snapshots (calibration; sibling artifacts, not re-fetched by me)

I ran the counter's own matcher over the `snapshot.md` files the source seats have saved so far, to see
whether the (a) shape is satisfiable from the bytes that will be pinned. **These are unverified siblings'
artifacts — this is a reachability probe, not evidence about any page.**

```
ExecSrcTrae        13351 B -> {'.trae/skills/': True, '~/.trae-cn/skills/': True, '.agents/skills/': True, 'name': True, 'description': True}
ExecSrcCodebuddyIde  3887 B -> {'.codebuddy/skills/': True, 'name': True, 'description': True, 'allowed-tools': True}
ExecSrcCodebuddyCli 25241 B -> {'.codebuddy/skills/': True, 'name': True, 'description': True, 'allowed-tools': True}
ExecSrcKimiEn      13528 B -> {'.kimi-code/skills/': False, '.agents/skills/': True, 'whenToUse': False, 'description': True}
ExecSrcKimiZh       6928 B -> {'.kimi-code/skills/': True, 'whenToUse': True, 'description': True}
ExecSrcZhipu        7381 B -> {'skills/': True, '.zhipu/skills/': False, 'type:zai': True, 'name': True, 'description': True}
```

Consequence for the scribe: **Kimi Code's row must cite the Chinese page** for `whenToUse` +
`.kimi-code/skills/` (the English raw extract carries neither), and **Zhipu's root token must be `skills/`**
(the extract carries no dot-root) with keys `type:zai` and `name`. All four vendors can therefore reach the
frozen `N == 4` shape from bytes already on disk — subject to the source seats' own verification.

## F5 — attacks on the frozen plan (all raised before any data)

- **A1 — (a) is satisfiable by a pure token row (the r72 errata-E3 shape).** § C1 counts backticked tokens
  and never asks the row for prose, so `| TRAE | `.trae/skills/` | `name`, `description` | frontmatter |` is a
  backed vendor if the tokens are on the page. That is faithful to the frozen sentence (the row's content
  *is* its tokens); r72's `MIN_BODY_WORDS` existed because a *checklist box* is supposed to state a rule.
  **Recommendation to the L1:** leave the predicate as frozen, and if a prose floor is wanted, add it as a
  pre-data erratum now, not after the scribe's entry is scored.
- **A2 — the plan's (c) never says how a `S###` row maps to a snapshot file** (round 72 used an L1-filled
  in-code `SNAPSHOT_PINS` table; the 14-id package/lane collision `S203`–`S216` makes prefix-guessing
  unsafe). The manifest is only a sha list, so the counter freezes the two-step resolution in § F3.3. The
  L1 should restate that convention in the freeze commit, because two compliant-looking manifests (one
  named `S217-trae-ide.md`, one named `trae.md` with the id only in the entry) behave differently.
- **A3 — a pin proves a page's bytes exist in the tree, not that they are the URL's bytes.** (c)/(d) can be
  satisfied by a committed snapshot of any page that carries the tokens. I closed the cheap half before
  data: the entry's `source:` line must name the row's URL, so the *claim* and the *pin* are at least the
  same page string. The remaining half — that the stored bytes were fetched from that URL — is not
  checkable without network at measurement; it stays a reader's audit against the fetch log each source
  seat commits.
- **A4 — (c) is exit 2, so one missing pin voids the whole measurement.** The plan freezes this ("a missing
  or tampered snapshot is exit 2"); operationally it means the manifest, the eight snapshots and the entry
  must land in one commit, or every C1 reading in between is *cannot evaluate* rather than a low N.
- **A5 — `Kimi Code` is a two-word vendor name.** `| Kimi |` and `| Moonshot |` do not name it, and a
  duplicated row (e.g. one row per Kimi page) disqualifies the vendor, so the second Kimi page belongs in
  the row's source cell, not in a second row.
- **A6 — word boundaries are ASCII, not `\w`.** Two of four vendors publish Chinese pages; `\w` treats a CJK
  character as a word character, so `.codebuddy/skills/` in `…/skills/目录` would fail a `\w` boundary.
  The draft freezes ASCII boundaries (arm 21 proves the direction; it can only accept more occurrences of
  the *same* token, never a different token).
- **A7 — `held at base` is measured at `BASE_REV`, not at `--rev`.** A reader comparing `0 of 4` at a later
  tip to `held at base: 0` is comparing different trees; the field is the do-nothing figure only.

## Limits

- Documentary counter only: it verifies that committed bytes carry the frozen tokens, keys, hosts, pins and
  quotes; it says nothing about whether a vendor's client actually reads the root (no execution, no
  network). Shaping is disclosed in the docstring, not only here: whitespace collapse for snapshots, one
  `~/`-less and one trailing-`/`-less form per token, and nothing else — (d) in particular does **not**
  strip backticks, fold case or decode entities.
- The 47-world self-test proves each conjunct and each plan-named shortcut world can fail; it does not
  prove the counter will read 4 at the r73 tip — that is data, and wave 1 owns no verdict on it.
- No findings here are claims about a vendor's documentation. § F4 numbers are a probe over siblings'
  uncommitted files and are labelled as such.

## Files changed

- added `.ufo/waves/round-73/w1/build/ExecCnCounter/check_cn_vendor_surfaces.py` (draft counter; the L1
  copies it to `verifiers/` at freeze 2 — the blanked self-sha is content-only, so a byte-identical copy
  keeps it green; any edit requires `--print-self-sha` and a refill)
- added `.ufo/waves/round-73/w1/build/ExecCnCounter/evidence.txt` (verbatim run log)
- added `.ufo/waves/round-73/w1/ExecCnCounter.md` (this report)
- no committed lane file, no fleet repo, no sibling lane, no jj state touched; scratch removed
- tooling: none installed, none needed (python3 stdlib only; read-only `git show`)
