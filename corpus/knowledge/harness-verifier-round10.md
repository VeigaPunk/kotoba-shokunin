# The harness claim set, executable — round 10

Sourced 2026-09-28 (round 10). This file is the human-readable half of
`verifiers/verify_harness_claims.py`; the script is the authority. Every number
below was printed by a command in the run that produced `verifiers/baseline.json`
(`as_of` 2026-09-28T18:42-03:00, host `vgpnk`).

## What changed this round

The round-9 harness model was a set of hand-run recipes: a reader (or an agent)
had to re-type `sqlite3 -readonly`, `strings`, and three `grep` pipelines, and
then judge the output. A recipe re-run by a human is lane-attested evidence —
nothing fails when it stops being true. Round 10 converts it into a committed
program with a recorded baseline: `verifiers/verify_harness_claims.py`
(**27 checks**, exit 0 agree / 1 drift / 2 environment unreadable / 3 no
baseline; `--self-test` checks the script's own model). A claim now fails
loudly the moment the host stops agreeing with it. Runtime ≈3 s (2.6 s of it is
the session-log scan below).

## The authority is readable source, not disassembly

Both harnesses ship as single-file executables with **embedded readable JS**.
`strings -n 6` already exposes it; the exact bytes are more useful:

```bash
python3 - <<'PY'
from pathlib import Path
b = (Path.home()/".local/bin/omp").read_bytes()
i = b.find(b"skill_descriptions")
print(b[i-2000:i+1500].decode("utf-8", "replace"))
PY
```

From that region (`omp`, sha256 `55016ef5…`, mtime 2026-09-28 15:14):

```js
// packages/coding-agent/src/extensibility/skill-descriptions.ts
function A8n(e) {
  return new Bun.CryptoHasher("sha256").update(K7s).update("\x00")
    .update(e.name).update("\x00").update(e.description).digest("hex");
}
function H7s(e) {                                    // previewSkillDescription
  const t = e.replace(/\s+/g, " ").trim();
  if (t.length <= _8n) return t;                     // _8n = 100
  const s = t.slice(0, _8n - 1);
  const o = s.match(/^.*?[.!?](?=\s|$)/)?.[0];
  if (o && o.length >= 40) return o;
  const n = s.slice(0, s.lastIndexOf(" ")).trimEnd();
  return `${n || s}\u2026`;
}
function ldl(e) {                                    // compressor acceptance
  const t = e.trim();
  if (!t || /[\r\n]/.test(t) || t.length > idl) return null;   // idl = 160
  if (t.split(/\s+/).length > adl) return null;                // adl = 12
  return t;
}
// var _8n = 100, idl = 160, adl = 12
```

`nV.render` is exactly `cache.get(key) ?? previewSkillDescription` followed by a
fire-and-forget `#o()` write — the round-7/9 "cache-or-truncate" model, now read
rather than inferred. Earlier rounds cited ELF *offsets* (which drift across
builds) and one round cited a stale `slice(0,99)` literal; the source is stable
and self-describing, so this file cites functions.

## The key prefix is 273 bytes, not one sentence

Round 9 recorded the template as the single line `"Compress into one routing
hint of at most 12 words: …"`. That is *part* of the keyed prompt — the ELF
carries the whole bunfs file (`de("/$bunfs/root/compress-description-<hash>.md")`)
NUL-terminated in one run:

```
Compress into one routing hint of at most 12 words: WHEN to use; WHEN NOT only if it prevents confusion. Retain recognizable trigger words. Do not restate the skill name or market it. Output one line without bullets or quotes.\n\nSkill: {{name}}\nDescription: {{description}}\n
```

273 bytes, sha256 `c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51`.
`A8n` hashes this string **with the `{{…}}` placeholders intact** — the rendered
prompt is only the compressor's input. The verifier recovers it by anchoring on
`Compress into one routing hint`, taking bytes to the next NUL, and asserting
both placeholders are present; a prompt change (new build) therefore moves
`omp.elf.template_sha256` and re-stales every cache row at once.

## The description salt is YAML scalar style — confirmed, not inferred

`e.description` is the loader-held string, so the block scalar decides:

| Style | Loader-held value | Skills on this host | Key variant that hits |
|---|---|---|---|
| plain, `>-` | ws-collapsed, stripped | 11 | `re.sub(r"\s+"," ",d).strip()` |
| `>`, `\|` | ws-collapsed + one trailing `"\n"` | 6 (omarchy, wwkd, xbrd-ask, sekhmet-l3, kimi-webbridge, ufo) | same + `"\n"` |

Measured: offered 17, `keys_reproduced` **17/17**, `cache_misses` **0**,
`db_rows_wellformed` 17/17 (every cached row satisfies `ldl`: one line, ≤160
chars, ≤12 words), `descriptions_over_cliff` 17/17 (every live description is
>100 ws chars, so no offered skill could even take the truncator path today),
`name_mismatches` 0 (every frontmatter `name:` equals its folder name).

## Offer gate roots — the round-9 list was incomplete

The 17-row cache is explained by the roots the verifier walks, not by the one
round 7 named. `~/.agents/skills` (**not** listed in the round-9 offer-gate row)
holds 15 live skills; `~/.omp/agent/skills` adds `kimi-webbridge` and `ufo`;
`~/.config/opencode/skills` and `~/.claude/skills` are symlink trees into
`~/.bailian/skills` that duplicate names already seen (first root wins).

```
~/.agents/skills: 17 entries, 2 dangling -> sekhmet, xbrd
    (symlinks into ~/Projects/origin-work/ufo-fsd-alpha/ports/xbgst-codex/skills)
```

The dangling pair is recorded as a baseline number (`omp.offered.dangling` = 2),
not dropped: a broken symlink is exactly how a catalogue silently shrinks. It
also explains why the host shows 17 offered names while 19 directories exist.

## opencode side — what is checkable

There is no verbatim offer record, so the checks are counter-shaped:

| Check | Value today | Why it is the check |
|---|---|---|
| `oc.log.init_count_max` == `oc.roots.names_plus_builtin` | 18 == 17+1 | the only logged evidence of the catalogue size; builtin `customize-opencode` confirmed present in the opencode ELF |
| `oc.log.available_skills_hits` / `skills_tag_hits` | 0 / 0 | the opencode catalogue is never logged verbatim; a non-zero means the logging surface changed and the counters above stop being the only evidence |
| `oc.dup.roots_both_sided` | 3 roots | dedupe is last-parsed-wins under `concurrency:"unbounded"`: every root appears on both the `existing=` and `duplicate=` side. Deterministic dedupe would collapse this to one-sided |
| `oc.log.init_count_monotone` | no violation | counts only grow (15→16→17→18 across 2026-08-28…09-28); a decrease means the roots changed incompatibly |
| `oc.permission.skill_allow` / `skill_lines` | 471 / 471 | the `skill` permission gate is open via `permissions["*"]="allow"`; a deny would show up as non-allow lines |

`~/.claude/plugins/cache` absent, `~/.config/opencode/skill` (singular) absent —
both recorded as zero-mode checks.

## The render check: what the model actually saw

`omp.catalogue.*` closes the last gap between keys and renders. The newest
captured `<skills>` block is found by walking `~/.omp/agent/sessions/**`
(5924 files, 2.6 s) and keeping the newest block that parses into ≥10
`- name: description` lines with ≥10 known names — the raw literal count is
**contaminated** (8194 `<skills>` literals vs 4116 catalogue blocks, round-10
sentinel), so an unfiltered grep reports a world that does not exist.

```
newest catalogue 2026-09-28T21:47:06.212Z (17/17 lines from cache, 5924 session files scanned)
```

Two traps were paid for here, both silent-miss generators:

- **JSON escaping.** The block lives inside a session jsonl record; quotes and
  newlines are escaped. Matching raw bytes reported `16/17` with `wwkd` missing
  (`\"plan this\"` vs the db's `"plan this"`). Decoding the record (`json.loads`
  → walk every string) gives 17/17. A verifier that does not decode reports a
  false staleness finding — the same defect class round 9 caught in its own
  description census.
- **Escaped-vs-real rendering.** Because the catalogue freezes at session start,
  a *lagging* block is a legitimate state: the check compares against the db as
  it is now, so a skill whose description was edited mid-session can read as a
  miss. That is the correct signal (it is what the model saw) but it must not be
  diagnosed as "the cache is broken".

## Guards: fail loudly, never guess a key

The frontmatter reader models plain (single-line and continuation), `>`/`>-`/`>+`,
`|`/`|-`/`|+`, and single/double-quoted scalars; ` #` comments, trailing-space
trimming, and `''`-escapes follow YAML. Anything it does **not** model — multiple
documents, anchors/aliases, flow collections, an explicit indentation indicator,
a multi-line quoted scalar — is recorded in `omp.descriptions.unmodelled` and
**excluded from the pass/fail set**: a guessed key would produce a false DRIFT.
Eight such guard cases were derived by an independent fixture lane (8 synthetic
SKILL.md files under `/tmp/round10/fixtures`), and the value of the guard is
measured, not assumed: nothing on this host currently trips it (17/17 verified
skills, `unmodelled` = 0), while the *live* corpus exercises only 4 of the 12
style cells (2 plain, 9 `>-`, 5 `>`, 1 `|`; zero quoted, `|-`, `|+`, `>+`,
multi-line plain) — so ~5 rule cells are unfalsifiable here. Say that rather than
claiming the parser is complete.

## Falsification of the verifier itself

| Test | Result |
|---|---|
| `--self-test` (7 truncator vectors + 3 chomping assertions) | 0 failures / 10 — the script's model of `H7s` and of block-scalar chomping, not the host |
| perturbed baseline (17→16 keys, 17→16 catalogue lines) | exit 1, `DRIFT` names exactly those two checks |
| `HOME=/tmp/...emptyhome` | exit 2 `INCONCLUSIVE: omp binary not found` |
| baseline deleted | exit 3, observations printed |
| real host | exit 0, 27/27 |
| independent recomputation (3 other lanes) | critic: rule holds as mechanism / fails as documented (round-9 quote → 0/17); executor `omp_verify.py`: 17/17 and 11/11 of this baseline's omp values; scout: 17/17, 273 B template, sha256 match |
| the round-9 hand recipe itself | `strings -n 6 \| grep 'Compress into one routing hint'` → 226-byte first line → **0/17 keys** — the recipe it replaces cannot reproduce the claim set |
| 10 planted faults in `/tmp` fixture worlds (independent mutation lane) | 9 detected with exit 1 and the firing check id (deleted db row, edited db description, stale skill tree, uncached new skill, short description, low `init count`, leaked `<available_skills>`, name≠folder, altered template bytes); 1 undetected — a `>-` description differing **only** in trailing whitespace. That is an *equivalent* mutation: YAML strip-chomping discards the trailing blank, the loader-held description is byte-identical, the key is identical, and agreeing is correct. Recorded as an acceptable non-goal; the mutation must change the loader-held bytes to be a fault. |

## Open gaps (not claimed)

- Truncation is *predicted* (`H7s` reimplemented and unit-tested) but not
  *exercised live*: with 17/17 keys cached, no offered skill takes that path.
  Proving the prediction end-to-end needs a host mutation, which the lane refuses
  to do to the operator's skill tree.
- The cache write is async (`M8n = new mO(4)` semaphore, fire-and-forget): a
  freshly edited description is a *known* transient miss, so a verifier failure
  right after an edit is expected, not a defect. The script says nothing about
  age.
- `oc.log` is append-only and grows; snapshot checks there are `at_least`, so a
  log rotation would read as a regression rather than a change of record.
- Descriptions for 5 of the 17 rows (the `>`-styled set) reproduce only because
  the trailing-newline salt is right; if the loader ever changed its YAML
  library, `cache_misses` would jump to 6 — the check would fire, but the
  *diagnosis* is this file's job, not the script's.
- Root order is load-bearing and untested by construction: the shadowed
  `~/.config/opencode/skills/ufo` copy hashes to a key the db does not contain
  (`c78fa9df…` vs the offered `~/.omp/agent/skills/ufo`, `892555ed…`), so a
  precedence flip would orphan ufo's row silently. The verifier detects it as a
  miss, but nothing in the host prevents the flip.
- The catalogue check reads the *newest* block only; a host that stops producing
  catalogues freezes the check at the last one. `catalogue_timestamp` is printed
  so the reader can see the age, but no staleness threshold is enforced.