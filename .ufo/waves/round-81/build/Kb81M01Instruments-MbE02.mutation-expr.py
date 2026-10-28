anchor = '(external if token.lower() in externals\n                         else unresolvable).append(site)'
out = src.replace(anchor, 'external.append(site)')
assert out != src, "M-b anchor not found in independent"
