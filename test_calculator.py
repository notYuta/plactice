"""
Test suite for the calculator module.

This module contains comprehensive tests for all functions in calculator.py
using pytest framework.
"""

import pytest
from calculator import add, subtract, multiply, divide, power, is_even, factorial


class TestAddition:
    """Test cases for the add function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, -10) == -20

    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2

    def test_add_with_zero(self):
        """Test adding with zero."""
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(0, 0) == 0

    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.7) == pytest.approx(6.2)
        assert add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtraction:
    """Test cases for the subtract function."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(10, 3) == 7
        assert subtract(20, 5) == 15

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -20) == 10

    def test_subtract_with_zero(self):
        """Test subtracting with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        assert subtract(5.5, 2.3) == pytest.approx(3.2)


class TestMultiplication:
    """Test cases for the multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(3, 4) == 12
        assert multiply(7, 8) == 56

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-3, -4) == 12
        assert multiply(-5, 6) == -30

    def test_multiply_with_zero(self):
        """Test multiplying with zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0

    def test_multiply_with_one(self):
        """Test multiplying with one."""
        assert multiply(5, 1) == 5
        assert multiply(1, 10) == 10

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        assert multiply(2.5, 4.0) == pytest.approx(10.0)


class TestDivision:
    """Test cases for the divide function."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-10, 2) == -5
        assert divide(10, -2) == -5
        assert divide(-10, -2) == 5

    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        assert divide(7.5, 2.5) == pytest.approx(3.0)
        assert divide(1.0, 3.0) == pytest.approx(0.333333, rel=1e-5)

    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0


class TestPower:
    """Test cases for the power function."""

    def test_power_positive_exponent(self):
        """Test raising to positive exponents."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(10, 0) == 1

    def test_power_negative_exponent(self):
        """Test raising to negative exponents."""
        assert power(2, -1) == 0.5
        assert power(10, -2) == 0.01

    def test_power_zero_exponent(self):
        """Test raising to zero exponent."""
        assert power(5, 0) == 1
        assert power(100, 0) == 1

    def test_power_fractional_exponent(self):
        """Test raising to fractional exponents."""
        assert power(4, 0.5) == pytest.approx(2.0)
        assert power(27, 1/3) == pytest.approx(3.0)


class TestIsEven:
    """Test cases for the is_even function."""

    def test_even_positive_numbers(self):
        """Test even positive numbers."""
        assert is_even(2) is True
        assert is_even(4) is True
        assert is_even(100) is True

    def test_odd_positive_numbers(self):
        """Test odd positive numbers."""
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(99) is False

    def test_even_negative_numbers(self):
        """Test even negative numbers."""
        assert is_even(-2) is True
        assert is_even(-4) is True

    def test_odd_negative_numbers(self):
        """Test odd negative numbers."""
        assert is_even(-1) is False
        assert is_even(-3) is False

    def test_zero_is_even(self):
        """Test that zero is considered even."""
        assert is_even(0) is True


class TestFactorial:
    """Test cases for the factorial function."""

    def test_factorial_base_cases(self):
        """Test factorial of 0 and 1."""
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_factorial_small_numbers(self):
        """Test factorial of small positive numbers."""
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120

    def test_factorial_larger_numbers(self):
        """Test factorial of larger numbers."""
        assert factorial(6) == 720
        assert factorial(10) == 3628800

    def test_factorial_negative_raises_error(self):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-10)


class TestEdgeCases:
    """Test edge cases and integration scenarios."""

    def test_chained_operations(self):
        """Test combining multiple operations."""
        result = add(multiply(2, 3), divide(10, 2))
        assert result == 11

    def test_large_numbers(self):
        """Test operations with large numbers."""
        assert add(1000000, 2000000) == 3000000
        assert multiply(10000, 10000) == 100000000

    def test_very_small_floats(self):
        """Test operations with very small floating point numbers."""
        assert add(0.000001, 0.000002) == pytest.approx(0.000003)


# Parametrized tests for more comprehensive coverage
class TestParametrized:
    """Parametrized tests for better coverage."""

    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 2),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
        (1.5, 2.5, 4.0),
    ])
    def test_add_parametrized(self, a, b, expected):
        """Parametrized test for addition."""
        assert add(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize("a,b,expected", [
        (10, 5, 2.0),
        (9, 3, 3.0),
        (7, 2, 3.5),
        (1, 1, 1.0),
    ])
    def test_divide_parametrized(self, a, b, expected):
        """Parametrized test for division."""
        assert divide(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize("n,expected", [
        (0, True),
        (2, True),
        (4, True),
        (1, False),
        (3, False),
        (-2, True),
        (-3, False),
    ])
    def test_is_even_parametrized(self, n, expected):
        """Parametrized test for is_even."""
        assert is_even(n) == expected


if __name__ == "__main__":
    # Allow running tests directly with: python test_calculator.py
    pytest.main([__file__, "-v"])
