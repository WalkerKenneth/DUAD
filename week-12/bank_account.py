class BankAccount:

    def __init__(self) -> None:
        self.balance = 0


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        self.balance += (-amount)