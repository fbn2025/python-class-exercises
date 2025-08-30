class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"


# SavingsAccount inherits from BankAccount
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate < 0:
            print("Interest rate must be positive.")
            return
        interest = self.balance * rate
        self.balance += interest

    def __str__(self):
        return f"{self.name} has a savings balance of {self.balance}"


# Example usage
account = BankAccount("Reagan", 1000)
print(account)
account.deposit(500)
account.withdraw(300)
print(account)

savings = SavingsAccount("Ijeomah", 2000)
print(savings)
savings.add_interest(0.05)  # 5% interest
print(savings)
