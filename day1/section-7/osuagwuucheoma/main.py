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
            #self.history["addition"].append((num1, num2)is {result})
            #goal
        self.history.addition.append((num1, num2, result))

        return result
        
    def subtract (self, num1, num2):
        difference = num1 - num2
        self.history.subtraction.append((num1, num2, difference))
        return difference

    def divide (self, num1, num2):
        result = num1 / num2
        self.history.division.append((num1, num2, result))
        return result

    def multiplication(self, num1, num2):
        product = num1 * num2

        self.history.multiplication.append((num1, num2, product))

        return product
            

calculator = Calculator()

calculator.add(4,5)
calculator.subtract(40,20)
calculator.subtract(20,20)
calculator.divide(80,2)
calculator.multiplication(20,20)

print("The calculator history is", calculator.history)




        




