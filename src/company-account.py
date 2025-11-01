from src.account import Account
class CompanyAccount:
    def __init__(self, company_name, NIP):
        self.company_name = company_name
        self.NIP = NIP
        self.balance = 0.0
        self.NIP = NIP if self.is_NIP_valid(NIP) else "Invalid"
    def is_NIP_valid(NIP):
        if NIP and len(NIP)==11: 
            return True 
        else: 
            return False
    def przelew_przych(self,kwota):
        if kwota>0:
            self.balance=self.balance+kwota
            return self.balance
    def przelew_wych(self,kwota):
        if kwota>0 and kwota-self.balance<0:
            self.balance=self.balance-kwota
            return self.balance
