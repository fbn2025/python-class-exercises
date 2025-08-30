from abc import ABC, abstractmethod

class AbstractBankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def __str__(self):
        pass


class BankAccount(AbstractBankAccount):
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            print("Insufficient funds. Withdrawal cancelled.")
        else:
            self.balance -= amount

    def __str__(self):
        return f"{self.name} has a balance of {self.balance:.2f}"


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate < 0:
            raise ValueError("Interest rate cannot be negative")
        self.balance += self.balance * (rate / 100)


# --- Example usage ---
account = BankAccount("Alice Yetunde", 2500)
account.deposit(500)
account.withdraw(300)
print(account)  # Alice has a balance of 2700.00


savings = SavingsAccount("Bob Marley", 5000)
savings.add_interest(5)   # add 5% interest
print(savings)  # Bob has a balance of 5250.00

