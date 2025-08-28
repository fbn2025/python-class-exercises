class CalculatorHistory:
    def __init__(self):
        # add the remaining
        self.addition = []

    def __str__(self):
        return f"""
            Addition: {self.addition}
        """

class Calculator:
    def __init__(self, log_results: bool = False):
        self.log_results = log_results
        self.history = {
            "addition": []
        }

    def add(self, num1: float, num2: float):
        result = num1 + num2

        if self.log_results:
            print(f"The sum of {num1} and {num2} is {result}")

        self.history["addition"].append((num1, num2, result))
        # goal 
        # self.history.addition.append((num1, num2, result))

        return result


calculator = Calculator()

calculator.add(4, 5)
calculator.add(20, 25)
calculator.add(-20, 30)

print(calculator.history)

