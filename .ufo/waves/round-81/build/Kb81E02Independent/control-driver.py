"""Retarget the fleet root in an instrument's own bytes and run its CLI (control worlds).

argv: <script> <fake-fleet> <arg>... . The instrument's source is exec'd with its
FLEET_ROOT constant line replaced (str and Path forms), so every function default
binds the control fleet and the measured logic is otherwise byte-identical.
"""
import sys

script, fake = sys.argv[1], sys.argv[2]
src = open(script, encoding="utf-8").read()
src2 = src.replace('FLEET_ROOT = Path("/home/vgpnk/Projects/shokunin")',
                   'FLEET_ROOT = Path(%r)' % fake)
if src2 == src:
    src2 = src.replace('FLEET_ROOT = "/home/vgpnk/Projects/shokunin"',
                       'FLEET_ROOT = %r' % fake)
assert src2 != src, "FLEET_ROOT constant not found"
ns = {"__name__": "instrument", "__file__": script}
exec(compile(src2, script, "exec"), ns)
sys.exit(ns["main"](sys.argv[3:]))
