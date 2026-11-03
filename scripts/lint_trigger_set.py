#!/usr/bin/env python3
"""Read-only preflight of authored trigger-evaluation inputs, not label semantics."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 1048576
MAX_ROWS = 1000
MAX_QUERY = 10000


class InvalidInput(ValueError):
    pass


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise InvalidInput(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise InvalidInput('duplicate JSON key')
        result[key] = value
    return result


def reject_constant(value):
    raise InvalidInput('nonfinite JSON constant')


def read_set(filename):
    path = Path(filename)
    if not path.is_file():
        raise InvalidInput('not a regular file')
    with path.open('rb') as stream:
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise InvalidInput('input too large')
    records = json.loads(raw.decode('utf-8'), object_pairs_hook=unique_object,
                         parse_constant=reject_constant)
    if not isinstance(records, list) or not 1 <= len(records) <= MAX_ROWS:
        raise InvalidInput('expected bounded nonempty list')
    for record in records:
        if not isinstance(record, dict):
            raise InvalidInput('expected record')
        query = record.get('query')
        if not isinstance(query, str) or not query.strip() or len(query) > MAX_QUERY:
            raise InvalidInput('invalid query')
        if type(record.get('should_trigger')) is not bool:
            raise InvalidInput('invalid label')
    return records


def boundary(runs_text, threshold_text):
    if not re.fullmatch(r'[0-9]+', runs_text):
        raise InvalidInput('invalid runs')
    # Redundant zeroes do not change value; avoid interpreter digit-limit rejection.
    runs_digits = runs_text.lstrip('0') or '0'
    if len(runs_digits) > 5:
        raise InvalidInput('runs outside bound')
    runs = int(runs_digits)
    if not 1 <= runs <= 10000:
        raise InvalidInput('runs outside bound')
    if not re.fullmatch(r'[0-9]+(?:\.[0-9]+)?|[0-9]+/[0-9]+', threshold_text):
        raise InvalidInput('invalid threshold')
    if '/' in threshold_text:
        numerator, denominator = threshold_text.split('/')
        normalized = (numerator.lstrip('0') or '0') + '/' + (denominator.lstrip('0') or '0')
    elif '.' in threshold_text:
        whole, fractional = threshold_text.split('.')
        normalized = (whole.lstrip('0') or '0') + '.' + (fractional.rstrip('0') or '0')
    else:
        normalized = threshold_text.lstrip('0') or '0'
    threshold = Fraction(normalized)
    if not 0 <= threshold <= 1:
        raise InvalidInput('threshold outside range')
    count = runs * threshold
    reachable = count.denominator == 1
    return {'runs': runs,
            'threshold': f'{threshold.numerator}/{threshold.denominator}',
            'equality_reachable': reachable,
            'equality_count': count.numerator if reachable else None}


def duplicates(records, dataset):
    first = {}
    issues = []
    for index, record in enumerate(records):
        query = record['query']
        if query in first:
            prior = first[query]
            same = records[prior]['should_trigger'] == record['should_trigger']
            issues.append({'code': 'DUPLICATE_QUERY' if same else 'CONFLICTING_LABELS',
                           'set': dataset, 'indexes': [prior, index]})
        else:
            first[query] = index
    return issues, first


def emit(status, diagnostics, reachability):
    print(json.dumps({'status': status, 'diagnostics': diagnostics,
                      'boundary': reachability}, ensure_ascii=True, separators=(',', ':')))
    return {'ok': 0, 'conflict': 1, 'invalid': 2}[status]


def invalid(dataset):
    return emit('invalid', [{'code': 'INVALID_INPUT', 'set': dataset, 'indexes': []}], None)


def main(argv=None):
    parser = Parser(description=__doc__)
    parser.add_argument('train')
    parser.add_argument('--validation')
    parser.add_argument('--runs', default='3')
    parser.add_argument('--threshold', default='1/2')
    errors = (OSError, ValueError, TypeError, RecursionError, OverflowError, ZeroDivisionError)
    try:
        args = parser.parse_args(argv)
    except InvalidInput:
        return invalid('settings')
    try:
        train = read_set(args.train)
    except errors:
        return invalid('train')
    validation = None
    if args.validation is not None:
        try:
            validation = read_set(args.validation)
        except errors:
            return invalid('validation')
    try:
        reachability = boundary(args.runs, args.threshold)
    except errors:
        return invalid('settings')
    issues, first_train = duplicates(train, 'train')
    if validation is not None:
        validation_issues, _ = duplicates(validation, 'validation')
        issues.extend(validation_issues)
        for index, record in enumerate(validation):
            if record['query'] in first_train:
                issues.append({'code': 'SPLIT_OVERLAP', 'set': 'validation',
                               'indexes': [first_train[record['query']], index]})
    return emit('conflict' if issues else 'ok', issues, reachability)


if __name__ == '__main__':
    sys.exit(main())
