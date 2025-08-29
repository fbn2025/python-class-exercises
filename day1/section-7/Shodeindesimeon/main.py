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

        #self.history["addition"].append((num1, num2, result))
        # goal 
        self.history.addition.append((num1, num2, result))

        return result
    
    def subtract(self, num1: float, num2: float):
        result = num1 - num2

        if self.log_results:
            print(f"The sum of {num1} and {num2} is {result}")

        #self.history["subtraction"].append((num1, num2, result))
        # goal 
        self.history.subtraction.append((num1, num2, result))

        return result
    
    def divide(self, num1: float, num2: float):
        result = num1 / num2

        if self.log_results:
            print(f"The sum of {num1} and {num2} is {result}")

        #self.history["division"].append((num1, num2, result))
        # goal 
        self.history.division.append((num1, num2, result))

        return result
    
    def multiply(self, num1: float, num2: float):
        result = num1 * num2

        if self.log_results:
            print(f"The sum of {num1} and {num2} is {result}")

        #self.history["multiplication"].append((num1, num2, result))
        # goal 
        self.history.multiplication.append((num1, num2, result))

        return result


calculator = Calculator(log_results=True)

calculator.add(4, 5)
calculator.subtract(20, 25)
calculator.divide(20, 25)
calculator.multiply(-20, 30)

#print(f"The calculator history is", calculator.history)
print(f"The calculator history is {calculator.history}")
