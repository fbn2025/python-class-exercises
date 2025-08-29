class CalculatorHistory:
    def __init__(self):
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
    
    def subtract(self, num1: float, num2: float):
        result = num1 - num2

        if self.log_results:
            print(f"The difference of {num1} and {num2} is {result}")

        self.history.subtraction.append((num1, num2, result))

        return result
    
    def divide(self, num1: float, num2: float):
        try:
            result = num1 / num2

            if self.log_results:
                print(f"The quotient of {num1} and {num2} is {result}")

            self.history.division.append((num1, num2, result))

            return result
        except ZeroDivisionError:
            print("You attempted to divide by zero")
            return None
        
    def multiply(self, num1: float, num2: float):
        result = num1 * num2

        if self.log_results:
            print(f"The product of {num1} and {num2} is {result}")

        self.history.multiplication.append((num1, num2, result))

        return result


calculator = Calculator()

calculator.add(4, 5)
calculator.subtract(25, 5)
calculator.divide(50, 2)
calculator.multiply(5, 6)

print(calculator.history)
