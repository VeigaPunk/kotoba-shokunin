# A07LaneDivergence — falsify attack point 4

Seat: `KotobaR48.A07LaneDivergence` (leaf reviewer). Date 2026-10-22 (UTC).
Target: `corpus/knowledge/frontmatter-rule-authorities-round48.md` point 4 (lines 63-74 at 887b6af5):
"6 of 10 verdicts differ from the packager, 3 of 10 from the docs' tag rule", both directions,
and "single-quoted `'\u003cb\u003e'`: lane FAIL, packager PASS". Attacked at the assigned commit 887b6af5.

## Verdict
- CONFIRMED: counts re-derived from executed runs. 6/10 diverge from the packager's
  description-angle rule; 3/10 diverge from the docs' tag rule.
- CONFIRMED: both directions. Lane PASS / packager FAIL on f02, f02b, f05, f06, f07; lane FAIL /
  packager PASS on f08.
- CONFIRMED: single-quoted `'\u003cb\u003e'` (f08). Lane exit 1 (FAIL); packager exit 0, "Skill is valid!".
- DEFECT D1, LOW (wording). "6 of 10 verdicts differ from the packager" is unqualified. It holds
  only for the description-angle rule. On the packager's file-level verdict the divergence is
  7 of 10: f04 also differs (packager fails `café-skill` on its name rule; the measured check
  `trigger.no_xml_tag` has no name-charset test).
- DEFECT D2, LOW (precision). f02b's packager FAIL comes from the unknown top-level key `shared`
  (`qv.py:44-48` returns before the description check); its tag verdict is an emulation of the
  one-line rule (`qv.py:80`). f04's tag verdict is also emulated (name check returns at `qv.py:66`).
  The alias bullet should cite f02, where the packager executes the angle check.
- DEFECT D3, LOW (disclosure). The 3/10 rests on reading S003's prose "Cannot contain XML tags"
  as a well-formed tag shape; the entry does not say so. Robust to implementation (see below), not to the reading.
- D1-D3 are still present at lane tip `27887041` (point 4 text unchanged there).
- Suggested wording: "On the packager's description-angle rule, 6 of 10 diverge (f02b by emulation:
  the packager stops at its unexpected-key check). On the packager's file verdict, 7 of 10 diverge
  (f04 adds the name rule, which the measured check does not evaluate). On the docs' tag rule, 3 of 10
  diverge, with 'XML tag' operationalised as a well-formed tag shape."

## Lane moved during the run
- My first read matched C1 (`verify_skill_checklist.py:1307-1308`). Falsify-wave commits `d28b16b`
  and `2788704` then landed (tip `27887041bd82f2de31cf33bb223783749fb5cbc9`). The working copy now
  equals tip (sha256 `e456be3f95dd0b763b0a1e8b5f4142ca8bcf845a28f9f6723d7de5bdc3d755a1`).
- Checker diff 887b6af5..tip touches only the FAIL detail string (now `:1307-1311`). Tip rerun gives
  identical exit codes on all ten fixtures; outputs differ only in `detail` lines.
- `PROVINCE.md` at tip has zero "stricter" hits, so its claimed correction holds.

## Rebuild and runs
- Private clone (`git clone -q` of the lane), `git checkout -q 887b6af5`; HEAD
  `887b6af54d3f4446f1fe51dc16f26b2e83bc82e1`.
- Checker sha256 `4ea2100dee220077eead8ed8cfc2c5acb311ffff8746451bb5fd12b202c5e38a` = build receipt;
  `git diff 75f671b1 887b6af5 -- verifiers/verify_skill_checklist.py` empty. `--self-test` exit 0,
  "0 failure(s) over 1845 assertions".
- Ten fixtures written from the C2 report's descriptions, using the build seat's text as reference;
  `diff -r` against the build seat exit 0. This proves transcription accuracy, not independent derivation.
- Packager `quick_validate.py` at `dbd4588f9e1033efb41dad4bef2f7947c8993d44`, sha256
  `67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365`.

## Rerun at 887b6af5
Lane = `trigger.no_xml_tag` CLI exit. Packager = `qv.py` exit and rule that fired. "Emulated" = the
one-line rule applied to the YAML-parsed description, because the packager returned earlier.

| case | lane exit | packager exit / rule that fired | P tag | S003 regex / tokenizer | P diverges | S003 diverges |
|---|---|---|---|---|---|---|
| f01 raw tag | 1 FAIL | 1 angle (executed) | FAIL | FAIL / FAIL | no | no |
| f02 alias in metadata | 0 PASS | 1 angle (executed) | FAIL | FAIL / FAIL | yes | yes |
| f02b alias top key | 0 PASS | 1 unexpected key `shared` (emulated) | FAIL | FAIL / FAIL | yes | yes |
| f03 escaped unicode | 1 FAIL | 1 angle (executed) | FAIL | FAIL / FAIL | no | no |
| f04 unicode name | 0 PASS | 1 name kebab-case (emulated) | PASS | PASS / PASS | no | no |
| f05 arrow | 0 PASS | 1 angle (executed) | FAIL | PASS / PASS | yes | no |
| f06 comparison | 0 PASS | 1 angle (executed) | FAIL | PASS / PASS | yes | no |
| f07 folded split | 0 PASS | 1 angle (executed) | FAIL | PASS / PASS | yes | no |
| f08 single-quoted | 1 FAIL | 0 "Skill is valid!" (executed) | PASS | PASS / PASS | yes | yes |
| f09 fullwidth | 0 PASS | 0 (executed) | PASS | PASS / PASS | no | no |

- Packager description-angle divergence: f02, f02b, f05, f06, f07, f08 = **6/10**.
- S003 divergence: f02, f02b, f08 = **3/10**.
- Packager file-level divergence (lane FAIL vs packager exit not 0): f02, f02b, f04, f05, f06, f07, f08 = **7/10**.

## Single-quoted claim (f08)
- Lane exit 1; `detail` = `XML tag in description: '\\u003c'`. Mechanism: `YAML_ANGLE_ESCAPE_RE` text
  match on the unparsed value. PyYAML parses the value to literal text `\u003cb\u003e`, which holds no `<`.
- Packager exit 0, "Skill is valid!". CONFIRMED: lane FAIL, packager PASS, and the lane's FAIL is a text match.

## Independent S003 check (correction to my first draft)
My first draft called the S003 column "two independent implementations". That was false: the second
regex was a copy of the lane's `XML_TAG_RE`. Replacement: stdlib `html.parser.HTMLParser` tokenizer
(shares no code) on the YAML-parsed description. It flags f01, f02, f02b, f03, the same set as the
lane regex. The 3/10 stands under this implementation.

## Freshness receipts
- S012 `quick_validate.py` at `dbd4588f`: `https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py`;
  accessed 2026-10-22T08:59:05Z; sha256 `67cf5703…fde365` (matches the sha256 the entry cites). Quote (line 81,
  8 words): "Description cannot contain angle brackets (< or >)".
- Pin still upstream HEAD: `git ls-remote https://github.com/anthropics/skills.git HEAD` at
  2026-10-22T09:01:36Z returned `dbd4588f9e1033efb41dad4bef2f7947c8993d44 HEAD`.
- S019 docs: `https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md`;
  accessed 2026-10-22T09:01:35Z (timestamp before fetch); 42169 bytes; sha256
  `f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960`, the same as the C1 SOURCES S019 row.
  Quote (line 155, 4 words): "Cannot contain XML tags". Rule lines at 154, 155, 162.

## Commands and exit codes
- `git clone -q`, `git checkout -q 887b6af5`, `git fetch -q origin` (private clone; reads lane objects): 0 each.
- Lane `--self-test`: 0. Ten lane CLI runs (`--repo fixtures --skill fixtures/<case>/SKILL.md --check trigger.no_xml_tag --json`):
  1 for f01, f03, f08; 0 otherwise. Same at tip.
- Ten `python3 -B qv.py fixtures/<case>`: 1 for f01, f02, f02b, f03, f04, f05, f06, f07; 0 for f08, f09.
- `diff -r` fixtures vs build seat: 0. `git ls-remote` and `curl -fsSL` (qv.py, bp.md): 0 each.

## Residual risk and gaps
1. The 3/10 rests on the S003 prose reading. An NFKC-first reading would change f09; no authority in the set applies NFKC.
2. The f02b and f04 packager tag verdicts are emulations of the packager's own line 80: faithful, not executed.
3. S019 "editorial drift only" (round 47: 42028 bytes, sha `727f3fa1…`; now 42169 bytes) is not re-derived:
   no round-47 copy is in the lane or my scratch. I confirmed the rule lines exist, not that only editorial bytes changed.
4. Tip corrections audited only where they touch point 4 (checker diff, entry text, PROVINCE wording, tip rerun).
5. Counts describe this ten-fixture set, not the rule space.

## Writes and installs
- Lane: no writes. Git reads only, via a fetch into the private clone; no `git status`, `jj`, or index command ran in the lane.
- Installs and updates: none. System Python 3.14.8 and PyYAML 6.0.3 used as-is; no pacman transaction.
- Scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A07LaneDivergence/` (clone, fixtures, `qv.py`, `bp.md`, `out-c1/`, `out-tip/`, entry copies).

Report: .ufo/waves/round-48/falsify/A07LaneDivergence.md
