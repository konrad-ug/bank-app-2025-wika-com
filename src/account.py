
class Account:
    def __init__(self, first_name, last_name,pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.historia = []
        self.balance = 0.0
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
    def is_pesel_valid(self,pesel):
        if pesel and len(pesel)==11:
            return True
        else:
            return False
    def przelew_przych(self,kwota):
        if kwota>0.0:
            self.balance=self.balance+kwota
            self.historia.append(kwota)
            return self.balance, self.historia
    def przelew_wych(self,kwota,typ):
        if typ=="n":
            if kwota>0.0 and kwota-self.balance<=0.0:
                self.balance=self.balance-kwota
                self.historia.append(kwota*-1)
                return self.balance, self.historia
        elif typ=="e":
            if kwota>0.0 and kwota-self.balance<=0.0:
                oplata=1
                self.balance=self.balance-kwota-oplata
                self.historia.append(kwota*(-1))
                self.historia.append(-oplata)
                return self.balance, self.historia
            else:
                return "nieudany przelew"
    def submit_for_loan(self,kwota):
        if len(self.historia)>2:
            for i in range(1,4):
                if self.historia[-i]<0:
                    if len(self.historia)>4:
                        for i in range(1,6):
                            suma=suma+self.historia[i]
                        if suma>kwota:
                            return True
                    return False
            return True
        else:
            return False
