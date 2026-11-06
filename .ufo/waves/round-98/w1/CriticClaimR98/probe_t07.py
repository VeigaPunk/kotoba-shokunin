import importlib.util, sys, tempfile, shutil
from pathlib import Path
SRC = Path(sys.argv[1])
def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
h = load(SRC, "h")
good = h.SELF_TEST_PROMPT.format(round=7)
root = Path(tempfile.mkdtemp(prefix="t07-"))
try:
    for label, baseline, legacy_dir in (("baseline", "9\n", True), ("no-baseline", None, True)):
        case = root / label
        (case / "prompts").mkdir(parents=True); (case / "state").mkdir(); (case / "fleet" / "kote-shokunin").mkdir(parents=True)
        (case / "prompts" / "kote-round-7.md").write_text(good, encoding="utf-8")
        if baseline is not None:
            (case / "state" / "kote.report-baseline").write_text(baseline, encoding="utf-8")
        if legacy_dir:
            (case / "state" / "kote.round").mkdir()
        print(label, "state_source", h.state_source(case / "state", "kote"))
        r = h.evaluate_dispatch_08(case / "prompts", case / "state", case / "fleet")
        print(label, "honest dispatch.08", r["status"], [(f["file"], f["verdict"], f["conjuncts"]["round_le_latest_dispatched"]) for f in r["files"]])
        text = SRC.read_text(encoding="utf-8")
        a, b = "    if legacy.is_file():", "    if legacy.exists():"
        assert text.count(a) == 1
        mut = root / ("mut-%s.py" % label); mut.write_text(text.replace(a, b), encoding="utf-8")
        m = load(mut, "m" + label)
        print(label, "mutant state_source", m.state_source(case / "state", "kote"))
        r2 = m.evaluate_dispatch_08(case / "prompts", case / "state", case / "fleet")
        print(label, "mutant dispatch.08", r2["status"], [(f["file"], f["verdict"], f["conjuncts"]["round_le_latest_dispatched"]) for f in r2["files"]])
finally:
    shutil.rmtree(root, ignore_errors=True)
