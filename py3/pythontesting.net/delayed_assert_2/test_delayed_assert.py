from delayed_assert import expect

def test_should_pass():
  expect(1 == 1, 'one is one')

def test_should_fail():
  expect(1 == 2)
  expect(3 == 4, 'three is four')

# Run: $ python -m pytest -s test_delayed_assert.py