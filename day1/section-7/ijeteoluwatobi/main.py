class CalculatorHistory:
    def __init__(self):
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
        self.history = CalculatorHistory()   # use object instead of dict

    def add(self, num1: float, num2: float):
        result = num1 + num2

        if self.log_results:
            print(f"The sum of {num1} and {num2} is {result}")

        # now object-based access
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
            print(f"The product of {num1} and {num2} is {result}")
        self.history.multiplication.append((num1, num2, result))
        return result

    def divide(self, num1: float, num2: float):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = num1 / num2
        if self.log_results:
            print(f"The division of {num1} by {num2} is {result}")
        self.history.division.append((num1, num2, result))
        return result


calculator = Calculator()

calculator.add(4, 5)
calculator.subtract(20, 25)
calculator.divide(20, 25)
calculator.multiply(-20, 30)

# This prints object history
print(calculator.history)

# or you access directly through the self history
print("Addition history:", calculator.history.addition)
print("Subtraction history:", calculator.history.subtraction)
print("Multiplication history:", calculator.history.multiplication)
print("Division history:", calculator.history.division)
