class CalculatorHistory:
    def __init__(self):
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

        return result
    
    def subtract(self, num1: float, num2: float):
        difference = num1 - num2

        if self.log_results:
            print(f"The difference between {num1} and {num2} is {difference}")

        self.history.subtraction.append((num1, num2, difference))

        return difference
    
    def multiply(self, num1: float, num2: float):
        product = num1 * num2

        if self.log_results:
            print(f"The product of {num1} and {num2} is {product}")

        self.history.multiplication.append((num1, num2, product))

        return product
    
    def divide(self, num1: float, num2: float):
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        quotient = num1 / num2
        if self.log_results:
            print(f"The quotient of {num1} and {num2} is {quotient}")
        self.history.division.append((num1, num2, quotient))
        return quotient
    


calculator = Calculator()

calculator.add(4, 5)
calculator.add(44, 5)
calculator.subtract(20, 25)
calculator.subtract(50, 20)
calculator.multiply(20, 30)
calculator.multiply(5, 30)
calculator.divide(100, 10)
calculator.divide(50, 2)


print("The calculator history is", calculator.history)
