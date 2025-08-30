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

        # self.history["addition"].append((num1, num2, result))
        # goal 
        self.history.addition.append((num1, num2, result))

        return result
    def subtract(self, num1: float, num2: float):
        Difference = num1 - num2
        if self.log_results:
            print(f"The difference of {num1} and {num2} is {Difference}")
        
        self.history.subtraction.append((num1, num2, Difference))
        return Difference
    
    def divide(self, num1: float, num2: float):
        Division = num1 / num2
        if self.log_results:
            print(f"The division of {num1} and {num2} is {Division}")
        
        self.history.division.append((num1, num2, Division))
        return Division
    
    def multiply(self, num1: float, num2: float):
        Multiplication = num1 * num2
        if self.log_results:
            print(f"The multiplication of {num1} and {num2} is {Multiplication}")
        
        self.history.multiplication.append((num1, num2, Multiplication))
        return Multiplication



calculator = Calculator()
calculator = Calculator()

calculator.add(4, 5)
calculator.add(20, 25)
calculator.add(-20, 30)
calculator.subtract(-20, 30)
calculator.subtract(20, 10)
calculator.divide(20, 10)
calculator.divide(68, 7)
calculator.multiply(20, 10)
calculator.multiply(68, 7)

print(calculator.history)
