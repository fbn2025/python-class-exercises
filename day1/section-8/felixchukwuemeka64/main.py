class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"


# SavingsAccount inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.02):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added. New balance: {self.balance}")


# Example usage
account = BankAccount("Alice", 1000)
print(account)
account.deposit(500)
account.withdraw(300)
print(account)

savings = SavingsAccount("Bob", 2000, 0.05)
print(savings)
savings.add_interest()
print(savings)
