from abc import ABC, abstractmethod

# Abstract base class
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

class BankAccount (AbstractBankAccount):
    def __init__(self, name, balance=0):
        self.name = name
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
            print("Insufficient funds or invalid amount.")

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"
    
    # SavingsAccount subclass
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            self.balance += self.balance * (rate / 100)
        else:
            print("Interest rate must be positive.")


# TODO: Create a SavingsAccount class that inherits from BankAccount

# Example usage
account = BankAccount("Onyinye", 1000)
print(account)

account.deposit(1000)
print(account)

account.withdraw(700)
print(account)

savings = SavingsAccount("Maryjane", 5000)
print(savings)

savings.add_interest(10)  # Add 10% interest
print(savings)
