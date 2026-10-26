#!/usr/bin/env python3
"""Generate the round-74 C1 shortcut-control worlds as git patches against base 1e03d19.

Every world is a patch that, applied to a fresh `git clone --shared` of the lane at the
base, produces one committed revision; the C1 counter then runs `--rev HEAD` in that
clone.  Nothing is written into the lane tree.

The world shape is the counter's frozen shape (ExecSpecCounterR74, 2026-10-25):
  entry  corpus/knowledge/spec-skill-creation-craft-round74.md
         rule table | page | S id | rule | quote | tokens | action |
  snapshots .ufo/waves/round-74/snapshots/{best-practices,using-scripts,quickstart}.md
  manifest  .ufo/waves/round-74/snapshots/MANIFEST.sha256   "<sha256>  <name>"
  registry  corpus/SOURCES.md  S223 best-practices, S224 using-scripts, S225 quickstart
  SKILL.md  ### Body craft — the specification's skill-creation guides
  PROVINCE.md  ## Core bullet naming the entry
"""

import hashlib
import os
import pathlib
import subprocess
import sys

LANE = pathlib.Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
BASE = "1e03d1991bc02281b00a5b7a5e00c9d5d5d72908"
OUT = LANE / ".ufo/waves/round-74/w1/build/ExecSpecControlsR74"
STAGED_ENTRY = pathlib.Path("/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/spec-script-craft-rules.md")
STAGED_ROWS = pathlib.Path("/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md")
# The three page fetches this seat made on 2026-10-25 (curl -sL --max-time 60 -A
# 'Mozilla/5.0', HTTP 200): best-practices 15 060 B sha256 ab9f3b60…, using-scripts
# 12 078 B sha256 2cd77271…, quickstart 4 080 B sha256 7c480b44….  Re-fetch them into
# $W74_PAGES (default /tmp/k74w1-pages) to regenerate; the generated world patches
# already embed the bytes, so regeneration is provenance only.
PAGES_DIR = pathlib.Path(os.environ.get("W74_PAGES", "/tmp/k74w1-pages"))
PAGES = {p: str(PAGES_DIR / f"{p}.md") for p in
         ("best-practices", "using-scripts", "quickstart")}
IDS = {"best-practices": "S223", "using-scripts": "S224", "quickstart": "S225"}
ENTRY_PATH = "corpus/knowledge/spec-skill-creation-craft-round74.md"
SNAP_DIR = ".ufo/waves/round-74/snapshots"

ENTRY_TITLE = "# Skill-creation body craft — the specification's own authoring guides\n"

ENTRY_SOURCES = """source: S223 — https://agentskills.io/skill-creation/best-practices.md — fetched `.md` 15 060 B on 2026-10-25, sha256 ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41
source: S224 — https://agentskills.io/skill-creation/using-scripts.md — fetched `.md` 12 078 B on 2026-10-25, sha256 2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f
source: S225 — https://agentskills.io/skill-creation/quickstart.md — fetched `.md` 4 080 B on 2026-10-25, sha256 7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb
verified-at: 2026-10-25
recheck: 90d — re-fetch the three `.md` pages and confirm each token below still locates word-bounded in its page (ran 2026-10-25)
"""

ENTRY_BODY = """
## What the guides add

The `skill-creation/` set states three body-craft rules the lane's other sources do not:
instruction specificity tracks the fragility of the task (S223); a reusable package is
referenced directly with a pinned version instead of being bundled as a script (S224);
and the specification's own tutorial writes a skill under `.agents/skills/`, its default
discovery root (S225).

## Rule table

| page | S id | rule | quote | tokens | action |
|---|---|---|---|---|---|
| best-practices | S223 | match instruction specificity to the fragility of the task | "Match the specificity of your instructions to the fragility of the task." | `references/api-errors.md`; `python scripts/migrate.py --verify --backup` | Read `references/api-errors.md` for the error table instead of a generic pointer. |
| using-scripts | S224 | reference an existing package directly and pin its version | "Pin versions with `npx package@version` for reproducibility." | `uvx ruff@0.8.0 check .`; `pipx run 'black==24.10.0' .` | Prefer `uvx ruff@0.8.0 check .` in the body over a bundled script. |
| quickstart | S225 | the tutorial's default discovery root | "VS Code looks for skills in `.agents/skills/` by default." | `.agents/skills/`; `.agents/skills/roll-dice/SKILL.md` | Place the skill at `.agents/skills/roll-dice/SKILL.md` before shipping it. |

## Limits

Form and located tokens only; whether a rule sentence is true of the page is a
reviewer's judgement, not this table's.
"""

SKILL_BLOCK = """
### Body craft — the specification's skill-creation guides

Round 74; the three `skill-creation/` guides state the body-craft rules the lane lacked
(S223–S225). Snapshot and token table: `corpus/knowledge/spec-skill-creation-craft-round74.md`;
counted by `verifiers/check_spec_craft.py --rev <rev>`.

| page | action | rule token |
|---|---|---|
| best-practices (S223) | Read `references/api-errors.md` when an API call returns a non-200 status code. | `references/api-errors.md` |
| best-practices (S223) | Run `python scripts/migrate.py --verify --backup` exactly as written and add no flags of your own. | `python scripts/migrate.py --verify --backup` |
| using-scripts (S224) | Reference `uvx ruff@0.8.0 check .` directly in the body instead of bundling a script. | `uvx ruff@0.8.0 check .` |
| using-scripts (S224) | Pin the formatter call as `pipx run 'black==24.10.0' .` so repeated runs match. | `pipx run 'black==24.10.0' .` |
| quickstart (S225) | Put the skill at `.agents/skills/roll-dice/SKILL.md` so a compliant client finds it. | `.agents/skills/roll-dice/SKILL.md` |
| quickstart (S225) | Keep the one-file skill under `.agents/skills/` and check `roll-dice` appears. | `.agents/skills/` |
"""

# (-- swap for world 5: best-practices rows carry quickstart-only tokens)
SKILL_CROSS_PAGE = """
### Body craft — the specification's skill-creation guides

Round 74; the three `skill-creation/` guides state the body-craft rules the lane lacked
(S223–S225). Snapshot and token table: `corpus/knowledge/spec-skill-creation-craft-round74.md`;
counted by `verifiers/check_spec_craft.py --rev <rev>`.

| page | action | rule token |
|---|---|---|
| best-practices (S223) | Put the skill at `.agents/skills/roll-dice/SKILL.md` so a compliant client finds it. | `.agents/skills/roll-dice/SKILL.md` |
| best-practices (S223) | Keep the one-file skill under `.agents/skills/` and check it appears. | `.agents/skills/` |
| using-scripts (S224) | Reference `uvx ruff@0.8.0 check .` directly in the body instead of bundling a script. | `uvx ruff@0.8.0 check .` |
| using-scripts (S224) | Pin the formatter call as `pipx run 'black==24.10.0' .` so repeated runs match. | `pipx run 'black==24.10.0' .` |
| quickstart (S225) | Put the skill at `.agents/skills/roll-dice/SKILL.md` so a compliant client finds it. | `.agents/skills/roll-dice/SKILL.md` |
| quickstart (S225) | Keep the one-file skill under `.agents/skills/` and check `roll-dice` appears. | `.agents/skills/` |
"""

PROVINCE_BULLET = (
    "- Skill-creation body craft (round 74): the open specification's own three `skill-creation/`\n"
    "  authoring guides (best practices, using scripts, quickstart) state the body-craft rules for\n"
    "  instruction specificity, direct package reference and the default discovery root —\n"
    "  `corpus/knowledge/spec-skill-creation-craft-round74.md`, counted by\n"
    "  `verifiers/check_spec_craft.py --rev <rev>` (S223–S225).\n"
)

REG_ROWS = """| S223 | Agent Skills — Best practices for skill creators — https://agentskills.io/skill-creation/best-practices.md | docs | A | the open specification's own body-craft guide for a skill: specificity against fragility, defaults over menus, procedures over declarations | "Calibrating control" and "Provide defaults, not menus"; quote "Match the specificity of your instructions to the fragility of the task."; fetched as `.md` 15 060 B on 2026-10-25 | match instruction specificity to task fragility, give one default instead of a menu, and prefer procedures over declarations | {status} | {opened} | 90d | {usedby} |
| S224 | Agent Skills — Using scripts in skills — https://agentskills.io/skill-creation/using-scripts.md | docs | A | the open specification's own guidance for the deterministic half of a skill: one-off commands, bundled scripts, agent-facing script interfaces | "One-off commands" and "Designing scripts for agentic use"; quote "Pin versions with `npx package@version` for reproducibility."; fetched as `.md` 12 078 B on 2026-10-25 | reference an existing package directly when it does the job, pin versions, and design script interfaces for an agent | {status} | {opened} | 90d | {usedby} |
| S225 | Agent Skills — Quickstart — https://agentskills.io/skill-creation/quickstart.md | docs | A | the open specification's own first-skill tutorial, including the default skill root its client reads | "Create the skill" and "How it works"; quote "VS Code looks for skills in `.agents/skills/` by default."; fetched as `.md` 4 080 B on 2026-10-25 | the tutorial writes the skill to `.agents/skills/<name>/SKILL.md` and states that root is the default discovery location | {status} | {opened} | 90d | {usedby} |
"""


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        sys.exit(f"FAILED {' '.join(cmd)}\n{r.stdout}\n{r.stderr}")
    return r.stdout


def base_text(path):
    return run(["git", "-C", str(LANE), "show", f"{BASE}:{path}"])


def insert_before(text, marker, block):
    i = text.index(marker)
    return text[:i] + block + "\n" + text[i:]


def snap_bytes(name):
    return pathlib.Path(PAGES[name]).read_bytes()


def manifest_line(name):
    data = snap_bytes(name)
    return f"{hashlib.sha256(data).hexdigest()}  {name}.md\n"


def rows(status="mined", opened="2026-10-25", usedby=ENTRY_PATH, pages=("best-practices", "using-scripts", "quickstart")):
    out = ""
    for page in pages:
        out += REG_ROWS.split("\n")[["best-practices", "using-scripts", "quickstart"].index(page)].format(
            status=status, opened=opened, usedby=usedby) + "\n"
    return out


def entry_text(sources=ENTRY_SOURCES, body=ENTRY_BODY):
    # the counter's entry_head() reads the provenance trio at the very top:
    # leading source: lines, then verified-at:, then recheck:.  A heading first
    # makes (a) fail, so the title and prose follow the trio.
    return sources + "\n" + ENTRY_TITLE + body


def build_world(name, files, entry=True):
    """files: dict path->bytes/str; returns patch text."""
    run(["git", "-C", str(W), "reset", "-q", "--hard", BASE])
    run(["git", "-C", str(W), "clean", "-fdxq"])
    for rel, data in files.items():
        p = pathlib.Path(W) / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(data, str):
            p.write_text(data, encoding="utf-8")
        else:
            p.write_bytes(data)
    run(["git", "-C", str(W), "add", "-A"])
    patch = run(["git", "-C", str(W), "diff", "--cached", BASE])
    return patch


def common(pages=("best-practices", "using-scripts", "quickstart"), skill=SKILL_BLOCK,
           province=PROVINCE_BULLET, entry=ENTRY_PATH, entry_body=None, snap_edit=None,
           entry_override=None):
    files = {}
    if entry:
        files[entry] = entry_override if entry_override is not None else entry_text(body=entry_body or ENTRY_BODY)
    for page in ("best-practices", "using-scripts", "quickstart"):
        data = snap_bytes(page)
        if snap_edit and page in snap_edit:
            data = snap_edit[page](data)
        files[f"{SNAP_DIR}/{page}.md"] = data
    files[f"{SNAP_DIR}/MANIFEST.sha256"] = "".join(manifest_line(p) for p in ("best-practices", "using-scripts", "quickstart"))
    return files


def with_sources(files, new_rows):
    src = base_text("corpus/SOURCES.md")
    files["corpus/SOURCES.md"] = insert_before(src, "\n## Paths\n", new_rows)
    return files


def with_skill(files, block):
    skill = base_text("SKILL.md")
    files["SKILL.md"] = insert_before(skill, "\n## Trigger-fidelity checklist\n", block)
    return files


def with_province(files, bullet):
    prov = base_text("PROVINCE.md")
    files["PROVINCE.md"] = insert_before(prov, "\n## Frontier\n", bullet)
    return files


W = None


def main():
    global W
    scratch = os.environ.get("W74_SCRATCH")
    if not scratch:
        sys.exit("set W74_SCRATCH to a fresh scratch dir")
    W = pathlib.Path(scratch) / "worldwork"
    if W.exists():
        sys.exit(f"{W} exists; use a fresh W74_SCRATCH")
    run(["git", "clone", "--shared", "-q", "--no-checkout", str(LANE), str(W)])
    run(["git", "-C", str(W), "checkout", "-q", BASE])

    OUT.mkdir(parents=True, exist_ok=True)

    worlds = {}

    # w00 — positive control: everything honest, 3 of 3.
    f = common()
    with_sources(f, rows())
    with_skill(f, SKILL_BLOCK)
    with_province(f, PROVINCE_BULLET)
    worlds["w00-honest-full"] = dict(
        files=f, census=0, expected="3 of 3, exit 0",
        change="every conjunct honest: entry with the 6-column rule table, three `mined` tier-A registry rows opened 2026-10-25, three snapshots pinned in the manifest, six SKILL rows with the token inside each action cell, PROVINCE Core bullet.",
        defeats="none — the positive control; if this world reads below 3 the counter is wrong (plan kill rule).")

    # w01 — staged entry copied unchanged, staged ids, no registry rows.
    f = common(entry_override=STAGED_ENTRY.read_text())
    with_skill(f, SKILL_BLOCK)
    with_province(f, PROVINCE_BULLET)
    worlds["w01-staged-entry"] = dict(
        files=f, census=0, expected="0 of 3, exit 1",
        change="the staged package entry `knowledge/corpus/knowledge/spec-script-craft-rules.md` copied unchanged to the frozen entry path (it cites staged S236/S237), no S### registry rows added for this round.",
        defeats="(a) each page has no rule-table row, and (b) the cited ids have no 11-cell registry row with status `mined`.")

    # w02 — rows appended with status queued.
    f = common()
    with_sources(f, rows(status="queued"))
    with_skill(f, SKILL_BLOCK)
    with_province(f, PROVINCE_BULLET)
    worlds["w02-queued-status"] = dict(
        files=f, census=0, expected="0 of 3, exit 1",
        change="the same three rows appended with status `queued` instead of `mined`.",
        defeats="(b) status is `queued`, so no page is backed — form-complete, admission-not-made.")

    # w03 — invented token absent from its snapshot.
    body = ENTRY_BODY.replace(
        "`references/api-errors.md`; `python scripts/migrate.py --verify --backup`",
        "`references/api-errors.md`; `--frobnicate-index .`")
    f = common(entry_body=body)
    with_sources(f, rows())
    with_skill(f, SKILL_BLOCK)
    with_province(f, PROVINCE_BULLET)
    worlds["w03-invented-token"] = dict(
        files=f, census=0, expected="2 of 3, exit 1",
        change="the S223 row's second token is `--frobnicate-index .`, invented and absent from the best-practices snapshot.",
        defeats="(a) for best-practices: a rule token does not locate word-bounded in the snapshot.")

    # w04 — snapshot hand-edited, manifest pin left.
    def edit_quickstart(data):
        old = b"VS Code looks for skills in `.agents/skills/` by default."
        new = b"VS Code looks for skills in `.agents/skills/` by convention."
        assert old in data
        return data.replace(old, new)

    f = common(snap_edit={"quickstart": edit_quickstart})
    with_sources(f, rows())
    with_skill(f, SKILL_BLOCK)
    with_province(f, PROVINCE_BULLET)
    worlds["w04-snapshot-edited"] = dict(
        files=f, census=0, expected="exit 2, no score line (below 3)",
        change="the quickstart snapshot's `by default` hand-edited to `by convention`; the manifest keeps the fetched sha256.",
        defeats="(c) sha256 of the snapshot no longer equals the manifest pin — the counter must exit 2, not score.")

    # w05 — SKILL rows cite best-practices with quickstart-only tokens.
    f = common()
    with_sources(f, rows())
    with_skill(f, SKILL_CROSS_PAGE)
    with_province(f, PROVINCE_BULLET)
    worlds["w05-cross-page-tokens"] = dict(
        files=f, census=0, expected="2 of 3, exit 1",
        change="the two SKILL.md rows citing `best-practices (S223)` carry `.agents/skills/...` tokens that occur only in the quickstart snapshot (real text, wrong page — Q37).",
        defeats="(e) for best-practices: no row citing S223 has an action-cell token of its own snapshot.")

    # w06 — token-stuffed entry row for using-scripts.
    body = ENTRY_BODY.replace(
        "`uvx ruff@0.8.0 check .`; `pipx run 'black==24.10.0' .`",
        "`pdfplumber`; `pdf2image`; `pypdf`; `PyMuPDF`")
    f = common(entry_body=body)
    with_sources(f, rows())
    with_skill(f, SKILL_BLOCK)
    with_province(f, PROVINCE_BULLET)
    worlds["w06-token-stuffed"] = dict(
        files=f, census=0, expected="2 of 3, exit 1",
        change="the S224 tokens cell carries four real best-practices tokens that are all absent from the using-scripts snapshot (count satisfied, location absent).",
        defeats="(a) for using-scripts: every token of the row must locate in that page's snapshot.")

    # w07 — entry outside corpus/knowledge/.
    moved = "corpus/spec-skill-creation-craft-round74.md"
    f = common(entry=False, province=PROVINCE_BULLET.replace(ENTRY_PATH, moved))
    f[moved] = entry_text()
    with_sources(f, rows(usedby=moved))
    with_skill(f, SKILL_BLOCK)
    worlds["w07-entry-outside"] = dict(
        files=f, census=0, expected="0 of 3, exit 1",
        change="the entry sits at `corpus/spec-skill-creation-craft-round74.md`; registry `used-by` and the PROVINCE bullet name that path.",
        defeats="(a) the frozen entry path `corpus/knowledge/spec-skill-creation-craft-round74.md` does not exist.")

    # w08 — staged rows appended as-is (campaign schema, second header, prose recheck).
    f = common()
    staged = STAGED_ROWS.read_text()
    src_rows = rows() + staged
    with_sources(f, src_rows)
    with_skill(f, SKILL_BLOCK)
    with_province(f, PROVINCE_BULLET)
    worlds["w08-staged-rows"] = dict(
        files=f, census=1, expected="0 of 3 or exit 2 (below 3)",
        change="the package's `SOURCES.append.md` appended as-is inside `## Registry` (campaign-schema rows, its own header row, prose recheck, ids S203–S3xx that collide with the lane's).",
        defeats="(b) the registry is not census-conformant: E02 on the second header row and E03/E04 on the colliding campaign ids.")

    # w09 — SKILL rows without the entry.
    f = common(entry=False)
    with_skill(f, SKILL_BLOCK)
    with_province(f, PROVINCE_BULLET)
    worlds["w09-skill-rows-only"] = dict(
        files=f, census=0, expected="0 of 3, exit 1",
        change="the SKILL.md subsection is present; the entry file and all three registry rows are absent.",
        defeats="(a)/(f) there is no entry for the rows to act on (the entry-absent branch returns 0 before any manifest access).")

    # w10 — honest for two pages, no quickstart row anywhere.
    body = ENTRY_BODY.replace(
        "| quickstart | S225 | the tutorial's default discovery root | \"VS Code looks for skills in `.agents/skills/` by default.\" | `.agents/skills/`; `.agents/skills/roll-dice/SKILL.md` | Place the skill at `.agents/skills/roll-dice/SKILL.md` before shipping it. |\n", "")
    skill_two = SKILL_BLOCK.replace(
        "| quickstart (S225) | Put the skill at `.agents/skills/roll-dice/SKILL.md` so a compliant client finds it. | `.agents/skills/roll-dice/SKILL.md` |\n"
        "| quickstart (S225) | Keep the one-file skill under `.agents/skills/` and check `roll-dice` appears. | `.agents/skills/` |\n", "")
    f = common(entry_body=body)
    with_sources(f, rows(pages=("best-practices", "using-scripts")))
    with_skill(f, skill_two)
    with_province(f, PROVINCE_BULLET)
    worlds["w10-two-pages"] = dict(
        files=f, census=0, expected="2 of 3, exit 1",
        change="fully honest for best-practices and using-scripts; no quickstart registry row, entry row or SKILL row (its snapshot and pin stay, so the manifest is not tampered).",
        defeats="(a)/(b)/(e) for quickstart only — the reachable two-page boundary, which must read 2 of 3.")

    # w11 — opened set to the staged package's date.
    f = common()
    with_sources(f, rows(opened="2026-10-23"))
    with_skill(f, SKILL_BLOCK)
    with_province(f, PROVINCE_BULLET)
    worlds["w11-opened-staged-date"] = dict(
        files=f, census=0, expected="0 of 3, exit 1",
        change="the three registry rows carry `opened` 2026-10-23, the staged package's fetch date, instead of a round-74 date.",
        defeats="(b) `opened` is not a round-74 date, so the row is not a row opened this round.")

    for name, spec in worlds.items():
        patch = build_world(name, spec["files"])
        d = OUT / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "world.patch").write_text(patch)
        (d / "README.md").write_text(world_readme(name, spec, patch))

    run(["git", "-C", str(W), "reset", "-q", "--hard", BASE])
    run(["git", "-C", str(W), "clean", "-fdxq"])
    print(f"wrote {len(worlds)} worlds under {OUT}")


def measured_scores():
    f = OUT / "scores.txt"
    out = {}
    if f.exists():
        for line in f.read_text().splitlines():
            parts = line.split()
            if len(parts) >= 4:
                out[parts[0]] = " ".join(parts[1:])
    return out


MEASURED = measured_scores()


def world_readme(name, spec, patch):
    files = spec["files"]
    listing = "\n".join(f"- `{k}` ({len(v.encode() if isinstance(v, str) else v)} B)" for k, v in sorted(files.items()))
    return f"""# {name} — round-74 C1 shortcut control

Base: lane `kotoba-shokunin`, branch `master`, rev `{BASE}` (the r73 non-author closure
spot-check commit, r74 plan `329e7d91d7d750031c35d264f0e34af1d0ce8385`). Plan § C1 shortcut
controls. The world is a single patch applied to a **fresh `--shared` clone** of the base in a
fleet-shaped `/tmp` sandbox; the commit exists only inside that clone.

## What it changes

{spec['change']}

Files carried by `world.patch` (complete new content for each):

{listing}

## Predicate clause it defeats and expected score

- expected: **{spec['expected']}**
- defeats: {spec['defeats']}
- census at the applied revision (`scripts/sources-census.sh validate --today 2026-10-26 --file <clone>/corpus/SOURCES.md kotoba`): **exit {spec['census']}**
- measured score: **{MEASURED.get(name, 'not run — counter absent at build time; see ../score-worlds.out')}**

## Replay (exact)

```
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BASE={BASE}
W=<this world dir>
P=$(mktemp -d /tmp/k74w1-fleet-{name}.XXXXXX)
for e in /home/vgpnk/Projects/shokunin/*; do n=$(basename "$e")
  [ "$n" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$n"; done
git clone --shared -q --no-checkout "$L" "$P/kotoba-shokunin"
C=$P/kotoba-shokunin
git -C "$C" checkout -q --detach "$BASE"
[ "$(git -C "$C" rev-parse --show-toplevel)" = "$C" ] || exit 1
git -C "$C" apply --whitespace=nowarn "$W/world.patch"
git -C "$C" add -A
git -C "$C" -c user.name='round-74 C1 control' -c user.email='control@example.invalid' \\
  commit -q -m '{name}: shortcut world on {BASE}'
COUNTER=${{COUNTER:-$L/.ufo/waves/round-74/w1/build/ExecSpecCounterR74/check_spec_craft.py}}
cp "$COUNTER" "$C/_check_spec_craft_ctl.py"
cd "$C" && python3 -B _check_spec_craft_ctl.py --rev HEAD; echo "exit=$?"
```

`{name}/score.stdout.txt` is the counter's own stdout for that run, `{name}/score.stderr.txt` its
stderr (present only for a world in the counter's exit-2 class). `../score-worlds.out` is the whole
table over every world, produced by `../score_worlds.sh`; `../README.md` names the counter sha the
table was measured at.
"""


if __name__ == "__main__":
    main()
