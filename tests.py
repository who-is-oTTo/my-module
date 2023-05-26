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

    # Тести з очікуваними помилками

    def test_missing_method(self):
        with self.assertRaises(AttributeError):
            result = self.calculator.nonexistent_method(2, 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            result = self.calculator.add("2", 3)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            result = self.calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
