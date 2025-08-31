from abc import ABC, abstractmethod
from decimal import Decimal


# Abstract base class
class AbstractBankAccount(ABC):
    @abstractmethod
    def deposit(self, amount: Decimal) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: Decimal) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


# Concrete BankAccount class
class BankAccount(AbstractBankAccount):
    def __init__(self, name: str, balance=0):
        self.name = name
        self.balance = Decimal(balance)

    def deposit(self, amount: Decimal) -> None:
        amount = Decimal(amount)
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: Decimal) -> None:
        amount = Decimal(amount)
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds. Withdrawal cancelled.")

    def __str__(self) -> str:
        # Format to 2 decimal places for money display
        return f"{self.name} has a balance of {self.balance:.2f}"


# SavingsAccount subclass
class SavingsAccount(BankAccount):
    def add_interest(self, rate: float) -> None:
        if rate > 0:
            interest = self.balance * Decimal(rate / 100)
            self.balance += interest
        else:
            print("Interest rate must be positive.")


# Example usage
account = BankAccount("Alice", 1000)
print(account)
account.deposit(250.75)
print(account)
account.withdraw(200.50)
print(account)
account.withdraw(5000)  # insufficient
print(account)

savings = SavingsAccount("Bob", 2000)
print(savings)
savings.add_interest(5)   # Add 5% interest
print(savings)
