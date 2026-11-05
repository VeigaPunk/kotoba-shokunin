import mmap,re
h=open("/home/vgpnk/.local/bin/omp","rb")
b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)
def ctx(o,bef,aft):
    return b[max(0,o-bef):o+aft].decode("utf-8","replace")
# helpers.ts module region
print("### helpers.ts header region 172783600-172786200")
print(ctx(172783600,0,2700))
