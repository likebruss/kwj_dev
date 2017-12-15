from __future__ import print_function
import pytest, time

@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
  print('\n-----------------')
  print('module      : %s' % request.module.__name__)
  print('-----------------')

@pytest.fixture(scope="function", autouse=True)
def func_header(request):
  print('\n-----------------')
  print('function    : %s' % request.function.__name__)
  print('time        : %s' % time.asctime())
  print('-----------------')

def test_one():
  print('in test_one()')
def test_two():
  print('in test_two()')

# Run: $ py.test -s fixture_autouse.py
