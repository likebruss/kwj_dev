def test_should_pass(expect):
  expect(1 == 1, 'one is one')

def test_should_fail(expect):
  expect(1 == 2)
  expect(3 == 4, 'three is four')

# Run: $ python -m pytest test_expect_fixture.py
