
        # goal 
        # Write a function that finds the min and max number in a list of numbers
        # self.history.addition.append((num1, num2, result))

class CalculatorHistory:
    def __init__(self):
        self.addition = []
        self.subtraction = []
        self.multiplication = []
        self.division = []

    def __str__(self):
        return (
            f"Addition: {self.addition}\n"
            f"Subtraction: {self.subtraction}\n"
            f"Multiplication: {self.multiplication}\n"
            f"Division: {self.division}"
        )

class Calculator:
    def __init__(self, log_results: bool = False):
        self.log_results = log_results
        self.history = CalculatorHistory() 

    def add(self, num1: float, num2: float):
        result = num1 + num2
        if self.log_results:
            print(f"The sum of {num1} and {num2} is {result}")
        self.history.addition.append((num1, num2, result))
        return result

    def subtract(self, num1: float, num2: float):
        result = num1 - num2
        if self.log_results:
            print(f"The difference of {num1} and {num2} is {result}")
        self.history.subtraction.append((num1, num2, result))
        return result

    def multiply(self, num1: float, num2: float):
        result = num1 * num2
        if self.log_results:
            print(f"The multiplication of {num1} and {num2} is {result}")
        self.history.multiplication.append((num1, num2, result))
        return result

    def divide(self, num1: float, num2: float):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        result = num1 / num2
        if self.log_results:
            print(f"The division of {num1} by {num2} is {result}")
        self.history.division.append((num1, num2, result))
        return result
calculator = Calculator()

calculator.add(4, 5)
calculator.subtract(20, 25)
calculator.multiply(-20, 30)
calculator.divide(200, 5)

print(calculator.history)

