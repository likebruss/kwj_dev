from __future__ import print_function
import pytest

@pytest.yield_fixture(scope="module")
def cheese_db():
  print('\n[setup] cheese_db, connect to db')
  a_dictionary_for_now = {'Brie': 'No.', 'Camenbert': 'Ah! We have Camenbert, yessir.'}
  yield a_dictionary_for_now
  print('\n[teardown] cheese_db finalizer, disconnect from db')

def test_brie(cheese_db):
  print('in test_brie()')
  assert cheese_db['Brie'] == 'No.'

def test_camenbert(cheese_db):
  print('\nin test_camenbert()')
  assert cheese_db['Camenbert'] != 'No.'

# Run: $ py.test -s fixture_yield.py
