## Practice Keeping State

# Task: implement a new class called CalculatorHistory, then initialize it within the __init__ method of the calculator class.
# Purpose: To make it possible to use object accessors to access history methods rather than dictionary accessors
# Starting point:

class CalculatorHistory:
    def __init__(self):
        # add the remaining
        self.addition = []
        self.subtraction = []
        self.multiplication = []
        self.division = []

    def __str__(self):
        return f"""
            Addition: {self.addition}
            Subtraction: {self.subtraction}
            Multiplication: {self.multiplication}
            Division: {self.division}
        """

class Calculator:
    def __init__(self, log_results: bool = False):
        self.log_results = log_results
        self.history = CalculatorHistory()

    def add(self, num1: float, num2: float):
        result = num1 + num2

        if self.log_results:
            print(f"The sum of {num1} and {num2} is {result}")

        # goal
        self.history.addition.append((num1, num2, result))

        return result

    def subtract(self, num1: float, num2: float):
        result = num1 - num2

        if self.log_results:
            print(f"The difference of {num1} and {num2} is {result}")

        # goal
        self.history.subtraction.append((num1, num2, result))

        return result

    def multiply(self, num1: float, num2: float):
        result = num1 * num2

        if self.log_results:
            print(f"The multiplication of {num1} and {num2} is {result}")

        # goal
        self.history.multiplication.append((num1, num2, result))

        return result

    def divide(self, num1: float, num2: float):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print(f"Error: Cannot divide by zero!")

        if self.log_results:
            print(f"The division of {num1} and {num2} is {result}")

        # goal
        self.history.division.append((num1, num2, result))

        return result


# calculator = Calculator()

# calculator.add(4, 5)
# calculator.add(20, 25)
# calculator.add(-20, 30)

# calculator.subtract(4, 5)
# calculator.subtract(20, 25)
# calculator.subtract(-20, 30)

# calculator.multiply(4, 5)
# calculator.multiply(20, 25)
# calculator.multiply(-20, 30)

# calculator.divide(4, 5)
# calculator.divide(20, 25)
# calculator.divide(-20, 30)

# print(calculator.history)
