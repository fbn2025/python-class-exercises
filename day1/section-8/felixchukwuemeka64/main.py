class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        pass  # implement this

    def withdraw(self, amount):
        pass  # implement this

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"

# TODO: Create a SavingsAccount class that inherits from BankAccount

# Example usage
account = BankAccount("Alice", 1000)
print(account)

