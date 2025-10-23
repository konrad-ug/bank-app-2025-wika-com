class CompanyAccount:
    def __init__(self, company_name, NIP):
        self.company_name = company_name
        self.NIP = NIP
        self.balance = 0.0
        self.NIP = NIP if self.is_pesel_valid(NIP) else "Invalid"
    def przelew_przych(self,kwota):
        if kwota>0:
            self.balance=self.balance+kwota
            return self.balance
    def przelew_wych(self,kwota):
        if kwota>0 and kwota-self.balance<0:
            self.balance=self.balance-kwota
            return self.balance
