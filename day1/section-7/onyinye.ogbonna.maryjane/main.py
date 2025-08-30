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
    
    def divide(self,num1: float, num2: float):
        result = num1 / num2

        if self.log_results:
            print(f"The division of {num1} and {num2} is {result}")

        self.history.division.append((num1, num2, result))
        return result

        # goal 
        # self.history.addition.append((num1, num2, result))  

calculator = Calculator()

calculator.add(4, 5)
calculator.add(20, 25)
calculator.add(-20, 30)
calculator.subtract(40, 20)
calculator.subtract(60, 10)
calculator.subtract(30, 20)
calculator.multiply(5, 3)
calculator.multiply(10, 20)
calculator.multiply(11, 7)
calculator.divide(5, 3)
calculator.divide(10, 3)
calculator.divide(25, 5)


print(calculator.history)
