import importlib.util, json, os, socket, subprocess, sys, threading, time
from pathlib import Path
S = Path("/fast/scratch/hyaku/kotoba-r86/Sentinel")
spec = importlib.util.spec_from_file_location("ocr", "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_omp_catalogue_repro.py")
ocr = importlib.util.module_from_spec(spec); spec.loader.exec_module(ocr)
captured = {}
real_run = subprocess.run
class Stop(Exception): pass
def fake_run(cmd, **kw):
    captured["cmd"] = cmd; captured["kw"] = kw
    raise Stop()
ocr.subprocess.run = fake_run
try:
    ocr.run_module("x=1", ["a"], "00", "/home/vgpnk/Projects/shokunin", S / "box", "probe", ocr.default_hide())
except Stop:
    pass
ocr.subprocess.run = real_run
cmd = captured["cmd"]
i = cmd.index(sys.executable)
wrap, inner = cmd[:i], cmd[i:]
print("WRAP", json.dumps(wrap))
print("KW", captured["kw"])
box = inner[2].rsplit("/", 1)[0]
lst = socket.socket(); lst.bind(("127.0.0.1", 0)); lst.listen(1); port = lst.getsockname()[1]
got = []
def acc():
    lst.settimeout(15)
    try:
        c, _ = lst.accept(); got.append(c.recv(10)); c.close()
    except OSError as e:
        got.append(str(e))
t = threading.Thread(target=acc); t.start()
(S / "canary").write_text("canary")
(Path(box) / "probe.py").write_text((S / "probe.py").read_text())
out = real_run(wrap + [sys.executable, "-B", box + "/probe.py", box, str(os.getpid()), str(port)],
               capture_output=True, text=True, timeout=60)
t.join()
print("RC", out.returncode)
print(out.stdout); print("STDERR", out.stderr[-500:])
print("listener got", got)
print("escape-write exists on host:", (S / "escape-write.txt").exists(),
      (S / "escape-write.txt").read_text() if (S / "escape-write.txt").exists() else "")
time.sleep(2)
ps = real_run(["pgrep", "-af", "sleep 47.123"], capture_output=True, text=True)
print("surviving grandchild after bwrap exit:", ps.stdout.strip() or "none")
