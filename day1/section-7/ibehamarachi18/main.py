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

        # dictionary accessor
        #self.history["addition"].append((num1, num2, result))

        self.history.addition.append((num1, num2, result)) 

        return result
    
    def subtract(self, num1, num2):
        difference = num1 - num2
        self.history.subtraction.append((num1, num2, difference)) 

        return difference
    
    def multiplication(self, num1, num2):
        product = num1 * num2
        self.history.multiplication.append((num1, num2, product)) 

        return product
    
    def division(self, num1, num2):
        divide = num1 / num2
        self.history.division.append((num1, num2, divide)) 

        return divide


# Example usage
calculator = Calculator()

calculator.add(4, 5)
calculator.subtract(25, 20)
calculator.multiplication(-20, 30)
calculator.division(20, 20)

print("The calculator history is", calculator.history)
