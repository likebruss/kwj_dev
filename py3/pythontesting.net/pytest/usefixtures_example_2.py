from __future__ import print_function
import pytest

@pytest.fixture()
def before():
  print('\nbefore each test')

class Test:
  @pytest.mark.usefixtures("before")
  def test_1(self):
    print('test_1()')

  @pytest.mark.usefixtures("before")
  def test_2(self):
    print('test_2()')

# Run: $ py.test -s usefixtures_example_2.py
