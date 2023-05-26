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
        # Перевірка додавання двох чисел
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        # Перевірка віднімання двох чисел
        result = self.calculator.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        # Перевірка множення двох чисел
        result = self.calculator.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_divide(self):
        # Перевірка ділення двох чисел
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        # Перевірка ділення на нуль, очікується помилка ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)

    def test_square_root(self):
        # Перевірка обчислення квадратного кореня
        result = self.calculator.square_root(16)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
