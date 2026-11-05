import os
import os, sys
LANE_GATE = os.environ['GATE_PATH']
src = open(LANE_GATE, encoding="utf-8").read()
needle = "        target = fleet_root / token\n"
assert src.count(needle) == 1, src.count(needle)
src = src.replace(needle, "        target = (Path(os.environ['RR_ROOT']) if os.environ.get('RR_ROOT') else fleet_root) / token\n")
import os as _os
g = {"__name__": "__main__", "__file__": LANE_GATE, "os": _os}
sys.argv = [LANE_GATE, "--json"]
exec(compile(src, LANE_GATE, "exec"), g)
