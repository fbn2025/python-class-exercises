from abc import ABC, abstractmethod

##################
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


#############
class BankAccount(AbstractBankAccount):
    def __init__(self, holder_name, balance=0.0):
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
            print("Insufficient funds or invalid amount.")

    def __str__(self):
        return f"Account Holder: {self.holder_name}, Balance: ₦{self.balance:.2f}"


##################
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
        else:
            print("Interest rate must be positive.")


########
if __name__ == "__main__":
    account = SavingsAccount("Gbolahan", 10000)
    print(account)

    account.deposit(5000)
    account.withdraw(3000)
    account.add_interest(5) 

    print(account)

