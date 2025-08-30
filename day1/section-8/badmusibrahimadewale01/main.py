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


# usage
account = BankAccount("Badmus Ibrahim", 1500)
account.deposit(700)
account.withdraw(500)
print(account) 


savings = SavingsAccount("Yemi Alade", 2000)
savings.add_interest(5)
print(savings) 

