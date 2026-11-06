#!/usr/bin/env python3
"""Probe: does each c1 mutant change a box status/verdict? (CriticClaimR98, scratch only)"""
import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path

SRC = Path(sys.argv[1])  # honest instrument path
MUT = {
    "t01": ('ROUND_FILE_RE = re.compile(r"^(?P<lane>.+)-round-(?P<round>\\d+)\\.md$")',
            'ROUND_FILE_RE = re.compile(r"^(?P<lane>.+)-round-(?P<round>\\d+)\\.md")'),
    "t02": ("dirs = sorted({r for r, _s in paths})",
            "dirs = sorted({r for r, _s in paths})[:1]"),
    "t03": ('    for f in result["files"]:', '    for f in result["files"][:1]:'),
    "t04": ('        if entry.get("disposition") != want:',
            '        if entry.get("disposition") is None:'),
    "t05": ("        if live.get(cid) != pinned:", "        if live.get(cid) is None:"),
    "t06": ("        if m and m.group(1)[0] * 3 == fence:", "        if m:"),
    "t07": ("    if legacy.is_file():", "    if legacy.exists():"),
    "t08": ('    """The dispatch.04 box over the prompts directory."""\n'
            "    names = sorted(p.name for p in prompts_dir.iterdir() if p.is_file())",
            '    """The dispatch.04 box over the prompts directory."""\n'
            "    names = sorted(p.name for p in prompts_dir.iterdir() if True)"),
    "t09": ('        if stem.endswith(".md"):',
            '        if stem.endswith(".md") or stem.endswith(".MD"):'),
}


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fixture(root: Path, prompt: str, fname: str = "kote-round-7.md",
            baseline: str | None = "9\n", legacy_dir: bool = False,
            extra: dict[str, str] | None = None) -> Path:
    case = root / ("case-%d" % len(list(root.iterdir())))
    (case / "prompts").mkdir(parents=True)
    (case / "state").mkdir()
    (case / "fleet" / "kote-shokunin").mkdir(parents=True)
    (case / "prompts" / fname).write_text(prompt, encoding="utf-8")
    if baseline is not None:
        (case / "state" / "kote.report-baseline").write_text(baseline, encoding="utf-8")
    if legacy_dir:
        (case / "state" / "kote.round").mkdir()
    for n, t in (extra or {}).items():
        (case / "prompts" / n).write_text(t, encoding="utf-8")
    return case


def run(mod, case: Path):
    out = {}
    for cid, fn in (("dispatch.04", mod.evaluate_dispatch_04),
                    ("dispatch.08", mod.evaluate_dispatch_08)):
        try:
            r = fn(case / "prompts", case / "state", case / "fleet")
            out[cid] = {"status": r["status"], "evaluated": r["evaluated"],
                        "files": [(f["file"], f["verdict"],
                                   {k: v["status"] for k, v in f["conjuncts"].items()})
                                  for f in r["files"]]}
        except Exception as exc:
            out[cid] = {"raised": "%s: %s" % (exc.__class__.__name__, exc)}
    return out


def main() -> int:
    honest = load(SRC, "honest_instrument")
    good = honest.SELF_TEST_PROMPT.format(round=7)
    root = Path(tempfile.mkdtemp(prefix="critic-probe-"))
    try:
        # fixtures per mutant
        cases = {}
        # t01: a .bak file in the prompts dir carrying a placeholder report path
        cases["t01"] = fixture(root, good.replace("/round-7/kote.md", "/round-7/<lane>.md"),
                               extra={"kote-round-7.md.bak": good.replace("/round-7/kote.md", "/round-7/<lane>.md")})
        # t02: a second report dir ABOVE the file-name round
        cases["t02"] = fixture(root, good + "Earlier: `/fleet/.ufo/reports/round-8/kote.md`.\n")
        # t03: two files in one prompts dir (verdict lookup breadth)
        cases["t03"] = fixture(root, good,
                               extra={"kote-round-8.md": good.replace("round 7", "round 8")
                                      .replace("/round-7/", "/round-8/")})
        # t04/t05/t06: box_proof paths -> handled by the self-test's proof tree; probe via
        # dispatch_box_sha256 for t06 only (map-side checks need the proof tree).
        # t07: a DIRECTORY named kote.round
        cases["t07"] = fixture(root, good, legacy_dir=True)
        # t08: a DIRECTORY named like a prompt
        cases["t08"] = fixture(root, good)
        (cases["t08"] / "prompts" / "ghost-round-7.md").mkdir()
        # t09: an upper-case .MD report suffix
        cases["t09"] = fixture(root, good.replace("/round-7/kote.md", "/round-7/kote.MD"))
        for name, (a, b) in MUT.items():
            if name not in cases:
                continue
            text = SRC.read_text(encoding="utf-8")
            if text.count(a) != 1:
                print("%s: ANCHOR MISS %d" % (name, text.count(a)))
                continue
            mut = root / ("mut-%s.py" % name)
            mut.write_text(text.replace(a, b), encoding="utf-8")
            m = load(mut, "mut_" + name)
            h = run(honest, cases[name])
            v = run(m, cases[name])
            print("%s honest %s" % (name, h))
            print("%s mutant %s" % (name, v))
        # t03 direct: _verdict_of on a two-file result, target second
        two = {"files": [{"file": "a-round-7.md", "verdict": "PASS"},
                         {"file": "kote-round-7.md", "verdict": "FAIL"}]}
        print("t03 honest _verdict_of %r" % (honest._verdict_of(two, "kote-round-7.md"),))
        text3 = SRC.read_text(encoding="utf-8")
        mut3 = root / "mut-t03.py"
        mut3.write_text(text3.replace(*MUT["t03"]), encoding="utf-8")
        print("t03 mutant _verdict_of %r" % (load(mut3, "mut_t03")._verdict_of(two, "kote-round-7.md"),))
        # t06 direct: dispatch_box_sha256 with a ~~~ line inside a ``` block
        skill = ("## Dispatch-prompt fidelity checklist\n"
                 "- [ ] dispatch.01 first box text\n"
                 "```\n"
                 "~~~\n"
                 "- [ ] dispatch.02 inside the fence\n"
                 "```\n"
                 "- [ ] dispatch.03 third box text\n")
        print("t06 honest hash %s" % honest.dispatch_box_sha256(skill))
        text = SRC.read_text(encoding="utf-8")
        mut = root / "mut-t06.py"
        mut.write_text(text.replace(*MUT["t06"]), encoding="utf-8")
        print("t06 mutant hash %s" % load(mut, "mut_t06").dispatch_box_sha256(skill))
        return 0
    finally:
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
