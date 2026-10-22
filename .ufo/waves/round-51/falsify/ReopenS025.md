# ReopenS025 — attack C2's VS Code row (round 51 falsify, 2026-10-22)

Verdict: **HOLDS** — all four points hold; no defect found in the landed VS Code row.

Freshness: re-opened https://code.visualstudio.com/docs/agent-customization/agent-skills.md myself,
2026-10-22T15:15:16Z, HTTP 200, 22,871 bytes, sha256
`de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5` (expected prefix `de5ba34f` ✓).
Byte-identical to the hash recorded in SOURCES S025 (fetched 2026-10-22T12:29:33Z, 22871 B) and to
the entry's `recheck` hash; the lesson records the L1's 15:08Z re-fetch as byte-identical too. The
page's quoted line is unchanged since all three fetches.

## Findings by point

**1. Quote verbatim, ≤25 words, key term an exact backtick span — HOLDS.**
Entry `corpus/knowledge/skill-overlap-levers-round51.md:22` quotes: "Use the `user-invocable` and
`disable-model-invocation` frontmatter properties to control how each skill is accessed:"
(agent-skills.md:289). My fetched line 289 reads: "By default, all skills appear in the `/` menu.
Use the `user-invocable` and `disable-model-invocation` frontmatter properties to control how each
skill is accessed:" — the quote is a verbatim substring including the trailing colon. Word count:
14 (≤25). Key term `` `disable-model-invocation` `` (SKILL.md:398, column 6) appears in the quote as
an exact backtick span; it is in the counter's `REVIEWED_LEVERS["VS Code"]`
(verifiers/check_overlap_levers.py:146) and contains no "description".

**2. Page says what the lever / held-by / effect cells say — HOLDS.**
- Page `:151` (§ SKILL.md file format → § Header (required)): "`disable-model-invocation` | No |
  Controls whether the agent can automatically load the skill based on relevance. Defaults to
  `false`. Set to `true` to require manual invocation through the `/` slash command only."
- Page `:289-296` (§ Use skills as slash commands): same sentence as the quote, then the
  configuration table: `disable-model-invocation: true` → Slash command **Yes**, Auto-loaded by
  Copilot **No**.
- Entry lever cell ("a frontmatter flag stops the agent loading the skill on its own; the `/`
  command still works") and SKILL.md:398 lever cell ("frontmatter flag; manual `/` invocation only")
  both match `:151`+`:295`.
- SKILL.md `held by` = "skill author": both flags are YAML frontmatter fields of the skill's own
  SKILL.md (`:143-151`), filled by whoever writes the skill ("Complete the `SKILL.md` file by
  filling in the YAML frontmatter", `:85`). Correct.
- SKILL.md `effect` = "automatic choice off": `:151` ("agent can automatically load… require manual
  invocation") and the `:295` row (auto-load No, slash Yes) match; manual use kept, matching the
  entry's three-effect taxonomy ("automatic choice off with manual use kept").
- Bonus: the lesson's rejection of `user-invocable` as the lever is accurate — `:150` says
  `user-invocable: false` hides the skill from the `/` menu "while still allowing the agent to load
  it automatically", the opposite effect. The landed row correctly uses `disable-model-invocation`.
- Counter note: `evaluate()` pins `held by` and `effect` but leaves the SKILL.md lever cell
  free-form (check_overlap_levers.py:344-351), so the landed wording is not machine-pinned — it is
  backed by the page as shown above.

**3. S025 row shape and Gate record — HOLDS.**
`corpus/SOURCES.md:38`: kind `docs`, tier `A`, status `mined`; URL
https://code.visualstudio.com/docs/agent-customization/agent-skills — under the pinned vendor
prefix `https://code.visualstudio.com/docs/` (check_overlap_levers.py:129). `used-by` ends with
`corpus/knowledge/skill-overlap-levers-round51.md`. Lesson `corpus/lessons/round-51.md` § Gate →
Admitted records S025 among the re-opened rows (seat `SrcVSCode`, hash `de5ba34f…`, quote
`agent-skills.md:289`). The row's teach cell also discloses the page's only precedence statement
(see point 4) and the recorded fetch hash/bytes that my fetch reproduces exactly.

**4. No rule deciding between two skills that both remain candidates — HOLDS.**
Sweep `grep -niE 'overlap|conflict|precedence|tie|both|choose|select|priorit'` on my 395-line
fetch: 28 matching lines. Counts: overlap 0, conflict 0, priorit 0, precedence 1, tie 10 (all
inside words like "capabili-ties" — no tie-break text), select+Select 17 (UI menu actions),
both+Both 5, choose 2. Substantive hits read in context:
- `:64` — "If skills in `.github/skills/` have duplicate names across workspace roots, the primary
  root takes precedence." The closest call. It is a same-name discovery rule across workspace
  roots: the shadowed copy stops being a candidate, so it does not decide between two skills that
  both remain candidates, and it is not keyed on description overlap. The entry's negative
  (finding 2; SKILL.md:388-389) therefore stands; SOURCES S025 already discloses this exact hit.
- `:129` — same-name skill in another supported location: "both skills appear on the Skills page"
  (menu visibility only; no model-invocation arbitration stated).
- `:148` — Copilot "decide[s] when to load the skill" from the `description` (the known description
  lever, not a second-candidate tie-break).
- `:289-296`, `:302` — the frontmatter access controls and description-based Discovery quoted above.
None of these is a documented rule that picks between two differently named skills whose
descriptions both match. The entry's "none" claim holds for this page.

## Counter re-run

In my scratch clone at HEAD `59903b26`: `python3 -B verifiers/check_overlap_levers.py --rev HEAD`
→ 7 BACKED lines ("BACKED VS Code" included), "overlap levers backed 7 of 7 clients", exit 0.

## Evidence (commands → exit codes)

- `curl -sS -o vsce-agent-skills.md -w '...' --max-time 60 https://code.visualstudio.com/docs/agent-customization/agent-skills.md`
  → `HTTP:200 bytes:22871`, exit 0; `sha256sum` → `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5`;
  `date -u` → 2026-10-22T15:15:16Z.
- `git clone -q <lane> lane && git -C lane checkout -q 59903b26… && python3 -B verifiers/check_overlap_levers.py --rev HEAD`
  → exit 0, 7 of 7.
- `grep -oiE 'overlap|conflict|precedence|tie|both|choose|select|priorit' … | sort | uniq -c`
  → counts above.
- Reads: entry `:22`, SOURCES `:38`, SKILL.md `:368-:402` (table inside `## Anti-patterns` at
  `:368`, VS Code row `:398`), fetched bytes `:135-175`, `:270-330`.
- Scratch: /fast/scratch/hyaku/kotoba-r51/falsify/ReopenS025/ (clone + fetch). Lane untouched
  except this report file. No tools installed (curl/git/python3/grep preinstalled); no pacman use.

## Residual risk / gaps

- I did not run `--fetch` myself; the L1 reported `--fetch` 7 of 7 at 15:10:48Z. For the VS Code row
  I verified the quote on live bytes manually, which is stronger for this one row (raw substring,
  not whitespace-normalized).
- The plain counter never checks quote-on-page; only `--fetch` does. A silent upstream rewrite that
  preserves the counter's other pins would pass the plain run — mitigated here by the hash recheck.
- `:64`'s precedence sentence is the only page text that could be read as a tie-break; it is
  same-name/discovery-scoped and already disclosed in the S025 row, but a future strict reading of
  SKILL.md:388 ("two skills that both remain candidates") without the entry's differently-named
  scope would need to address it explicitly.
- Single-point-in-time fetch; page currency beyond 15:15:16Z not re-verified.
