#!/usr/bin/env python3
"""Copy carried-reds.py and apply one minimal mutant per copy (scratch only)."""
import sys
from pathlib import Path

SRC = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-99/carried-reds.py")
OUT = Path(sys.argv[1]).resolve()
OUT.mkdir(parents=True, exist_ok=True)
base = SRC.read_text(encoding="utf-8")

MUTANTS = {}

# M1 drop the reds conjunct
old = "        met = green == 3 and held == 3 and frozen == 4 and guards_ok\n"
MUTANTS["M1-drop-reds"] = (old, "        met = held == 3 and frozen == 4 and guards_ok\n")
# M2 drop the selftests conjunct
MUTANTS["M2-drop-selftests"] = (old, "        met = green == 3 and frozen == 4 and guards_ok\n")
# M3 drop the frozen conjunct
MUTANTS["M3-drop-frozen"] = (old, "        met = green == 3 and held == 3 and guards_ok\n")
# M8 drop the guards conjunct
MUTANTS["M8-drop-guards"] = (old, "        met = green == 3 and held == 3 and frozen == 4\n")
# M4 weaken CHECKLIST_PASS_MIN
MUTANTS["M4-pass-min-10"] = ("CHECKLIST_PASS_MIN = 11\n", "CHECKLIST_PASS_MIN = 10\n")
# M5 accept N/A lines
MUTANTS["M5-accept-na"] = (
    '                others = sum(ln.startswith(("FAIL ", "N/A ")) for ln in lines)\n',
    '                others = sum(ln.startswith("FAIL ") for ln in lines)\n')
# M6 skip the checklist literal_eval (accept a non-literal block)
MUTANTS["M6-skip-checklist-literal"] = (
    """    except (ValueError, SyntaxError) as exc:
        return False, "corrections block not literal data: %s" % exc
""",
    """    except (ValueError, SyntaxError):
        return True, ""  # M6: non-literal corrections block accepted
""")
# M7 skip the battery-pin literal_eval (accept a dict-shaped block)
MUTANTS["M7-skip-pins-literal"] = (
    """                try:
                    ok = isinstance(ast.literal_eval(
                        PINS_RE.search(sb).group(0).split("=", 1)[1].strip()), dict)
                except (ValueError, SyntaxError):
                    ok = False
""",
    """                ok = PINS_RE.search(sb).group(0).split("=", 1)[1].strip().startswith("{")
""")

for name, (old, new) in MUTANTS.items():
    assert base.count(old) == 1, (name, base.count(old))
    text = base.replace(old, new)
    (OUT / (name + ".py")).write_text(text, encoding="utf-8")
    print(name, "ok")
