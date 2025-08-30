class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Unable to withdraw: Insufficient funds"
        self.balance -= amount
        return self.balance


def __str__(self):
        return f"{self.name} your account balance is {self.balance}"

# TODO: Create a SavingsAccount class that inherits from BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return f"{self.name} you have a balance of {self.balance} and an interest rate of {self.interest_rate}"

    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        return f"after adding interest your new balance is {self.balance}"

# Example usage
account = BankAccount("Alice", 1000)
danies = SavingsAccount("Ghandi", 2000)
print(account)
print(danies)
print(danies.withdraw(5000))
