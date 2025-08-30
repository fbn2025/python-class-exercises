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

    def withdraw(self, amount):
        if amount > 0:
            self.balance = max(0, self.balance - amount)

    def __str__(self):
        return f"Account holder: {self.name}, Balance: {self.balance}"

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            self.balance += self.balance * (rate / 100)

# Example usage:
if __name__ == "__main__":
    acc = SavingsAccount("Ezinne", 1000)
    print(acc)
    acc.deposit(400)
    print(acc)
    acc.withdraw(200)
    print(acc)
    acc.add_interest(5)
    print(acc)


