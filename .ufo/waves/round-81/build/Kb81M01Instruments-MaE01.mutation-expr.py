out = src.replace('REPORT_MARKER, REPORT_MIN_BYTES = b"## SHONEN", 400',
                  'REPORT_MARKER, REPORT_MIN_BYTES = b"## ", 400')
assert out != src, "M-a anchor not found in integrity"
