class CalculatorHistory:
    def __init__(self):
        # add the remaining
        self.addition = []
        self.subtraction = []
        self.multiplication = []
        self.division = []

    def __str__(self):
        return f"""
            Addition: {self.addition} \n
            Subtraction: {self.subtraction} \n
            Multiplication: {self.multiplication} \n
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
        # goal 
        # self.history.addition.append((num1, num2, result))

        return result
    
    def sub(self, num1: float, num2: float):
        result = num1 - num2

        if self.log_results:
            print(f"The difference of {num1} and {num2} is {result}")

        self.history.subtraction.append((num1, num2, result))
        # goal 
        # self.history.subtraction.append((num1, num2, result))

        return result
    
    def mul(self, num1: float, num2: float):
        result = num1 * num2

        if self.log_results:
            print(f"The product of {num1} and {num2} is {result}")

        self.history.multiplication.append((num1, num2, result))
        # goal 
        # self.history.multiplication.append((num1, num2, result))

        return result
    
    def div(self, num1: float, num2: float):
        result = num1 / num2

        if self.log_results:
            print(f"The division of {num1} and {num2} is {result}")

        self.history.division.append((num1, num2, result))
        # goal 
        # self.history.division.append((num1, num2, result))

        return result




calculator = Calculator()

calculator.add(4, 5)
calculator.add(20, 25)
calculator.add(-20, 30)

calculator.sub(25, 7)
calculator.sub(2, 25)
calculator.sub(-20, 30)

calculator.mul(4, 5)
calculator.mul(20, 25)
calculator.mul(-20, 30)

calculator.div(40, 5)
calculator.div(200, 25)
calculator.div(-200, 20)

print(calculator.history)
