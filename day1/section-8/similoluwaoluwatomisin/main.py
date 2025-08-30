## Class Exercise on OOP

# Task: Create a simple BankAccount class.
# It should store the account holder's name and balance.
# It should inherit from the AbstractBankAccount abstract class

# It should have methods:

# deposit(amount) -> adds to balance
# withdraw(amount) -> removes from balance (but not below 0)
# __str__() -> prints account details

# Then Create a subclass called SavingsAccount that:
# Inherits from BankAccount
# Adds a method add_interest(rate) that increases the balance by a percentage

# Goal: To practice creating your own classes, methods, inheritance, and state management.

import abc

class AbstractBankAccount(abc.ABC):
    @abc.abstractmethod
    def deposit(self, amount):
        pass

    @abc.abstractmethod
    def withdraw(self, amount):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass


class BankAccount(AbstractBankAccount):
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"

# TODO: Create a SavingsAccount class that inherits from BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def add_interest(self, rate):
        self.balance += (rate / 100) * self.balance

    def __str__(self):
        return f"{self.name} savings account has a balance of {self.balance}"

#Example usage
account = BankAccount("Alice", 1000)
print(account)
account.deposit(2000)
print(account)
account.withdraw(400)
print(account)

savings_account = SavingsAccount("Alice", 3000)
print(savings_account)
savings_account.deposit(4500)
print(savings_account)
savings_account.add_interest(12)
print(savings_account)
savings_account.withdraw(5500)
print(savings_account)

