import pytest
import math
from Lab_3_SortingMethods.src.fact_fibo.fact_recursive import factorial_recursive
from Lab_3_SortingMethods.src.fact_fibo.factorial import factorial
from Lab_3_SortingMethods.src.fact_fibo.fibo_recursive import fibonacci_recursive
from Lab_3_SortingMethods.src.fact_fibo.fibonacci import fibonacci


class TestFactorial:

    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040)
    ])
    def test_small_values(self, n, expected):
        assert factorial_recursive(n) == expected
        assert factorial(n) == expected

    def test_compare_two_implementations(self):
        for n in range(1, 20):
            assert factorial_recursive(n) == factorial(n)

    def test_large_values(self):
        for n in [50, 100, 150, 200]:
            assert factorial_recursive(n) == math.factorial(n)
            assert factorial(n) == math.factorial(n)

    def test_negative_values(self):
        with pytest.raises(ValueError):
            factorial_recursive(-5)
        with pytest.raises(ValueError):
            factorial(-10)

class TestFibonacci:

    @pytest.mark.parametrize("n, expected", [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (10, 55),
    ])
    def test_small_values(self, n, expected):
        assert fibonacci_recursive(n) == expected
        assert fibonacci(n) == expected

    def test_compare_two_implementations(self):
        for n in range(0, 25):
            assert fibonacci_recursive(n) == fibonacci(n)

    def test_large_values(self):
        for n in [30, 35, 40]:
            assert fibonacci_recursive(n) == fibonacci(n)

    def test_negative_values(self):
        with pytest.raises(ValueError):
            fibonacci_recursive(-1)
        with pytest.raises(ValueError):
            fibonacci(-5)