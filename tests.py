import unittest
import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else None

    def square_root(self, a):
        return math.sqrt(a) if a >= 0 else None

class TestCalculator(unittest.TestCase):
  # test_my_module.py
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.calculator.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = self.calculator.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        result = self.calculator.divide(10, 0)
        self.assertIsNone(result)

    def test_square_root(self):
        result = self.calculator.square_root(16)
        self.assertEqual(result, 4)

    def test_square_root_negative_number(self):
        result = self.calculator.square_root(-16)
        self.assertIsNone(result)

    def test_power(self):
        result = self.calculator.power(2, 3)
        self.assertEqual(result, 8)

    def test_power_zero_exponent(self):
        result = self.calculator.power(5, 0)
        self.assertEqual(result, 1)

    def test_power_negative_exponent(self):
        result = self.calculator.power(3, -2)
        self.assertAlmostEqual(result, 0.111, places=3)

    def test_max(self):
        result = self.calculator.max(7, 5)
        self.assertEqual(result, 7)

    def test_max_negative_numbers(self):
        result = self.calculator.max(-3, -8)
        self.assertEqual(result, -3)

    def test_max_equal_numbers(self):
        result = self.calculator.max(4, 4)
        self.assertEqual(result, 4)

    def test_min(self):
        result = self.calculator.min(7, 5)
        self.assertEqual(result, 5)

    def test_min_negative_numbers(self):
        result = self.calculator.min(-3, -8)
        self.assertEqual(result, -8)

    def test_min_equal_numbers(self):
        result = self.calculator.min(4, 4)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
