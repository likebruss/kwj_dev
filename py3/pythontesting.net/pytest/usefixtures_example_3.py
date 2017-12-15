from __future__ import print_function
import pytest

@pytest.fixture()
def before():
  print('\nbefore each test')


@pytest.mark.usefixtures("before")
class Test:
  def test_1(self):
    print('test_1()')

  def test_2(self):
    print('test_2()')

# Run: $ py.test -s usefixtures_example_3.py
