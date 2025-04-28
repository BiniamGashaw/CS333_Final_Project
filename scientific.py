import math

class ScientificCalculator:
    def __init__(self):
        self.inputA = 0
        self.inputB = 0
        self.output = 0

    def set_inputs(self, a, b):
        self.inputA = a
        self.inputB = b

    def get_output(self):
        return self.output

    def square_root(self, x):
        if x >= 0:
            return math.sqrt(x)
        else:
            return "Error: Negative input"

    def exponentiate(self, inputA, inputB):
        return inputA ** inputB

    def logarithm(self, x):
        if x > 0:
            return math.log(x)
        else:
            return "Error: Logarithm undefined for non-positive values"
