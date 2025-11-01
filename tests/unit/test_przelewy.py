from src.account import Account

class TestPrzelew:
    def przelew_przy(self):
        account = Account("John", "Doe","12345678910")
        account.przelew_przych(120)
        assert account.balance == 120.0
        assert account.przelew_przych(200) 
        assert account.balance == 320.0
    def przelew_wy(self):
        account = Account("John", "Doe","12345678910")
        ccount.przelew_przych(320)
        account.przelew_wych(200) 
        assert account.balance == 120.0
    def przelew_wy_ekspres(self):
        account = Account("John", "Doe","12345678910")
        ccount.przelew_przych(320)
        account.przelew_wych(200,"e") 
        assert account.balance == 119.0