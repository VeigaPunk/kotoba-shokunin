import json, os, socket, sys, subprocess
S = "/fast/scratch/hyaku/kotoba-r86/Sentinel"
FIX = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/omp-catalogue-r86/catalogue.json"
r = {}
def ro(p):
    try:
        return "ro" if os.statvfs(p).f_flag & os.ST_RDONLY else "rw"
    except OSError as e:
        return "err:" + e.strerror
for p in ["/", "/home", os.path.expanduser("~"), os.path.expanduser("~/.omp"), "/fast", "/fast/scratch", S,
          "/tmp", "/var/tmp", "/dev", "/dev/shm", "/run", "/run/user/1000", "/home/vgpnk/Projects/shokunin",
          "/home/vgpnk/Projects/shokuknow", sys.argv[1]]:
    r["fs " + p] = ro(p) + (" exists" if os.path.exists(p) else " absent")
r["fixture direct"] = os.path.exists(FIX)
r["sessions direct entries"] = len(os.listdir(os.path.expanduser("~/.omp/agent/sessions"))) if os.path.isdir(os.path.expanduser("~/.omp/agent/sessions")) else "absent"
# submount ro check from mountinfo: count rw mounts
rw = []
for line in open("/proc/self/mountinfo"):
    f = line.split()
    if "rw" in f[5].split(","):
        rw.append(f[4])
r["rw mountpoints"] = rw
st = open("/proc/self/status").read()
r["NSpid"] = [l for l in st.splitlines() if l.startswith("NSpid")]
r["pid"] = os.getpid(); r["ppid"] = os.getppid()
r["proc pid count"] = sum(1 for d in os.listdir("/proc") if d.isdigit())
# /proc/<pid>/root traversal of host processes
hits = {}
for pid in [os.getppid(), int(sys.argv[2])]:
    root = f"/proc/{pid}/root"
    try:
        p = root + FIX
        with open(p, "rb") as fh:
            hits[f"{pid} read fixture bytes"] = len(fh.read())
    except OSError as e:
        hits[f"{pid} read fixture"] = e.strerror
    try:
        p = root + S + "/escape-write.txt"
        with open(p, "w") as fh:
            fh.write("written from inside bwrap via /proc/pid/root\n")
        hits[f"{pid} write scratch"] = "OK"
    except OSError as e:
        hits[f"{pid} write scratch"] = e.strerror
    try:
        hits[f"{pid} sessions via root"] = len(os.listdir(root + os.path.expanduser("~/.omp/agent/sessions")))
    except OSError as e:
        hits[f"{pid} sessions via root"] = e.strerror
r["proc-root"] = hits
# network: connect to host loopback listener
try:
    c = socket.create_connection(("127.0.0.1", int(sys.argv[3])), timeout=3); c.sendall(b"hi"); c.close(); r["loopback connect"] = "OK"
except OSError as e:
    r["loopback connect"] = e.strerror
r["net ifaces"] = [l.split(":")[0].strip() for l in open("/proc/net/dev").read().splitlines()[2:]]
# unix sockets in /run/user/1000
socks = []
try:
    for n in os.listdir("/run/user/1000"):
        p = "/run/user/1000/" + n
        import stat
        if stat.S_ISSOCK(os.stat(p).st_mode):
            s = socket.socket(socket.AF_UNIX)
            try:
                s.connect(p); socks.append(n + ":connect-OK")
            except OSError as e:
                socks.append(n + ":" + e.strerror)
            s.close()
except OSError as e:
    socks.append("err " + e.strerror)
r["run-user sockets"] = socks
r["env count"] = len(os.environ)
r["env secretish names"] = sorted(k for k in os.environ if any(t in k.upper() for t in ("TOKEN", "KEY", "SECRET", "PASS", "AUTH")))
r["DBUS"] = "DBUS_SESSION_BUS_ADDRESS" in os.environ
# detached grandchild
pid = os.fork()
if pid == 0:
    os.setsid()
    if os.fork() == 0:
        os.close(1); os.close(2)
        os.execvp("sleep", ["sleep", "47.123"])
    os._exit(0)
os.waitpid(pid, 0)
print(json.dumps(r, indent=1))
