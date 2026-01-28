from src.account import Account
from src.smtp.smtp import SMTPClient
import os
import requests
from datetime import date

#Feature 7
class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        if nip is not None and len(nip) == 10 and nip.isdigit():
            if self.validate_nip(nip):
                self.nip = nip
            else:
                raise ValueError("Company not registered!!")
        else:
            self.nip = "Invalid"
        self.company_name = company_name
        super().__init__()
        
    def to_dict(self):
        return {
            "name": self.company_name,
            "nip": self.nip,
            "balance": self.balance,
            "historia": self.historia
        }

    def is_NIP_valid(self,NIP):
        if NIP and len(NIP)==10 and NIP.isdigit(): 
            return True 
        else: 
            return False
    
    #Feature 13
    def take_loan(self,kwota):
        if self.balance > 2*kwota:
            if -1775 not in self.historia:
                return False
            else:
                self.balance=self.balance+kwota
                self.historia.append(kwota)
                return True
        else:
            return False
        
    def send_history_via_email(self, email_address) -> bool:
        today = date.today().isoformat()
        subject =f"Account Transfer History {today}"
        text = f"Company account history: {self.historia}"
        return SMTPClient.send(subject, text, email_address)
    
    #Feature 18
    @staticmethod
    def validate_nip(nip) -> bool:
        url = os.getenv(
            "BANK_APP_MF_URL",
            "https://wl-test.mf.gov.pl"
        )
        today = date.today().isoformat()
        full_url = f"{url}/api/search/nip/{nip}?date={today}"
        response = requests.get(full_url)
        print("MF API Response for",{nip},{response.text})
        if response.status_code != 200:
                return False
        data = response.json()
        subject = data.get("result", {}).get("subject")
        if not subject:
            return False
        return subject.get("statusVat") == "Czynny"