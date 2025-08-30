class CalculatorHistory:
    def __init__(self, ):
        # add the remaining
        self.addition = []
        self.subtraction = []
        self.division = []
        self.multiplication = []

    def __str__(self):
        return f"""
            Addition: {self.addition}
            Subtraction: {self.subtraction}
            Division: {self.division}
            Multiplication: {self.multiplication}
        """

class Calculator:
    def __init__(self, log_results: bool = False):
        self.log_results = log_results
        self.history = CalculatorHistory()

    def add(self, num1: float, num2: float):
        result = num1 + num2

        if self.log_results:
            print(f"The sum of {num1} and {num2} is {result}")

        self.history.addition.append((num1, num2, result))
        # goal 
        # self.history.addition.append((num1, num2, result))

        return result
    
    def subtract(self, num1, num2,):
        result = num1 - num2

        if self.log_results:
            print(f"The difference of {num1} and {num2} is {result}")

        self.history.subtraction.append((num1, num2, result))

        return result
    def multiply(self, num1, num2):
        product = num1 * num2

        self.history.multiplication.append((num1, num2, product))

        return product
    def divide(self, num1, num2):
        try:
            result = num1 / num2

            self.history.division.append((num1, num2, result))

            return result
        except ZeroDivisionError:
            print("You attempted to divide by zero")
            return None

calculator = Calculator()

calculator.add(4, 5)
calculator.add(20, 25)
calculator.add(-20, 30)
calculator.subtract(10, 5)
calculator.multiply(3, 7)
calculator.divide(10, 2)

print(calculator.history)
