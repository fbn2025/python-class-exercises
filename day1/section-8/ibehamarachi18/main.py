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
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print ("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            print("Insufficient funds. Withdrawal cancelled.")
        else:
            self.balance -= amount

    def __str__(self):
        return f"{self.account_holder} has a balance of {self.balance}"

# TODO: Create a SavingsAccount class that inherits from BankAccount

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate < 0:
            raise ValueError("Interest rate must be positive")
        self.balance += self.balance * (rate / 100)


# Example usage
account = BankAccount("Alice", 1000)
account.deposit(5000)
account.withdraw(3000)
print(account)  # Alice has a balance of 3000.00


savings = SavingsAccount("Osinachi", 5000)
savings.add_interest(10)   # add 10% interest
print(savings)  # Osinachi has a balance of 5500.00
