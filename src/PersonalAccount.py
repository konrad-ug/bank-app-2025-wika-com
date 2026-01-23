from src.account import Account
from datetime import date
from src.smtp.smtp import SMTPClient
class PersonalAccount(Account):
    def __init__(self, first_name, last_name,pesel):
        if not self.is_pesel_valid(pesel):
            raise ValueError("Niepoprawny PESEL")
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel
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
    def send_history_via_email(self, email_address: str) -> bool:
        today = date.today().isoformat()
        subject = f"Account Transfer History {today}"
        text = f"Personal account history:{self.historia}"

        return SMTPClient.send(subject, text, email_address)