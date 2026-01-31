from datetime import date
from src.smtp.smtp import SMTPClient

#Feature 6
class Account:
    def __init__(self):
        self.balance = 0.0
        self.historia=[]

    def przelew_przych(self,kwota):
        if kwota>0.0:
            self.balance=self.balance+kwota
            #Feature 11
            self.historia.append(kwota)
        else:
            return "Przelew nieudany"
        
    #Feature 8
    def przelew_wych(self,kwota,typ):
        if kwota>0.0 and kwota-self.balance<=0.0:
            if typ=="n":
                self.balance=self.balance-kwota
                self.historia.append(-kwota)
            elif typ=="e":
                oplata=1
                if self.balance >= kwota + oplata:
                    self.balance=self.balance-kwota-oplata
                    self.historia.append(-kwota)
                    self.historia.append(-oplata)
                else:
                    raise ValueError("Brak wystarczających środków")
            else:
                raise ValueError("Nieznany typ przelewu")
        else:
            raise ValueError("Brak wystarczających środków")
        
    def send_history_via_email(self, email_address):
        today = date.today().isoformat()
        subject = f"Account Transfer History {today}"
        text = f"Company account history: {self.historia}"
        return SMTPClient.send(subject, text, email_address)