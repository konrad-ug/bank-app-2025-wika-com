from src.account import Account
class PersonalAccount(Account):
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