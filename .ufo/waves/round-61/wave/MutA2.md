# MutA2 — arm A2 (semantic action) attack: invented actions that survive word support

Seat: `kotoba-r61-wave-MutA2` (leaf mutation tester, round 61 attempt 1, hyaku run 5).
Date of measurements: 2026-10-23, 19:12–19:22 UTC (stamped below).
Lane (READ-ONLY): `/home/vgpnk/Projects/shokunin/kotoba-shokunin` at
`7827628a939b0333c89892dfcedc72e390ccfb60` (plan freeze commit; counter v2
`verifiers/check_scoped_rules.py` sha256
`ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`).
Base: `f3246d1493b60ea1c0d947a19c39f9e08e92f326`.
Scratch rig (untrusted, never an evidence source):
`/fast/scratch/hyaku/kotoba-r61/MutA2/` — a `git clone --shared` of the lane at
`7827628a`, used only to commit Action-cell mutations and run the committed counter.
No lane, fleet, sibling, `.ufo/state`, or jj/git-index file was written except this
report. No tool was installed; pacman untouched.

**Bottom line.** Arm A2 as frozen ("every load/event claim in the Action cell must be
supported by text on the committed snapshot page, not vocabulary matching alone") has
no implementation in the wave yet. Against the committed v2 counter that v3 must
start from ("change the minimum"), **ten invented-Action cells were measured with the
counter's own judge (`action_conjunct`); all ten pass it, and five of the ten were also
committed end-to-end as one-cell SKILL.md mutations.** The five committed mutants each
print `scoped rule files backed on committed snapshots 4 of 4` (and, for the three run
with `--fetch`, `found on the live page 4 of 4`, **exit 0**), identical to the pristine
row. The four requested attack classes all land: scattered-word false support, quoted
action text, nav/footer support, and listed-but-unwired events. A measured guard
conjunction (G5 ∧ G7 for the frozen W6 class, + G9 for the compound-purpose bypass)
rejects all ten cells and keeps the four eligible r60 rows; one mutant class (F6,
non-load purpose claims) remains a filed bypass of the frozen A2 *scope* even under
the full guard.

This is a coverage finding. It does not change the frozen contract; it tells the L1
what W6 must contain and what A2 must implement.

## 1. Evidence basis and hashes

Committed snapshot pages used (bytes read from the lane; sha256/size/lines measured here,
`date -u` 2026-10-23 19:22:35Z):

| Page | bytes | lines (`wc -l`) | sha256 |
|---|---|---|---|
| `.ufo/waves/round-60/snapshots/S103.page` | 54043 | 664 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` |
| `.ufo/waves/round-60/snapshots/S105.page` | 23715 | 367 | `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f` |
| `.ufo/waves/round-60/snapshots/S106.page` | 8730 | 110 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` |
| `.ufo/waves/round-60/snapshots/S108.page` | 17403 | 399 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` |

Files whose bytes changed during the probe (scratch clone only):

| file | pristine | mutant F4 | restored |
|---|---|---|---|
| `SKILL.md` | `2d2c1d5f78bc3d5f6dcb4ee30b40ccc647c286bf63a76f49127e60558b9a3909` | `f5b2d140918d41d0c63effb4d39a5b4d3076a901f7e9cb25a92a437d57a441f0` | `2d2c1d5f78bc3d5f6dcb4ee30b40ccc647c286bf63a76f49127e60558b9a3909` |
| `verifiers/check_scoped_rules.py` | `ca2585a4…c04a` | `ca2585a4…c04a` (never mutated) | `ca2585a4…c04a` |

## 2. Baseline and restoration (mutation-tester record)

Pristine clone at `7827628a`:

```
$ date -u
Fri 23 Oct 2026 07:10:21 PM UTC
$ python3 -B verifiers/check_scoped_rules.py --rev 7827628a939b0333c89892dfcedc72e390ccfb60
scoped rule files backed on committed snapshots 4 of 4; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 7827628a939b0333c89892dfcedc72e390ccfb60
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
exit=1                        # no --fetch: the frozen predicate is not this run

$ python3 -B verifiers/check_scoped_rules.py --self-test
self-test: 0 failure(s) over 318 assertions
exit=0

$ python3 -B verifiers/check_scoped_rules.py --rev 7827628a… --fetch   # pristine full predicate
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
exit=0                        # pristine control for the mutant --fetch runs below
```

The mutation is the smallest behavior-bearing point: one SKILL.md table cell
(`### Scoped rule files by client`, first table, one `Action` cell and its
`S### :L` citation). Every other committed byte is the lane's.

**Mutant M-F4** — Claude Code Action cell:

```
| Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `paths` (e.g. `src/api/**/*.ts`, S103 :198) | Write the SessionStart hook so rule files load after each file edit. (S103 :593) |
```

Expected detector: the committed v2 counter at the mutant revision. Offline it must
still print `backed … 4 of 4` (the counter's action conjunct is inside `backed`); with
`--fetch` it must still meet the frozen predicate. Actual:

```
$ git -c user.name=mutA2 -c user.email=muta2@scratch.local commit -am "MutA2: invented SessionStart action…"
8893ce041d6f4bcc9fcc2af3c3d99c93ff87623f
$ sha256sum SKILL.md
f5b2d140918d41d0c63effb4d39a5b4d3076a901f7e9cb25a92a437d57a441f0  SKILL.md
$ python3 -B verifiers/check_scoped_rules.py --rev 8893ce041d6f4bcc9fcc2af3c3d99c93ff87623f
scoped rule files backed on committed snapshots 4 of 4; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 8893ce041d6f4bcc9fcc2af3c3d99c93ff87623f
exit=1

$ date -u
Fri 23 Oct 2026 07:21:10 PM UTC
$ python3 -B verifiers/check_scoped_rules.py --rev 8893ce04… --fetch
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 8893ce041d6f4bcc9fcc2af3c3d99c93ff87623f
exit=0
```

Verdict: **SURVIVED** — the invented event action is indistinguishable from the
pristine row at the frozen v2 predicate (`F = 4 ≥ TARGET = 3`, exit 0). The same
detector on the restored bytes is identical to baseline.

Restoration:

```
$ git reset --hard -q 7827628a939b0333c89892dfcedc72e390ccfb60
$ git rev-parse HEAD
7827628a939b0333c89892dfcedc72e390ccfb60
$ sha256sum SKILL.md
2d2c1d5f78bc3d5f6dcb4ee30b40ccc647c286bf63a76f49127e60558b9a3909  SKILL.md
$ diff -u baseline.out restored.out && echo "RESTORED OUTPUT IDENTICAL"
RESTORED OUTPUT IDENTICAL
$ git status --porcelain | grep -v '^??' || echo tracked-clean
tracked-clean
```

The F4 mutant commit and the other mutant commits remain in the scratch clone only;
the lane has no commit from this seat.

## 3. End-to-end mutants (all four requested classes + the wave's W6 + one scope gap)

Each row is one committed Action-cell-only mutation in the scratch clone; the rest of
the world (entry, SOURCES, Gate, snapshots) is the lane's committed r60 world. The
`--fetch` runs are the frozen predicate; the offline runs show the internal `backed`
count that A2 must reject inside. `date -u` for the batch: 2026-10-23 19:21:04Z.

| Mutant | client / cited line | commit | `SKILL.md` sha | offline | `--fetch` |
|---|---|---|---|---|---|
| Pristine | — | `7827628a` | `2d2c1d5f…3909` | 4 of 4, exit 1 | 4 of 4, **exit 0** |
| F1 scattered false support | VS Code / S105:287 | `436b9ad7` | `78ef0924…9eb5` | 4 of 4, exit 1 | 4 of 4, **exit 0** |
| F2a quoted action | Claude Code / S103:599 | `c55730c9` | `d490884f…0df3` | 4 of 4, exit 1 | not run (see §8) |
| F3 nav text | Claude Code / S103:3 | `d7164609` | `89623b95…e9c4` | 4 of 4, exit 1 | not run (see §8) |
| F4 unwired event | Claude Code / S103:593 | `8893ce04` | `f5b2d140…41f0` | 4 of 4, exit 1 | 4 of 4, **exit 0** |
| F6 compound purpose | Copilot CLI / S106:60 | `a1f1bc02` | `dae1b5e6…2ada` | 4 of 4, exit 1 | 4 of 4, **exit 0** |

Exact cells (inserted verbatim into the named client's Action cell; citation appended):

- F1: `Create a settings profile and sync it so the instructions load from the project directory. (S105 :287)`
- F2a: `Use the `InstructionsLoaded` hook to log which `CLAUDE.md` and rules files are loaded, when they load, and why. (S103 :599)`
  (the page sentence, backticks kept, cited at its own line)
- F3: `Discover available pages so the instructions load before exploring further. (S103 :3)`
- F4: `Write the SessionStart hook so rule files load after each file edit. (S103 :593)`
- F6: `Create instructions files with glob syntax and organize the copies in the project directory. (S106 :60)`

Consolidated evidence transcript (`date -u` 19:21:04Z; both stamps in `evidence.txt`):

```
--- rev 7827628a939b0333c89892dfcedc72e390ccfb60
2d2c1d5f78bc3d5f6dcb4ee30b40ccc647c286bf63a76f49127e60558b9a3909  SKILL.md
scoped rule files backed on committed snapshots 4 of 4; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 7827628a…
exit=1
--- rev 8893ce041d6f4bcc9fcc2af3c3d99c93ff87623f
f5b2d140918d41d0c63effb4d39a5b4d3076a901f7e9cb25a92a437d57a441f0  SKILL.md
scoped rule files backed on committed snapshots 4 of 4; live not run
exit=1
--- rev 436b9ad74c1fa936dc8b1b9c01bf37169fb171f8
78ef0924c862e1a2cf1b93587a391ed6fdb6f8591df36e462deb6cd33d049eb5  SKILL.md
scoped rule files backed on committed snapshots 4 of 4; live not run
exit=1
--- rev c55730c90ac4e1a93c3232276fcaa953f2982e31
d490884faafd082c0dbdd96e0eaa9cc3eee9f998a95cf3a6d8f179b824710df3  SKILL.md
scoped rule files backed on committed snapshots 4 of 4; live not run
exit=1
--- rev d7164609ea2d478c993c56d88f693663f7aac7a3
89623b95d1bcc4ceddc1b24b5dc52bd18dd605c81399815d72418317c84de9c4  SKILL.md
scoped rule files backed on committed snapshots 4 of 4; live not run
exit=1
--- rev a1f1bc0288c9cb9cec31b02b00b57dfaaca8c76a
dae1b5e65c071efee4dc6dffccefc8d8f3eee09c8a25eb2d1efaf0f76042ada5  SKILL.md
scoped rule files backed on committed snapshots 4 of 4; live not run
exit=1
```

## 4. Word-level measurements (the counter's own functions)

Probe: read-only import of the clone's committed counter (sha verified
`ca2585a4…c04a`), pages read from the lane snapshots. `v2` is
`cs.action_conjunct(lines, cell, cited)`; `|W|`/`need` are the counter's own content
words and threshold; `shared` is against the cited line. `D1raw` is a naive page-bag
v3 (every content word occurs somewhere on the page on a raw tokenizer, backticked
tokens included). `D2 all-words` is every content word on one line. Full probe output
is pasted in the appendix; the decisive columns:

| Case | cell words \|W\| / need | cited-line shared | v2 | D1raw page-bag | D2 all-words on one line |
|---|---|---|---|---|---|
| P-S103 (pristine) | 11 / 6 | 10 | PASS | True | [] |
| P-S105 (pristine) | 6 / 3 | 5 | PASS | True | [] |
| P-S106 (pristine) | 12 / 6 | 9 | PASS | True | [] |
| P-S108 (pristine) | 9 / 5 | 9 | PASS | True | [131] |
| F1 | 8 / 4 | 4 | PASS | True | [] |
| F2a (backticks kept) | 5 / 3 | 5 | PASS | True | [599] |
| F2a-plain (backticks removed) | 7 / 4 | 6 | PASS | True | [599] (raw) |
| F2b (S108:160) | 12 / 6 | 12 | PASS | True | [160] |
| F3 | 6 / 3 | 4 | PASS | True | [] |
| F3b (footer, S105:365) | 6 / 3 | 4 | PASS | True | [] |
| F4 | 8 / 4 | 4 | PASS | True | [] |
| F5 (S103:599, log→load) | 7 / 4 | 5 | PASS | True | [] |
| F6 | 9 / 5 | 5 | PASS | True | [] |
| W6-sib (the wave's W6 cell) | 8 / 4 | 6 | PASS | True | [] |

Two measured facts the v3 implementer must not miss:

1. **A "all words on one line" A2 would reject three eligible rows.** P-S103, P-S105
   and P-S106 have no single snapshot line holding all their content words
   (`D2 all-words = []`), because they are paraphrases. A2 must keep a support
   threshold (the v2 half rule, or a measured equivalent), not demand a verbatim span.
   The Cursor row is the exception: its Action is line 131 verbatim modulo backticks,
   so a blanket "reject verbatim quotes" rule would reject a real row.
2. **The counter's `content_words` strips backticked spans.** F2a's event name
   `` `InstructionsLoaded` `` disappears from W (5 words instead of 7), so an A2 that
   decides "is this a load/event claim?" with `content_words` can be blinded by putting
   the event in backticks. Claim detection must run on raw bytes; the support check may
   still use the counter's tokenizer.

## 5. The attacks, one by one, with expected catch / filed bypass and guard

### F1 — scattered-word false support (VS Code, S105:287)

Cell: `Create a settings profile and sync it so the instructions load from the project
directory.` Cited at S105:287, the Settings Sync line:

```
To sync profile instructions, enable Settings Sync and run **Settings Sync: Configure**
from the Command Palette (`kb(workbench.action.showCommands)`). Select **Prompts and
Instructions** from the list of settings to sync.
```

The words are all on the page (`create` 13×, `settings` 17×, `profile` 5×, `sync` 12×,
`instructions` 157×, `load` 3×, `project` 16×, `directory` 3×) but no sentence says
instructions load from a project directory because of a synced settings profile. v2
passes on the half rule (4 of 8 words on line 287). `--fetch` exit 0, 4 of 4 live.

Expected under the frozen A2 as a *page-bag* reading: **passes** → filed bypass.
Expected under a claim-span reading: caught. Guard: **G5 + G7** (cited line carries
the row's `applyTo` key and the half overlap; the load claim's words must co-occur on
one line).

### F2 — quoted action text (S103:599 and S108:160)

- F2a quotes the page's own troubleshooting sentence verbatim
  (`` Use the `InstructionsLoaded` hook to log which `CLAUDE.md` and rules files are
  loaded, when they load, and why. ``) as the Claude Code *Action*, cited at 599. It is
  true page text, but it is not the scoping act the row documents (the row's key is
  `paths`, whose action line is 194).
- F2b quotes S108:160 (`Reference files instead of copying their contents. Agent reads
  a referenced file when it needs it…`) as the Cursor Action, cited at 160; true text
  about rule-body references, not the `globs` scoping act at 131.

Both pass v2 with full overlap (5/5 and 12/12) and D2; the quotes are on the page by
construction. The Cursor *real* row is itself line 131 verbatim modulo backticks, so
the discriminator cannot be "is a quote". Expected under any bare "text occurs on the
page" reading: **passes** → filed bypass. Expected under a row-act binding: caught.
Guard: **G5** (the cited line must carry the row's scope key; 599 and 160 do not).
A scoping-section rule would also exclude both quotes (160 is under "Best practices",
599 under "Troubleshoot memory issues"), but that rule is not in the measured matrix;
G5 already decides these two. Keep the row-act sentence: the Action must state what
the author does with the scope key, not any true page text.

### F3 — nav and footer text (S103:2–3, S105:365)

- F3: `Discover available pages so the instructions load before exploring further.`
  cited at S103:3, the documentation-index blockquote:
  `> Use this file to discover all available pages before exploring further.`
  v2: 4 of 6 words on line 3, PASS. The page has `instructions` and `load` elsewhere,
  so the page-bag check passes too.
- F3b: `Create and manage agent customizations to configure instructions.` cited at
  S105:365, a footer link label under `## Related resources`:
  `* [Create and manage agent customizations](/docs/agent-customization/overview.md)`.
  v2: 4 of 6 on line 365, PASS.

Expected under a page-bag reading: **passes** → filed bypass. Expected under a
markup-class rule: caught. Guard: **G2** (exclude the leading `>` index block, lines
under `Related resources` / `Further reading` / `Related` / `Sitemap` /
`Documentation Index`, and link-dense lines with ≥3 Markdown links) plus **G5**
(neither line carries the row's key).

### F4 — event listed but not wired to rule files (S103:593/438/427)

Cell: `Write the SessionStart hook so rule files load after each file edit.` Cited at
S103:593 (`… such as before every commit or after each file edit, write it as a
[hook] … Hooks execute as shell commands at fixed lifecycle events …`). `SessionStart`
occurs on the page only at line 438, where a `SessionStart` hook that prints
`AGENTS.md` is told to be **removed** (it duplicates context); line 427 is an
`InstructionsLoaded` table for `AGENTS.md`; line 599 logs which rules files load. No
line wires `SessionStart` to loading rule files, and the page's rule-loading statement
is line 209 (path-scoped rules load on matching-file access, not at SessionStart).
v2 passes on line 593's `write`, `hook`, `file`, `edit` (4 of 8); full predicate
`--fetch` exit 0.

Expected catch: **yes, under any A2 that checks the event claim itself** (this is the
class the frozen wording names). Expected under a page-bag or half-line check:
**survives** → filed bypass. Guard: **G4** (an event token must be wired on one line
to a rule/instruction-file noun and a load/attach verb) + **G6** (the purpose verb
after "to" must agree) + **G7**.

### F5 — event wired, but for the wrong act (S103:599)

Cell: `Use the InstructionsLoaded hook to load rule files in subdirectories before they
fire.` The page genuinely says the `InstructionsLoaded` hook **logs** which rules files
are loaded (599) and that it **fires** for `CLAUDE.md`/`AGENTS.md` (427). A wiring-only
check passes: event + rule files + load verb co-occur at 599 (`G4 = True`). The false
part is the direction: log ≠ load. v2 passes 5 of 7 on line 599; full predicate would
pass on the same live page.

Expected under a wiring-only A2: **passes** → filed bypass. Expected under a
predicate-argument check: caught. Guard: **G6** (page purpose verb `log`, cell purpose
verb `load` → reject) and **G7** (all seven cell words occur on no single line:
`fire` only at 427, the rest at 599).

### F6 — compound purpose with the key grafted on (S106:60) — the scope gap

Cell: `Create instructions files with glob syntax and organize the copies in the
project directory.` Cited at S106:60, the real Copilot CLI action line, which contains
`create`, `instructions`, `files`, `glob`, `syntax` (5 of 9, exactly need) and the key
`applyTo`. The first clause is true; the second ("organize the copies in the project
directory") is invented: S106:30 says duplicate copies are **removed** when files are
combined, and S106:56 says create subdirectories of `.github/instructions` to organize
files — not copy them into a project directory. v2 passes; `--fetch` exit 0.

Expected under the frozen A2 scope ("every **load/event** claim"): **outside the arm by
construction** — the cell makes no load/event claim → filed bypass of the frozen
contract, not just of an implementation. Guard: **G9** (every clause must be supported
in the cited line's section; the second clause's `copies` occurs only at S106:30,
outside the "Creating path-specific custom instructions" section, so the compound
claim fails), or an explicit scope extension to *every* Action claim with the entry's
limit recorded. G5 alone passes F6 (the key is on the cited line and the first clause
supplies the overlap); this is why A2 cannot be key-binding only.

### W6-sib — the wave's published W6 cell (S103:209)

Cell reproduced independently by `MutWorldW5W6.md`:
`Create the rule file in the project and add frontmatter so it loads only for the
matching files.` cited at S103:209 (the *unconditional-load* sentence). v2 passes
6 of 8; `--fetch` exit 0 (their report). **G5 alone passes it** (line 209 carries
`paths` and 6 shared words), which is the sharpest implementation warning in this
report: **an A2 implemented only as "cited line carries the canonical key" does not
reject W6.** G7 rejects it (no single line holds `create`, `frontmatter`, `loads`,
`project`, …). If the v3 self-test's W6 fixture is this cell, A2 must include the
claim-span conjunct or W6 will survive the arm.

## 6. Measured guard matrix and recommended A2 implementation

Prototype guards (implemented in the probe; all measured on the committed pages):

- **G2 body**: cited line is body prose — not the leading `>` index block, not under a
  Related/Further-reading/Sitemap heading, not link-dense (≥3 links).
- **G4 wire**: for an event token in the cell, one page line holds the event token, a
  rule/instruction-file noun, and a load/attach/fire/log/read verb.
- **G5 key+overlap**: the cited line carries the row's canonical scope key at an
  identifier boundary (raw bytes, backticks included) **and** shares ≥ the v2 need.
- **G6 verb direction**: for an event token, the first verb after "to" within 80 chars
  after the event in the cell equals a verb attached to that event on a page line.
- **G7 claim-span**: if the cell contains a raw load/attach/fire/read or event token,
  every content word of the cell occurs on one page line (raw tokenizer).
- **G9 clause-span**: every clause (split on `;`, `.`, ` and `) with ≥2 content words
  has all its content words present in the cited line's section (nearest heading
  through the next heading of the same or higher level), plural/`-ed`/`-ing` tolerant.

| Case | G2 | G4 | G5 | G6 | G7 | G9 | rejected by |
|---|---|---|---|---|---|---|---|
| P-S103 | body | – | True | – | True | True | — (must pass) |
| P-S105 | body | – | True | – | True | True | — |
| P-S106 | body | – | True | – | True | True | — |
| P-S108 | body | – | True | – | True | True | — |
| F1 | body | – | **False** | – | **False** | **False** | G5/G7/G9 |
| F2a | body | True | **False** | True | True | True | G5 |
| F2a-plain | body | True | **False** | True | True | True | G5 |
| F2b | body | – | **False** | – | True | True | G5 |
| F3 | **nav** | – | **False** | – | **False** | True | G2/G5/G7 |
| F3b | **footer** | – | **False** | – | True | **False** | G2/G5/G9 |
| F4 | body | **False** | **False** | **False** | **False** | **False** | G4/G5/G6/G7/G9 |
| F5 | body | True | **False** | **False** | **False** | **False** | G6/G5/G7/G9 |
| F6 | body | – | True | – | True | **False** | G9 |
| W6-sib | body | – | True | – | **False** | True | G7 |

("–": vacuous, no event token.) **No single guard rejects every mutant**: G5 alone
misses F6 and W6-sib; G7 alone misses F2a/F2b/F3b/F6; G9 alone misses F2a/F2b/F3 and
W6-sib. The measured minimum that rejects the four requested classes *and* the
published W6 while keeping all four positives is **G5 ∧ G7**; adding **G9** covers the
F6 compound-purpose hole; **G4/G6** are needed for a semantically correct event
rejection (F5) and for the reject line to say *why*, not merely *that*.

Recommended A2 implementation sentence (for the counter docstring, label and the
self-test arm; the L1 decides whether this is a clarification or an erratum against
the frozen plan wording):

> A2 semantic action — the Action cell's claims are supported by the committed
> snapshot: the cited line is body prose (not the leading index block, a Related/
> Further-reading/Sitemap list, or a link-dense line) and carries the row's canonical
> scope key; the cell shares at least half its content words with that line; every
> clause of the cell is supported inside that line's section; and if the cell names a
> load or lifecycle event (raw tokenizer, backticks not stripped), one page line wires
> that event to a rule/instruction file with the same purpose verb.

Suggested reject lines (matching the entry's existing W6 wording style):

- F1/F3/F3b/F6: `reject <client>: A2 invented action claim is not supported by the cited committed section`
- F2a/F2b: `reject <client>: A2 the Action is page text but not the row's scoped act (key <K> absent from the cited line)`
- F4: `reject <client>: A2 event claim SessionStart is not wired to a rule file on the snapshot`
- F5: `reject <client>: A2 event claim uses verb 'load' but the snapshot wires 'log'`

Arm-killer fixtures for `--self-test` (content-derived; each fails only if A2 is
deleted/inverted; none touches A1/A3/A4):

1. **Primary A2 killer — F1 cell** on the VS Code row (`Create a settings profile and
   sync it so the instructions load from the project directory. (S105 :287)`). Passes
   v2's action conjunct; fails G5/G7/G9. If A2 is removed, the world backs 4 of 4 and
   the arm's expected reject line is missing.
2. **G7 sub-conjunct killer — W6-sib** (the wave's W6 cell at S103:209). Passes G5, so
   it kills an A2 that is key-binding only; fails G7.
3. **G5 sub-conjunct killer — F2a** (the S103:599 quote). Passes G7, so it kills an A2
   that is claim-span only; fails G5.
4. **Guard-limit fixture (not a claim) — F6**. Survives G5/G7; fails G9. If the L1
   adopts only G5∧G7, F6 must be recorded as a declared A2 limit in the entry, not
   claimed as rejected.

## 7. What this means for the frozen claim / entry wording

- W6 as realized by the wave's own reproduction (`MutWorldW5W6.md`, cell at S103:209)
  passes a key-binding-only A2. The plan's sentence "Rejects W6 (invented action)" is
  only true for an A2 that includes the claim-span conjunct (G7). This should be
  checked in the integrated self-test, not assumed from the arm label.
- A2 must be a conjunction of structural checks, not a page-bag word list. "Supported
  by text on the committed snapshot page" without section/claim/key binding is false
  support (F1, F6) and makes quoted (F2) and nav/footer (F3) text automatically valid.
- The tokenizer matters: `content_words` deletes backticked spans, so event names and
  keys written in backticks vanish from the word set. Claim detection and key binding
  must read raw bytes; only the overlap threshold should use the counter's tokenizer.
- The entry's "Not held" bullet is correct and should be kept, with the F6 class named:
  the arm constrains *load/event* claims; a non-load purpose clause (placement,
  copying, ordering) grafted onto a key-bearing line is outside the frozen scope. The
  counter must not be reported as semantic proof of the Action cell.

## 8. What I could not verify (honesty ledger)

- **No v3 draft source was published to the wave directory at attack time**
  (`.ufo/waves/round-61/wave/` had 41 reports, none from `ExecCounterV3`; no v3 source
  under `/fast/scratch/hyaku/kotoba-r61`). All measurements are against the committed
  v2 counter that the draft must start from ("change the minimum"), and the guard
  matrix is a prototype on the committed pages, not the draft's code. If the draft
  changes the tokenizer, thresholds, or citation handling, re-run the probe.
- `--fetch` was run for pristine, F1, F4 and F6 (all exit 0, 4 of 4 live). F2a and F3
  were not run with `--fetch`; the live path does not read the Action cell, so the
  offline `backed 4 of 4` is the A2-relevant measurement, but the full-predicate exit
  for those two is unmeasured here.
- The live pages are third-party bytes fetched today; the `--fetch` runs prove the
  pages still carry the quotes and key sites at run time, not at snapshot time.
- The guards are lexical/structural heuristics, not entailment. An adversary who reads
  them can still graft a true first clause onto a misleading second clause (G9 raises
  the cost; it does not close the class), and any true verbatim sentence from a
  key-bearing scoping line remains indistinguishable from a legitimate Action without
  an entailment model. P-S108 is exactly such a legitimate case.

## Appendix — probe transcript (excerpt; full output in the scratch rig)

```
$ python3 -B probe_a2.py
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
date-run 2026-10-23T19:15:43Z

== P-S103 S103 line 194 | cited class: body
 W(11) need 6: apply files frontmatter matching patterns rules scope specific specified using yaml
 v2 shared 10 -> PASS | D1raw True missing []
 D2 all-words lines [] | D2raw [] | best (194, 10)
 claims [] | G4 wire True | G5 key+need True | G6 verb True | G7 claim-span True | G9 clause-span True | first scope

== F1-S105 S105 line 287 | cited class: body
 W(8) need 4: create directory instructions load profile project settings sync
 v2 shared 4 -> PASS | D1raw True missing []
 D2 all-words lines [] | D2raw [] | best (48, 4)
 claims ['load'] | G4 wire True | G5 key+need False | G6 verb True | G7 claim-span False | G9 clause-span False | first create

== F4-S103 S103 line 593 | cited class: body
 W(8) need 4: edit file files hook load rule sessionstart write
 v2 shared 4 -> PASS | D1raw True missing []
 D2 all-words lines [] | D2raw [] | best (209, 5)
 claims ['load', 'sessionstart'] | G4 wire False | G5 key+need False | G6 verb False | G7 claim-span False | G9 clause-span False | first write

== F6-S106 S106 line 60 | cited class: body
 W(9) need 5: copies create directory files glob instructions organize project syntax
 v2 shared 5 -> PASS | D1raw True missing []
 D2 all-words lines [] | D2raw [] | best (60, 5)
 claims [] | G4 wire True | G5 key+need True | G6 verb True | G7 claim-span True | G9 clause-span False | first create

== W6-sib-S103 S103 line 209 | cited class: body
 W(8) need 4: create file files frontmatter loads matching project rule
 v2 shared 6 -> PASS | D1raw True missing []
 D2 all-words lines [] | D2raw [] | best (209, 6)
 claims ['loads'] | G4 wire True | G5 key+need True | G6 verb True | G7 claim-span False | G9 clause-span True | first create
```

---

Installs: none (no tool installed or upgraded; pacman not touched).
Blockers: none.
Attacked arm A2 (semantic action) with ten invented-action cells through the committed
counter's own judge, five of them end-to-end, filed the bypasses and measured a guard
matrix; produced the mutation probe record with before/after hashes and exact-byte
restoration.
