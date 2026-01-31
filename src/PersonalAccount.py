from src.account import Account
from datetime import date
from src.smtp.smtp import SMTPClient

#Feature 1
class PersonalAccount(Account):
    def __init__(self, first_name, last_name,pesel, promo=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

        #Feature 2
        if self.is_pesel_valid(pesel):
            self.pesel = pesel
        else:
            self.pesel = "Invalid"

        if self._is_promo_valid(promo, pesel):
            self.balance = 50
        

    def to_dict(self):
        return {
            "name": self.first_name,
            "surname": self.last_name,
            "pesel": self.pesel,
            "balance": self.balance,
            "historia": self.historia
        }

    #Feature 4 i 5
    def _is_promo_valid(self, code, pesel):
        if code is None or not code.startswith("PROM_"):
            return False
        if len(code) != 8:
            return False
        
        year = int(pesel[0:2])
        month = int(pesel[2:4])
        if month > 20:
            full_year = 2000 + year
        else:
            full_year = 1900 + year
        return full_year > 1960
    
    #Feature 3
    def is_pesel_valid(self,pesel):
        if pesel and len(pesel)==11:
            return True
        else:
            return False
        
    #Feature 12
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
        
    def send_history_via_email(self, email_address: str) -> bool:
        today = date.today().isoformat()
        subject = f"Account Transfer History {today}"
        text = f"Personal account history: {self.historia}"
        return SMTPClient.send(subject, text, email_address)