from delayed_assert import expect, assert_expectations
import unittest

class DelayedAssertTest(unittest.TestCase):

  def test_should_pass(self):
    expect(1 == 1, 'one is one')
    assert_expectations()

  def test_should_fail(self):
    expect(1 == 2)
    x = 1
    y = 2
    expect(x == y, 'x:%s y:%s' % (x, y))
    expect(1 == 1)
    assert_expectations()

# Run:
# $ python -m unittest test_delayed_assert_unittest
