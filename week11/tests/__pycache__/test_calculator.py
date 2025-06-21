import pytest
from mypackage.calculator import add, subtract, multiply, divide, power, root, sine, cosine, tangent

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_power():
    assert power(2, 3) == 8

def test_root():
    assert root(16) == 4

def test_root_negative():
    with pytest.raises(ValueError, match="Cannot take root of negative number"):
        root(-9)

def test_sine():
    assert round(sine(30), 2) == 0.5

def test_cosine():
    assert round(cosine(60), 2) == 0.5

def test_tangent():
    assert round(tangent(45), 2) == 1.0
