from __future__ import print_function
import pytest

@pytest.fixture()
def before():
  print('\nbefore each test')

def test_1(before):
  print('test_1()')

def test_2(before):
  print('test_2()')


# Run: $ py.test -s bare_bones_example.py