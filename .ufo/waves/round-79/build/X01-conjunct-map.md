# X01 — conjunct map: plans/round-79.md § C2 → counter function → failing self-test arm

Counter: `.ufo/waves/round-79/build/check_allowed_tools.py` (2,288 lines, 80 self-test worlds /
231 assertions, `--self-test` exit 0). Line numbers below are of that file at sha256
`74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`
(blanked sha `1f9744c84cce7fe9978074f6379a547f4d7affae8905fde0fd811e493693ccf9`).

"Fails when falsified" = the named arm's assertion(s) go red if the conjunct's code path is removed
or made vacuous. Arms assert `exit code` + the printed verdict line + the specific finding.

| Plan conjunct (§ C2) | Counter function(s) (line) | Self-test arm(s) that fail when it is falsified |
|---|---|---|
| frozen table: surfaces, rows S226–S231, hosts, labels, page tokens | `SURFACES` (196-240), `SURFACE_ORDER`, `FIX` (1330-1341) | `honest world scores 6 of 6`; `(b) the assigned docs.factory.ai URL is not the canonical pin`; `(b) factory's sibling path ... skills-old`; `(b) sibling host ... pi-mono-evil` |
| (a) provenance trio `source:`… `verified-at:`… `recheck:` | `entry_head` (445), `entry_problems` (607) | `(a) entry without verified-at:`; `(a) entry without recheck:`; `(a) cited id absent from the source: lines` |
| (a) frozen surface-table header, exactly one such table, five cells | `surface_tables` (472), `surface_of` (481), `surface_rows` (490), `entry_problems` (607) | `(a) entry with no surface table`; `(a) surface table header drifted`; `(a) two rows name the same surface`; `(a) surface row with six cells`; `(a) first cell is a longer client name` |
| (a) entry names the snapshot text view (Q42/Q53/Q56) | `shaping_named` (345) | `(a) entry that does not name the text view` |
| (a) ≥3 backticked tokens incl. `allowed-tools`, a value form and a grant-semantics token | `row_tokens` (513), `token_role` (529), `grant_role` (524), `token_forms` (540) | `(a) row with only two tokens`; `(a) row with no value-form token`; `(a) row with no grant-semantics token` |
| (a) every token occurs ASCII-word-bounded in the cited snapshot(s) | `word_bounded` (312), `text_view` (325), `surface_holds` (897) | `(a) token the page never carries`; `(a) two rows carry tokens no page carries`; `(a) a .html snapshot's script block does not carry the quote` |
| text view: `.html` script/style→space, tags→space, entities decoded; Markdown backticks deleted + list marker removed; then whitespace collapse | `text_view` (325) | `(d) deleting backticks is what this quote relies on`; `(d) the quote spans a raw line break and is still found`; `(a) a .html snapshot's script block does not carry the quote` |
| (b) 11-cell row, status `mined`, tier A/B, `used-by` names the entry | `registry_rows` (767), `registry_problems` (808), `REGISTRY_CELLS` | `(b) cited row is queued, not mined`; `(b) two cited rows are queued`; `(b) cited row is tier C`; `(b) cited row has 12 cells`; `(b) cited row's used-by omits the entry`; `(b) two registry rows for one cited id`; `(b) staged four-cell rows appended as-is` |
| (b) URL host + whole-segment path prefix equals the frozen host (Q32) | `host_ok` (782), `urls_of` (778) | `(b) cited row's URL is on another host`; `(b) sibling host raw.githubusercontent.com/badlogic/pi-mono-evil`; `(b) factory's sibling path docs.factory.com/harness/skills-old` |
| (c) snapshot sha256 = `MANIFEST.sha256` pin = anchor `fetched … sha256 <hex>` | `Repo.manifest` (696), `Repo.snapshot_name` (727), `Repo.read_snapshot` (755), `FETCHED_RE`, `surface_holds` (897) | `(c) tampered snapshot (manifest hash left)`; `(c) no manifest at all`; `(c) manifest line not <sha256> <basename>`; `(c) manifest path escapes the snapshot directory`; `(c) two pinned snapshots begin with one cited id`; `(c) anchor sha256 is not the snapshot pin` |
| (c)/entry binding: the entry's `source:` line URL is the cited page | `page_key` (578), `same_page` (585), `source_line` (599) | `factory's .md route is the same canonical pin` (passes) and any URL drift (see `(b) …` arms) |
| (d) located quote 5–25 words, whitespace-collapsed, contains `allowed-tools`, found in its own snapshot; one backtick-deleted retry (formatting, not content) | `quote_of` (552), `ws` (307), `quote_location` (882), `_line_of` (868) | `(d) located quote under 5 words`; `(d) located quote over 25 words`; `(d) located quote absent from its snapshot`; `(d) two quotes are absent from their snapshots`; `(d) located quote without the token allowed-tools`; `(d) quote from another surface's page`; `(d) a backtick-wrapped quote cell is formatting, not content`; `(d) a backtick-wrapped quote that is absent still fails` |
| a real row shape: quote spanning an indented YAML list inside a fenced example | `text_view` (325) list-marker rule | `S231 row shape: quote spans an indented list inside a fenced example` |
| a real row shape: pipe-bearing table-row quote whose page prints no syntactic value form | `token_role` (529) bare-name value role, `_split_cells` (378) `\|` unescape | `S230 row shape: a pipe-bearing table-row quote with a bare word as the value form` |
| (d) Q70: not a heading, not the first-heading block, not a shared banner line | `quote_location` (882), `Ctx.other_pages` (856) | `(d) quote is the page's title line (first-heading block)`; `(d) quote is a line shared with a different page (banner)` |
| (e) `opened` cell = entry `verified-at:` = 2026-10-27 | `surface_holds` opened block (930-941), `opened_count` (1044), `CAPTURE` | `(e) one row opened before the round date`; `(e) every row opened before the round date`; `(e) entry verified-at is not the round date` |
| (f) grant cell plain text, exactly one frozen label, the surface's own | `GRANT_LABELS`, `clean` (373), `word_bounded_ci` (319), `surface_holds` grant block (990-1006) | `(f) grant cell is backticked`; `(f) grant label is another surface's`; `(f) two grant labels are another surface's`; `(f) grant cell carries two labels` |
| (f) the quote carries the page token that grounds the grant | `grant_role` (524), `word_bounded_ci` | `(f) quote lacks the page token that grounds the grant` |
| (g) SKILL.md rule line citing the entry and naming ≥3 surfaces | `skill_rule_ok` (1098), `surfaces_named` (1091) | `(g) rule line naming two surfaces reads MISSING` |
| (g) conformant gate registry row for the counter | `registry_home_ok` (1108) | `(g) SKILL.md without a registry row reads MISSING`; `(g) a registry row with an empty field reads MISSING` |
| (h) PROVINCE.md `## Core` has one bullet naming the entry path | `province_bullets` (1120), `province_state` (1140) | `(h) PROVINCE.md without the bullet reads named 0 of 6`; `(h) two Core bullets name the entry` |
| (i) `script-only world: M of 6` printed, M measured by the same `check()` | `script_only_world` (1209), `_mech_quote` (1155), `_mech_value` (1176), `_mech_tokens` (1198), `_mech_entry` (1280), `_score_world` (1255) | `(i) a mechanical world below the target prints the line` (M=1); `(i) a script-only world that reaches the target stops the claim` (M=6 → exit 1) |
| exit 0 iff N ≥ 5 and M < 5 and (g)(h) hold | `main` verdict (2190-2196) | `base world (entry absent) is the do-nothing control`; every arm above that asserts exit 1 at `4 of 6` / exit 2 |
| do-nothing figure (hosts already in the base registry) | `held_at_base` (1029) | `surface hosts already in the base registry read held 6`; `base registry with one factory pin reads held at base: 1` |
| plan controls C0/C1/C2/C3/C5/C6/C7/C8 | as their conjuncts above | `base world … do-nothing`; `C1 token dump …`; `C5 label-only world …`; `(d) quote from another surface's page`; `(d) … shared … banner`; `(b) sibling host …`; `(c) anchor sha256 is not the snapshot pin` |
| not-a-commit / absent registry / counter drift → exit 2 | `main` (2160-2180) | `unknown revision is exit 2`; `registry absent at the revision is exit 2`; `counter drift is exit 2 (SELF_SHA does not match)` |

## Notes a reviewer should carry

1. The target has margin one over a population of six, so a single broken surface still exits 0 at
   `5 of 6`. Every conjunct therefore has (i) a one-surface arm asserting the specific finding, and
   (ii) for (a), (b), (d) and (f), a two-surface arm that flips the verdict to `4 of 6`, exit 1.
2. `held at base: 5` — at the r79 base, five of the six frozen hosts already appear in
   `corpus/SOURCES.md` (all but factory, whose canonical page the L1 moved to
   `docs.factory.com/harness/skills`). The counter's discriminating work is therefore in (c), (d)
   and (f), not in the host test; the base still reads `0 of 6` because the entry does not exist.
3. `row_tokens` counts every backticked span after the surface cell, including inside the located
   quote cell. A data seat that backticks a phrase in the quote adds tokens that must also occur
   word-bounded in the snapshot.
4. The mechanical world's label is the single no-judgement label `unstated`; that is why M is 1 in
   the honest fixture (vibe is the one surface whose frozen label is `unstated`) and why a world
   whose pages let a scraper reach six is reported as a defect rather than repaired.
