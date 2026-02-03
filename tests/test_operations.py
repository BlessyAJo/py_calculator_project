import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition_positive():
    assert addition(2, 3) == 5
def test_addition_negative():
    assert addition(-2, -3) == -5

def test_subtraction_positive():
    assert subtraction(5, 3) == 2
def test_subtraction_negative():
    assert subtraction(3, 5) == -2

def test_multiplication_positive():
    assert multiplication(4, 3) == 12
def test_multiplication_negative():
    assert multiplication(-4, 3) == -12

def test_division_positive():
    assert division(10, 2) == 5
def test_division_negative():
    assert division(-10, 2) == -5
def test_division_by_zero():
    with pytest.raises(ValueError) as excinfo:
        division(10, 0)
    assert str(excinfo.value) == "Cannot divide by zero."