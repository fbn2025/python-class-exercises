# 8.6 OOP Class Exercise: Bank Account and Savings Account
class BankAccount:
    def __init__(self, owner, opening_balance=0):
        self.owner = owner
        self.balance = opening_balance

    def make_deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} deposited {amount}. Balance is now {self.balance}.")
        else:
            print("Deposit failed: amount must be greater than zero.")

    def make_withdrawal(self, amount):
        if amount <= 0:
            print("Withdrawal failed: amount must be greater than zero.")
        elif amount > self.balance:
            print("Withdrawal failed: insufficient funds.")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. Balance is now {self.balance}.")

    def __str__(self):
        return f"Account[{self.owner}] → Current Balance: {self.balance}"


class SavingsAccount(BankAccount):
    def apply_interest(self, percentage):
        if percentage > 0:
            earned = self.balance * (percentage / 100)
            self.balance += earned
            print(f"Interest of {percentage}% applied. Earned {earned}, new balance: {self.balance}.")
        else:
            print("Interest rate must be above zero.")


# Demo run
acct1 = BankAccount("Alice Johnson", 1000)
print(acct1)
acct1.make_deposit(400)
acct1.make_withdrawal(250)
print(acct1)

print("\n--- Savings Account Demonstration ---")
savings_acct = SavingsAccount("Robert Smith", 2000)
print(savings_acct)
savings_acct.apply_interest(4)
savings_acct.make_withdrawal(500)
print(savings_acct)
