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

    # Тест для перевірки наявності неіснуючого методу
    def test_missing_method(self):
        with self.assertRaises(AttributeError):
            # Виклик неіснуючого методу "nonexistent_method"
            self.calculator.nonexistent_method(2, 3)

    # Тест для перевірки некоректного типу вхідних даних
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            # Виклик методу "add" з рядковим аргументом
            self.calculator.add("2", 3)

    # Тест для перевірки ділення на нуль
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            # Виклик методу "divide" з діленням на нуль
            self.calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
