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
            
    def submit_for_loan(self,kwota):
        if len(self.historia)>2:
            for i in range(1,4):
                if self.historia[-i]<0:
                    if len(self.historia)>=5:
                        suma=0
                        for j in range(1,6):
                            suma=suma+self.historia[-j]
                        if suma>kwota:
                            self.balance=self.balance+kwota
                            return True
                    return False
            self.balance=self.balance+kwota
            return True
        else:
            return False