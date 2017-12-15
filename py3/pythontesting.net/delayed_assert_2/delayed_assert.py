# ---- Called from tests

def expect(expr, msg=''):
    if not expr:
        _log_failure(msg)

# ----- Called from pytest plugin

def clear_expectations():
    global _failed_expectations
    _failed_expectations = []

def any_failures():
    return bool(_failed_expectations)

def get_failure_report():
    if any_failures():
        _failed_expectations.append('Failed Expectations:%s' % len(_failed_expectations))
        return ('\n'.join(_failed_expectations))
    else:
        return ''

# ------ Keeping _log_failure separate, mostly because it's ugly code

import inspect
import os.path

_failed_expectations = []

def _log_failure(msg=''):
    (filename, line, funcname, contextlist) = inspect.stack()[2][1:5]
    filename = os.path.basename(filename)
    context = contextlist[0]
    msg = '%s\n' % msg if msg else ''
    _failed_expectations.append('>%s%s%s:%s\n--------' % (context, msg, filename, line))
