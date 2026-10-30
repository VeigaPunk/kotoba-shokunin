import hashlib
import importlib.util
import sys
import tempfile
from pathlib import Path

mod_path = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("vsc", mod_path)
vsc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vsc)

with tempfile.TemporaryDirectory(prefix="probe-corr2-") as td:
    repo = Path(td)
    (repo / "corpus").mkdir()
    (repo / "corpus" / "live.md").write_text("", encoding="utf-8")
    log = repo / "LOG.md"
    # notice names the dead corrected token on its own line (repaired fixture shape)
    log.write_text("`corpus/live.md`\n"
                   "SCORECARD.md:9 token \"corpus/gone.md\" -> "
                   "\"corpus/absent-xyz.md\" (round-65 notice).\n", encoding="utf-8")
    sc = repo / "SCORECARD.md"
    sc.write_text("padding line\n" * 8 + "`corpus/gone.md`\n", encoding="utf-8")
    notice = log.read_text(encoding="utf-8").splitlines()[1]
    digest = hashlib.sha256(notice.encode("utf-8")).hexdigest()
    row = (2, digest, "SCORECARD.md", 9, "corpus/gone.md", "corpus/absent-xyz.md")
    status, evaluated, detail = vsc.check_governance_citations(
        repo, errata=(), corrections=(row,), corrections_horizon=2)
    print("module=%s" % mod_path)
    print("status=%s evaluated=%s" % (status, evaluated))
    print("detail=%s" % detail)
    print("arm_would_be_red_if_PASS=%s" % (status != "FAIL" or "corrected token" not in detail))
