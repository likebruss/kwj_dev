from unnecessary_math import multiply

def test_numbers_3_4():
    assert multiply(3,4) == 12

def test_strings_a_3():
    assert multiply('a',3) == 'aaa'

# Run: nosetests -v test_um_nose.py

# Running:
# $ python -m pytest test_um_pytest.py
# $ py.test test_um_pytest.py
# $ py.test -v test_um_pytest.py