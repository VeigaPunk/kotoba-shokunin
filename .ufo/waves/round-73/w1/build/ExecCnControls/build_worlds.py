#!/usr/bin/env python3
"""Generate the C1 shortcut worlds for kotoba round 73 (plans/round-73.md § C1).

Not a gate and not a claim counter. This script only paints the committed file
bundles a replay copies into a fresh ``--shared`` clone of the base revision:

    _common/tree/      the honest scaffold (frozen entry, six mined rows,
                       six sha256-pinned page snapshots, a manifest)
    <world>/tree/      one overlay per shortcut world, applied on top of
                       _common/tree (world 1 applies on the bare base)

Run:  python3 -B build_worlds.py
Read README.md at the root of this directory for the replay contract and for
the assumption the manifest filename convention rests on.
"""

from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILD_ROOT = HERE.parent
LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
BASE = "072048fa8e8a52c707d25f7079772fa317244eb7"
ENTRY = "corpus/knowledge/chinese-vendor-skill-surfaces-round73.md"
SNAPDIR = ".ufo/waves/round-73/snapshots"
SOURCES = "corpus/SOURCES.md"

# Page snapshots already fetched in this wave by the source-opening seats.
# Copied byte-for-byte; the sha256 recorded below is of these committed bytes.
SNAP_SRC = {
    "S217": "ExecSrcTrae/snapshot.md",
    "S218": "ExecSrcCodebuddyIde/snapshot.md",
    "S219": "ExecSrcCodebuddyCli/snapshot.md",
    "S220": "ExecSrcKimiEn/snapshot.md",
    "S221": "ScoutCnCensus/snap/kimicom.txt",
    "S222": "ExecSrcZhipu/snapshot.md",
}

QUOTES = {
    "S217": ("若你在 TRAE 内创建的技能（位于 `.trae/skills/` 目录）与 "
             "`.agents/skills/` 中的技能重名，系统将优先调用 `.trae/skills/` "
             "目录中的技能。"),
    "S218": ("元数据 (YAML Frontmatter):name 和 description 决定了 AI 何时会使用这个 "
             "Skill。描述需具体说明 Skill 的功能和使用场景。"),
    "S219": ("1. **项目级 Skills**：`.codebuddy/skills/`（项目根目录下） 2. **用户级 "
             "Skills**：`~/.codebuddy/skills/`（用户主目录下）"),
    "S220": ("when a skill name is defined in more than one scope, the more specific "
             "scope wins"),
    "S221": ("模型也可以根据 description 和 whenToUse 自动调用 Skill。"
             "disableModelInvocation 设为 true 或 type 设为 flow 时不自动调用。"
             "Skill 调用最多允许嵌套 3 层，超过后会被终止。"),
    "S222": ("Skill 将领域工作流程、模板和脚本打包给云端 Agent。Agent 先读名称与描述，"
             "再按任务读取正文和配套资料，不必每次把整套方法塞进 system prompt。"),
}

ROW = {
    "S217": dict(
        source="TRAE Docs — 技能（Skill） — https://docs.trae.cn/ide_skills",
        tier="B",
        scope=("ByteDance TRAE IDE skill discovery roots, the rules-vs-skills split and "
               "the `.agents` toggle; one vendor's implementation, tier B"),
        anchor=("§ 使用 .agents 技能目录 through the user-root bullets; "
                f"quote \"{QUOTES['S217']}\"; page text fetched 2026-10-25"),
        teaches=("TRAE reads `.trae/skills/` and `~/.trae-cn/skills` and can read the "
                 "shared `.agents/skills/` root; `.trae/skills/` wins a name collision"),
    ),
    "S218": dict(
        source=("腾讯云代码助手 CodeBuddy Docs — Skills — "
                "https://www.codebuddy.ai/docs/zh/ide/Features/Skills"),
        tier="B",
        scope=("Tencent CodeBuddy IDE skill structure and the metadata/body disclosure "
               "budget; IDE page only, tier B"),
        anchor=("§ Skill 的结构 and § 渐进式披露设计原则; "
                f"quote \"{QUOTES['S218']}\"; page text fetched 2026-10-25"),
        teaches=("CodeBuddy's IDE requires `name` and `description`, takes optional "
                 "`allowed-tools`, and builds skills under `.codebuddy/skills/`"),
    ),
    "S219": dict(
        source=("腾讯云代码助手 CodeBuddy Docs — CodeBuddy Code Skills（技能系统） — "
                "https://www.codebuddy.ai/docs/zh/cli/skills"),
        tier="B",
        scope=("Tencent CodeBuddy CLI skill roots and frontmatter example; CLI page only, "
               "tier B"),
        anchor=("§ 目录结构 and § SKILL.md 格式; "
                f"quote \"{QUOTES['S219']}\"; page text fetched 2026-10-25"),
        teaches=("the CodeBuddy CLI reads `.codebuddy/skills/` and `~/.codebuddy/skills/` "
                 "and its frontmatter example uses hyphenated `allowed-tools`"),
    ),
    "S220": dict(
        source=("Kimi Code CLI Docs — Agent Skills — "
                "https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md"),
        tier="B",
        scope=("Moonshot Kimi Code CLI discovery roots and description resolution; English "
               "GitHub doc, tier B"),
        anchor=("§ Skill discovery through § Description resolution; "
                f"quote \"{QUOTES['S220']}\"; file read from main 2026-10-25"),
        teaches=("Kimi Code CLI injects names, paths and descriptions into the system "
                 "prompt and resolves project over user over extra over built-in"),
    ),
    "S221": dict(
        source=("Kimi Code 文档 — Agent Skills — "
                "https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html"),
        tier="B",
        scope=("The Chinese-language Kimi Code skill page: `.kimi-code/skills/` roots, "
               "`whenToUse` and `type`; tier B"),
        anchor=("§ Skill 存放位置 and § 调用 Skill; "
                f"quote \"{QUOTES['S221']}\"; page text fetched 2026-10-25"),
        teaches=("Kimi's Chinese page reads `.kimi-code/skills/` and `$KIMI_CODE_HOME/skills/`, "
                 "adds `whenToUse`, and nests skill calls at most three levels"),
    ),
    "S222": dict(
        source=("智谱 AI 开放文档 — Agent Skills — "
                "https://docs.bigmodel.cn/cn/managed-agents/skills.md"),
        tier="B",
        scope=("Zhipu managed-agents skill packaging, upload and runtime placement; one "
               "vendor's implementation, tier B"),
        anchor=("§ 选择内置或自定义 Skill and § 挂载到 Agent; "
                f"quote \"{QUOTES['S222']}\"; page text fetched 2026-10-25"),
        teaches=("Zhipu keeps a skill out of the system prompt: the agent reads name and "
                 "description, then `/workspace/skills/<name>/` on demand"),
    ),
}

ENTRY_SOURCE_LINE = {
    "S217": ("source: S217 — TRAE Docs 技能（Skill） — https://docs.trae.cn/ide_skills — "
             f"located quote \"{QUOTES['S217']}\" — retrieved 2026-10-25"),
    "S218": ("source: S218 — CodeBuddy Docs Skills（IDE） — "
             "https://www.codebuddy.ai/docs/zh/ide/Features/Skills — "
             f"located quote \"{QUOTES['S218']}\" — retrieved 2026-10-25"),
    "S219": ("source: S219 — CodeBuddy Code Skills（CLI） — "
             "https://www.codebuddy.ai/docs/zh/cli/skills — "
             f"located quote \"{QUOTES['S219']}\" — retrieved 2026-10-25"),
    "S220": ("source: S220 — Kimi Code CLI Agent Skills (English) — "
             "https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md "
             f"— located quote \"{QUOTES['S220']}\" — file read from main 2026-10-25"),
    "S221": ("source: S221 — Kimi Code 文档 Agent Skills — "
             "https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html — "
             f"located quote \"{QUOTES['S221']}\" — retrieved 2026-10-25"),
    "S222": ("source: S222 — 智谱 AI 开放文档 Agent Skills — "
             "https://docs.bigmodel.cn/cn/managed-agents/skills.md — "
             f"located quote \"{QUOTES['S222']}\" — retrieved 2026-10-25"),
}

# vendor table rows: (vendor, ids, placement tokens, frontmatter key tokens, note)
VENDOR_ROWS = [
    ("TRAE", "S217", (".trae/skills/", "~/.trae-cn/skills", ".agents/skills/"),
     ("name", "description"), "rules always load, skills on demand"),
    ("CodeBuddy", "S218, S219", (".codebuddy/skills/", "~/.codebuddy/skills/"),
     ("name", "description", "allowed-tools"), "IDE + CLI share the hyphenated spelling"),
    ("Kimi Code", "S220, S221", (".kimi-code/skills/", ".agents/skills/"),
     ("name", "description", "whenToUse"), "project over user over extra over built-in"),
    ("Zhipu", "S222", ("/workspace/skills/",), ("name", "description", "type:zai"),
     "uploaded package, read on demand, never injected"),
]


def entry_text(vendor_rows=VENDOR_ROWS, extra_note=""):
    rows = []
    for vendor, ids, roots, keys, note in vendor_rows:
        rows.append("| %s | %s | %s | %s | %s |" % (
            vendor, ids,
            ", ".join("`%s`" % t for t in roots),
            ", ".join("`%s`" % t for t in keys), note))
    out = [ENTRY_SOURCE_LINE[s] for s in ("S217", "S218", "S219", "S220", "S221", "S222")]
    out += [
        "verified-at: 2026-10-25",
        ("recheck: 60d — re-fetch all six pages and re-count each vendor's discovery "
         "roots and frontmatter keys, confirming none has silently changed (ran 2026-10-25)"),
        "ground: round-73 Q1 — which Chinese-vendor clients expose an Agent Skills surface",
        "",
        "# Four Chinese-vendor skill surfaces: discovery roots, frontmatter vocabulary, placement",
        "",
        "All six pages were re-opened this round. The vendor table carries one row per",
        "vendor; the tokens in a row are the placement paths and frontmatter keys that",
        "row's cited page states.",
        "",
        "| vendor | source ids | placement tokens | frontmatter keys | note |",
        "|---|---|---|---|---|",
    ] + rows + [
        "",
        "**The practical hazard is the placement split, not the file format.** TRAE,",
        "CodeBuddy and Kimi Code all read a skill body from a directory and name it from",
        "`description`; Zhipu uploads a package and reads `/workspace/skills/` on demand",
        "instead of injecting the body. A skill copied between them keeps its frontmatter",
        "and loses the placement or the key spelling the target client reads.",
        "",
        "**Two live divergences the six pages carry.** TRAE's international user root does",
        "not appear in the page text fetched this round (only the domestic",
        "`~/.trae-cn/skills`); Kimi's English page names `.kimi/skills/` while the Chinese",
        "page names `.kimi-code/skills/`. Both are recorded as observations, not fixed",
        "values: the census decides which vendors the live pages back.",
        "",
        "## Gate",
        "",
        "- all six pages re-fetched 2026-10-25; quotes above are copied from the",
        "  committed snapshots under `.ufo/waves/round-73/snapshots/`",
        "- one row per vendor; no vendor is backed by a token its cited page lacks",
    ]
    if extra_note:
        out.append(extra_note)
    return "\n".join(out) + "\n"


SOURCES_ROW = ("| {sid} | {source} | docs | {tier} | {scope} | {anchor} | {teaches} | "
               "mined | 2026-10-25 | 60d | {usedby} |")


def sources_rows(status="mined", usedby=ENTRY):
    out = []
    for sid in ("S217", "S218", "S219", "S220", "S221", "S222"):
        r = ROW[sid]
        line = SOURCES_ROW.format(sid=sid, source=r["source"], tier=r["tier"],
                                  scope=r["scope"], anchor=r["anchor"],
                                  teaches=r["teaches"], usedby=usedby)
        if status != "mined":
            line = line.replace(" | mined | ", " | %s | " % status, 1)
        out.append(line)
    return out


def base_sources():
    import subprocess
    return subprocess.run(
        ["git", "-C", str(LANE), "show", BASE + ":" + SOURCES],
        check=True, capture_output=True).stdout.decode("utf-8")


def append_rows(base, rows):
    lines = base.splitlines()
    idx = next(i for i, ln in enumerate(lines) if ln.startswith("## Paths"))
    return "\n".join(lines[:idx] + rows + [""] + lines[idx:]) + "\n"


def put(root: Path, rel: str, data):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, bytes):
        p.write_bytes(data)
    else:
        p.write_text(data, encoding="utf-8")


def main():
    build = HERE
    scratch = Path("/tmp") / "k73w1-ExecCnControls-snaps"
    if scratch.exists():
        shutil.rmtree(scratch)
    scratch.mkdir(parents=True)

    # 1. snapshots (byte-for-byte copies of the wave's fetched page text)
    pins = {}
    for sid, rel in SNAP_SRC.items():
        data = (BUILD_ROOT / rel).read_bytes()
        put(scratch, sid + ".page", data)
        pins[sid] = hashlib.sha256(data).hexdigest()

    manifest = "".join("%s  %s.page\n" % (pins[s], s) for s in sorted(pins))

    # 2. honest scaffold
    common = build / "_common"
    if common.exists():
        shutil.rmtree(common)
    put(common, "tree/" + ENTRY, entry_text())
    put(common, "tree/" + SOURCES, append_rows(base_sources(), sources_rows()))
    for sid in SNAP_SRC:
        put(common, "tree/%s/%s.page" % (SNAPDIR, sid),
            (scratch / (sid + ".page")).read_bytes())
    put(common, "tree/%s/MANIFEST.sha256" % SNAPDIR, manifest)

    # 3. worlds
    for name in [d for d in build.iterdir() if d.is_dir() and d.name[0].isdigit()]:
        shutil.rmtree(name)

    staged_entry = Path("/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/"
                        "knowledge/chinese-client-skill-surfaces.md").read_text(encoding="utf-8")
    staged_rows = []
    staged_lines = Path("/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md"
                        ).read_text(encoding="utf-8").splitlines()
    for n in (18, 20, 21, 22, 23, 25):
        staged_rows.append(staged_lines[n - 1])

    # world 1: staged entry unchanged, staged ids, no registry rows
    w = build / "1-staged-entry-unchanged"
    put(w, "tree/" + ENTRY, staged_entry)

    # world 2: honest set, rows appended with status queued
    w = build / "2-rows-queued"
    put(w, "tree/" + SOURCES,
        append_rows(base_sources(), sources_rows(status="queued")))

    # world 3: honest set, TRAE row carries an invented root absent from S217.page
    w = build / "3-invented-root"
    rows = list(VENDOR_ROWS)
    rows[0] = ("TRAE", "S217", (".bytedance/skills/", "~/.trae-cn/skills",
                                ".agents/skills/"),
               ("name", "description"), "rules always load, skills on demand")
    put(w, "tree/" + ENTRY, entry_text(vendor_rows=rows))

    # world 4: honest set, S217.page hand-edited after the manifest was pinned
    w = build / "4-tampered-snapshot"
    edited = (scratch / "S217.page").read_bytes() + (
        "\n<!-- appended after the manifest pin: the sentence below is not in the "
        "fetched page -->\nTRAE also reads `.bytedance/skills/`.\n").encode()
    put(w, "tree/%s/S217.page" % SNAPDIR, edited)

    # world 5: honest set, one token-stuffed vendor row (9 tokens, one invented)
    w = build / "5-token-stuffed"
    rows = list(VENDOR_ROWS)
    rows[0] = ("TRAE", "S217",
               (".trae/skills/", "~/.trae-cn/skills", ".agents/skills/",
                "~/.trae/skills/"),
               ("name", "description"),
               "rules always load, skills on demand; `.trae/skills/` wins on names")
    put(w, "tree/" + ENTRY, entry_text(vendor_rows=rows))

    # world 6: honest set, entry placed outside corpus/knowledge/ (rows follow it)
    w = build / "6-entry-outside-knowledge"
    moved = "corpus/chinese-vendor-skill-surfaces-round73.md"
    put(w, "tree/" + moved, entry_text())
    put(w, "tree/" + SOURCES,
        append_rows(base_sources(), sources_rows(usedby=moved)))

    # world 7: staged rows appended as-is (campaign schema), staged entry
    w = build / "7-staged-rows-as-is"
    put(w, "tree/" + ENTRY, staged_entry)
    put(w, "tree/" + SOURCES, append_rows(base_sources(), staged_rows))
    staged_pins = {"S214": pins["S217"], "S216": pins["S218"], "S217": pins["S219"],
                   "S218": pins["S220"], "S219": pins["S221"], "S221": pins["S222"]}
    for sid, srcsid in (("S214", "S217"), ("S216", "S218"), ("S217", "S219"),
                        ("S218", "S220"), ("S219", "S221"), ("S221", "S222")):
        put(w, "tree/%s/%s.page" % (SNAPDIR, sid), (scratch / (srcsid + ".page")).read_bytes())
    put(w, "tree/%s/MANIFEST.sha256" % SNAPDIR,
        "".join("%s  %s.page\n" % (staged_pins[s], s) for s in sorted(staged_pins)))

    print("pins:")
    for s in sorted(pins):
        print(" ", s, pins[s])




# --------------------------------------------------------------------------
# READMEs: every world carries its own replay steps, the conjunct it is built
# to break, and the reading the plan's predicate predicts.

REPLAY = """\
## Replay (fresh `--shared` clone of the base; git writes only inside the sandbox)

```sh
# 1. fleet-shaped sandbox: symlink every fleet-root entry except the lane
P=$(mktemp -d /tmp/k73fleet-<you>.XXXX)
for e in /home/vgpnk/Projects/shokunin/*; do
  b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$b"
done

# 2. a fresh shared clone at the frozen base, checked out on a throwaway branch
git clone --shared -q --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin \\
    "$P/kotoba-shokunin"
R=$P/kotoba-shokunin
git -C "$R" checkout -q -B world 072048fa8e8a52c707d25f7079772fa317244eb7
[ "$(git -C "$R" rev-parse --show-toplevel)" = "$R" ] || exit 1

# 3. apply the bundles (B = this bundle root; adjust the path if you copied it)
B=/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ExecCnControls
{apply}
# 4. commit with a throwaway identity inside the sandbox only
git -C "$R" add -A
git -C "$R" -c user.name=<seat> -c user.email=<seat>@localhost commit -q -m "{world}"

# 5. read it
REV=$(git -C "$R" rev-parse HEAD)
python3 -B "$B/own-reading.py" --repo "$R" --rev "$REV"
python3 -B "$B/../ExecCnCounter/check_cn_vendor_surfaces.py" --repo "$R" --rev "$REV"
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \\
     --file "$R/corpus/SOURCES.md" --today "$(date -I)"
```

`bash replay.sh {world}` from the parent directory performs exactly these steps.
If the counter draft's `SELF_SHA` is still all zeros it exits 2 with
`counter drifted`; replay.sh then runs a local copy with the value
`--print-self-sha` reports filled in, and the draft itself is never edited here.
"""

WORLDS = {
    "1-staged-entry-unchanged": dict(
        title="staged entry, unchanged, with staged ids and no registry rows",
        defect=("the assimilation package's entry copied byte-for-byte to the frozen path: "
                "a `# ` title precedes the `source:` lines (so the entry does not open with "
                "them), the ids are the package's S214/S216/S217/S218/S219/S221, no registry "
                "row exists at all, and no snapshot or manifest is committed"),
        conjunct="(a) entry trio; (b) registry rows; (c) pinned snapshots",
        reading="0 of 4, exit 1 (counter stops at the entry-level trio)",
        apply='cp -a "$B/1-staged-entry-unchanged/tree/." "$R"/',
        extra=("[`_common`](../_common/README.md) is deliberately NOT applied: a porter who "
               "dropped the package in would not have built the registry or the snapshots "
               "either.\n"),
    ),
    "2-rows-queued": dict(
        title="honest entry and pinned snapshots, rows appended with status queued",
        defect=("the six new rows are well-formed 11-cell rows with the right hosts, tiers and "
                "`used-by`, but every status cell reads `queued`"),
        conjunct="(b) status `mined`",
        reading="0 of 4, exit 1",
        apply='cp -a "$B/_common/tree/." "$R"/\ncp -a "$B/2-rows-queued/tree/." "$R"/',
        extra=("The census accepts this registry (exit 0): `queued` is a legal status, so an "
               "unmined row is invisible to the schema gate.\n"),
    ),
    "3-invented-root": dict(
        title="honest set, one vendor row carries an invented root",
        defect=("the TRAE row's discovery-root cell names `.bytedance/skills/`, a path that does "
                "not occur in `S217.page`; every other token, row and pin is honest"),
        conjunct="(a) token occurrence",
        reading="3 of 4, exit 1 (TRAE fails)",
        apply='cp -a "$B/_common/tree/." "$R"/\ncp -a "$B/3-invented-root/tree/." "$R"/',
        extra="",
    ),
    "4-tampered-snapshot": dict(
        title="honest set, one snapshot hand-edited after the manifest pin",
        defect=("`S217.page` gains an appended comment and a sentence naming "
                "`.bytedance/skills/`; `MANIFEST.sha256` keeps the pre-edit pin"),
        conjunct="(c) sha256 pin",
        reading="exit 2, cannot evaluate (not a number)",
        apply='cp -a "$B/_common/tree/." "$R"/\ncp -a "$B/4-tampered-snapshot/tree/." "$R"/',
        extra=("The counter must exit 2 here, never 0 and never a content 3 of 4: a tampered "
               "snapshot is an unreadable input, not a vendor that fails.\n"),
    ),
    "5-token-stuffed": dict(
        title="honest set, one token-stuffed vendor row",
        defect=("the TRAE row adds `~/.trae/skills/` to its roots. The page states the project "
                "root `.trae/skills/` and the user root `~/.trae-cn/skills`; it never states an "
                "international `~/.trae/skills/` (0 occurrences in `S217.page`)"),
        conjunct="(a) token occurrence, under the counter's token shaping",
        reading=("3 of 4, exit 1 by this bundle's own reading (the token, as written, is absent); "
                 "the wave-1 counter draft reads 4 of 4, exit 0 — a kill-rule hit"),
        apply='cp -a "$B/_common/tree/." "$R"/\ncp -a "$B/5-token-stuffed/tree/." "$R"/',
        extra=("Why the counter passes it: `token_forms()` (counter lines 337-346 in draft sha256 `051d3e2d…`) also tries the "
               "token with a leading `~/` removed, so `~/.trae/skills/` is backed by the "
               "snapshot's `.trae/skills/` — the project root standing in for a user root. The "
               "one-line delta that clears it: drop the `~/`-strip form (keep only the "
               "trailing-slash form); the token then reads absent, exactly as written.\n"),
    ),
    "6-entry-outside-knowledge": dict(
        title="honest set, entry filed at corpus/ instead of corpus/knowledge/",
        defect=("the entry file is `corpus/chinese-vendor-skill-surfaces-round73.md`; every "
                "registry `used-by` cell names the moved path, so the registry stays "
                "census-clean and (b) passes on its own terms"),
        conjunct="(a) the frozen entry path",
        reading="0 of 4, exit 1 (counter: frozen path absent)",
        apply=('cp -a "$B/_common/tree/." "$R"/\ncp -a "$B/6-entry-outside-knowledge/tree/." "$R"/\n'
               'rm -f "$R/corpus/knowledge/chinese-vendor-skill-surfaces-round73.md"'),
        extra=("This is the world a path-globbing counter fails: the only defect is where the "
               "entry sits, and the census cannot see it (exit 0).\n"),
    ),
    "7-staged-rows-as-is": dict(
        title="staged rows appended as-is in campaign schema",
        defect=("the six package rows (S214, S216, S217, S218, S219, S221) appended verbatim to "
                "the lane's registry under the staged entry; their `recheck` cells are prose, "
                "their `used-by` cells name package paths that do not exist in the lane, and "
                "S214/S216 collide with lane rows"),
        conjunct="(b) plus the registry schema",
        reading="0 of 4, exit 1; census exit 1",
        apply='cp -a "$B/7-staged-rows-as-is/tree/." "$R"/',
        extra=("Observed schema findings on the committed sandbox tree: E03 x2 (S214, S216 already "
               "in the lane), E09 x6 (every row's `recheck` is prose), E11 x15 (`used-by` package "
               "paths missing), W04 x20 (pre-existing) — exit 1. Running `--file` against this "
               "bundle's partial `tree/corpus/SOURCES.md` also exits 1 but reports 228 E11, "
               "because the bundle carries no `SKILL.md` and no `corpus/knowledge/` files; use the "
               "sandbox copy for attributable findings. The staged rows carry 11 cells and no "
               "escaped pipe (`grep -c '\\\\|'` over the six lines is 0), so the campaign schema's "
               "defect here is prose cells and package paths, not an escaped pipe.\n"),
    ),
}

ROOT_README = """\
# C1 shortcut worlds — ExecCnControls (kotoba round 73, wave 1)

Seven committed worlds for the frozen C1 predicate in
`plans/round-73.md` § C1. Each world is the cheapest input that would satisfy a
counter reading only the *form* of the predicate; each must read below 4 of 4.

**Headline.** Six of the seven worlds score below 4 of 4 under both readers.
World 5 does not: the wave-1 counter draft
(`../ExecCnCounter/check_cn_vendor_surfaces.py`) reads **4 of 4, exit 0** on it,
because `token_forms()` strips a leading `~/`, letting the project root
`.trae/skills/` back the never-stated user root `~/.trae/skills/`. Under the
plan's kill rule (“any shortcut world scoring 4 means the counter is wrong;
fixed before data”) the counter needs that one-line fix before any seat scores
C1 data.

| world | conjunct attacked | own reading | counter draft |
|---|---|---|---|
| base (do-nothing) | — | 0 of 4, exit 1 | 0 of 4, exit 1 |
| 1-staged-entry-unchanged | (a) trio, (b), (c) | 0 of 4, exit 1 | 0 of 4, exit 1 |
| 2-rows-queued | (b) status | 0 of 4, exit 1 | 0 of 4, exit 1 |
| 3-invented-root | (a) token | 3 of 4, exit 1 | 3 of 4, exit 1 |
| 4-tampered-snapshot | (c) pin | exit 2 | exit 2 |
| 5-token-stuffed | (a) token | 3 of 4, exit 1 | **4 of 4, exit 0** |
| 6-entry-outside-knowledge | (a) frozen path | 0 of 4, exit 1 | 0 of 4, exit 1 |
| 7-staged-rows-as-is | (b) + schema | 0 of 4, exit 1 | 0 of 4, exit 1 |

## Layout

    _common/tree/            honest scaffold: frozen entry, six mined rows,
                             six sha256-pinned snapshots, MANIFEST.sha256
    <world>/tree/            one overlay per world (lane-relative paths)
    <world>/README.md        the world's defect, conjunct, reading, replay
    own-reading.py           an independent re-read of the four conjuncts
    replay.sh                replays a world in a fresh fleet-shaped sandbox
    readings.txt             measured output of `bash replay.sh` (all worlds)

World 1 and world 7 are applied on the bare base (they carry the staged entry,
no scaffold); worlds 2-6 apply `_common/tree` first and then their overlay.
World 6 additionally deletes the frozen-path entry after copying.

`_common` is the honest baseline, not a candidate submission: it reads 4 of 4
in both readers and its registry is census-clean (exit 0, 20 pre-existing W04
warnings), which is what makes each world's failure attributable to its own
defect. It is also what the real entry/rows must still look like when the Scribe
lands them; only the L1 decides whether to reuse any of this text.

## Assumptions a reviewer must check

1. **Snapshot file names.** Pin table convention: `<S###>.page` under
   `.ufo/waves/round-73/snapshots/` (the lane's round-59/round-60 convention),
   with `MANIFEST.sha256` lines `<sha256>  <bare filename>`. The counter's
   `snapshot_name()` resolves a cited id by that filename prefix, so a manifest
   that pinned repo-root-relative paths would need the counter and the manifest
   changed together.
2. **Quote placement.** Each `source: S###` line carries one
   `located quote "…"` span (the lane's r67-r72 convention and the counter's
   `quote_for()`), 5-25 whitespace-separated words, verbatim from the snapshot
   after whitespace collapse only.
3. **Snapshots are byte copies of this wave's fetches** (`SNAP_SRC` in
   `build_worlds.py`): ExecSrcTrae, ExecSrcCodebuddyIde, ExecSrcCodebuddyCli,
   ExecSrcKimiEn and ExecSrcZhipu page texts, plus ScoutCnCensus's Kimi Chinese
   page text. Their sha256 values are the pins in `MANIFEST.sha256`.
4. **`own-reading.py` is not the counter.** It reads the four conjuncts
   independently so a disagreement is visible. Where it disagrees with the
   counter draft, the counter wins until the plan says otherwise — except that
   the plan's kill rule (world 5) is exactly such a case.
"""



COMMON_README_HEAD = """\
# `_common` — the honest scaffold, not a candidate submission

This tree is applied first by worlds 2-6. It is the baseline the shortcut
worlds perturb: one entry at the frozen path, six `mined` registry rows, six
sha256-pinned page snapshots and their manifest. It reads **4 of 4** (exit 0)
under both `own-reading.py` and the wave-1 counter draft, and its registry is
census-clean (exit 0, the 20 pre-existing W04 warnings only) — so each world's
failure is attributable to that world's defect.

The lane's real entry is the Scribe's to write; the text here exists only to
give the worlds a satisfying baseline. Nothing in the lane was edited.

## Files

    tree/corpus/knowledge/chinese-vendor-skill-surfaces-round73.md
    tree/corpus/SOURCES.md                        (base + six rows under ## Registry)
    tree/.ufo/waves/round-73/snapshots/S217.page … S222.page
    tree/.ufo/waves/round-73/snapshots/MANIFEST.sha256

## Snapshot provenance (byte copies; sha256 of the committed bytes)

| commit id | copied from (wave-1 build artifact) | bytes | sha256 |
|---|---|---|---|
"""
COMMON_README_TAIL = """
The copied artifacts are those seats' own fetches of this wave; this scaffold
does not re-fetch anything and makes no claim about the pages. S221 is the
scout's text extraction (HTML shell included), so its quote sits further into
the file than the other five.

## Manifest convention (an assumption a reviewer must check)

`MANIFEST.sha256` lines are `<sha256>  <bare filename>` and the files sit under
`.ufo/waves/round-73/snapshots/` (the round-59/round-60 `<S###>.page`
convention). The counter draft resolves a cited id by that filename prefix; a
manifest that pinned repo-root-relative paths would need both changed together.
"""


def write_readmes(build: Path):
    for name, w in WORLDS.items():
        body = ["# World %s — %s\n" % (name.split("-", 1)[0], w["title"]),
                "Defect: %s.\n" % w["defect"],
                "Conjunct under test: **%s**.\n" % w["conjunct"],
                "Predicted reading (plan's predicate): **%s**.\n" % w["reading"],
                "## Bundle\n",
                "    tree/      the overlay copied over the sandbox worktree\n",
                REPLAY.format(apply=w["apply"], world=name),
                "\n", w["extra"]]
        put(build / name, "README.md", "\n".join(body))
    put(build, "README.md", ROOT_README)
    rows = []
    for sid in sorted(pins_of()):
        data = (build / "_common/tree" / SNAPDIR / (sid + ".page")).read_bytes()
        rows.append("| %s | `%s` | %d | `%s` |" % (
            sid, SNAP_SRC[sid], len(data), hashlib.sha256(data).hexdigest()))
    put(build / "_common", "README.md",
        COMMON_README_HEAD + "\n".join(rows) + "\n" + COMMON_README_TAIL)


def pins_of():
    return list(SNAP_SRC)


# call it from main
_orig_main = main
def main():          # noqa: F811 - wrap the generator with the README pass
    _orig_main()
    write_readmes(HERE)


if __name__ == "__main__":
    main()
