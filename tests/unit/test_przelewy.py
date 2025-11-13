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
        account.przelew_przych(320)
        account.przelew_wych(200,"n") 
        assert account.balance == 120.0
    def przelew_wy_ekspres(self):
        account = Account("John", "Doe","12345678910")
        account.przelew_przych(320)
        account.przelew_wych(200,"e") 
        assert account.balance == 119.0

class TestHist:
    def test_hist_przych(self):
        account=Account("John", "Doe","12345678910")
        account.przelew_przych(120)
        account.przelew_przych(200)
        assert account.historia == [120,200]
    def test_hist_wych(self):
        account=Account("John", "Doe","12345678910")
        account.przelew_przych(200)
        account.przelew_przych(120)
        account.przelew_wych(200,"n") 
        assert account.historia == [200,120,-200]
    def test_hist_wych_e(self):
        account=Account("John", "Doe","12345678910")
        account.przelew_przych(200)
        account.przelew_przych(120)
        account.przelew_wych(200,"e") 
        assert account.historia == [200,120,-200,-1]
