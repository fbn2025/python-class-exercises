## Class Exercise on OOP

Task: Create a simple BankAccount class.
It should store the account holder's name and balance.
It should inherit from the AbstractBankAccount abstract class

It should have methods:

deposit(amount) -> adds to balance
withdraw(amount) -> removes from balance (but not below 0)
__str__() -> prints account details

Then Create a subclass called SavingsAccount that:
Inherits from BankAccount
Adds a method add_interest(rate) that increases the balance by a percentage

Goal: To practice creating your own classes, methods, inheritance, and state management.

# Solution
    
from abc import ABC, abstractmethod

# Abstract Base Class
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


# Concrete BankAccount Class
class BankAccount(AbstractBankAccount):
    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def __str__(self):
        return f"Account Holder: {self.holder_name}, Balance: {self.balance:.2f}"


# SavingsAccount subclass
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
        else:
            print("Interest rate must be positive.")


# --- Testing the classes ---
if __name__ == "__main__":
    # Create a BankAccount
    acc1 = BankAccount("Alice", 500)
    print(acc1)
    acc1.deposit(200)
    acc1.withdraw(100)
    print(acc1)

    print("\n--- Savings Account Example ---")
    # Create a SavingsAccount
    sav_acc = SavingsAccount("Bob", 1000)
    print(sav_acc)
    sav_acc.add_interest(5)   # 5% interest
    print(sav_acc)

