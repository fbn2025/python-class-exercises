from abc import ABC, abstractmethod

class AbstractBankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class BankAccount(AbstractBankAccount):
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Current balance is {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance is {self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            print("Insufficient funds")

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance * (rate / 100)
        self.balance += interest
        print(f"Added interest of {interest}. Current balance is {self.balance}")

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
