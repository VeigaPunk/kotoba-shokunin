Result: DONE — 31 single-rule mutants of the frozen C1 counter were built and each was run through the counter's own `--self-test` plus two purpose-built sandbox worlds plus six discriminating probe worlds; 21 mutants survive `--self-test`, three of those survive every detector built here, and the lane counter (revised to v2 by a sibling seat after my target was frozen) closes five of the survivors.

# MutC1Counter — mutation testing of the frozen round-55 C1 counter

## 1. Scope and what was tested

Target: `verifiers/check_explicit_invocation.py`, the round-55 C1 counter **as frozen at the plan commit**
`a10240c0940f770a5f2a5f32a7e3c363dd5d40c0` ("round-55: plan, frozen C1/C2 counters and §9 control receipts").
sha256 of the frozen file: `4fc6e01ad576531c95265c7dcd2440b0b2bda0cd3520a0b317c46cd78b3ff5e5`
(unchanged in the sandbox at the end of this seat's work: same digest).

The **lane file was never edited**. `git status --porcelain verifiers/check_explicit_invocation.py`
in `/home/vgpnk/Projects/shokunin/kotoba-shokunin` is empty for this seat's edits. All mutation
work happened in the sandbox clone
`/fast/scratch/hyaku/kotoba-r55/MutC1Counter` (cloned from the lane, checked out at
`a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`).

**Drift notice.** After this seat's target was frozen, a sibling seat replaced the counter with
"erratum v1 → v2 (strictly stricter)" at lane commit `b04a9005c494d14e4667b201b723857005effb0d`
(2026-10-22 20:22:16 -0300, "round-55: erratum 1 — C1 counter v2 (strictly stricter) and shortcut
receipts, before any C1 content"), and the round-55 C1 content landed at `9615579`. The lane file
now hashes `e13eb88d8cfc32fc8975968280aa5a0055416fb07e43facbf1f585d951787e5a`. Section 6 repeats
the whole mutation set against that v2 source so the findings stay usable.

## 2. Method

Three independent detectors, all run against the same byte-level mutant set:

1. **The counter's own `--self-test`** — the frozen detector the counter ships
   (`self-test: 0 failure(s) over 29 assertions`, exit 0). Baseline first: the pristine counter's
   self-test passes, so a mutant that also exits 0 is a genuine survivor and not a broken baseline.
2. **Two required sandbox worlds** (section 3) — the assignment's own scenarios.
3. **Six discriminating probe worlds** (section 4) — small fixtures built so that one rule
   each is the only thing that can change a verdict.

Every mutant is a single textual substitution applied to a **copy** of the counter; the pristine
file is never edited. Mutants live in `<sandbox>/mutants/` (31 files) and `<sandbox>/mutants_v2/`
(21 files). Harness and evidence: `work/mutate.py`, `work/mutate_v2.py`, `work/world_matrix.py`,
`work/probe_matrix.py`, `work/make_worlds.py`, `work/make_probes.py`; results in
`work/mutants.json`, `work/world_matrix.json`, `work/probe_matrix.json`, `work/v2_mutants.json`.

## 3. The two required sandbox worlds (both behave exactly as specified)

### World A — `work/worlds/worldA_base_row_id` — a real quote under a row id that exists at BASE

Four clients, all fully sourced with real quotes from pages fetched on 2026-10-22, but the **Codex
row id is `S022`, which is already a row of `corpus/SOURCES.md` at BASE** (`f0e5de82`). Everything
else about that client is valid: tier A, kind docs, status `mined`, opened `2026-10-22`, `used-by`
the round-55 entry, URL `learn.chatgpt.com` (a pinned Codex host), quote recorded verbatim in the
round-55 `## Gate` table.

Pristine verdict (`--root work/worlds/worldA_base_row_id`, exit 1):

    Claude Code  BACKED token=/skill-name new=True
    Codex        no S022 already a SOURCES row at base
    VS Code      BACKED token=/webapp-testing new=True
    Gemini CLI   BACKED token=activate_skill new=True
    explicit invocation forms backed 3 of 7 clients; new ground 3

With `--fetch` (exit 1): `explicit invocation forms found on the live page 3 of 3; new ground 3`.

**The base-absence rule holds:** the real quote under a base-existing row id is **not counted**
(Codex is absent from the backed set, and the reason line names the rule).

### World B — `work/worlds/worldB_base_corpus_token` — a token that occurs in the BASE corpus

Four clients, all fully sourced with real quotes; three of their explicit-form tokens already occur
in the BASE corpus, so they must not count as new ground:

| client | token | where the token already occurs at BASE |
|---|---|---|
| Claude Code | `/skill-name` | nowhere → new ground |
| Codex | `$skill` | `corpus/knowledge/skill-overlap-levers-round51.md:26` (1 hit), `corpus/SKILL.md` 0 hits |
| VS Code | `/skills` | `corpus/SKILL.md` 19 hits, `corpus/knowledge/` 68 hits |
| opencode | `/name` | `corpus/SKILL.md:433` 1 hit, `corpus/knowledge/` 3 hits |

Pristine verdict (exit 1):

    Claude Code  BACKED token=/skill-name new=True
    Codex        BACKED token=$skill new=False
    VS Code      BACKED token=/skills new=False
    opencode     BACKED token=/name new=False
    explicit invocation forms backed 4 of 7 clients; new ground 1

With `--fetch` (exit 1): `explicit invocation forms found on the live page 4 of 4; new ground 1`.

**The new-ground rule holds:** a token that already occurs in the BASE corpus is counted as backed
but **not** as new ground.

## 4. Probe worlds used to discriminate the survivors

Six fixtures, each isolating one rule (all are sandbox fixtures, not corpus claims):

| probe | isolates | discriminating input |
|---|---|---|
| `P_TOKEN` | `TOKEN_RE` | form cell holds `$1` (digit after the prefix) and a bare `/`; the quote holds the same token, so only the token rule can fail |
| `P_HOST` | host pins | source URL host `evilcode.claude.com` vs the pin `code.claude.com` |
| `P_GATE` | Gate-quote equality | S900's Gate row holds a **longer** string containing the S900 quote; S902's Gate row holds the **S901** quote |
| `P_WORDS` | 3–25 word limit | a 31-word quote and a 2-word quote |
| `P_NORM` | `--fetch` normalisation | a quote that matches only when tags are dropped, only when entities are unescaped, and one whose case differs from the page |
| `P_FOUND` | found-vs-backed | a backed client whose quote is **not** on the live page (`found=False`) |

## 5. Results — the mutation table

`K` = killed (detector output differs from pristine), `S` = survived (identical output).

| mutant | rule broken | `--self-test` | world A / world B | probe worlds |
|---|---|---|---|---|
| M01 | `TOKEN_RE` accepts a bare identifier | **K** | S / S | S / S |
| M02 | `TOKEN_RE` accepts a digit after the prefix | **S** | S / S | K / K |
| M03 | `TOKEN_RE` accepts any char after the prefix | **S** | S / S | K / K |
| M04 | base-absence check dropped | **K** | **K** / S | S / S |
| M05 | base-absence compares case-insensitively | **S** | S / S | S / S |
| M06 | `BASE` pin moved to the plan commit | **S** | S / S | S / S |
| M07 | `OPENED` gains a third day | **K** | S / S | S / S |
| M08 | opened-date check loosened to a range | **K** | S / S | S / S |
| M09 | host pin suffix without the dot | **S** | S / S | **K** / K |
| M10 | path pin without the segment boundary | **K** | S / S | S / S |
| M11 | `.`/`..` path segments allowed | **K** | S / S | S / S |
| M12 | Gate quote accepted as a substring | **S** | S / S | **K** / K |
| M13 | Gate quote accepted under any row id | **S** | S / S | **K** / K |
| M14 | Gate-quote check dropped | **K** | S / S | **K** / K |
| M15 | word cap 25 → 40 | **S** | S / S | **K** / K |
| M16 | word floor 3 → 1 | **S** | S / S | **K** / K |
| M17 | word window 1–35 | **S** | S / S | **K** / K |
| M18 | new ground always true | **K** | S / **K** | **K** / K |
| M19 | new ground drops the knowledge haystack | **K** | S / **K** | S / S |
| M20 | new ground drops the SKILL.md haystack | **K** | S / S | S / S |
| M21 | new ground counted over *backed* not *found* | **S** | S / S | K / K |
| M22 | normalisation drops the tag strip | **S** | S / S | S / **K** |
| M23 | normalisation drops entity unescaping | **S** | S / S | S / **K** |
| M24 | normalisation drops the underscore strip | **S** | S / S | S / S |
| M25 | normalisation becomes case-sensitive | **S** | S / S | S / **K** |
| M26 | normalisation drops whitespace collapsing | **S** | S / S | S / **K** |
| M27 | exit drops the `ground >= NEW_TARGET` half | **S** | S / **K** | S / S |
| M28 | `TARGET` 4 → 1 | **S** | **K** / S | **K** / K |
| M29 | `NEW_TARGET` 2 → 0 | **S** | S / **K** | S / S |
| M30 | `--fetch` counts *backed* not *found* | **S** | S / S | S / **K** |
| M31 | exit code always 0 | **S** | **K** / **K** | **K** / K |

**21 of 31 mutants survive the counter's own `--self-test`.** The world runs show the two required
worlds are good behavioural probes for six of them (M04, M18, M19, M27, M28, M29, M31) and the
probe worlds kill sixteen more.

### 5.1 The three mutants no detector here can kill

These survive `--self-test`, both required worlds, and all six probe worlds. Two are **equivalent
mutants** (they cannot change any verdict on this corpus); one is a **live pin risk**.

* **M05 (case-insensitive base-absence) — equivalent.** `SID_RE = ^`?(S\d{3,})`?$` only ever yields
  uppercase ids, and all 64 BASE ids are uppercase (`S001`…`S064`), so `sid.lower() in {x.lower() …}`
  is the same predicate as `sid in at_base`. Verified: `git show f0e5de82:corpus/SOURCES.md` yields
  64 ids, all uppercase. Not a coverage gap in the rules; a coverage gap in the *self-test*, which
  never asserts the case of the compared id.
* **M24 (no underscore strip in `norm`) — equivalent on this corpus.** `norm()` strips `_` from
  both the quote and the page, so the mutation can only matter when the two spell the same word
  differently. Exhaustive search over every sentence of all six fetched markdown pages against all
  four fetched HTML pages found **0 flips** (`work/pages/`): no page renders an identifier with a
  space where its markdown has an underscore. A quote copied from the same page always spells it the
  same way, so the rule is unobservable here.
* **M06 (`BASE` pin moved to the plan commit) — a live pin risk, currently invisible.** The plan
  commit `a10240c0` and the BASE `f0e5de82` currently carry **byte-identical** `corpus/SOURCES.md`
  (72 642 B each), `SKILL.md` (48 175 B) and the same `corpus/knowledge/` listing, so the mutation
  changes nothing today. But the pin is what defines "at BASE" for the base-absence rule and the
  new-ground haystack, and **nothing in `--self-test` asserts the value of `BASE`** (the string
  `f0e5de82` does not appear in `self_test()`). The moment the plan commit stops being
  corpus-identical to the base revision, the base-absence rule silently changes meaning and the
  self-test stays green. This is the sharpest untested invariant in the frozen counter.

## 6. The same mutation set against the lane's current counter (erratum v2)

Read from the lane with `git show b04a900:verifiers/check_explicit_invocation.py` into the sandbox
(sha256 `e13eb88…` is the lane file; the v2 source read for the run is recorded in
`work/v2_mutants.json`). The v2 self-test passes: `self-test: 0 failure(s) over 44 assertions`.

| mutant | v2 `--self-test` | note |
|---|---|---|
| M01 bare identifier accepted | **K** | v2's stricter `TOKEN_RE` refuses it |
| M04 base-absence dropped | **K** | still asserted |
| M07 `OPENED` gains a day | **K** | still asserted |
| M14 Gate-quote check dropped | **K** | still asserted |
| M18 new ground always true | **K** | still asserted |
| M19 new ground drops knowledge haystack | **K** | v2 asserts both haystacks |
| M20 new ground drops SKILL.md haystack | **K** | v2 asserts both haystacks |
| M22 no tag strip | **K** | v2 asserts page tags dropped |
| M25 case-sensitive normalisation | **K** | v2 asserts the quote side |
| M02 digit after prefix | **S** | still open |
| M05→M06 `BASE` pin moved | **S** | still open |
| M09 host suffix without the dot | **S** | still open |
| M12 Gate quote as substring | **S** | still open |
| M13 Gate quote under any row id | **S** | still open |
| M15 word cap 25 → 40 | **S** | still open |
| M16 word floor 3 → 1 | **S** | still open |
| M23 no entity unescaping | **S** | still open |
| M27 exit drops the ground half | **S** | still open |
| M28 `TARGET` 4 → 1 | **S** | still open |
| M29 `NEW_TARGET` 2 → 0 | **S** | still open |
| M31 exit code always 0 | **S** | still open |

**v2 closes five of the seven self-test survivors v1 left open** (M01, M19, M20, M22, M25) and adds
15 assertions. It leaves the **exit-condition family** (M27, M28, M29, M31) entirely unasserted:
no assertion in the v2 self-test reaches `main()`'s exit rule, so a counter that always exits 0
still passes its own self-test.

## 7. Two weaknesses of the frozen v1 counter that the landed round-55 data exposes

Running the frozen v1 counter against the landed round-55 commit `9615579` (v1 `--rev … --fetch`,
exit 0):

    Claude Code  BACKED token=/skill-name new=True found=True
    Codex        BACKED token=$setup-demo-app new=True found=True
    VS Code      BACKED token=/webapp-testing new=True found=True
    Copilot CLI  BACKED token=/frontend-design new=True found=True
    Gemini CLI   BACKED token=activate_skill new=True found=True
    Cursor       BACKED token=/skill-name new=True found=True
    opencode     BACKED token=@skill-id new=True found=True
    explicit invocation forms found on the live page 7 of 7; new ground 7

Two observations about the frozen counter, both of which the v2 erratum addresses:

1. **`new ground 7` double-counts one token.** Claude Code and Cursor both use `/skill-name`;
   v1's `new_ground` is evaluated per client, so the same token contributes 2 to the ground count
   (`new_ground("/skill-name", "", [])` is `True` twice — verified by calling the function). The
   claim is about *distinct* forms; v2 counts per distinct case-folded token.
2. **v1's `new_ground` is case-sensitive while `--fetch` is case-insensitive.** v1's
   `new_ground` does `token not in base_skill` (case-sensitive) but the fetch path matches
   case-insensitively, so a token differing only in case from a base corpus token is scored as
   **new ground**. Verified directly against the frozen source:

       new_ground('/Skills', base containing '/skills')  ->  True   (wrongly "new")
       new_ground('/skills', base containing '/skills')  ->  False  (correctly "held")

   The same frozen counter on the same data says `new ground 7`; v2 on the same revision says
   `user-typed invocation forms found on the live page 5 of 5; new ground 4` and additionally refuses
   the VS Code and Gemini CLI rows (no `skill` word in the quote; `activate_skill` is a tool call,
   not a user-typed form). v2 is stricter on every axis the erratum lists.

## 8. Limits of this report

* The probe worlds are **fixtures for mutation detection, not corpus claims**. Their quotes are
  byte-exact substrings of real pages (listed in section 9), but the world files themselves are
  synthetic SKILL.md / SOURCES.md / lesson / entry trees under `<sandbox>/work/`.
* "Survived" always means *not distinguished by the detectors listed in section 5* — the frozen
  `--self-test`, world A, world B and the six probe worlds, with and without `--fetch`. It does not
  mean the rule is unreachable.
* M05 and M24 are shown equivalent **on this corpus** (section 5.1); a corpus containing an
  identifier rendered two ways would make M24 observable.
* The `--fetch` runs depend on the live pages and on network reachability; every `--fetch` number
  quoted here was observed on 2026-10-22 between 23:12 and 23:52 UTC.
* The counter's own `--self-test` was the detector for the survivor column; I did not modify it.

## 9. Sources fetched (ordinary HTTP GET, 2026-10-22 UTC)

Fetched with `curl` into `<sandbox>/work/pages/`; `date -u` at the fetch window: 23:12–23:17 UTC and
23:52 UTC. sha256 of the bytes as saved:

| URL | HTTP | bytes | sha256 of saved bytes |
|---|---|---|---|
| `https://code.claude.com/docs/en/skills.md` | 200 | 112 748 | `909dd50ab595e5511d0c24e00527ec4f5ad9acc90e308f7df992c071b1ddc737` |
| `https://code.claude.com/docs/en/skills` | 200 | 1 239 681 | `8fe3aad3a7abecae39ef0aba6df6831531ece011c2aaede617b91140719af70e` |
| `https://learn.chatgpt.com/docs/build-skills.md` | 200 | 11 035 | `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` |
| `https://code.visualstudio.com/docs/agent-customization/agent-skills.md` | 200 | 23 082 | `26973567be23eb5756eb6db62afacf055455fbe6f427d40b45659aacb44d361a` |
| `https://code.visualstudio.com/docs/agent-customization/agent-skills` | 200 | 157 088 | `62ff3a269e96dbe7f0a67bb8378bb7acc2d1294a5b6d8765b3cefb0e20551fab` |
| `https://opencode.ai/docs/skills.md` | 200 | 5 365 | `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561` |
| `https://geminicli.com/docs/cli/skills.md` | 200 | 5 763 | `8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590` |
| `https://geminicli.com/docs/cli/skills/` | 200 | 114 148 | `b17895012da7cbefb20291d6210a3b016d0680a53d6fbc4eaed703d9b0f98640` |
| `https://cursor.com/docs/skills.md` | 200 | 18 477 | `a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d` |
| `https://cursor.com/docs/skills` | 200 | 487 844 | `82f937d9497aa32c5f538eb2d33946e9eb0438b78cb3ecaccb6d448eb8b4aeae` |

Quotes used as the load-bearing fixture text (each a byte-exact substring of the named page):

* `Claude uses skills when relevant, or you can invoke one directly with `/skill-name`.`
  — `code.claude.com/docs/en/skills.md:9`
* `For example, `/webapp-testing for the login page`` — `code.visualstudio.com/…/agent-skills.md:287`
* `it calls the `activate_skill` tool` — `geminicli.com/docs/cli/skills.md:24`
* `explicit `$skill` invocation still works` — `learn.chatgpt.com/docs/build-skills.md:218`
* `type `/skills` in the chat input to quickly open the **Configure Skills** menu`
  — `code.visualstudio.com/…/agent-skills.md:52`
* `expose the skill as a `/name` command in the TUI` — `opencode.ai/docs/skills.md:44`
* `To give an automation a skill, add it to the repository's `.cursor/skills/` folder.`
  — `cursor.com/docs/skills.md` (the HTML rendering writes the apostrophe as `&#x27;`, which is what
  makes it the M23 discriminator)

No headless browser was used and no bot challenge was encountered; no paid model call was made.

## 10. What a reviewer should do with this

1. **Add exit-rule assertions to the counter's `--self-test`** (M27, M28, M29, M31 are all still
   open in v2). A self-test that drives `main()` on a tiny fixture tree would close the whole
   family at once.
2. **Assert the `BASE` pin** in the self-test (M06): assert that `git show BASE:corpus/SOURCES.md`
   is the round-55 base revision's registry, so the base-absence rule cannot be re-pointed silently.
3. **Assert the word window as a window**, not as one endpoint at a time: today a 2-word quote and a
   31-word quote each fail for the *other* reason in the fixture (M15, M16, M17).
4. **Assert the Gate-quote equality in both directions** — the current self-test catches a Gate that
   records a *fragment* of the quote, but not one that records a *superstring* of it (M12) nor one
   that records the right quote under the wrong row id (M13).
5. Consider closing the three remaining **equivalent-but-unasserted** invariants (M05, M24) with
   cheap assertions, so a future refactor that makes them observable is caught.

## 11. Evidence pointers

* Frozen target digest: `4fc6e01ad576531c95265c7dcd2440b0b2bda0cd3520a0b317c46cd78b3ff5e5`
  (unchanged at the end of the seat's work).
* Sandbox clone: `/fast/scratch/hyaku/kotoba-r55/MutC1Counter`, HEAD `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`.
* Mutants: `<sandbox>/mutants/M01…M31*.py` (31) and `<sandbox>/mutants_v2/` (21).
* Harnesses: `<sandbox>/work/{mutate,mutate_v2,world_matrix,probe_matrix,make_worlds,make_probes}.py`.
* Result JSON: `<sandbox>/work/{mutants,world_matrix,probe_matrix,v2_mutants}.json`.
* Worlds: `<sandbox>/work/worlds/{worldA_base_row_id,worldB_base_corpus_token}`.
* Probes: `<sandbox>/work/probes/{P_TOKEN,P_HOST,P_GATE,P_WORDS,P_NORM,P_FOUND}`.
* Fetched pages: `<sandbox>/work/pages/` (digests in section 9).
* Lane counter untouched by this seat: `git status --porcelain verifiers/check_explicit_invocation.py`
  → empty.
