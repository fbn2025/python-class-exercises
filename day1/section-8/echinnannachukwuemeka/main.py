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
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}"

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
            print(f"Added interest: {interest}. New balance: {self.balance}")
        else:
            print("Interest rate must be positive.")

# Example usage:
if __name__ == "__main__":
    account = BankAccount("Smart", 1000)
    print(account)
    account.deposit(500)
    account.withdraw(200)
    print(account)

    savings = SavingsAccount("Nnanna", 2000)
    print(savings)
    savings.add_interest(5)
    print(savings)
