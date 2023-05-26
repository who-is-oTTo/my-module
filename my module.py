# my_module.py
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
