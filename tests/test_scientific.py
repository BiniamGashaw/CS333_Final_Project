
import unittest
from scientific import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = ScientificCalculator()
    
    def test_square_root_positive(self):
        self.setUp()
        self.assertEqual(self.calc.square_root(16), 4)

    def test_square_root_negative(self):
        self.setUp()
        self.assertEqual(self.calc.square_root(-9), "Error: Negative input")

    def test_exponentiate(self):
        self.setUp()
        self.assertEqual(self.calc.exponentiate(2, 3), 8)

    def test_logarithm_positive(self):
        self.setUp()
        self.assertEqual(self.calc.logarithm(1), 0)

    def test_logarithm_zero(self):
        self.setUp()
        self.assertEqual(self.calc.logarithm(0), "Error: Logarithm undefined for non-positive values")