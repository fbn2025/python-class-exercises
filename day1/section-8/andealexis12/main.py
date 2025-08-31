class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal must be positive")

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
        else:
            print("Rate must be positive")
# Example usage
account = BankAccount("Alice", 1000)
print(account)

