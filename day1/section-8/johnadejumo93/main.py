# TODO: Create a SavingsAccount class that inherits from BankAccount

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
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
        elif amount > self.balance:
            print("Insufficient funds. Withdrawal not allowed.")
        else:
            self.balance -= amount

    def __str__(self):
        return f"{self.name} has a balance of {self.balance:.2f}"


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
        else:
            print("Interest rate must be positive.")


account = BankAccount("Alice", 1000)
print(account)
account.deposit(500)
print(account)
account.withdraw(300)
print(account)

savings = SavingsAccount("Bob", 2000)
print(savings)
savings.add_interest(5)   
print("After interest:", savings)
