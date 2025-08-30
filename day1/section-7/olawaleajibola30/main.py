## Practice Keeping State
""""
Task: implement a new class called CalculatorHistory, then initialize it within the __init__ method of the calculator class. 
Purpose: To make it possible to use object accessors to access history methods rather than dictionary accessors
Starting point:
"""

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

        #dictionary accessor
        self.history.addition.append((num1, num2, result))
        # goal 
        # self.history.addition.append((num1, num2, result))

        return result

    def subtract(self, num1: float, num2: float):
        result = num1 - num2

        if self.log_results:
            print(f"The difference of {num1} and {num2} is {result}")

        #dictionary accessor
        self.history.subtraction.append((num1, num2, result))
        # goal 
        # self.history.subtraction.append((num1, num2, result))

        return result

    def division(self, num1: float, num2: float):
        result = num1/num2

        if self.log_results:
            print(f"The division of {num1} and {num2} is {result}")

        #dictionary accessor
        self.history.division.append((num1, num2, result))
        # goal 
        # self.history.division.append((num1, num2, result))

        return result

    def multiplication(self, num1: float, num2: float):
        result = num1*num2

        if self.log_results:
            print(f"The multiplication of {num1} and {num2} is {result}")

        #dictionary accessor
        self.history.multiplication.append((num1, num2, result))
        # goal 
        # self.history.multiplication.append((num1, num2, result))

        return result


calculator = Calculator()

calculator.add(4, 5)
calculator.subtract(20, 25)
calculator.multiplication(-20, 30)
calculator.division(-20, 30)

print(calculator.history)

