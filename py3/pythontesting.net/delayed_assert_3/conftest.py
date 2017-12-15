import pytest
import inspect
import os.path

@pytest.fixture
def expect(request):
  def do_expect(expr, msg=''):
    if not expr:
      _log_failure(request.node, msg)
  return do_expect

def _log_failure(node, msg=''):
  # get filename, line, and context
  (filename, line, funcname, contextlist) = inspect.stack()[2][1:5]
  filename = os.path.basename(filename)
  context = contextlist[0]
  # format entry
  msg = '%s\n' % msg if msg else ''
  entry = '>%s%s%s:%s\n--------' % (context, msg, filename, line)
  # add entry
  if not hasattr(node, '_failed_expect'):
    node._failed_expect = []
  node._failed_expect.append(entry)

@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
  report = __multicall__.execute()
  if (call.when == "call") and report.passed and hasattr(item, '_failed_expect'):
    report.outcome = "failed"
    summary = 'Failed Expectations:%s' % len(item._failed_expect)
    item._failed_expect.append(summary)
    report.longrepr = '\n'.join(item._failed_expect)
  return report