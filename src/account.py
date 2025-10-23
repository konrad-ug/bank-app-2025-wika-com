class Account:
    def __init__(self, first_name, last_name,pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
    def is_pesel_valid(self,pesel):
        if pesel and len(pesel)==11:
            return True
        else:
            return False
    def przelew_przych(self,kwota):
        if kwota>0:
            self.balance=self.balance+kwota
            return self.balance
    def przelew_wych(self,kwota,typ):
        if typ=="n":
            if kwota>0 and kwota-self.balance<0:
                self.balance=self.balance-kwota
                return self.balance
        elif typ=="e":
            if kwota>0 and kwota-self.balance-1<0:
                self.balance=self.balance-kwota
                return self.balance
