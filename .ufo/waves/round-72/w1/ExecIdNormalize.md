# ExecIdNormalize — round 72, wave 1 (assimilation id normalization, lane kotoba)

**Verdict: done, validated, no admission decided.** All eight staged rows (`S248 S254 S255 S256
S261 S262 S263 S264`) now normalize into the fleet 11-column schema with a re-runnable script; the
candidate blocks, the URL-keyed renumber map (`S214`–`S221`, stable across every admission subset),
the Gate notes and the candidate knowledge entries are under
`.ufo/waves/round-72/w1/build/ExecIdNormalize/`. A scratch mirror of the base tree with the block
in its Registry table validates **exit 0** with **20 W04 warnings — the same count as the base**,
no E-code, at 145 rows (theme admission) and 147 rows (all candidate rows); four negative worlds
turn the same mirror red with **E01 / E03 / E04 / E11** respectively. Two rows are **held back**,
not refused: staged `S255`/`S256` are cited by none of the plan's two theme entries.

**Axes I moved (godspeed).** *Coverage* — every candidate row is producible, including the two the
plan's grouping over-counts, and every rewrite the schema forces (prose `recheck`, pipe guard,
cross-references, `used-by`, ids) is implemented and self-tested. *Operability* — one command
(`receipt.sh [rev]`) rebuilds the mirror from any revision and re-validates; one flag (`--only`,
`--entry`, `--cite`, `--blocks`) re-emits any subset; a held-back row keeps its id, so a later
admission changes nothing but its block.

I opened none of the eight pages: this seat normalizes rows, it does not open sources. Every
`verified-at:` in the generated entries is the staged rows' own access date, marked as carried.

## Deliverables

`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-72/w1/build/ExecIdNormalize/`

| path | what |
|---|---|
| `normalize-staged-rows.py` | the transform: staged row → fleet row, block/emit, mirror, self-test |
| `receipt.sh` | one-command reproduction of the receipt below (mirror under `/tmp`, removed on exit) |
| `blocks/entry-1.md`, `blocks/entry-2.md`, `blocks/entry-3.md` | candidate append blocks (4 + 2 + 2 rows) |
| `blocks-all.json` | the maximal block definition (three entries, the campaign's own citation edges) |
| `renumber-map.json`, `renumber-map.md` | renumber map **keyed by URL**, all eight rows, `emitted` flag |
| `gate-notes.md` | stripped `recheck` prose + every rewrite, as a `## Gate` candidate |
| `collisions.md` | W04 / E04 / advisory URL findings over all eight selected rows |
| `entries/*.md` | candidate knowledge entries at their repo-relative names |
| `theme/` | the plan's two-entry admission: same map, `S220`/`S221` held back |
| `validate-receipt.txt` | full transcript of every command below, exit codes included |

## F1 — the transform runs, and its own 14 arms are all killed

```
$ python3 -B normalize-staged-rows.py --self-test
killed	pipe-refused-without-repair
killed	pipe-rewritten-to-semicolon
killed	refuse-policy-raises
killed	recheck-prose-stripped
killed	recheck-symbolic-kept
killed	recheck-iso-kept
killed	recheck-garbage-raises
killed	ids-sequential-from-214
killed	cross-reference-repointed
killed	used-by-admitted-only
killed	E04-within-scope-refused
killed	W04-across-scopes-noted
killed	rendered-line-NF-13
killed	held-back-when-uncited
self-test ok
exit=0
```

The arms cover each requirement the seat item names: a pipe is refused or rewritten, the `recheck`
prose is stripped and an unparseable cadence raises `E09`, ids run sequentially from the next free
id, a cross-reference is re-pointed, `used-by` keeps only admitted paths, `E04` is refused and
`W04` is only noted, a rendered row splits to `NF=13`, and an uncited row is held back.

## F2 — `recheck` prose is stripped and kept as a Gate note

Every selected row carries a prose `recheck` cell. Observed, staged row `S248` cell 10, run from
`/home/vgpnk/Projects/shokuknow/merge/kotoba` (`$11` is the `recheck` column under the census's own
`|` split):

```
$ awk -F'|' '$2 ~ /^ S248 $/ {print $11}' SOURCES.append.md
 90d — re-fetch the post and confirm the 56%, 53/53/79/100% figures and the 40KB→8KB compression result are unchanged (ran 2026-10-23)
```

Emitted `recheck` cell: `90d`; the stripped prose lands in `gate-notes.md`:

```
- S248: recheck `90d`; stripped prose: "re-fetch the post and confirm the 56%, 53/53/79/100% figures and the 40KB→8KB compression result are unchanged (ran 2026-10-23)"
```

Six of the eight rows are `90d`, two are `180d` (`S254`, `S256`) — all eight become a bare cadence,
which is what `sources-census.sh` accepts (`E09` otherwise; the arm `recheck-garbage-raises`
proves the refusal path).

## F3 — no literal and no escaped `|` anywhere in the staged document; the guard still bites

Run from `/home/vgpnk/Projects/shokuknow/merge/kotoba`:

```
$ grep -E '^ {0,3}\| S[0-9]{3,} ' SOURCES.append.md | grep -cF '\|'
0
$ grep -E '^ {0,3}\| S[0-9]{3,} ' SOURCES.append.md | grep -cF '\\'
0
```

So no selected row needs an anchor rewrite — but the guard is real and proven both ways: a row with
a pipe in a cell is refused at cell count (`EXC:splits into 13 cells, not 11`), and with
`--repair SID:6 --pipe-policy rewrite` the surplus cells are joined into the anchor with `; ` and no
backslash survives (`killed pipe-rewritten-to-semicolon`). The census splits on a literal `|`
(`gawk -F'|'`), so an escaped `\|` splits too — the rewrite is the only safe repair.

## F4 — ids re-pointed by document from S214; stable across admission states

`corpus/SOURCES.md` holds 139 rows and its highest id is `S213`, so the next free id is `S214`:

```
$ grep -cE '^ {0,3}\| S[0-9]{3,} ' corpus/SOURCES.md
139
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --file corpus/SOURCES.md | grep '^file'
file	rows	139
file	tier.A	131
file	tier.B	7
file	tier.C	1
file	status.mined	131
file	status.queued	7
file	status.rejected	1
```

Map (keyed by URL, `renumber-map.json`): `S261→S214`, `S262→S215`, `S263→S216`, `S264→S217`,
`S248→S218`, `S254→S219`, `S255→S220`, `S256→S221`. One new id per distinct source URL, assigned in
the order the blocks declare their rows (entry 1 first — the r70 precedent, where the first-declared
entry's rows took the lower ids). The same eight ids come out of the two-entry theme run, the
`--only S262` run (one row, still `S215`) and the all-rows run: **a held-back row keeps its id**.

Two cross-references inside the rows were re-pointed, and both are recorded:

```
$ grep -E 'cross-reference' gate-notes.md
- S263: cross-reference S262 -> S215 in column 7
- S254: cross-reference S248 -> S218 in column 7
```

They land in the emitted cells (`as S215 from a different vendor`, `always-on strategy S218
measures`). Lane ids the rows already cite (`S002`, `S164`) are not in the map and are untouched.

## F5 — `used-by` is exactly the admitted paths that cite the row, and the campaign agrees

The staged rows' `used-by` cells and the staged package's own entries (`source:` lines) agree for
all eight rows — checked, not assumed. Run from `/home/vgpnk/Projects/shokuknow/merge/kotoba`; the
command prints basenames of the two path sets and their equality:

```
$ python3 - <<'PY'   # rows' used-by vs the staged entries' `source:` lines
...
PY
S248: row used-by=2 ['context-rot-and-always-on-context.md', 'skill-invocation-is-the-bottleneck.md'] | staged entries citing it=2 ['context-rot-and-always-on-context.md', 'skill-invocation-is-the-bottleneck.md'] | agree=True
S254: row used-by=1 ['context-rot-and-always-on-context.md'] | staged entries citing it=1 ['context-rot-and-always-on-context.md'] | agree=True
S255: row used-by=2 ['client-frontmatter-and-discovery-divergence.md', 'client-loading-and-distribution-models.md'] | staged entries citing it=2 ['client-frontmatter-and-discovery-divergence.md', 'client-loading-and-distribution-models.md'] | agree=True
S256: row used-by=2 ['client-frontmatter-and-discovery-divergence.md', 'client-implementation-loading-model-amendment-2026-10-23.md'] | staged entries citing it=2 ['client-frontmatter-and-discovery-divergence.md', 'client-implementation-loading-model-amendment-2026-10-23.md'] | agree=True
S261: row used-by=2 ['skill-paths-and-precedence.md', 'skill-vs-always-on-boundary.md'] | staged entries citing it=2 ['skill-paths-and-precedence.md', 'skill-vs-always-on-boundary.md'] | agree=True
S262: row used-by=1 ['skill-vs-always-on-boundary.md'] | staged entries citing it=1 ['skill-vs-always-on-boundary.md'] | agree=True
S263: row used-by=1 ['skill-vs-always-on-boundary.md'] | staged entries citing it=1 ['skill-vs-always-on-boundary.md'] | agree=True
S264: row used-by=1 ['skill-vs-always-on-boundary.md'] | staged entries citing it=1 ['skill-vs-always-on-boundary.md'] | agree=True
```

The transform emits `staged used-by ∩ admitted`, plus any `--cite PATH=ID,ID` edge the caller
asserts; a row with no admitted citer is held back rather than emitted with `—`, because
`status: mined` with an empty `used-by` is a W03 warning and a row nobody cites is not admitted.

The C1 A4 entry (`corpus/knowledge/resident-index-and-rungs-round72.md`, drafted this wave at
`.ufo/waves/round-72/w1/build/ScribeEntryRung/resident-index-and-rungs-round72.md`) is a **new**
citer, so its edges are not in any staged `used-by` cell and must be declared. That draft carried
no `source:` line when I read it, so the ids are the C1 seat's to fix; once fixed, this is the
invocation, and it is receipt phase H (observed `exit=0`, `W04 lines: 20`, 8 rows):

```
$ python3 -B normalize-staged-rows.py --blocks blocks-all.json \
    --entry corpus/knowledge/skill-vs-always-on-boundary.md \
    --entry corpus/knowledge/context-rot-and-always-on-context.md \
    --entry corpus/knowledge/client-frontmatter-and-discovery-divergence.md \
    --entry corpus/knowledge/resident-index-and-rungs-round72.md \
    --cite corpus/knowledge/resident-index-and-rungs-round72.md=S214,S215,S216,S217 \
    --entry-src corpus/knowledge/resident-index-and-rungs-round72.md=<that draft> \
    --rev <rev> --mirror <dir>
S214 -> corpus/knowledge/skill-vs-always-on-boundary.md, corpus/knowledge/resident-index-and-rungs-round72.md
S215 -> ... (same two paths)  S216 -> ...  S217 -> ...
```

`--entry` must name the A4 path as well, or `used-by` drops it — the intersection is over admitted
paths; `--entry-src` **copies** another seat's entry into the mirror and never authors it; `--cite`
accepts a staged id or a new id and resolves both. Without `--entry-src`, `E11` fires: the mirror
must contain the entry a row cites.

## F6 — finding: the plan's entry-2 grouping over-counts its citations

The plan groups entry 2 as `{S248 S254 S255 S256}`. The staged entry
`knowledge/corpus/knowledge/context-rot-and-always-on-context.md` cites **only** `S254` and `S248`:

```
$ grep -oE '^source: S[0-9]{3}' context-rot-and-always-on-context.md | tr '\n' ' '
source: S254 source: S248
```

`S255` and `S256` are cited by `client-frontmatter-and-discovery-divergence.md`,
`client-loading-and-distribution-models.md` and
`client-implementation-loading-model-amendment-2026-10-23.md` — none of them this round's theme.
Under the theme admission the transform therefore **holds back `S220` (staged `S255`) and `S221`
(staged `S256`)** and says why:

```
- S220 (staged S255) -- no admitted entry cites it; staged used-by was 'corpus/knowledge/client-frontmatter-and-discovery-divergence.md, corpus/knowledge/client-loading-and-distribution-models.md'
- S221 (staged S256) -- no admitted entry cites it; staged used-by was 'corpus/knowledge/client-frontmatter-and-discovery-divergence.md, corpus/knowledge/client-implementation-loading-model-amendment-2026-10-23.md'
```

This is not a refusal and not this seat's decision: the maximal block (`blocks-all.json`) admits
`client-frontmatter-and-discovery-divergence.md` for exactly those two rows and emits all eight.

## F7 — the mirror validates clean, at both admission states

```
$ ./receipt.sh
== B. THEME admission (the plan's two entries): 6 rows, S255/S256 held back ==
rows inserted: 6 (S214, S215, S216, S217, S218, S219)
command: bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file /tmp/k72w1-ExecIdNormalize.mirror.kuLg/b/corpus/SOURCES.md
file	ok	/tmp/k72w1-ExecIdNormalize.mirror.kuLg/b/corpus/SOURCES.md
exit=0
W04 lines: 20

== C. row count of mirror B under census mode ==
file	rows	145
file	tier.A	131
file	tier.B	13
file	tier.C	1
file	status.mined	137
...
== E. ALL candidate rows (campaign citation edges): 8 rows, ids unchanged ==
rows inserted: 8 (S214, S215, S216, S217, S218, S219, S220, S221)
file	ok	.../e/corpus/SOURCES.md
exit=0
W04 lines: 20

== F. row count of mirror E under census mode ==
file	rows	147
file	tier.A	133
file	tier.B	13
file	tier.C	1
file	status.mined	139
```

Arithmetic: base 139 (A 131 / B 7 / C 1, mined 131) → theme 145 (B 7+6) → all 147 (A 131+2,
B 13, mined 139). The row counts are also the proof that the block landed **inside** `## Registry`:
the census does not count a row outside that section (it emits `E12` and skips it), so 145 and 147
are only reachable with the rows in the table. The mirror is a full `git archive` of the base tree
plus the block and the candidate entries — a superset of `corpus/`, because existing rows cite
`SKILL.md` and a mirror without it prints `E11` (the r70 lesson's own note).

The block is inserted immediately before the `## Paths` heading, i.e. at the end of the Registry
table; `## Paths` is `corpus/SOURCES.md:156`.

## F8 — E03 / E04: none for these eight rows, and both are refused when present

- **E03 (duplicate id):** none — the assignment starts at the registry's next free id and every
  emitted line is checked against the registry before it is written (`--force` overrides, unused).
- **E04 (duplicate URL within one scope):** none — the eight URLs are distinct, and no two selected
  rows share a scope. The transform refuses the shape rather than passing it through
  (`killed E04-within-scope-refused`), and a control world makes the census itself say it:
  `dup-url  exit=1 codes=E04,W04`.
- **E11 (dangling `used-by`):** none — every emitted path exists in the mirror;
  `missing-usedby  exit=1 codes=E11,W04` proves the check is live.

## F9 — W04: the lane already holds one of these documents, and the census cannot see it

No exact-URL collision exists between the eight staged rows and the 139 registry rows: the whole
`collisions.md` finding list is one bullet, the advisory one quoted below (it opens
`Selected rows checked: 8 (8 emitted: …; 0 held back: -)`).

```
- S221: advisory -- same document as S002 under `.md`-insensitive normalization (agentskills.io/client-implementation/adding-skills-support.md); the census's url_of() keeps `.md`, so neither W04 nor E04 fires
```

`S002` cites `https://agentskills.io/client-implementation/adding-skills-support`, staged `S256`
cites the same page as `…-support.md`; the census's `url_of()` drops a fragment and one trailing
slash but keeps `.md`, so the two strings differ. Their scopes also differ, so even an exact match
would be `W04`, not `E04`. The staged row itself says the page is held as `S002` and that the round-4
row `S164` records only its trust-gate paragraph — if the L1 admits `S221`, it is a **same-document
second row**, and the `teaches` cell is the place to say which sections it adds (the row already
does). W04 stays at 20 in every mirror, the base count, so nothing new is duplicated.

## F10 — four negative worlds, one per E-code, all red

```
== G. negative controls on mirror B (one row appended, then restored) ==
  pipe            exit=1 codes=E01,W04
  dup-id          exit=1 codes=E03,W04
  dup-url         exit=1 codes=E04,W04
  missing-usedby  exit=1 codes=E11,W04

clean mirror exit=0; controls red=4/4
```

Each control appends one row to the same validated mirror, runs the census, and restores the file;
the clean exit 0 is re-established by the same run's first block. This is the non-vacuity proof for
F7: the same command that reads `ok` reads the E-code when the row is wrong.

## F11 — candidate knowledge entries: generated, provenance-complete, admission-neutral

`entries/skill-vs-always-on-boundary.md`, `entries/context-rot-and-always-on-context.md`,
`entries/client-frontmatter-and-discovery-divergence.md` each open with one `source:` line per cited
row (new id, title, URL, the row's anchor, the carried access date), then `verified-at:`, `recheck:`
(cadence **with** the first row's stripped prose), `ground:`, then the body: each row's own
`teaches` cell and the quoted spans from its anchor cell. They state on their face that admission is
the source-opening seats' and the L1's, and that the rule prose for `SKILL.md` § Trigger-fidelity
checklist is the C1 seat's — the A4 rung entry (`resident-index-and-rungs-round72.md`) is not
written here and is not mine to write.

The entries exist in the mirror because `E11` requires every `used-by` path to exist: a normalized
block cannot be validated without the entry it cites. That is the guard working as designed, not a
convenience.

## Runbook (L1)

```
cd .ufo/waves/round-72/w1/build/ExecIdNormalize
python3 -B normalize-staged-rows.py --self-test
./receipt.sh c69711ee08279609374d895bb0f3c8c18ccf15c9        # phases A-H, exit 0

# re-emit the landed set (all eight candidate rows, campaign edges), then validate a mirror:
python3 -B normalize-staged-rows.py --blocks blocks-all.json \
  --entry corpus/knowledge/skill-vs-always-on-boundary.md \
  --entry corpus/knowledge/context-rot-and-always-on-context.md \
  --entry corpus/knowledge/client-frontmatter-and-discovery-divergence.md \
  --out . --rev <rev> --mirror <dir>

# any subset: --only takes staged ids or new ids, --entry takes any admitted path,
# --cite adds an edge from an entry that the staged used-by cell does not name,
# --entry-src copies a second seat's entry file into the mirror (never authored here),
# --repair SID:COL --pipe-policy rewrite is the only path that touches a cell's bytes.
python3 -B normalize-staged-rows.py --blocks blocks-all.json \
  --entry corpus/knowledge/skill-vs-always-on-boundary.md \
  --entry corpus/knowledge/context-rot-and-always-on-context.md \
  --only S214,S218 --out /tmp/subset      # emits S214 and S218; ids as in the full map
```

Admitting one more staged entry (e.g. `skill-paths-and-precedence.md` for `S261`) is `--entry` plus
one block entry; `used-by` widens to `staged ∩ admitted` automatically. A row whose page was not
re-opened this round must not be landed: the entries carry the campaign's access date, not this
round's.

## Risks and blockers

- **`verified-at` is carried, not observed.** I opened no page; the source-opening seats must
  re-open all eight and update the entry's `verified-at:`/`recheck:` before the L1 lands anything.
- **The plan's entry-2 row list is wrong by two rows** (F6). If the L1 lands the block as the plan
  words it, `S220`/`S221` would be emitted with a `used-by` that no admitted entry backs — which the
  transform refuses by holding them back.
- **`S221` duplicates `S002`'s document** (F9) and the census cannot see it. Whether that is a
  second row or a supersede is the L1's call; the staged row's `teaches` argues for a second row
  (different sections), and its scope differs from `S002`'s.
- **Nothing here decides admission.** No staged row is refused; two are held back pending a citer.

## Contract compliance

- No committed lane file touched. `git diff --stat` is empty. `git status --porcelain` in the lane
  lists only untracked paths; at my last check they were `.ufo/waves/round-72/snapshots/`,
  `.ufo/waves/round-72/w1.ready`, `.ufo/waves/round-72/w1.ready.dispatched`, `.ufo/waves/round-72/w1/`,
  `verifiers/fixtures/oc2-v2.1.4-anchor.txt` and `verifiers/fixtures/oc2-v2.1.4-decoy-moved.txt`.
  The two `verifiers/fixtures/` files are **not mine**: this seat writes only
  `build/ExecIdNormalize/**`, this report, and scratch mirrors under
  `/tmp/k72w1-ExecIdNormalize.mirror.XXXX`; they carry an mtime of `18:51:58`, after my last
  receipt run finished (`date: 2026-10-25T18:51:11-03:00`, wall time 4.02 s), and no command of
  mine names `verifiers/`. They are another seat's concurrent writes.
- Writes: `build/ExecIdNormalize/**` (deliverables) and this report; scratch mirrors under
  `/tmp/k72w1-ExecIdNormalize.mirror.XXXX` were created and removed by `receipt.sh`'s `trap`.
- No tool installed or upgraded: none was needed (`python3` stdlib + the fleet census script).
- No credential material, session URL or `op://` reference read or written.
