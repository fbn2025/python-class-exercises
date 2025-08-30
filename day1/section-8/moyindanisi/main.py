from abc import ABC, abstractmethod

class AbstractBankAccount(ABC):
    @abstractmethod
    def deposit(self, amount): pass
    @abstractmethod
    def withdraw(self, amount): pass
    @abstractmethod
    def __str__(self): pass


class BankAccount(AbstractBankAccount):
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0: self.balance += amount
        else:
            print("Deposit amount must be positive")  # implement this

    def withdraw(self, amount):
         if 0 < amount <= self.balance: self.balance -= amount
         else:
             print("Insufficient funds")  # implement this

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"
    
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0: self.balance += self.balance * (rate/100)
        else:
            print("interest rate must be positive.")

# Example usage
account = BankAccount("Alice", 1000)
print(account)
account.deposit(500) 
print(account)
account.withdraw(700)
print(account)  


savings = SavingsAccount("Moyin", 2000)
savings.add_interest(50)
print(savings)
