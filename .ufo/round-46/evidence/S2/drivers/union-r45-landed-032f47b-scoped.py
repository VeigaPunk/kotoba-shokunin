import os, sys
driver = '/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/round-46/evidence/S2/drivers/r45-landed-032f47b.py'
scope = '/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/round-46/evidence/S2/drivers/r41-scope-1c79e86.json'
os.execv(sys.executable, [sys.executable, driver, *sys.argv[1:], '--scope-file', scope])
