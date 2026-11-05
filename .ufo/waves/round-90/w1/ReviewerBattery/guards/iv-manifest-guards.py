import sys, importlib.util
def import_module_hardlinked():
    # place the module in sys.modules BEFORE exec (the dataclass machinery resolves __module__ via sys.modules)
    spec = importlib.util.spec_from_file_location("cmb_iv", "verifiers/check_mutation_battery.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["cmb_iv"] = mod
    spec.loader.exec_module(mod)
    return mod
def parse(load_txt, mod):
    try:
        mod.parse_manifest(load_txt)
        return "PARSED-OK"
    except mod.CouldNotEvaluate as e:
        return "COULD-NOT-EVALUATE: %s" % e
mod = import_module_hardlinked()
HDR = 'id\ttarget\tclass\trecipe\tdisposition'
row5 = 'fg-m1\tverifiers/check_freeze_gate.py\tkill\t{"op":"replace","edits":[{"anchor":"x","with":"y"}]}\ttest'
print("1) 5-col sanity:", parse(HDR+"\n"+row5+"\n", mod))
print("2) bad class name:", parse(HDR+"\n"+'fg-m2\tverifiers/check_freeze_gate.py\tkillk\t{"op":"replace","edits":[]}\td'+"\n", mod))
print("3) wrong header:", parse('id\ttarget\tklass\trecipe\tdisposition\n', mod))
print("4) header only:", parse(HDR+"\n", mod))
print("5) missing class column (4 cols in a row):", parse(HDR+"\n"+'fg-m1\tverifiers/check_freeze_gate.py\tkill\t{"op":"replace"}'+"\n", mod))
print("6) extra column (6 cols):", parse(HDR+"\n"+'fg-m1\tverifiers/check_freeze_gate.py\tkill\t{"op":"replace","edits":[]}\textra\td'+"\n", mod))
print("7) survivor with empty disposition:", parse(HDR+"\n"+'fg-s1\tverifiers/check_freeze_gate.py\tsurvivor\t{"op":"replace","edits":[]}\t'+"\n", mod))
print("8) survivor with 1-col textual disposition:", parse(HDR+"\n"+'fg-s2\tverifiers/check_freeze_gate.py\tsurvivor\t{"op":"replace","edits":[]}\tsome-reason-text'+"\n", mod))
print("9) valid 6-col-hdr整齐 5-col survivor:", parse(HDR+"\n"+'fg-s3\tverifiers/check_freeze_gate.py\tsurvivor\t{"op":"replace","edits":[{"anchor":"a","with":"b"}]}\tdead-code-rename[observed-no-probe]'+"\n", mod))
print("10) survivor 0 textual, dead-function note:", parse(HDR+"\n"+'fg-s4\tverifiers/check_freeze_gate.py\tsurvivor\t{"op":"replace","edits":[{"anchor":"a","with":"b"}]}\t'+" deadRenameSurvivor [pristine-if-not-grew]==="+"\n", mod))
print("11) survivor with empty obj msg:", parse(HDR+"\n"+'fg-s5\tverifiers/check_freeze_gate.py\tsurvivor\t{"op":"replace","edits":[{"anchor":"a","with":"b"}]}\t'+" \x20\x20"+"\n", mod))
print("12) fg-s2 survivor with genuine 1-col msg (replaced recipe to satisfy earlier reject):", parse(HDR+"\n"+'fg-s6\tverifiers/check_freeze_gate.py\tsurvivor\t{"op":"replace","edits":[{"anchor":"a","with":"b"}]}\tdead-rename-is-invisible'+"\n", mod))
print("13) recipe with non-JSON:", parse(HDR+"\n"+'fg-t1\tverifiers/check_freeze_gate.py\tkill\tTHIS IS NOT JSON\td'+"\n", mod))
print("14) recipe wrong op:", parse(HDR+"\n"+'fg-t2\tverifiers/check_freeze_gate.py\tkill\t{"op":"prepend","edits":[]}\td'+"\n", mod))
print("15) equivalent recipe wrong kind:", parse(HDR+"\n"+'fg-u1\tverifiers/check_freeze_gate.py\tequivalent\t{"op":"rewrite","kind":"bananas"}\td'+"\n", mod))
print("16) edit dict missing anchor:", parse(HDR+"\n"+'fg-v1\tverifiers/check_freeze_gate.py\tkill\t{"op":"replace","edits":[{"nope":"a","with":"b"}]}\td'+"\n", mod))
print("17) no edits list:", parse(HDR+"\n"+'fg-v2\tverifiers/check_freeze_gate.py\tkill\t{"op":"replace","edits":"nope"}\td'+"\n", mod))
