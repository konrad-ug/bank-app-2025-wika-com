class Account:
    def __init__(self):
        self.balance = 0.0
        self.historia=[]

    def przelew_przych(self,kwota):
        if kwota>0.0:
            self.balance=self.balance+kwota
            self.historia.append(kwota)
        else:
            return "Przelew nieudany"
        
    def przelew_wych(self,kwota,typ):
        if typ=="n":
            if kwota>0.0 and kwota-self.balance<=0.0:
                self.balance=self.balance-kwota
                self.historia.append(-kwota)
            else:
                return "Przelew nieudany"
        elif typ=="e":
            if kwota>0.0 and kwota-self.balance<=0.0:
                oplata=1
                self.balance=self.balance-kwota-oplata
                self.historia.append(-kwota)
                self.historia.append(-oplata)
            else:
                return "Przelew nieudany"
            