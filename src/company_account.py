from src.account import Account
class CompanyAccount(Account):
    def __init__(self, company_name, NIP):
        self.company_name = company_name
        self.NIP = NIP
        self.balance = 0.0
        self.NIP = NIP if self.is_NIP_valid(NIP) else "Invalid"
        super().__init__()

    def is_NIP_valid(self,NIP):
        if NIP and len(NIP)==10: 
            return True 
        else: 
            return False
        
    def take_loan(self,kwota):
        if self.balance > 2*kwota:
            if -1775 not in self.historia:
                return False
            else:
                self.balance=self.balance+kwota
                return True
        else:
            return False