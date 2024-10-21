import pytest
from math_operations import add, subtract, multiply, divide, chain_operations

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 15) == -5
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 4) == -8
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(10, 2) == 5
    assert pytest.approx(divide(1, 3)) == 0.3333333

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_chain_operations():
    x, y = 10, 5
    operations = [add, multiply, subtract, divide]
    expected_result = ((10 + 5) * 5 - 5) / 5
    assert pytest.approx(chain_operations(x, y, operations)) == expected_result

def test_chain_operations_zero_division():
    x, y = 10, 0
    operations = [add, multiply, divide]
    with pytest.raises(ValueError):
        chain_operations(x, y, operations)
