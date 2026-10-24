# ReviewCensus — round-66 SOURCES census freshness re-run

Seat: ReviewCensus (read-only reviewer). Lane: kotoba. Date: 2026-10-24 (UTC).
Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (plan `plans/round-66.md`).
Measured tip: lane Git HEAD `2a8eba56b3f9321b70c569fa2816d42237ca49a2`; SOURCES.md blob
`1e3fec49c15ddb837b6f3c9d2348e6d21a3296da`; `git status --porcelain corpus/` empty.
The jj working copy (`omvyzpns…`) carries concurrent peer edits confined to
`.ufo/waves/round-66/w1/swarm-registry.json` plus untracked peer reports; no corpus byte is
touched.

## Verdict

Fresh re-run at the tip, exit **0**, source rows **120**, **16** W04 duplicate-URL warnings,
**no new W04**, disposition unchanged from the pinned base. No actionable defect in this scope.

## Exact output (fresh run)

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
```

Measured: exit `0`, stdout 17 lines, stderr 0 bytes. No `E` code of any class. Today is
2026-10-24 UTC, so S122's `opened` value is a present date (E08 clean).

## Source row count

`census` mode over the same tree (exit 0):

```
kotoba	rows	120
kotoba	tier.A	117
kotoba	tier.B	2
kotoba	tier.C	1
kotoba	status.mined	112
kotoba	status.queued	7
kotoba	status.rejected	1
FLEET	rows	120 … FLEET	missing	0
```

Independent count agreement at the tip:

| Method | Result |
|---|---|
| `census` `rows` metric | 120 |
| Registry-section `S`-row grep (`^ {0,3}\| *S[0-9]{3,} *\|`, lines 10–134) | 120 |
| `|`-split field count per registry row | 13 fields × 120 rows (contract NF=13) |

Base check in a temporary copy (`git show 11385e04:corpus/SOURCES.md`, `--file` mode):
**119 rows**, tier.A 116 / B 2 / C 1, mined 111 / queued 7 / rejected 1, and the same 16 W04
IDs. The base→tip delta in `corpus/SOURCES.md` is 3 added lines and 0 removed: the S122 row
plus two append-only round-66 search-log lines. So the tip row count is base 119 + S122 = 120,
consistent with the committed receipt `.ufo/waves/round-66/census-after.txt` (`120`).

Caveat on that base probe: `--file` runs against a `/tmp` copy, so its E11 `used-by` checks
resolve against the temp parent and the process exits 1 with E11 noise. The base probe is a
count/W04 comparison only and is not evidence about base validation status.

## W04 duplicate disposition

- **Class semantics:** W04 is a warning, not a failure. The script header states "W04 same URL
  across scopes (warnings do not affect clean lanes)" and the lane prints `kotoba ok …/corpus/SOURCES.md`
  with exit 0; the selftest's `W-only-warning-reported` / `W-only-registry-exit-0` cases pin this.
- **Set:** 16 warnings at both the pinned base and the tip, byte-for-byte the same IDs in the same
  order (S018, S019, S021, S054, S055, S056, S065, S086, S103, S104, S106, S110, S111, S114,
  S115, S118). Tip adds none.
- **Cause:** every flagged row is `status=mined` and duplicates an earlier row's URL under a
  *different* scope — i.e. the expected shape of a re-open/supersede row that narrows the scope
  (for example S118 re-opens S103's `code.claude.com/docs/en/memory.md`; S114 re-opens
  S048/S106's `add-custom-instructions.md`; S115 re-opens S108's `cursor.com/docs/rules`).
  There is no E04 same-scope duplicate, so W04 is the only duplicate class present.
- **S122:** the FORCE11 URL is new to the registry and appears in no duplicate pair; the round's
  only added registry row therefore adds no 17th W04 — the same outcome round 63 recorded for S119.
- **Receipt parity:** `.ufo/waves/round-66/census-before.txt` and `census-after.txt` both record
  16 W04, `ok`, `exit=0`; the fresh run's 17 `kotoba`/`ok` lines are **byte-identical** to the
  committed `census-after.txt` body. SOURCES.md last changed in commit `9e75e73`, the same commit
  that wrote `census-after.txt`, so the receipt and the fresh measurement are at the same blob.
  The round's census-before and census-after bodies are identical, consistent with an added row
  whose URL and scopes introduce no duplicate.

## Instrument freshness

- `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`: fleet-root Git HEAD `a6b957e`,
  tracked commit `6a1dd8c` (2026-10-19), working tree clean for the script, sha256
  `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`, mtime 2026-10-19 21:22.
  No lane-local copy shadows it.
- `sources-census.sh selftest`: exit 0, **96 killed, 0 SURVIVED**, terminal line `selftest ok`.
  The validator used for the measurement is therefore the selftest-green instrument, not a
  drifting copy.

## Findings by severity

- **P0/P1/P2:** none in scope.
- **P3 (documentation only, no gate effect):** `corpus/lessons/round-66.md` has no census/Gate row
  and no W04 disposition sentence, unlike the r63–r65 lessons, which record the round-start and
  round-end census and the carried duplicate set. The round's disposition is therefore recoverable
  only from the contract plus `.ufo/waves/round-66/census-{before,after}.txt`, not from the lesson.
  This does not affect exit status, row count, or any frozen predicate.

## Residual risk and verification gaps

- Row count here is the **registry-row** count (120). It is a different metric from
  `verify_corpus_integrity.py`'s `corpus.index.tracked_files=118` (indexed Markdown files), so the
  two numbers are not in conflict and must not be reconciled to each other.
- The census validates registry structure only; it does not fetch or re-verify the 120 source URLs.
  URL liveness/anchors are out of scope for this seat.
- The base comparison used a `/tmp` `--file` copy, so only counts and W04 IDs were compared at the
  base; base exit status was not measured (and would be dominated by the temp-path E11 artifact).
- Concurrent peers are amending only `.ufo` files in the jj working copy. The measured corpus blob
  is unchanged before and after the run; a later change to `corpus/SOURCES.md` would invalidate
  this receipt and requires a re-run.
- Out of scope: C1/C2 scoring, controls, counters, and the other reviewers' assignments. No claim,
  counter, threshold, plan, or receipt was modified by this seat.
