from __future__ import print_function
import pytest  # 1

@pytest.fixture(scope='module')  #2 / 3
def resource_a_setup(request):  # 4
  print('\nresources_a_setup()')
  def resource_a_teardown():
    print('\nresources_a_teardown()')
  request.addfinalizer(resource_a_teardown)  # 4


def test_1_that_needs_resource_a(resource_a_setup):
  print('test_1_that_needs_resource_a()')

def test_2_that_does_not():
  print('\ntest_2_that_does_not()')

def test_3_that_does(resource_a_setup):  # 5
  print('\ntest_3_that_does()')

# Run:
# $ py.test -s -v test_three_funcs.py::test_2_that_does_not
# $ py.test -s -v test_three_funcs.py