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
            print(f"The sum of {num1} and {num2} is {result}")

        self.history.addition.append((num1, num2, result))
        return result
    
    def subtract(self, num1: float, num2: float):
        result = num1 - num2

        if self.log_results:
            print(f"The difference between {num1} and {num2} is {result}")

        self.history.subtraction.append((num1, num2, result))
        return result
    
    def divide(self, num1: float, num2: float):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")

        result = num1 / num2

        if self.log_results:
            print(f"{num1} divided by {num2} equals {result}")

        self.history.division.append((num1, num2, result))
        return result
    
    def multiply(self, num1: float, num2: float):
        result = num1 * num2

        if self.log_results:
            print(f"The product of {num1} and {num2} is {result}")

        self.history.multiplication.append((num1, num2, result))
        return result

# --- Example usage ---
calculator = Calculator(log_results=True)

calculator.add(4, 5)
calculator.subtract(20, 10)
calculator.divide(100, 4)
calculator.multiply(3, 7)

print(f"The calculator history is:\n{calculator.history}")
