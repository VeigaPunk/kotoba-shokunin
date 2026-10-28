out = src.replace('REPORT_MARKER, REPORT_MIN_BYTES = b"## SHONEN", 400',
                  'REPORT_MARKER, REPORT_MIN_BYTES = b"## SHONEN", 0')
assert out != src, "M-d anchor not found in integrity"
