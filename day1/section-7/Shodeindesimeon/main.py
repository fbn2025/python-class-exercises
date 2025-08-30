class CalculatorHistory:
    def __init__(self):
        self.addition = []
        self.subtraction = []
        self.division = []
        self.multiplication = []

    def __str__(self):
        return (
            f"Addition: {self.addition}\n"
            f"Subtraction: {self.subtraction}\n"
            f"Division: {self.division}\n"
            f"Multiplication: {self.multiplication}\n"
        )


class Calculator:
    def __init__(self, log_results: bool = False):
        self.log_results = log_results
        self.history = CalculatorHistory()

    def add(self, num1: float, num2: float):
        result = num1 + num2

        if self.log_results:
            print(f"{num1} + {num2} = {result}")

        self.history.addition.append((num1, num2, result))

        return result
    
    def subtract(self, num1: float, num2: float):
        result = num1 - num2

        if self.log_results:
            print(f"{num1} - {num2} = {result}")

        self.history.subtraction.append((num1, num2, result))

        return result
    
    def divide(self, num1: float, num2: float):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")

        result = num1 / num2

        if self.log_results:
            print(f"{num1} / {num2} = {result}")

        self.history.division.append((num1, num2, result))

        return result
    
    def multiply(self, num1: float, num2: float):
        result = num1 * num2

        if self.log_results:
            print(f"{num1} * {num2} = {result}")

        self.history.multiplication.append((num1, num2, result))

        return result

calculator = Calculator(log_results=True)

calculator.add(4, 5)
calculator.subtract(20, 25)
calculator.divide(20, 25)
calculator.multiply(-20, 30)

print(f"The calculator history is {calculator.history}")
