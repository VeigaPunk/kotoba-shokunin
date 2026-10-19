import os, sys
driver = '/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/round-46/evidence/S2/drivers/r44-dispatch-6881ce3.py'
scope = '/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/round-46/evidence/S2/drivers/r41-scope-1c79e86.json'
os.execv(sys.executable, [sys.executable, driver, *sys.argv[1:], '--scope-file', scope])
