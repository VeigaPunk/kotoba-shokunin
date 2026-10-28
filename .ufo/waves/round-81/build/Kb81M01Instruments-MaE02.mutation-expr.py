anchor = 'IDENTITY_FROM_ROUND, REPORT_MIN_BYTES, REPORT_MARKER = 19, 400, b"## SHONEN"'
out = src.replace(anchor, 'IDENTITY_FROM_ROUND, REPORT_MIN_BYTES, REPORT_MARKER = 19, 400, b"## "')
assert out != src, "M-a anchor not found in independent"
