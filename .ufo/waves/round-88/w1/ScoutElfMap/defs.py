import mmap
h=open("/home/vgpnk/.local/bin/omp","rb")
b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)
def line_at(o):
    s=b.rfind(b"\n",max(0,o-8192),o); s=0 if s<0 else s+1
    e=b.find(b"\n",o,o+8192); e=b.size() if e<0 else e
    return b[s:e].decode("utf-8","replace")
def ctx(o,bef,aft):
    return b[max(0,o-bef):o+aft].decode("utf-8","replace")
for label,o,bef,aft in [
  ("Ou@173814381",173814381,400,500),
  ("eh@173837626",173837626,600,600),
  ("y1@173864226",173864226,400,400),
  ("Gh@166884553",166884553,300,300),
]:
    print("="*90); print(label, "line:", repr(line_at(o))); print(ctx(o,bef,aft))
