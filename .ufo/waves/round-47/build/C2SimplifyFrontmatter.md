verdict: Add `trigger.description_no_xml_tag` as a sibling `check_* (fm)` after `check_anti_trigger` (~1248); wire once in `CHECK_IDS`, docstring, and `main()` dispatch (~2215); do not fold into `check_frontmatter` or re-parse.

## Axes (godspeed)
- **Operability:** one new check id, one parse site (`fm = parse_frontmatter(lines)` at 2197), same `(status, evaluated, detail)` tuple as `check_literal_trigger` / `check_anti_trigger`.
- **Calibration:** self-test `CASES` must treat the new id like the other description checks on broken frontmatter (fail lists + `evaluated>0` on `clean`); floors-registry `1597` and assertion count move with integrator (C2FloorsBoxes lane).
- **Freshness:** advice pinned to BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`; live repo HEAD matched at run time.

## Smallest insertion (reuse parse, no duplicate parsing)

**Do not extend `check_frontmatter` (1176–1191).** Docstring pins `trigger.frontmatter_parses` at `evaluated = 4` (67–75, 1178); that check only asserts structural parse + non-empty `name`/`description`. Folding XML into it would break the documented four-assertion contract and every self-test row that expects `evaluated == 4` on `trigger.frontmatter_parses`.

**Preferred shape:** mirror `check_anti_trigger` (1230–1248):

1. **Regex (module constants ~356–366):** add e.g. `XML_TAG_RE` next to `ANTI_TRIGGER_RE` / `QUOTED_SPAN_RE`. Build-spec asks for XML-Name-style tags (`<name>`, `</name>`, `<name/>`, optional attributes). A minimal discriminant aligned with round-47 before metric (`grep '<skills>'` on frontmatter) is something like `<[^>\s/][^>]*>` — verified on BASE interpreter:

   | description substring | matches tag regex? | intended label |
   |---|---|---|
   | `` `<skills>` router `` | yes (`<skills>`) | FAIL (live SKILL.md:14) |
   | `see <skills> router` | yes | FAIL |
   | `a <b> tag` | yes | FAIL |
   | `3 < 4` | no | PASS |
   | `<<heredoc` | no | PASS |

   **Counterexample vs naive “strip backticks first”:** stripping quoted/backticked spans (as `check_anti_trigger` does) would PASS the live kotoba description while the plan’s before-count (`SUMMARY.md:10`, `grep` on frontmatter) is `1` for `<skills>` **inside backticks**. Match S003 enforcement to **raw parsed `description` string**, not quote-stripped text, unless C2CriticRule explicitly overrides.

2. **Function (~1249, immediately after `check_anti_trigger`):** `def check_description_no_xml_tag(fm: tuple[dict | None, str]) -> tuple[str, int, str]:` — copy the guard block from `check_literal_trigger` (1211–1218): `fields is None` → `FAIL, 0, cannot evaluate`; empty `description` → same; else scan `fields["description"]`, `evaluated = 1`, PASS/FAIL detail naming first match (same detail verbosity as anti-trigger).

3. **`CHECK_IDS` (~282–293):** insert after `trigger.anti_trigger_clause` (keeps frontmatter cluster together). Use `trigger.description_no_xml_tag` (existing ids use `trigger.*`, not build-spec’s `frontmatter.description_no_xml_tag`).

4. **Module docstring (~87–96):** new `trigger.description_no_xml_tag` bullet: S003, structural tag definition, limit (comparison operators / `<<` not tags; backtick-wrapped tag names still count if regex is raw-string).

5. **`main()` dispatch (~2215–2216):** one `elif cid == "trigger.description_no_xml_tag": st, ev, detail = check_description_no_xml_tag(fm)` — **no second parse**.

6. **Self-test (~1677–1763):** add fixture dir (e.g. `description-xml-tag/SKILL.md` + map) with planted `<tag>` in description → expect FAIL on new id; add `clean`-style control. Extend every `CASES` `fails` list that already lists `trigger.literal_trigger_string` and `trigger.anti_trigger_clause` for broken/absent frontmatter (`no-frontmatter`, `fm-null`, `fm-malformed`, `fm-dup-key`, `fm-body-yaml`, `fm-stray-indent`, `empty-file`, …) to include the new id — otherwise self-test expects PASS + `evaluated>0` while `fm` is `None` or description empty (`evaluated 0`).

**Out of scope for this function (integrator/L1):** new checklist box + `checklist-baseline.json` row (prose rule at `SKILL.md:151` is not yet an executed box); `SKILL.md:14` rewrite; `corpus/SOURCES.md` S010 “no XML-tag rule” line update.

## Live BASE behavior (commands)

```text
git rev-parse HEAD → c61a973b2e02e1ded169703ddcb06466f4edd8bd (exit 0)
sed -n '/^---$/,/^---$/p' SKILL.md | grep -c '<skills>' → 1 (exit 0)
python3 -B verifiers/verify_skill_checklist.py --json → exit 1 (governance.citation_resolves FAIL); trigger.* all PASS
python3 -B verifiers/verify_skill_checklist.py --self-test → exit 0, "0 failure(s) over 1597 assertions"
parse_frontmatter(SKILL.md): description 814 chars, contains literal "<skills>" (inline probe, exit 0)
```

No XML check exists at BASE: `grep -i xml_tag / description_no_xml verifiers/verify_skill_checklist.py` → no matches.

## Dead / stale code near frontmatter checks (deletion candidates)

| Location | Finding | Evidence |
|---|---|---|
| `parse_frontmatter` 501–542 | `cur_open` is written on every branch but **never read** | `rg cur_open verify_skill_checklist.py` → assignments only |
| `check_literal_trigger` 1215 | detail says ``frontmatter carries %s: list`` | Parser stores nested YAML as folded strings, not YAML lists — misleading detail, not unreachable |
| `check_frontmatter` vs siblings | duplicated “empty description” logic | Intentional: `check_frontmatter` keeps `evaluated=4` on parse failure; siblings use `evaluated=0` — **not** dead |

**Not recommended:** deduplicating the three `(fm)` guard blocks into a helper unless integrator wants a shared `_require_description(fm)` — saves ~6 lines, adds a second convention.

## What would harm an axis

- Merging into `check_frontmatter` → breaks `evaluated=4` calibration and docstring parity.
- Re-parsing frontmatter inside the new check → duplicate authority vs 2197.
- Quote-stripping before tag scan → live kotoba `<skills>` in backticks would PASS while C2 before metric and `SKILL.md:151` prose say otherwise.

## What I did NOT check

- `C2Battery.json` ground-truth battery (peer lane).
- Full integrator patch in scratch clone / `--self-test` count after hypothetical edit.
- `check_assertion_floors.py` / box_total 41→42 ripple (C2FloorsBoxes).
- Fleet/host SKILL.md scans (C2HostSkillsScan / C2FleetScan).
- Semantic LSP `references` on `check_frontmatter` (no server run; text search only).
- Anthropic upload/API enforcement of S003 (SrcNewAnthropicPolicy lane).

## Tool installs

None.

Report: `.ufo/waves/round-47/build/C2SimplifyFrontmatter.md`
