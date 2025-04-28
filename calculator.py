import math

class Calculator:
    def __init__(self):
        self.inputA = 0
        self.inputB = 0
        self.output = 0

    def set_inputs(self, a, b):
        self.inputA = a
        self.inputB = b

    def get_output(self):
        return self.output

    def add(self):
        self.output = self.inputA + self.inputB
        return self.output

    def subtract(self):
        self.output = self.inputA - self.inputB
        return self.output

    def multiply(self):
        self.output = self.inputA * self.inputB
        return self.output

    def divide(self):
        if self.inputB != 0:
            self.output = self.inputA / self.inputB
        else:
            self.output = "Error: Division by zero"
        return self.output

    def square_root(self):
        if self.inputA >= 0:
            self.output = math.sqrt(self.inputA)
        else:
            self.output = "Error: Negative input"
        return self.output

    def exponentiate(self):
        self.output = self.inputA ** self.inputB
        return self.output

    def logarithm(self):
        if self.inputA > 0:
            self.output = math.log(self.inputA)
        else:
            self.output = "Error: Logarithm undefined for non-positive values"
        return self.output
