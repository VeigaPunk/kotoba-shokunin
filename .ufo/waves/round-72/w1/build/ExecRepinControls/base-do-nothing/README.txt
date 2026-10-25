# do-nothing control at the base c69711e, instruments at their own default paths (no flags)
# sandbox: fleet-shaped, clone of the lane at c69711e named kotoba-shokunin; run from the clone root
date: 2026-10-25T18:47:46-03:00

## command 1
python3 -B verifiers/check_substrate_pins.py --json
exit=2
{"pass":0,"fail":3,"exit_code":2}

## command 2
python3 -B verifiers/verify_surfaces.py --json
exit=2
{"pass":0,"fail":0,"exit_code":2,"error":"opencode binary not found: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe"}
