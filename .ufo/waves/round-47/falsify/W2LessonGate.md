verdict: PARTIAL — the round-47 `## Gate` table's mechanical claims all hold (URL, access time, ≤25-word quote, record file exists, every quote verbatim in its seat report, and "no existing row's status/recheck/used-by changed" is exactly true), but the Gate's C2-provenance sentence is false about `verifiers/verify_skill_checklist.py`, S015's `mined` status is unsupported by any citation, and the two defects the S003 seat named the round-47 Gate as the designated venue for are absent from it.

Scope of this lane: `corpus/lessons/round-47.md` § Gate at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`
(BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`). Leaf member — no subagents dispatched.
All commands below were run by me; the production tree was never written except this report and
`.ufo/waves/round-47/falsify/W2LessonGate.checks.txt`.

---

## What I attacked

1. Every row of the Gate table (S012–S015): URL, access time, quote length, quote location, record
   file existence, and quote↔seat-report agreement.
2. The statement "All four rows are new; no existing row's `status`, `recheck` or `used-by` changed
   (old→new: none)" against `git diff c61a973 -- corpus/SOURCES.md` (row-by-row field comparison).
3. The **Sourced claim** paragraph (C2 rests on S003 + S012; C1 rests on S015).
4. The **Existing rows re-opened** paragraph (S001–S008) against the five wave-1 seat records.
5. The **Rejected candidate** paragraph.
6. Mutation tests: can any instrument in the repo detect a broken Gate pointer / overlong quote /
   fabricated quote / false `mined` status?

---

## Findings

### F1 — MEDIUM — the Gate's C2-provenance sentence is false about the checklist's detail line

`corpus/lessons/round-47.md:42-43` (at 7ad7fad):

> "…and on S012, which the check's **detail line** and `SKILL.md` § Portability floor cite as the
> stricter vendor packager rule."

Only the second half is true.

```
$ grep -c "S012" verifiers/verify_skill_checklist.py
0
$ sed -n '97,104p' verifiers/verify_skill_checklist.py
trigger.no_xml_tag              the parsed ``name`` and ``description``
    values carry no XML markup: …  Source: S003,
    an Anthropic rule the open spec (S001/S002) lacks.  ``evaluated`` =
    non-empty fields scanned (1-2).
$ sed -n '208,212p' verifiers/verify_skill_checklist.py
  - the XML-tag check reads S003's words, not Anthropic's packager:
    ``quick_validate.py`` (used by ``package_skill.py``) rejects any ``<``
    or ``>``, so ``a -> b`` passes here and fails packaging; …
$ sed -n '1305,1309p' verifiers/verify_skill_checklist.py
    limit = ("S003 Anthropic rule, absent from the open spec (S001); "
             "Anthropic's packager bans any '<'/'>' and is stricter")
```

The checklist names **S003 / S001 / S002**; the string `S012` occurs **zero** times in
`verifiers/verify_skill_checklist.py` (exit 1, 0 matches). The code even says explicitly that it
implements S003's rule and *not* the packager's. `SKILL.md:151` does cite S012
("Anthropic's reference packager (S012) is stricter and refuses any `<`/`>`") — that part holds.

Impact: the sentence that carries C2's grounding misattributes the citation to an instrument that
does not make it. It is the same class the round itself logged as M22 (a pointer that does not
resolve), applied to a claim sentence rather than a path. `corpus/knowledge/instruction-surface-census-round13.md`
is unaffected. Repro: the two `grep`/`sed` commands above; `grep -c S012 verifiers/verify_skill_checklist.py` → `0`.

### F2 — MEDIUM — S015's `status = mined` is unsupported; its `used-by` file never cites S015

`corpus/SOURCES.md:28` (at 7ad7fad): `… | mined | 2026-10-21 | on-release | corpus/knowledge/instruction-surface-census-round13.md |`

Contract `SOURCES-CONTRACT-v1.md` defines `mined` as "**cited by ≥1 path in `used-by`**".

```
$ grep -c "S015" corpus/knowledge/instruction-surface-census-round13.md
0
$ grep -rn "S015" --exclude-dir=.git --exclude-dir=.ufo . | grep -v "SOURCES.md\|lessons/round-47.md\|LOG.md\|corpus/README.md"
(no output)
```

The cited file carries the *substance* of the row (`instruction-surface-census-round13.md:212-218`:
"**Substrate:** npm `opencode-ai` 1.19.3 … sha256 `179ca421d61e…` … Frozen copy and `strings -n 4`
dump: `/fast/scratch/kotoba-r47/shared/` (`SHA256SUMS`)") but never the row id. The `mined` status is
therefore asserted, not earned, and `corpus/lessons/round-47.md:44` ("C1 rests on S015") rests on a
row whose citation link does not close.

No instrument catches it — the only machine check is path *existence*
(`scripts/sources-census.sh:567`: `if [ ! -e "$dir/$path" ]`), and the contract's own census tail
does the same. Mutation proof (scratch clone, commit `45c998e`):

```
$ python3 - <<'EOF'   # corpus/SOURCES.md: S015 used-by -> corpus/README.md (a file that does not cite S015)
…EOF
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
      --root /fast/scratch/kotoba-r47/w2/W2LessonGate /fast/scratch/kotoba-r47/w2/W2LessonGate/kotoba-shokunin
kotoba-shokunin	ok	…/corpus/SOURCES.md
census exit=0
```

Fix is one token: put `S015` into the census's § B′ *Substrate* sentence (or into the row's `used-by`
as `corpus/lessons/round-47.md`, which does cite the row id).

### F3 — MEDIUM — the S003 seat's two recorded defects are absent from the Gate that was named as their venue

`.ufo/waves/round-47/build/SrcS003.md` reports two calibration defects and routes them explicitly:

> "D1 — the round-46 evidence pair is field-inverted … **Lessons are append-only, so the correction
> belongs in the round-47 lesson's `## Gate`, not as an edit.**"
> "D2 — `teaches` closing clause can be read as false … Rule 2 forbids in-place `teaches` edits:
> either accept the reading and **record the clarification in the round-47 lesson**, or open a
> `supersedes S003 —` row …"

`corpus/lessons/round-47.md:40-44` records neither. D2 is still live in the registry:

```
$ sed -n '16p' corpus/SOURCES.md
| S003 | … | The description cannot contain XML tags, must be third person, and states what the
  skill does and when; body under 500 lines; an Anthropic-only rule the open spec lacks | mined | …
$ grep -n "500 lines" /tmp/spec.md        # agentskills.io/specification.md, re-fetched 2026-10-21
237:Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files.
$ grep -c -i xml /tmp/spec.md        # 0   (exit 1)
$ grep -c -i "third person" /tmp/spec.md # 0 (exit 1)
```

The open spec **does** carry the 500-line rule; only the XML/third-person clauses are Anthropic-only,
and the clause's position after "body under 500 lines" makes it read as denying the spec a rule it
has. D1 (round-46 `fetch-log.json` `/rows/2` `quote_location` and `corpus/lessons/round-46.md:65`
invert md:155/md:162 — md:155 is the *name* bullet, md:162 the *description* bullet) is likewise
uncorrected, and the round-47 Gate repeats the same round-46 anchor text.

Convention break: `corpus/lessons/round-46.md` § Gate *does* log this class ("Timestamp defect:
S001–S008 `accessed_utc` read `18:40Z` while … the 18:40 values are local time (UTC−3) labelled
`Z`") and even logs pre-landing corrections ("S010's source cell first read …; the L1 re-ran both …
and corrected the cell before commit"). The round-47 Gate records only S001's anchor defect and drops
the rest.

### F4 — LOW/MEDIUM — a conditional `used-by` update whose trigger fired was neither applied nor logged

`SrcS003.md` ("Recommended row changes"): `used-by` `SKILL.md` → `SKILL.md, verifiers/verify_skill_checklist.py`
— "**conditional** — apply only when C2's description XML-tag check actually lands in that file; log
old→new in `corpus/lessons/round-47.md` per rule 2".

The condition is met by this round's own C2 work:

```
$ git show 7ad7fad:verifiers/verify_skill_checklist.py | grep -n "S003"
102:    NOT exempt (frontmatter is plain text to every client).  Source: S003,
210:  - the XML-tag check reads S003's words, not Anthropic's packager:
1307:    limit = ("S003 Anthropic rule, absent from the open spec (S001); "
```

`corpus/SOURCES.md:16` still reads `used-by = SKILL.md`, and `corpus/lessons/round-47.md:30` says
"no existing row's `status`, `recheck` or `used-by` changed (old→new: none)". The seat itself flagged
the literal-contract caveat ("`used-by` holds 'knowledge entries or lessons'"; a verifier is neither —
but `SKILL.md`, already listed, is neither either, so the registry's own reading is the broader one).
Either the addition should have been made and logged old→new, or the Gate should say why it was not.

### F5 — LOW — S015's Gate row has no quote at all (contract rule 1, form)

`corpus/lessons/round-47.md:38`: the "≤25-word quote (location)" cell holds
`` `bin/omp-18.12.5` `fdbc8136…`, `bin/opencode-1.19.3` `179ca421…` (SHA256SUMS lines) `` — hash
fragments, not a quoted sentence, and it grounds only the identity half of the row's `teaches`
("the opencode path moved channel (2.0.26 → npm 1.19.3) while the version string went down").
The seat record had a quotable line — `` `omp --version` → `omp/18.12.5` `` — that would have
discharged rule 1 and grounded the version clause. S012–S014 are fine (8 / 20 / 17 words, all ≤25).

### F6 — LOW — three of the four seat records headline a *different* row id than the one they landed as

```
$ head -1 .ufo/waves/round-47/build/SrcNewSkillCreator.md
verdict: ADMIT as S012 (…)
$ head -1 .ufo/waves/round-47/build/SrcNewCodexSkills.md
verdict: ADMIT S012 — OpenAI "Build skills" …                       ← landed as S013
$ head -1 .ufo/waves/round-47/build/SrcNewAnthropicEng.md
verdict: ADMIT S012 — the source exists and says it …               ← landed as S014
$ head -1 .ufo/waves/round-47/build/SrcOwnWorkSubstrate.md
verdict: two tier-A own-work SOURCES rows drafted and shape-checked (S012 substrate snapshot,
         S013 C2 frontmatter gate), both queued                     ← substrate landed as S015; the
                                                                          S013 draft landed nowhere
```

The Gate's row→record mapping is correct and each record does contain its quote, but the records'
own verdict lines contradict the mapping, and the S015 pointer
(`.ufo/waves/round-47/build/SrcOwnWorkSubstrate.md`) does not isolate the S015 draft — it also holds
a dropped draft whose provisional id now belongs to a different source. The Anthropic seat flagged
the collision itself ("the `S012` id is contested by two sibling drafts and must be assigned at
integration") and the integrator resolved it, but no note of the id remapping was written back.

### F7 — LOW — the elided record range implies two files that do not exist

`corpus/lessons/round-47.md:50`: "S002, S003, S004, S005, S008 still hold (`SrcS002.md` …
`SrcS008.md`). S006, S007 not re-opened."

```
$ for f in SrcS001 SrcS002 SrcS003 SrcS004 SrcS005 SrcS006 SrcS007 SrcS008; do
    [ -f ".ufo/waves/round-47/build/$f.md" ] && echo "EXISTS $f" || echo "MISSING $f"; done
EXISTS SrcS001 / SrcS002 / SrcS003 / SrcS004 / SrcS005
MISSING SrcS006
MISSING SrcS007
EXISTS SrcS008
```

The next sentence states S006/S007 were not re-opened, so the text is not false — but the elision
reads as seven records, and two of the five rows the sentence lists are not in it. Same class as
M22 (a pointer that does not resolve); the fix is to name the five files.

### F8 — LOW — the S014 seat's byte hash is not reproducible; the page bytes moved under the seat

`.ufo/waves/round-47/build/SrcNewAnthropicEng.md:1` records "HTTP 200, 216,618 bytes, sha256
`c2a4f973…`" and line 63 "byte-identical on refetch".

```
$ curl -sS -L --compressed -o anthropic-eng.html https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills
$ sha256sum anthropic-eng.html
7dfd6f15b8f6e7e30352d569203a8d0c285d4073c3a5793434396551f164e892   (216,541 B)
```

Different bytes from the seat's fetch 90 minutes earlier — the Anthropic page is not byte-stable.
Nothing false landed (the S014 row in `corpus/SOURCES.md:27` cites no hash), but a future byte-level
recheck will false-alarm, which is exactly the condition `SrcS004.md:47` warns about ("a round-47
freshness gate that tests raw-byte equality for unversioned live pages will false-positive") and
`SrcS002.md` observed in the wild (today's `.md` sha `79489bd2…` vs the round-46 hash; 4 renderer-only
hunks). Neither caveat reached the Gate.

### F9 — MEDIUM (gate coverage) — nothing in the repo checks the Gate table at all

Mutation tests in the canonical-layout scratch clone
`/fast/scratch/kotoba-r47/w2/W2LessonGate/kotoba-shokunin` (detached at `7ad7fad`, mutations
committed there only, then reset):

| mutation | commit | result |
|---|---|---|
| Gate record pointer → `.ufo/waves/round-47/build/SrcNewSkillCreatorGONE.md` (file does not exist) | `b02b0b9` | `verify_corpus_integrity.py` **exit 0** ("9/9 checks pass"); `verify_corpus_independent.py` **exit 0** |
| Gate quote padded to 40+ words (rule-1 ceiling) | `9edd054` | corpus integrity **exit 0** (9/9); corpus independent **exit 0** |
| Gate quote replaced by a sentence that appears in no seat report | `326d5a2` | corpus integrity **exit 0**; corpus independent **exit 0** |
| S015 `used-by` → a file that does not cite S015 | `45c998e` | fleet `sources-census.sh validate` **exit 0** |

```
$ grep -rn "## Gate" verifiers/*.py
(no output)
```

Contract rule 1 ("The round lesson's `## Gate` records, for every new row, the URL, the access
date, and a ≤25-word quote with its location grounding `teaches`") is enforced by nothing. The
Gate's own record pointers, quote lengths and quote fidelity are human-checked only — and the round
logged that exact class as M22 with `captured-by: none`.

---

## What HOLDS (claims that survived my attack)

* **"All four rows are new; no existing row's `status`, `recheck` or `used-by` changed (old→new: none)"
  — `corpus/lessons/round-47.md:30`.** True, exactly. Row-by-row field comparison of
  `git show c61a973:corpus/SOURCES.md` vs `git show 7ad7fad:corpus/SOURCES.md`:
  S001–S011 are **byte-identical row cells** (all 11 columns), no row removed, no row duplicated;
  only S012–S015 added. The diff also touches the header paragraph (`corpus/SOURCES.md:4-8`), the
  § Paths block and the search log — no status/recheck/used-by cell of any existing row.
* **All four record files exist** (`.ufo/waves/round-47/build/SrcNewSkillCreator.md`,
  `SrcNewCodexSkills.md`, `SrcNewAnthropicEng.md`, `SrcOwnWorkSubstrate.md`).
* **All three quoted sentences are verbatim in their seat records** (substring match, Python) and the
  access timestamps appear in the records: S012 `2026-10-21T15:55:51Z`, S013 `2026-10-21T15:54:43Z`,
  S014 `2026-10-21T15:57:06Z`. Quote lengths 8 / 20 / 17 words — all ≤25.
* **Every quote independently re-derived from the live sources today** (network re-fetch, no lane
  cache):
  * S012 — `https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py`
    → sha256 `67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365` (matches the Gate's
    `67cf5703…` and the seat's full hash), 3,972 B; line 81 is exactly
    `return False, "Description cannot contain angle brackets (< or >)"`. The tree entry
    `skills/skill-creator/scripts/quick_validate.py` is 3,972 B in the pinned tree — consistent.
  * S013 — `https://learn.chatgpt.com/docs/build-skills.md` → sha256 `ed6e324f…9d5` (matches the
    seat), the quote at md:38-39, heading `## How ChatGPT and Codex use skills` at md:91, and the
    `teaches` clauses also present (md:40 "Codex shortens skill descriptions first";
    md:207/218 `allow_implicit_invocation`). Note the quote alone grounds only the 2%/8,000 clause.
  * S014 — `https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills`
    → after stripping inline markup the quote occurs **exactly once**, in § The anatomy of a skill
    (`id="the-anatomy-of-a-skill"`); `article:published_time` 2025-10-16, `article:modified_time`
    2026-10-18T21:26:58Z — both as the row states.
  * S003 (C2's grounding) — `https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md`
    → sha256 `727f3fa1168eb1c33ce6a3cbfc94a02ef1dfd647388f6ca9daf7cb6294762f42`, **identical** to the
    round-46 fetch record `.ufo/round-46/evidence/w2/sources/fetch-log.json` `/rows/2` and to the
    Gate's `727f3fa1…` — so "byte-identical to the round-46 fetch" is independently confirmed;
    "Cannot contain XML tags" at md:155 (name) and md:162 (description).
  * S001 anchor defect — `https://agentskills.io/specification.md`: headings are
    `## Directory structure`, `## SKILL.md format`, `### Frontmatter`, `#### name field`,
    `#### description field`, … `## Progressive disclosure`; **no "Skill metadata table" heading
    exists**, so the Gate's recorded defect is TRUE (and `## Progressive disclosure` does exist).
* **S015's substance re-runs clean**: `cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS`
  → exit 0, 4/4 OK (bin/omp-18.12.5 `fdbc8136…`, bin/opencode-1.19.3 `179ca421…`, both `.strings`).
  The S015 anchor's two "equal" claims also hold today:
  `sha256sum /home/vgpnk/.local/bin/omp` → `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e`
  (equals the snapshot), and
  `sha256sum /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` →
  `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9` (equals the snapshot).
* **C1's pin identity**: `verifiers/baseline.json` `omp_binary_sha256` = `fdbc8136…` and
  `opencode_binary_sha256` = `179ca421…` — both equal the frozen snapshot bytes, so
  "`C1 rests on S015` (the pinned bytes are the snapshot bytes)" is factually right even though the
  row's `mined` citation is not (F2).
* **Rejected candidate is exactly as described**: `spec/agent-skills-spec.md` at the pinned commit is
  **3 lines / 87 B**, sha256 `ff22f2be775f4b757c9a7a2df0421de4c94021d34d9382cea5dd567ff0cdad2c`
  (matches the seat), content = a heading + "The spec is now located at
  <https://agentskills.io/specification>" — no rule content. My first fetch attempt against
  `skills/skill-creator/spec/agent-skills-spec.md` returned 404; the file lives at the repo root
  `spec/` — the Gate's path wording ("anthropics/skills `spec/agent-skills-spec.md`") is the correct one.
* **Gate battery green at 7ad7fad** (scratch clone, clean tree): `verify_corpus_integrity.py` exit 0
  ("9/9 checks pass"), `verify_corpus_independent.py` exit 0, `verify_skill_checklist.py --self-test`
  exit 0 ("0 failure(s) over 1845 assertions"), `check_substrate_pins.py` exit 0 ("OK 3/3 pins hold"),
  fleet `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` exit 0.
  Contract census on the landed `corpus/SOURCES.md`: 15 rows, 0 malformed (NF=13), A=14 C=1,
  status mined=6 queued=8 rejected=1, no duplicate ids, no enum violations, no missing used-by paths.

---

## Residual risk / verification gaps

* The S014 and S002 byte-hash drift (F8) means any *future* byte-equality freshness gate for these
  two pages will false-positive; the lesson records no such caveat for them.
* The Gate table's record pointers point into `.ufo/waves/round-47/build/`, which is **untracked**
  (`git status` in the production tree shows `?? .ufo/waves/`). Nothing in the committed history
  carries the seat records; the Gate's evidence chain exists only in the working tree.
* `corpus/SOURCES.md:25` (S012) has `used-by = SKILL.md` — justified: `SKILL.md:151` does cite
  `(S012)`. `corpus/SOURCES.md:26-27` (S013/S014) are `queued` with `used-by = —`, consistent with
  the contract's "queued (opened, worth mining)".

## What I did NOT check

* I did **not** execute `~/.local/bin/opencode` (contract) and did not run the npx wrapper; the
  opencode identity rests on sha256 + the strings dump only.
* I did not run `verifiers/verify_surfaces.py`, `verify_harness_claims.py`, `verify_harness_independent.py`
  or `check_assertion_floors.py` — C1's surface re-derivation is another lane's scope; I only checked
  that the *bytes* the C1 pins point at are the snapshot bytes.
* I did not audit the substance of C1's opencode class ledger beyond confirming the census file
  exists, is indexed by the lesson (`:56-58`) and contains zero `S015` citations.
* I did not re-open S006/S007 (not claimed as re-opened) and did not re-derive the round-46 fetch
  record's other rows (S001–S011 hashes) beyond S001/S003, which the Gate makes load-bearing.
* I did not review `corpus/QUALITY.md` Q19, the fault harness, or the C3 errata row except to confirm
  that the C3 errata mechanism (`GOVERNANCE_ERRATA` in `verifiers/verify_skill_checklist.py:377-378`)
  is a LOG.md-line-scoped exemption, not a general corpus errata registry that could have carried
  the S003 corrections (F3) elsewhere.
* I did not verify the live truth of the S013 row's `recheck`/cadence arithmetic beyond the quote
  re-derivation, and I did not check the round-47 lesson's § Mistakes rows (M20–M22), which another
  wave-2 lane owns.

## Artifacts

* `.ufo/waves/round-47/falsify/W2LessonGate.md` — this report.
* `.ufo/waves/round-47/falsify/W2LessonGate.checks.txt` — command/exit-code log backing every claim
  above.

Tooling: no installs, no upgrades, no pacman transaction. Tools used: `bash`, `curl` (read-only
public fetches), `python3` (stdlib only), `git` (read-only in the production tree; clone/commit only
in the scratch clone), `sha256sum`, `awk`, `grep`, `sed`, `wc`, `diff`.
