# tests/test_calculator.py
import pytest
from calculator.calculator import Calculator
from calculator.calculation import Calculation
from calculator.calculations import Calculations

def test_addition():
    assert Calculator.add(1, 2) == 3, "Expected addition of 1 and 2 to be 3"

def test_subtraction():
    assert Calculator.subtract(5, 3) == 2, "Expected subtraction of 3 from 5 to be 2"

def test_multiplication():
    assert Calculator.multiply(4, 3) == 12, "Expected multiplication of 4 and 3 to be 12"

def test_division():
    assert Calculator.divide(10, 2) == 5, "Expected division of 10 by 2 to be 5"

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)

@pytest.fixture
def sample_calculation():
    return Calculation('add', 1, 2)

def test_calculation(sample_calculation):
    assert sample_calculation.result == 3, "Expected result of adding 1 and 2 to be 3"

def test_calculation_history():
    # Clear history before the test
    Calculations.clear_history()
    
    # Perform calculations and add them to history
    calc1 = Calculation('add', 1, 2)
    calc2 = Calculation('subtract', 5, 3)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)

    # Check that the history contains the calculations
    assert Calculations.get_history() == [calc1, calc2], "Expected history to contain calc1 and calc2"

def test_last_calculation():
    Calculations.clear_history()
    calc = Calculation('multiply', 3, 4)
    Calculations.add_calculation(calc)
    assert Calculations.last_calculation() == calc, "Expected last calculation to be calc"

def test_clear_history():
    Calculations.clear_history()
    assert Calculations.get_history() == [], "Expected history to be cleared"
