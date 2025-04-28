import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.calc.set_inputs(4, -2)
        self.assertEqual(self.calc.add(), 2)

    def test_subtract(self):
        self.calc.set_inputs(5, 10)
        self.assertEqual(self.calc.subtract(), -5)

    def test_multiply(self):
        self.calc.set_inputs(3, 7)
        self.assertEqual(self.calc.multiply(), 21)

    def test_divide_normal(self):
        self.calc.set_inputs(8, 2)
        self.assertEqual(self.calc.divide(), 4)

    def test_divide_by_zero(self):
        self.calc.set_inputs(5, 0)
        self.assertEqual(self.calc.divide(), "Error: Division by zero")
