## Practice Keeping State

# Task: implement a new class called CalculatorHistory, then initialize it within the __init__ method of the calculator class. 
# Purpose: To make it possible to use object accessors to access history methods rather than dictionary accessors
# Starting point:


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
            subtraction: {self.subtraction}
            division: {self.division}
            multiplication: {self.multiplication}
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

    def sub(self, num1: float, num2: float):
        diff = num1 -num2
        if self.log_results:
            print(f"The sum of {num1} and {num2} is {diff}")

        self.history.subtraction.append((num1, num2, diff))
        return diff
    
    def div(self, num1: float, num2: float):
        di = num1 /num2
        if self.log_results:
            print(f"The sum of {num1} and {num2} is {di}")

        self.history.division.append((num1, num2, di))
        return di

    def mul(self, num1: float, num2: float):
        mu = num1 * num2
        if self.log_results:
            print(f"The sum of {num1} and {num2} is {mu}")

        self.history.multiplication.append((num1, num2, mu))
        return mu

        #self.history["addition"].append((num1, num2, result))
        # goal 

calculator = Calculator()

calculator.add(4, 5)
calculator.add(20, 25)
calculator.add(20, 30)
calculator.sub(40, 30)
calculator.sub(50, 30)
calculator.div(20, 2)
calculator.div(40, 4)
calculator.mul(3, 30)
calculator.mul(4, 10)

print(calculator.history)
