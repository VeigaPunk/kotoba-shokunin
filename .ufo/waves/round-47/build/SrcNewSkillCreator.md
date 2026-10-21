verdict: ADMIT as S012 (`code`, tier A, queued) — anthropics/skills carries an executable reference validator, `skills/skill-creator/scripts/quick_validate.py`, that refuses any angle bracket in `description` at package time; the row is contract-valid (maintained `validate` exit 0, 12 rows, 0 malformed) and gives C2 a vendor red-before/green-after oracle, but it also shows C2's stated "XML tag" rule is narrower than the vendor's character-class rule.

# SrcNewSkillCreator — candidate SOURCES row (round 47 BUILD)

Leaf lane, read-only on production. BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`git rev-parse HEAD`). Nothing under the lane was edited. Scratch: `/fast/scratch/kotoba-r47/SrcNewSkillCreator/`. Fetch metadata: `SrcNewSkillCreator.json` beside this file.

## 0. Ticket path drift (first counterexample)

The ticket names `skill-creator/SKILL.md` and "the repo README/spec". At this revision that literal path does not exist:

- `curl https://raw.githubusercontent.com/anthropics/skills/main/skill-creator/SKILL.md` → HTTP **404**, 14 bytes `404: Not Found`, 2026-10-21T15:57:31Z, exit 0.
- `…/main/skills/skill-creator/SKILL.md` → HTTP **200**, 33168 bytes, sha256 `dcd4803e…`, same minute.
- The move is commit `ef74077` "Move example skills into dedicated folder and create minimal top-level folder structure (#129)". Verified, not inferred: `git show ef74077^:skill-creator/SKILL.md` → exit 0 (frontmatter `name: skill-creator`), and the pre-move `skill-creator/scripts/quick_validate.py` already carries the same angle-bracket block, so the ticket's path was valid before that commit and the rule survived the move unchanged.

So the named artifact exists one level deeper; the row is admitted under the real path. A row written against the ticket's URL would have cited a dead link.

## 1. What the source actually says (external, commit `dbd4588`, 2026-10-09)

1. **The validator exists and is enforceable.** `skills/skill-creator/scripts/quick_validate.py` is 3972 bytes; `package_skill.py:17` imports `validate_skill`, `:70-76` runs it before archiving and returns `None` on failure ("Please fix the validation errors before packaging"). This is the enforcement point, not a lint suggestion.
2. **The rule is a character class, not a tag grammar.** `quick_validate.py:79-81`:
   `# Check for angle brackets` / `if '<' in description or '>' in description:` → `"Description cannot contain angle brackets (< or >)"`. A bare comparison fails too: fixture `description: "Compare a > b in prose"` → exit 1, same message. The vendor does not parse XML.
3. **Other enforced frontmatter rules.** 6-key allowlist `{name, description, license, allowed-tools, metadata, compatibility}` (`:45-50`); name kebab-case, no leading/trailing/double hyphen, ≤64 (`:60-71`); description ≤1024 (`:82-84`); optional compatibility ≤500 (`:86-92`).
4. **The validator is laxer than the lane on one axis.** `grep -n "directory\|parent\|resolve" quick_validate.py` → only the usage string at `:98`. There is no name==directory comparison; the repo's own `template/SKILL.md` (`name: template-skill`, directory `template`) validates **clean** (exit 0). The lane's `check_name_directory` (`verifiers/verify_skill_checklist.py:1194`) is stricter than the vendor tool.
5. **The repository no longer carries the spec.** `spec/agent-skills-spec.md` is 3 lines / 87 bytes: "The spec is now located at <https://agentskills.io/specification>". Yet `README.md:28` still advertises "`[./spec](./spec): The Agent Skills specification`" — a stale pointer in the vendor README. So the ticket's "README/spec" half yields **no spec row**; S001 remains the normative spec row and this row must not be tiered as a spec.
6. **The repo is not gated on its own validator.** No `.github/` at HEAD (`git ls-tree -r --name-only HEAD | grep -c '^\.github/'` → 0). Running the validator over all 19 top-level skills: **18 pass, 1 fail** — `skills/claude-api`, "Description is too long (1068 characters). Maximum is 1024 characters." Tier A is therefore correct only for the narrow scope "what Anthropic's reference packager refuses"; it is not evidence that the vendor corpus conforms.

## 1b. Rejected candidate rows from the same tree (kept as reasoning, not as rows)

The ticket also asks about "the repo README/spec". Both were opened; neither earns a row:

- **`spec/agent-skills-spec.md` as a `spec` row — REJECTED, absent content.** The file is 3 lines / 87 bytes: `# Agent Skills Spec` + "The spec is now located at <https://agentskills.io/specification>". Sweep: `wc -l` → 3; `grep -n -iE "angle|xml|description"` → 0 hits; sha256 `ff22f2be…`. A row here would cite a redirect as a specification, and the normative source is already S001 (`corpus/SOURCES.md:14`). Flip: none possible short of the repo re-adding spec text.
- **`README.md` as a `docs` row — REJECTED, redundant.** Its only frontmatter teaching is `README.md:65-72` ("The frontmatter requires only two fields: `name` … `description`"), which S001 already carries at tier A; its `:28` claim that `./spec` is "The Agent Skills specification" is false at this revision (see §1.5). Under contract rule 4 (no row quota; short registry) a redundant row costs more than it teaches. Flip: a README statement that adds a rule the registry lacks.

The validator row itself is **not** rejected: it exists, it is executable, and it says something the registry does not yet carry.

## 2. Why this matters to C2 (operability) — an external oracle, and a divergence

At BASE the lane states the rule but does not execute it, and its own description violates it:

- `SKILL.md:151` — "`description` ≤1024 chars, no XML tags (Anthropic rule) … This file's own description still carries `<skills>`".
- `SKILL.md:14` — the `<skills>` token sits on a folded continuation line of the `description: >` block.
- `verifiers/verify_skill_checklist.py:1176` `check_frontmatter` tests presence/emptiness only; `grep -n -i xml` matches only cmark-oracle comments at `:1551` and `:1894`.

Vendor tool against the lane at BASE (PyYAML 6.0.3, no install):

```
python3 scripts/quick_validate.py /home/vgpnk/Projects/shokunin/kotoba-shokunin
→ Description cannot contain angle brackets (< or >)          exit 1
```

Mechanical token removal on a scratch copy only (`sed` in `/fast/scratch/…/probe/`, production untouched) → `Skill is valid!`, exit 0. Measured lane description: 814 chars, 2 angle-bracket characters, keys `{name, description}`, name == directory. So the vendor tool is a **second, independent red-before/green-after arm for C2** that does not share the lane's parser (it uses `yaml.safe_load`; the lane's structural parser folds continuations itself).

**Divergence the integrator must decide.** C2 promises "the `description` value carries no XML tag". The vendor rule is broader: any `<` or `>` fails. A description containing "a > b" passes an XML-tag check and fails Anthropic's packager. Two coherent options: (a) implement `<`/`>` (vendor parity, one line, no tag grammar), or (b) keep the tag grammar and record the divergence, in which case the C2 self-test needs a deliberate control for a bare `>` so the choice is visible rather than accidental. This leaf does not choose; it records that the two rules are not the same rule.

## 3. Draft row (insert at the end of the Registry table, after `corpus/SOURCES.md:24`, before `## Paths` at `:26`)

```
| S012 | anthropics/skills — skill-creator reference skill (quick_validate.py + SKILL.md) — https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator | code | A | SKILL.md `description` frontmatter validation in Anthropic's own reference packaging tooling | `skills/skill-creator/scripts/quick_validate.py:79-81` "Check for angle brackets"; tree `dbd4588` (2026-10-09), file last changed `1ed29a0` (2026-02-06), rule present since init `37292f3` (2025-10-15) | Anthropic's own packager refuses any `<` or `>` in `description` ("Description cannot contain angle brackets"), not only well-formed XML tags; the open spec states no such rule | queued | 2026-10-21 | 90d | — |
```

Why these cells:

- `kind: code` — the load-bearing artifact is the script; SKILL.md is context, not the claim.
- `tier: A` — contract v1 lists "source code" under A, scoped to what that code enforces. Scope deliberately excludes the spec and the ecosystem (F6 above).
- `status: queued`, `used-by: —` — nothing cites it yet. A `mined` row would need a real used-by path; the round-47 lesson does not exist at BASE and `E11`/`W03` would fire or warn. If C2 lands and cites this row in `corpus/lessons/round-47.md`, flip to `mined` with that path in the same change (contract rule 2 logs the old→new).
- `recheck: 90d` — vendor code, no release tag to hang `on-release` on; the rule has been stable since `37292f3 init repo` (2025-10-15), last file touch 2026-02-06.

## 4. Gate record (contract rule 1)

| field | value |
|---|---|
| URL | `https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator` (bytes fetched from `raw.githubusercontent.com/anthropics/skills/dbd4588…/…`) |
| access UTC | 2026-10-21T15:55:51Z for the three pinned raw fetches; the clone/`ls-remote` ran minutes earlier at ≈15:54Z and was not separately timestamped |
| HTTP status | 200 for all three pinned raw fetches; 404 for the ticket's literal path (recorded above) |
| sha256 | `quick_validate.py` `67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365` (3972 B); `SKILL.md` `dcd4803e61e913e6fc27294184cd3a71f09f5e924ff20c8a9a20173e7b3c2bcf` (33168 B); `README.md` `2fb9c4cc026366ea6e21c60cb23c908a4d27c62071819cc06beffaac102d0694` (5552 B); `spec/agent-skills-spec.md` `ff22f2be775f4b757c9a7a2df0421de4c94021d34d9382cea5dd567ff0cdad2c` (87 B, read from the clone) |
| anchor + revision | `skills/skill-creator/scripts/quick_validate.py:79-81`; tree `dbd4588f9e1033efb41dad4bef2f7947c8993d44` (2026-10-09T18:45:49Z, main == HEAD); file last changed `1ed29a03dc852d30fa6ef2ca53a67dc2c2c2c563` (2026-02-06); rule present since init `37292f37bf4bdf33bbd75e415d5313292966e443` (2025-10-15) |
| quote (8 words) | "Description cannot contain angle brackets (< or >)" — `quick_validate.py:81`, emitted when `:80` matches, reached through `package_skill.py:72-76` |
| kind / tier | `code` / `A`, scoped to the reference packager's behavior |
| teaches | Anthropic's own packager refuses any `<` or `>` in `description` ("Description cannot contain angle brackets"), not only well-formed XML tags; the open spec states no such rule |
| source identity drift | `main` and the pinned commit are byte-identical for `SKILL.md` (sha `dcd4803e…` from both, 15:57:31Z), so the pin is not stale relative to `main` at access time |

## 5. Sweeps behind every negative claim

- "No XML-tag grammar" — `grep -rn "angle bracket"` over the repo: exactly 2 hits, both in `quick_validate.py:79,81`; the code tests membership of `<` and `>`; fixture with `a > b` fails (exit 1), which no tag grammar would reject.
- "No name==directory check" — `grep -n "directory\|parent\|resolve" skills/skill-creator/scripts/quick_validate.py` → only the usage string `:98`; behavioral confirmation: `template/` (`name: template-skill`) validates exit 0.
- "Spec not in repo" — `wc -l spec/agent-skills-spec.md` → 3; `sha256sum` above; the file body is a pointer. `grep -n "spec" README.md` → `:28` still claims otherwise.
- "Not CI-gated" — `git ls-tree -r --name-only HEAD | grep -c '^\.github/'` → 0; self-census 18/19 with `skills/claude-api` failing on length.
- "Lane violates the rule at BASE" — description 814 chars with 2 angle characters; vendor tool exit 1; `SKILL.md:14` is the token, inside the folded `description: >` block opened at `:3`.
- Row validity — scratch copy of `corpus/SOURCES.md` with S012 inserted in the Registry: frozen census `rows=12`, `malformed=0`, `A=11 C=1`, `mined=4 queued=7 rejected=1`, no duplicate ids, no enum/tier-inflation violations; maintained `scripts/sources-census.sh validate --file … --today 2026-10-21` → `file ok`, **exit 0**; `census` → rows 12, missing 0, **exit 0**.

## 6. Calibration notes (no production edit proposed)

- **S011's rejection survives, but its phrasing now has a better home.** `corpus/SOURCES.md:24` says the tutorial "credits an angle-bracket ban to the agentskills.io spec which has none (0 mentions)". True — and since the repo's own spec is now a pointer, the spec cannot gain the rule by accretion. The ban's real home is vendor code (this row). That does not flip S011 (its "will not load" claim still contradicts S002); it means a reader should not conclude "no angle-bracket rule exists". If the integrator wants that recorded, contract rule 2 makes it a **new** row opening `supersedes S0NN —`, never an edit to `:24`.
- **Distinct from S003, not a duplicate.** `corpus/SOURCES.md:16` (S003, `docs`) states "Cannot contain XML tags"; S012 (`code`) is the executable enforcement and is strictly broader. E04 (same URL+scope) does not fire — different URL, different scope. Keep both; S003 gives the authoring intent, S012 gives the machine check.
- **C2 fixture suggestion grounded in the vendor's own discrimination.** The vendor's three-way split is directly reusable as fixture classes: well-formed tag `<b>` → FAIL, bare `>` → FAIL (or a documented PASS under tag semantics), no bracket → PASS. The lane's self-test currently has no such control; adding the bare-`>` case is what makes the C2 rule's scope observable.
- **The vendor tool would fail most sibling skills on YAML before it ever reaches the angle rule.** Sweep over the fleet root (`*/SKILL.md`, 2026-10-21): 18 files, `yaml.safe_load` ok 8 / error 10 (`mapping values are not allowed here`, the S002/S008 plain-scalar `: ` defect — e.g. `kagi-shokunin/SKILL.md:2` "Rank: shonen"); of the 8 that parse, only `kotoba-shokunin` carries angle characters in `description` (2). Vendor tool on `kagi-shokunin` → exit 1 `Invalid YAML in frontmatter: mapping values are not allowed here … Rank: shonen.` So if C2 implements the rule via `yaml.safe_load`, 10 sibling files are red for an unrelated reason; the lane's structural parser (which accepts them) is the reason its own gate is green today. This is Q18 territory: the new rule must be scoped to the lane's own file, or the plain-scalar defect must be fixed first. First-pass caveat: a naive `grep '[<>]'` over frontmatter also counts the `>` folded indicator (`lore-shokunin/SKILL.md:1` `description: >`), which is not a value character — only the parsed-value sweep above is a valid count.

## 7. Commands run (exit codes)

| # | command | exit | key output |
|---|---|---|---|
| 1 | `git ls-remote https://github.com/anthropics/skills.git` | 0 | `main = dbd4588f9e1033efb41dad4bef2f7947c8993d44` |
| 2 | `git clone -q --depth 1 --no-single-branch … repo` | 0 | 445 tracked files; HEAD `dbd4588` (2026-10-09) |
| 3 | `git fetch -q --deepen=300`; `git log --follow -S "angle brackets" -- …/quick_validate.py` | 0 | `37292f3 init repo` |
| 4 | `curl -sS -o … -w '%{http_code}'` on 3 pinned raw URLs | 0 | 200 / 3972 B, 200 / 33168 B, 200 / 5552 B; shas as above |
| 5 | `curl …/main/skill-creator/SKILL.md` | 0 | HTTP 404, 14 B |
| 6 | `python3 scripts/quick_validate.py /home/vgpnk/…/kotoba-shokunin` | 1 | `Description cannot contain angle brackets (< or >)` |
| 7 | same, scratch copy with the token removed | 0 | `Skill is valid!` |
| 8 | validator over 5 fixtures (tag / bare `>` / clean / extra key / 1025 chars) | 1,1,0,1,1 | messages quoted in §1 and §2 |
| 9 | validator over all 19 `skills/*/` | 0 | pass 18 / fail 1 (`claude-api`, 1068 chars) |
| 10 | validator over `template/` | 0 | `Skill is valid!` despite `name: template-skill` |
| 11 | frozen SOURCES census awk set on scratch copy | 0 | rows 12, malformed 0, no enum/dup violations |
| 12 | `scripts/sources-census.sh validate --file <scratch> --today 2026-10-21` | 0 | `file ok` |
| 13 | `scripts/sources-census.sh census --file <scratch> --today 2026-10-21` | 0 | rows 12, tier.A 11, tier.C 1, queued 7 |
| 14 | first attempt: row appended after `## Leads` | 1 | `E12 S012 row outside Registry section` (recorded so it is not repeated) |
| 15 | `python3 -c json.load(SrcNewSkillCreator.json)` | 0 | 17 keys, valid (18 after the fleet-sweep block) |
| 16 | `yaml.safe_load` sweep over `<fleet root>/*/SKILL.md` frontmatter | 0 | total 18, yaml_ok 8, yaml_err 10, desc_angle 1 (kotoba, 2 chars) |
| 17 | `python3 scripts/quick_validate.py /home/vgpnk/Projects/shokunin/kagi-shokunin` | 1 | `Invalid YAML in frontmatter: mapping values are not allowed here … Rank: shonen.` |

No tool was installed or upgraded; PyYAML 6.0.3 was already present on the host. No pacman transaction was attempted.

## 8. What I did NOT check

- **The eval loop half of skill-creator** (`run_eval.py`, `run_loop.py`, `improve_description.py`, the 20-query / 3-run / 60-40 claims in `SKILL.md`) — not opened for admission; the lead at `corpus/SOURCES.md:71` stays a lead, not a row. That lead itself carries the stale path (`skill-creator/SKILL.md`), so opening it literally would 404; it is `skills/skill-creator/SKILL.md`. A row for it would need its own gate record and a different `teaches`.
- **GitHub API tree/contents endpoints** — `api.github.com` returned HTTP 403 (unauthenticated rate limit for this IP) at 15:54Z; I used `git ls-remote`/clone and pinned raw fetches instead. No GitHub HTML page was fetched.
- **Other branches** (`klazuka/spec`, `klazuka/export`, `andibrae/create-top-level-namespace`, …) — listed, not read; the row pins `main`.
- **`.claude-plugin/marketplace.json`** plugin wiring — not inspected; irrelevant to the frontmatter claim.
- **A production-tree run of `verify_skill_checklist.py`** — not performed by this leaf; the 9 PASS / 1 FAIL before-value is quoted from `.ufo/waves/round-47/before/SUMMARY.md`, not re-measured here. Whether C2's implementation should reuse the vendor's character-class rule is a design decision left to L1; this report supplies both the oracle and the divergence, not the choice.
- **The vendor validator's behavior on CRLF frontmatter or a `---`-with-header file** — untested; the script's regex is `^---\n(.*?)\n---` with `re.DOTALL`, so a CRLF checkout would likely miss the block. Not exercised.
