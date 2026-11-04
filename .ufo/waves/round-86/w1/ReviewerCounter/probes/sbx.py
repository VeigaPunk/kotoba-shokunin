"""Run a command inside the identical bwrap the frozen counter builds (default_hide + box ro-bind)."""
import importlib.util, subprocess, sys, tempfile
from pathlib import Path
C = "/fast/scratch/hyaku/kotoba-r86/ReviewerCounter/repo/verifiers/check_omp_catalogue_repro.py"  # frozen 2390eec2…
spec = importlib.util.spec_from_file_location("ocr", C)
ocr = importlib.util.module_from_spec(spec); spec.loader.exec_module(ocr)


def wrap(box: Path) -> list:
    w = ["bwrap", "--ro-bind", "/", "/", "--dev", "/dev", "--proc", "/proc", "--die-with-parent"]
    for h in ocr.default_hide():
        if h.is_dir():
            w += ["--tmpfs", str(h)]
        elif h.exists():
            w += ["--ro-bind", "/dev/null", str(h)]
    return w + ["--ro-bind", str(box), str(box)]


if __name__ == "__main__":
    box = Path(tempfile.mkdtemp(prefix="box-scan-"))
    r = subprocess.run(wrap(box) + sys.argv[1:], check=False)
    sys.exit(r.returncode)
