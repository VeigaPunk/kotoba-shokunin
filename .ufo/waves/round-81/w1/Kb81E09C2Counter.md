# Kb81E09C2Counter — C2 counter build (kotoba round 81, wave w1)

Seat: Kb81E09C2Counter (executor, leaf). Date: 2026-10-27 (host local; fetch stamps UTC).
Lane base: `b284223105f4d106f7e8f56ed4fd296c643cda0e`. Lane root:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Scope: the NEW C2 counter only (plan § C2). I wrote no lane file outside
`.ufo/waves/round-81/`; the lane's tracked tree is unmodified
(`git status --porcelain` at the lane prints only `?? .ufo/wapes` (inherited,
R80-D2) and `?? .ufo/waves/round-81/`).

## 1. What I built

`verifiers/check_sdk_allowed_tools.py` (published as
`.ufo/waves/round-81/build/check_sdk_allowed_tools.py`, patch
`build/Kb81E09C2Counter.patch`, `git apply --check` exit 0 against base in a
scratch clone, mode 100755):

- lines 1638, bytes 75324
- sha256 of the file: `739a71810453f83c94468db25fc39c55f3bfbfdb224894a630d91e5aea86f985`
- patch `build/Kb81E09C2Counter.patch` sha256
  `e53ed1b7ef0472b12f4c720010a7bda512d99dcd318deefad9b0c7f80d2e5b7f` (adds only
  `verifiers/check_sdk_allowed_tools.py`, mode 100755)
- blanked self-sha (`--print-self-sha`, the drift-guard constant):
  `38ac8513c8f693c58b9f4b4a582471bc41ee3c6e7072f1b5cec06f07b17c53b5`
- in-file pin (`--print-pins`): `SNAPSHOT_PIN = ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`,
  `SNAPSHOT_PATH = .ufo/waves/round-81/snapshots/S249.md`,
  `CANONICAL_URL = https://code.claude.com/docs/en/agent-sdk/skills.md`
- self-contained stdlib only (argparse, hashlib, json, re, subprocess, tempfile,
  urllib — no import of any other verifier).

Frozen predicate (the plan's sentence, printed by the counter's own docstring):

> `python3 -B verifiers/check_sdk_allowed_tools.py --rev <rev>` prints
> `sdk allowed-tools surface documented N of 1` and exits 0 iff N == 1 and the
> tree conjuncts hold; at the r81 base it prints `0 of 1` and exits 1.

Conjuncts as implemented (a)–(g), each printed on its own line as
`conjuncts: a ok|FAIL, ...`:

- (a) the entry `corpus/knowledge/allowed-tools-sdk-round81.md` carries a
  `source:` line naming S249 with the canonical URL (host+path identity, the
  bare route accepted on the entry line only) and the pinned snapshot named
  (full path or basename), plus `verified-at: 2026-10-27` and a non-empty
  `recheck:`.
- (b) row S249 is exactly one 11-cell row, `mined`, tier A/B, `used-by`
  listing the entry path, and a `source` URL whose host+path equals the
  canonical URL.
- (c) the S249 anchor names the snapshot and carries
  `fetched <date|date-timeZ>, HTTP 200, <bytes> B, sha256 <hex>` equal to the
  counter pin; the committed snapshot's own sha256 is that pin; the optional
  sibling `S249.fetch.json` must agree (a second digest or a different byte
  count is exit 2).
- (d) a quoted span on a line citing S249 (house `located quote "..."` form),
  5..25 words, containing `allowed-tools` or `allowedTools`, occurring in the
  committed snapshot's Markdown text view after the first heading, not on a
  heading line and not in the first-heading block (Q70). The located span and
  the view line are printed.
- (e) row S248's `used-by` names the entry, and
  `corpus/lessons/round-81.md` logs the old->new move on a line naming S248,
  the entry path and an arrow (`→`, `->`, `=>`).
- (f) `SKILL.md` has a non-table line naming `allowed-tools` + "pre-approval"
  whose block (to the next heading) names the SDK channel (`SDK` plus
  `allowedTools`/`allowed_tools`), and a gate row with 8 non-empty cells, kind
  `gate`, for `verifiers/check_sdk_allowed_tools.py`.
- (g) `corpus/README.md` has a coverage-map row naming the entry, and
  `PROVINCE.md` `## Core` has exactly one bullet naming the entry, that bullet
  naming the SDK channel.

Printed diagnostics: headline, `generator world: M of 1`, `measured-rev`,
`snapshot: ... pin`, the seven conjunct verdicts, the located quote, S248's
status and `used-by`, the S248 old->new lesson line, skill channel, registry
home, README row, province channel, province bullet count, then one line per
failing conjunct. Exit 0 = N==1 and (a)-(g); 1 = content verdict; 2 = could not
evaluate (unknown rev, SOURCES absent, snapshot absent/tampered/doubly pinned,
counter drift).

## 2. Declared readings (chosen before any after-value, named in the docstring)

1. The pin lives **in the counter** because (c) says "the pin in both the
   counter and the row's fetch record"; the L1 refills `SNAPSHOT_PIN` at freeze
   only from the reviewed fetch, never to green a world. **No refill is needed
   for this wave**: the wave's own `S249.md` is byte-identical to the pin (the
   counter hashes the committed bytes and would abort otherwise — it ran green
   on the candidate world, § 3.3).
2. (c) is **exit 2** when the committed snapshot is absent (the plan's C3: a
   quote asserted without committed snapshot bytes cannot be evaluated), when
   it does not hash to the pin (`snapshot_tampered`), and when the sibling fetch
   record states a second digest/byte count. A wrong digest in the **row's
   anchor** is a content finding (exit 1), not exit 2.
3. The located quote is the double-quoted span(s) on lines citing S249; several
   spans are allowed and the surface is documented when **at least one** meets
   (d). This is what keeps a second quoted sentence on the same line from being
   a defect.
4. `MIN_QUOTE_WORDS = 5` is the round-80 precedent; the plan freezes only
   "≤ 25 words". A one-word span (`allowed-tools`) is a token, not a located
   quote, so the floor is kept **and printed**. E08's 13-word span passes.
5. The snapshot text view is the round-79/r80 rule unchanged (Markdown:
   backticks deleted, list markers removed, whitespace collapsed, headings =
   `#`-lines outside fences). The frozen snapshot is Markdown; a non-Markdown
   snapshot reads as plain text (no headings, no backtick deletion).
6. The `allowed-tools` rule **area** is the block from the first non-table line
   naming `allowed-tools` + "pre-approval" to the next heading. A gate-table row
   is never the anchor (the table is instrumentation, not the rule); a sentence
   inside the paragraph, or an adjacent paragraph before the next heading, is
   inside the area.
7. The generator world is printed and **never gated** (§ 5).
8. `--fetch` is the plan's "documented recheck path": network, never the claim
   measurement, and not exercised by `--self-test` (declared, and run once for
   the receipt).

## 3. Evidence (exact commands, exits; receipts under build/)

Scratch: `/fast/scratch/hyaku/kotoba-r81/Kb81E09C2Counter/` (removed on exit).
`--work`/`TMPDIR` pointed inside it; every fixture is an isolated git repo.

### 3.1 Self-test — `build/Kb81E09C2Counter-selftest.txt`

```
$ python3 -B .ufo/waves/round-81/build/check_sdk_allowed_tools.py --self-test --work <scratch>/tmp
... 47 worlds ...
self-test: 0 failure(s) over 138 assertions in 47 world(s)
exit=0
```

47 PASS lines, 0 FAIL. The battery is one satisfying world (exit 0 with the
exact headline `sdk allowed-tools surface documented 1 of 1`, under an absolute
`--repo` and a relative `--repo .`), plus one broken world per conjunct (a:
absent entry/foreign path/no source line/missing verified-at/missing recheck/
URL/anchor; b: queued/tier C/12 cells/used-by/URL host and sibling path; c:
anchor digest, anchor not naming the snapshot, HTTP 404 record, missing
snapshot, pin mismatch, fetch-record disagreement; d: absent, floor, ceiling,
no field token, heading line, first-heading block, backtick form; e: S248
reverted, lesson missing/absent; f: no gate row, empty field, channel outside
the area, no rule paragraph, table-row anchor; g: README row, province channel,
two bullets), the plan's C0/C4 do-nothing controls, and three cannot-evaluate
arms (unknown rev, SOURCES absent, drift).

### 3.2 Base (do-nothing) — `build/Kb81E09C2Counter-base.txt`

```
$ python3 -B .ufo/waves/round-81/build/check_sdk_allowed_tools.py --repo . --rev b284223105f4d106f7e8f56ed4fd296c643cda0e
sdk allowed-tools surface documented 0 of 1
generator world: 0 of 1
...
conjuncts: a FAIL, b FAIL, c FAIL, d FAIL, e FAIL, f FAIL, g FAIL
quote MISSING: the entry is absent
  entry corpus/knowledge/allowed-tools-sdk-round81.md absent at b2842231... (the frozen path is the entry's only home)
exit=1
```

The absolute `--repo <lane>` form prints the same and exits 1 (same receipt).

### 3.3 Positive control on the wave's own bytes — `build/Kb81E09C2Counter-candidate.txt`

Candidate world = `--shared` clone of the lane at base + the wave's own
published artifacts: `build/Kb81S05SourcesEdits.patch`,
`build/Kb81S08ReadmeRows.patch`, `build/Kb81S10Province.patch`,
`build/Kb81S09SkillRule-SKILL.patch`, `build/allowed-tools-sdk-round81.md` ->
`corpus/knowledge/allowed-tools-sdk-round81.md`,
`.ufo/waves/round-81/snapshots/S249.md` (+ `S249.fetch.json`),
`build/Kb81S01Lesson.md` -> `corpus/lessons/round-81.md`; commit `c6e5452d`.

```
$ python3 -B .ufo/waves/round-81/build/check_sdk_allowed_tools.py --repo <clone> --rev c6e5452d66c4e3c1cea6a361de7c9a730e0ac64c
sdk allowed-tools surface documented 1 of 1
generator world: 1 of 1
conjuncts: a ok, b ok, c ok, d ok, e ok, f ok, g ok
quote located on snapshot line 234: 'frontmatter or with the allowedTools option (allowed_tools in Python) in your query configuration'
S248 status queued; used-by corpus/knowledge/allowed-tools-sdk-round81.md
s248 old->new logged in the lesson ok
skill sdk channel ok
registry home ok
readme coverage row ok
province sdk channel ok
province bullets naming the entry: 1
exit=0
```

This is **not** the claim measurement (the lane tree is unchanged); it is the
instrument's positive control on the real bytes, and it independently
reproduces E08's own view-line 234.

### 3.4 Shortcut/mutation worlds on those same real bytes — `build/Kb81E09C2Counter-realbytes.txt` (driver `build/Kb81E09C2-realbytes.py`)

```
as-expected  candidate world itself: exit 0 | ... 1 of 1
as-expected  drop the committed snapshot (quote without bytes): exit 2 | environment error
as-expected  S248 used-by reverted to em-dash: exit 1 | ... 0 of 1
as-expected  located quote replaced by an absent sentence: exit 1 | ... 0 of 1
as-expected  anchor sha256 zeroed: exit 1 | ... 0 of 1
as-expected  SDK channel line moved out of the rule area: exit 1 | ... 0 of 1
as-expected  snapshot tampered (pin left): exit 2 | environment error
as-expected  entry deleted: exit 1 | ... 0 of 1
as-expected  lesson deleted: exit 1 | ... 0 of 1
real-byte worlds: 0 divergence(s)
exit=0
```

(One driver bug was found and fixed while doing this: the first version of the
"channel outside the area" mutation moved the whole rule paragraph, which moves
the anchoring area with it, so the world legitimately stayed green. The
mutation now moves only the channel sentence. The same run exposed a real
reading gap — a gate-table row could anchor the area — and `rule_area` now
skips table rows; self-test arm "(f) a gate-table row is not the allowed-tools
rule area" pins that.)

**Independent confirmation on the same bytes.** Seat Kb81E07C2Worlds measured
these exact bytes (their receipt `build/c2_controls.txt`, driver
`build/c2_controls.py`) with 8 isolated worlds at base: C0 `0 of 1` exit 1, C1
exit 2 `snapshot_tampered`, C2 exit 1 on the S248 cell, C3 exit 2 on the
missing snapshot, C4 `0 of 1` exit 1, plus two oracles (`H1` the census seat's
S249 row, `R1` the entry seat's cells) both `1 of 1` exit 0 with `conjuncts: a
ok … g ok` — 0 divergence, and their N1 world confirms (e)'s lesson arm is
load-bearing (S248 cell updated with no lesson is refused).

### 3.5 Freshness recheck — `build/Kb81E09C2Counter-fetch.txt`

```
$ python3 -B .ufo/waves/round-81/build/check_sdk_allowed_tools.py --fetch --repo <clone> --rev c6e5452d
fetched 2026-10-28T02:42:39Z, HTTP 200, 28395 B, sha256 ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2
pin match: yes
quote re-located in the FETCHED bytes: yes
exit=0
```

A third independent fetch (after E08's two) reproduces 28395 B and the pin; the
entry's 13-word span is locatable in the fetched bytes.

## 4. Pin grounding

`ac62c2df…` is not a guess: the committed `corpus/SOURCES.md` S248 anchor
carries it for the same URL, the reviewed r80 fetch
`.ufo/waves/round-80/build/Kb80S05-agent-sdk-skills.md` hashes to it
(28395 B, `sha256sum`), the wave's own `.ufo/waves/round-81/snapshots/S249.md`
hashes to it under the counter's own gate, and § 3.5 re-derives it over the
network. No pin refill is required for this wave.

## 5. Q74 disclosure — the generator world

The counter builds the complete evidence shape mechanically from the measured
bytes (mechanical 5..25-word quote window, row cells, anchors, SKILL rule +
gate row, README row, PROVINCE bullet, lesson line) and scores it with the
**same** `check()`; its score is printed (`generator world: M of 1`) and never
gates. On the wave's own bytes it reads **1 of 1**: the counter therefore
measures the FORM of the evidence shape, not the semantic sourcing. The claim's
semantics — that the page documents a second grant channel (`allowedTools` /
`allowed_tools` in query config) and that managed settings can override both —
rest on the page's own words and belong to the non-author reviewers/critics,
never to the counter's number. The L1 should not cite `documented 1 of 1` as
semantic proof.

## 6. Port from r80, and what changed

Ported verbatim or near-verbatim from `verifiers/check_allowed_tools.py`:
`rendered` (comment/fence stripping for tree text), `ws`, `word_bounded(_ci)`,
`_fence_flags`, `view_with_headings` (Markdown branch), `text_view`,
`_split_cells`/`_cells`/`is_separator`, `registry_rows`, `urls_of`,
`page_key`/`same_page`, `cited_sids` (slug-tail skip), `_line_of`/
`quote_location` (Q70), `Repo` (`git show` committed bytes), `mktemp`,
`_commit_tree`, the `_world`/`_run_spec`/`selftest` harness, the `SELF_SHA`
drift guard and `--print-self-sha`, `province_bullets`, and the
`registry_home_ok` shape.

Dropped as dead weight for a one-surface claim: the frozen five-cell surface
table machinery (surface table identity, token roles, grant labels, page-token
coupling), the six-surface loop and order, the MANIFEST/per-page `.manifest`
ambiguity grammar and `snapshot_name` resolution (one snapshot, one pin), the
shared-banner arm (one page), the cited-id/source-line subset rule (the S249
line is the quoting line), the semantic-rider line, and `held_at_base` (r80's
diagnostic; the C2 do-nothing figure is the base run itself).

Changed because the round changed the claim: a single "N of 1" headline with no
partial credit; the snapshot is bound by an in-file constant plus an optional
fetch-record corroboration instead of a manifest; the anchor must NAME the
snapshot (new conjunct text); (d) accepts either spelling of the field and any
satisfying span; (e) adds the S248 used-by move and its lesson log; (f) is the
prose rule area plus the gate row; (g) is the README row plus the exactly-one
Core bullet; `--fetch` is new and is the plan's documented recheck path.

## 7. Cross-seat alignment (coordination, all by message)

- S05SourcesEdits: confirmed the row contract (canonical URL host+path, tier
  A/B, `mined`, `used-by` listing the entry path exactly, anchor naming
  `.ufo/waves/round-81/snapshots/S249.md` with the `fetched ... HTTP 200 ...
  sha256 <pin>` clause). Their regenerated row passes in the candidate world.
- E08C2Entry: told them the quote/source contract before they wrote; their
  13-word span and single-span source line pass, and their warning that S248
  is `queued` is correct — the counter does **not** require S248 to be mined.
- S01Lesson: asked for one line naming S248 + the entry + an arrow; their draft
  line passes in the candidate world.
- S09SkillRule: answered that `--self-test` exists as an exact
  `add_argument("--self-test", action="store_true")`; sent the final file
  sha256/self-sha so their registry receipt can be re-run; their rule sentence
  and gate row pass.
- S10Province: told them the exact (g) requirement (exactly one Core bullet
  naming the entry, and that bullet naming the SDK channel); their draft passes.
- E07C2Worlds: handed the frozen bytes, the drift rule (edited copies exit 2),
  and the expected control shapes.

## 8. Risks / blockers

1. **Pin refill**: only if the L1 lands a snapshot that is not byte-identical to
   `ac62c2df…`. Today it is identical (counter hash gate + `--fetch`), so no
   action. A refill must come from the reviewed fetch and be recorded in
   `receipts/freeze-shas.txt`, never from a measured world.
2. **5-word quote floor** is stricter than the plan's "≤25 words" and is
   declared in the docstring; E08's 13-word span passes. If the L1 prefers the
   bare plan reading, the constant is one line and must be changed before
   freeze, not after data.
3. **Exact entry path** `corpus/knowledge/allowed-tools-sdk-round81.md`; an
   entry published elsewhere reads as absent (0 of 1).
4. **Anchor content**: the S249 anchor must name the snapshot and carry a
   `fetched … HTTP 200 … sha256 <pin>` clause; S05's row does.
5. **`--fetch`** is not self-tested (needs the network) — declared; its receipt
   is a real run.
6. The counter is published at `verifiers/` only via the patch; the lane tree
   is untouched by this seat. The gate row that S09 drafted must land in the
   same commit as the counter (plan § C1 repair 6), otherwise `registry home
   MISSING` and exit 1.

## 9. Tooling

No install or upgrade was needed or attempted (python3 stdlib + git only);
`pacman` was never run. Scratch was used and deleted; the probe artifacts live
only under `.ufo/waves/round-81/` (the R80-D2 class this round is mining).

VERDICT: C2 counter built and frozen-ready — 47 self-test worlds / 138 assertions pass (exit 0), base prints `0 of 1` exit 1 in both `--repo` forms, and the wave's own bytes read `1 of 1` exit 0 with 8/8 real-byte mutation worlds as expected; headline is form-level (generator 1 of 1) and no pin refill is needed.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/check_sdk_allowed_tools.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E09C2Counter.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E09C2Counter-selftest.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E09C2Counter-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E09C2Counter-candidate.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E09C2Counter-realbytes.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E09C2-realbytes.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E09C2Counter-fetch.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E09C2Counter.md
