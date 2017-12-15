import delayed_assert

def pytest_runtest_setup(item):
  delayed_assert.clear_expectations()

def pytest_report_teststatus(report):
  if report.when == "call":
    if not report.failed:
      if delayed_assert.any_failures():
        report.outcome = "failed"
        report.longrepr = delayed_assert.get_failure_report()
        delayed_assert.clear_expectations()