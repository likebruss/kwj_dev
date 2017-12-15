from __future__ import print_function
import pytest

@pytest.fixture(params=[1, 2, 3])
def test_data(request):
  return request.param

def test_not_2(test_data):
  print('test_data: %s' % test_data)
  assert test_data != 2

# Run: $ py.test -v fixture_params_toy.py
