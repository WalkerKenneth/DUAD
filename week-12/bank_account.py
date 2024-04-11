class BankAccount:

    def __init__(self) -> None:
        self.balance = 0


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            self.balance -= amount
        else:
            print('Impossible transaction, Not enough balance in the account')