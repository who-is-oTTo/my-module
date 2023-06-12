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
        self.assertEqual(result, 5, "Помилка у методі add()")

    def test_subtract(self):
        result = self.calculator.subtract(5, 2)
        self.assertEqual(result, 3, "Помилка у методі subtract()")

    def test_multiply(self):
        result = self.calculator.multiply(4, 3)
        self.assertEqual(result, 12, "Помилка у методі multiply()")

    def test_divide(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5, "Помилка у методі divide()")

    def test_square_rootimport unittest
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
        self.assertEqual(result, 5, "Помилка у методі add()")

    def test_subtract(self):
        result = self.calculator.subtract(5, 2)
        self.assertEqual(result, 3, "Помилка у методі subtract()")

    def test_multiply(self):
        result = self.calculator.multiply(4, 3)
        self.assertEqual(result, 12, "Помилка у методі multiply()")

    def test_divide(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5, "Помилка у методі divide()")

    def test_square_root(self):
        result = self.calculator.square_root(16)
        self.assertEqual(result, 4, "Помилка у методі square_root()")

    def test_missing_method(self):
        with self.assertRaises(AttributeError):
            self.calculator.nonexistent_method(2, 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            self.calculator.add("2", 3)

    def test_zero_division(self):
        result = self.calculator.divide(5, 0)
        self.assertIsNone(result, "Повернення None при діленні на нуль")

if __name__ == '__main__':
    unittest.main(verbosity=2)





