from src.account import Account
class IndividualAccount(Account):
    def __init__(self, first_name, last_name,pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
        super().__init__()
    def is_pesel_valid(self,pesel):
        if pesel and len(pesel)==11:
            return True
        else:
            return False