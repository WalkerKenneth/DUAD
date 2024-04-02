from bank_account import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self) -> None:
        super().__init__()
        self.min_balance = 100