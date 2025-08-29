# Task: implement a new class called CalculatorHistory, then initialize it within the init method of the calculator class. Purpose: To make it possible to use object accessors to access history methods rather than dictionary accessors Starting point:

class CalculatorHistory:
    def __init__(self):
        self.addition = []
        self.subtraction = []
        self.division = []
        self.multiplication = []

    def log_addition(self, num1, num2, result):
        self.addition.append((num1, num2, result))

    def log_subtraction(self, num1, num2, result):
        self.subtraction.append((num1, num2, result))

    def log_division(self, num1, num2, result):
        self.division.append((num1, num2, result))

    def log_multiplication(self, num1, num2, result):
        self.multiplication.append((num1, num2, result))

class Calculator:
    def __init__(self, log_results: bool = False):
        self.log_results = log_results
        self.history = CalculatorHistory()

    def add(self, num1: float, num2: float):
        result = num1 + num2

        if self.log_results:
            print(f"The sum of {num1} and {num2} is {result}")

        self.history.log_addition(num1, num2, result)

        return result



# Example
calculator = Calculator()
print(calculator.add(4, 5))
calculatorHistory = calculator.history
print(calculatorHistory.addition)
