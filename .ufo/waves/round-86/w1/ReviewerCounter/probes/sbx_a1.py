"""Run a command inside the same bwrap the amended (b9ee548) counter builds."""
import importlib.util, subprocess, sys, tempfile, shutil
from pathlib import Path
C = "/fast/scratch/hyaku/kotoba-r86/ReviewerCounter/repo/verifiers/check_omp_catalogue_repro_a1.py"
spec = importlib.util.spec_from_file_location("ocr_a1", C)
ocr = importlib.util.module_from_spec(spec); spec.loader.exec_module(ocr)

if __name__ == "__main__":
    box = Path(tempfile.mkdtemp(prefix="box-scan-"))
    shutil.copy("/home/vgpnk/.local/bin/rg", box / "rg")
    w = ["bwrap", "--ro-bind", "/", "/", "--dev", "/dev", "--proc", "/proc", "--die-with-parent",
         "--unshare-net", "--unshare-pid", "--unshare-ipc", "--new-session", "--clearenv",
         "--setenv", "HOME", str(Path.home()), "--setenv", "PATH", "/usr/bin:/bin", "--setenv", "LANG", "C.UTF-8"]
    for h in ocr.default_hide():
        if h.is_dir():
            w += ["--tmpfs", str(h)]
        elif h.exists():
            w += ["--ro-bind", "/dev/null", str(h)]
    for r in ocr.default_rebind():
        if r.is_dir():
            w += ["--ro-bind", str(r), str(r)]
    w += ["--ro-bind", str(box), str(box)]
    args = [str(box / "rg") if a == "RG" else a for a in sys.argv[1:]]
    sys.exit(subprocess.run(w + args, check=False).returncode)
