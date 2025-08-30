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
            print(f"The difference of {num1} and {num2} is {difference}")

        self.history.subtraction.append((num1, num2, difference))

        return difference

    def division(self, num1: float, num2: float):
        division = num1/num2

        if self.log_results:
            print(f"The division of {num1} and {num2} is {division}")

        self.history.division.append((num1, num2, division))

        return division
    

    def multiplication(self, num1: float, num2: float):
        multi = num1*num2

        if self.log_results:
            print(f"The multiplication of {num1} and {num2} is {multi}")

        self.history.multiplication.append((num1, num2, multi))

        return multi


calculator = Calculator()

calculator.add(4, 5)
calculator.add(20, 25)
calculator.add(-20, 30)
calculator.subtract(10, 5)
calculator.multiplication(4,6)
calculator.division(65,5)

print(calculator.history)

cal = Calculator(log_results=True)
cal.add(2,2)
cal.division(65,7)
cal.subtract(54,8)
cal.multiplication(5,7)



