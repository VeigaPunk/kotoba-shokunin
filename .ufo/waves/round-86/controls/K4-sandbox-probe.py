# K4 (round-86 addendum-1 control; never production): a scored module that only reports what the
# sandbox lets it see, then aborts (the counter reports it as could-not-evaluate). Compact keys:
# L=~/.omp/logs S=sessions D=description cache A=agent.db F=fleet tree X=/fast/scratch U=/run/user
# M=/dev/shm P=plugin skills root G=~/.agents/skills C=~/.claude/skills N=network W=write home E=env
import os, socket, json
from pathlib import Path
H = Path.home()
o = {}
for k, p in {"L": H/".omp/logs", "S": H/".omp/agent/sessions", "D": H/".omp/agent/skill-descriptions.db",
             "A": H/".omp/agent/agent.db", "F": Path("/home/vgpnk/Projects/shokunin"), "X": Path("/fast/scratch"),
             "U": Path("/run/user"), "M": Path("/dev/shm"),
             "P": H/".omp/plugins/node_modules/ecc-pi-core/skills", "G": H/".agents/skills", "C": H/".claude/skills"}.items():
    try:
        o[k] = len(os.listdir(p)) if p.is_dir() else ("file" if p.exists() else "absent")
    except OSError as e:
        o[k] = type(e).__name__
try:
    socket.create_connection(("1.1.1.1", 443), timeout=3); o["N"] = "open"
except OSError:
    o["N"] = "blocked"
try:
    (H/".cache"/"k4-write-test").write_text("x"); o["W"] = "WRITABLE"
except OSError:
    o["W"] = "denied"
o["E"] = len(os.environ)
raise SystemExit("K4 " + json.dumps(o, separators=(",", ":")))
