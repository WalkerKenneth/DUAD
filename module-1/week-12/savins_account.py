from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, min_balance) -> None:
        super().__init__()
        self.min_balance = min_balance


    def withdraw(self, amount):
        if (self.balance - amount) < self.min_balance:
            self.balance -= amount
        else:
            print('Impossible transaction, Not enough balance in the account')