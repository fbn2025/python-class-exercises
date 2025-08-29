# class BankAccount:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         pass  # implement this

#     def withdraw(self, amount):
#         pass  # implement this

#     def __str__(self):
#         return f"{self.name} has a balance of {self.balance}"

# # TODO: Create a SavingsAccount class that inherits from BankAccount

# # Example usage
# account = BankAccount("Alice", 1000)
# print(account)



from abc import ABC, abstractmethod

# Abstract class
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


# BankAccount class inheriting from AbstractBankAccount
class BankAccount(AbstractBankAccount):
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} Withdrew {amount}. New balance is: {self.balance}")
        else:
            print("Can not withdraw, insufficient funds or invalid amount.")

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"


# SavingsAccount subclass
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
            print(f"Interest of {interest:.2f} added. New balance is: {self.balance}")
        else:
            print("Interest rate must be positive.")


# Example usage
account = BankAccount("Faith", 1000)
print(account)
account.deposit(200)
account.withdraw(300)
print(account)

savings = SavingsAccount("Stella", 2000)
print(savings)
savings.add_interest(5)  # 5% interest
print(savings)
