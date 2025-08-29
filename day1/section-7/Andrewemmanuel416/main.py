class CalculatorHistory:
    def __init__(self):
        self.addition = []
        self.subtraction = []
        self.multiplication = []
        self.division = []

    def __str__(self):
        return f"""
        Addition History: {self.addition}
        Subtraction History: {self.subtraction}
        Multiplication History: {self.multiplication}
        Division History: {self.division}
        """


class Calculator:
    def __init__(self, log_results: bool = False):
        self.log_results = log_results
        self.history = CalculatorHistory()

    def add(self, num1: float, num2: float):
        result = num1 + num2
        if self.log_results:
            print(f"{num1} + {num2} = {result}")
        self.history.addition.append((num1, num2, result))
        return result

    def sub(self, num1: float, num2: float):
        result = num1 - num2
        if self.log_results:
            print(f"{num1} - {num2} = {result}")
        self.history.subtraction.append((num1, num2, result))
        return result

    def multi(self, num1: float, num2: float):
        result = num1 * num2
        if self.log_results:
            print(f"{num1} * {num2} = {result}")
        self.history.multiplication.append((num1, num2, result))
        return result

    def div(self, num1: float, num2: float):
        if num2 == 0:
            print("Error: Division by zero is undefined.")
            return None
        result = num1 / num2
        if self.log_results:
            print(f"{num1} / {num2} = {result}")
        self.history.division.append((num1, num2, result))
        return result


# Example usage
if __name__ == "__main__":
    calc = Calculator(log_results=True)

    calc.add(10, 5)
    calc.sub(20, 7)
    calc.multi(3, 4)
    calc.div(15, 3)
    calc.div(10, 0)  # Division by zero test

    print(calc.history)
