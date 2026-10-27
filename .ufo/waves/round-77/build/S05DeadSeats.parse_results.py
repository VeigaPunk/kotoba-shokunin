#!/usr/bin/env python3
"""Per-seat status table for a UFO swarm <wave>-results.json. Stdout only; writes nothing.

usage: S05DeadSeats.parse_results.py <wave>-results.json [--report-dir DIR] [--tsv]

results.json shape (observed r76): {lane, round, wave, seats, results:[{name, agent, output, note}]}.
There is NO status field: `note` is null for every seat and dispatch registry agentId is null.
So status is DERIVED from `output` (the seat's final text) and the report file.

Verdict extraction (first hit wins), tolerant of JSON-wrapped final text (run-9 lesson):
  1. plain line   ^[ws>*_`]*VERDICT[ <seat>]: <text>   - last such line in the raw output
  2. JSON         whole output, ```json fence, or first {...} via raw_decode; then
                  a) any string value (recursive) holding a plain VERDICT: line,
                  b) key verdict_line | verdict | final_status | status | summary,
                  c) key error / aborted  -> "ERROR: ..."
  3. report file  last ^VERDICT: line of <report-dir>/<name>.md (source=file)
  4. none         verdict "-"

Status (derived from the FINAL OUTPUT; the report file only supplies a fallback verdict text):
  DONE       final output has a verdict (VERDICT: line or verdict-ish JSON key), not blocked
  BLOCKED    structured abort (error/aborted key) or verdict starting BLOCKED/INCONCLUSIVE/ABORT
  NOVERDICT  final output is a JSON object (yield reached) but no verdict key/line found
  UNYIELDED  final output is unstructured narration/<think> with no VERDICT: line (never reached yield)
  EMPTY      final output empty
Dead seat = UNYIELDED|EMPTY AND no report file (nothing recoverable). UNYIELDED with a report file
is counted separately (work landed, final message lost). Report presence is a separate column.
"""
import json, os, re, sys, collections

VLINE = re.compile(r'(?m)^[ \t>*_`#-]*VERDICT(?:[ \t]+[A-Za-z0-9_.-]+)?[*_`]*[ \t]*:[*_`]*[ \t]*(.+?)[ \t*_`]*$')
BLOCK = re.compile(r'^\W*(BLOCKED|INCONCLUSIVE|ABORT)', re.I)


def last_vline(text):
    m = VLINE.findall(text or '')
    return m[-1].strip() if m else None


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


def load_json(out):
    o = out.strip()
    o = re.sub(r'^```(?:json)?\s*|\s*```$', '', o)
    dec = json.JSONDecoder()
    for start in ([0] if o.startswith('{') else []) + [m.start() for m in re.finditer(r'\{', o)][:20]:
        try:
            v, _ = dec.raw_decode(o[start:])
            if isinstance(v, dict):
                return v
        except ValueError:
            continue
    return None


def compact(v, n=160):
    s = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, separators=(',', ':'))
    s = ' '.join(s.split())
    return s if len(s) <= n else s[:n - 1] + '…'


def classify(out, report_text):
    """-> (status, verdict, source, has_file_verdict). Status is decided from the FINAL OUTPUT only."""
    out = out or ''
    fv = last_vline(report_text) if report_text else None
    if not out.strip():
        return 'EMPTY', fv or '-', 'file' if fv else 'none'
    verdict, src, aborted = None, 'none', False
    pl = last_vline(out)
    if pl:
        verdict, src = pl, 'line'
    j = load_json(out)
    if j is not None:
        aborted = ('error' in j or 'aborted' in j) and not any(k in j for k in ('verdict', 'verdict_line'))
        if not verdict:
            for s in strings(j):
                v = last_vline(s)
                if v:
                    verdict, src = v, 'json-line'
                    break
        if not verdict:
            for k in ('verdict_line', 'verdict', 'final_status', 'status', 'summary', 'finding', 'counterexample'):
                if k in j and j[k] not in (None, '', [], {}):
                    verdict, src = compact(j[k]), 'json-key:' + k
                    break
        if not verdict and aborted:
            verdict, src = 'ERROR: ' + compact(j.get('error', j.get('aborted'))), 'json-key:error'
        if not verdict:
            return 'NOVERDICT', fv or '(keys: %s)' % ','.join(list(j)[:6]), 'file' if fv else 'json-keys'
    elif not verdict:
        # unstructured narration / <think> tail: the seat never reached yield
        return 'UNYIELDED', fv or '-', 'file' if fv else 'none'
    blocked = aborted or bool(BLOCK.match(verdict))
    return ('BLOCKED' if blocked else 'DONE'), verdict, src


def main(argv):
    args = [a for a in argv[1:] if not a.startswith('--')]
    tsv = '--tsv' in argv
    rdir = None
    if '--report-dir' in argv:
        rdir = argv[argv.index('--report-dir') + 1]
        args = [a for a in args if a != rdir]
    if len(args) != 1:
        print(__doc__)
        return 2
    path = args[0]
    data = json.load(open(path))
    base = os.path.dirname(os.path.abspath(path))
    rdir = rdir or os.path.join(base, data.get('wave', 'w1'))
    res = data['results']
    tot = collections.Counter()
    nofile, rows = [], []
    for x in res:
        name = x['name']
        rp = os.path.join(rdir, name + '.md')
        have = os.path.isfile(rp)
        rt = open(rp, errors='replace').read() if have else ''
        st, verdict, src = classify(x.get('output'), rt)
        tot[st] += 1
        tot['report_present' if have else 'report_absent'] += 1
        if st in ('UNYIELDED', 'EMPTY'):
            tot['dead' if not have else 'unyielded_with_file'] += 1
        if not have:
            nofile.append((name, st))
        rows.append((name, x.get('agent', '?'), st, 'y' if have else 'n', len(x.get('output') or ''), src, compact(verdict, 110)))
    sep = '\t' if tsv else ' | '
    print(sep.join(['name', 'agent', 'status', 'report', 'outlen', 'vsrc', 'verdict']))
    for r in rows:
        print(sep.join(str(c) for c in r))
    names = [r[0] for r in rows]
    print('--')
    print('seats_declared=%s results=%d unique_names=%d' % (data.get('seats'), len(res), len(set(names))))
    print('report_present=%d report_absent=%d' % (tot['report_present'], tot['report_absent']))
    for s in ('DONE', 'NOVERDICT', 'BLOCKED', 'UNYIELDED', 'EMPTY'):
        print('status.%s=%d' % (s, tot[s]))
    print('dead_seats(UNYIELDED|EMPTY, no report file)=%d' % tot['dead'])
    print('unyielded_with_report_file=%d' % tot['unyielded_with_file'])
    print('noreport_by_status=' + ', '.join('%s:%d' % kv for kv in sorted(collections.Counter(s for _, s in nofile).items())))
    print('noreport_names=' + ','.join(n for n, _ in nofile))
    disp = os.path.join(base, os.path.basename(path).replace('-results.json', '-dispatch.json'))
    if os.path.isfile(disp):
        want = [t['name'] for t in json.load(open(disp)).get('taskCall', {}).get('tasks', [])]
        print('dispatched=%d missing_from_results=%s extra_in_results=%s' % (
            len(want), sorted(set(want) - set(names)), sorted(set(names) - set(want))))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
