import subprocess
import unittest

class TestCLIIntegration(unittest.TestCase):

    def run_cli(self, inputs):
        proc = subprocess.Popen(
            ['python3', 'main.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        out, err = proc.communicate(inputs)
        return out

    def test_addition(self):
        inputs = "TestUser\n1\n4\n5\n0\n"
        output = self.run_cli(inputs)
        self.assertIn("Result: 9.0", output)

    def test_subtraction_negative(self):
        inputs = "TestUser\n2\n3\n8\n0\n"
        output = self.run_cli(inputs)
        self.assertIn("Result: -5.0", output)

    def test_division_by_zero(self):
        inputs = "TestUser\n4\n10\n0\n0\n"
        output = self.run_cli(inputs)
        self.assertIn("Error: Division by zero", output)

    def test_square_root(self):
        inputs = "TestUser\n5\n25\n0\n"
        output = self.run_cli(inputs)
        self.assertIn("Result: 5.0", output)

    def test_logarithm_positive(self):
        inputs = "TestUser\n7\n1\n0\n"
        output = self.run_cli(inputs)
        self.assertIn("Result: 0.0", output)

if __name__ == "__main__":
    unittest.main()
