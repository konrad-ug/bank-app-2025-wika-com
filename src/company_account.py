from src.account import Account

import os
import requests
from datetime import date

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip
        self.balance = 0.0

        if len(nip) != 10:
            return
        if not self.validate_nip(nip):
            raise ValueError("Company not registered!!")
        super().__init__()

    def is_NIP_valid(self,NIP):
        if NIP and len(NIP)==10: 
            return True 
        else: 
            return False
        
    def take_loan(self,kwota):
        if self.balance > 2*kwota:
            if -1775 not in self.historia:
                return False
            else:
                self.balance=self.balance+kwota
                return True
        else:
            return False
    @staticmethod
    def validate_nip(nip: str) -> bool:
        url = os.getenv(
            "BANK_APP_MF_URL",
            "https://wl-test.mf.gov.pl"
        )

        today = date.today().isoformat()
        full_url = f"{url}/api/search/nip/{nip}?date={today}"

        response = requests.get(full_url)
        data = response.json()
        print(data)
        subject = data.get("result", {}).get("subject")
        if not subject:
            return False

        return subject.get("statusVat") == "Czynny"