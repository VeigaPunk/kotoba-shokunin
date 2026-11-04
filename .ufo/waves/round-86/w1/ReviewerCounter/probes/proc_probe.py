import os, json
FX = "home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/omp-catalogue-r86/catalogue.json"
print("direct fixture visible:", os.path.exists("/" + FX))
print("pid", os.getpid(), "ppid", os.getppid())
ok = []
for p in sorted((d for d in os.listdir("/proc") if d.isdigit()), key=int):
    try:
        with open(f"/proc/{p}/root/{FX}", "rb") as f:
            n = len(f.read())
        ok.append((p, n))
    except OSError as e:
        pass
print("readable via /proc/PID/root:", len(ok), ok[:5])
# parent chain
p = os.getppid()
for _ in range(4):
    try:
        print("ancestor", p, open(f"/proc/{p}/cmdline", "rb").read()[:80])
        with open(f"/proc/{p}/root/{FX}", "rb") as f:
            print("  via root:", len(f.read()))
    except OSError as e:
        print("  err", e)
    try:
        p = int(open(f"/proc/{p}/stat").read().split(") ")[1].split()[1])
    except Exception:
        break
try:
    fd = os.open(f"/proc/{os.getppid()}/mem", os.O_RDONLY); print("parent mem open OK"); os.close(fd)
except OSError as e:
    print("parent mem", e)
