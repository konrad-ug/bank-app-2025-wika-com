from src.company_account import CompanyAccount

class TestPrzelew:
    def test_przelew_przy(self):
        account = CompanyAccount("Netflix","1234567891")
        account.przelew_przych(120)
        assert account.balance == 120.0
        account.przelew_przych(200)
        assert account.balance == 320.0
    def test_przelew_wy(self):
        account = CompanyAccount("Netflix","1234567891")
        account.przelew_przych(320)
        account.przelew_wych(200,"n")
        assert account.balance ==120.0
    def test_przelew_wy_ekpres(self):
        account = CompanyAccount("Netflix","1234567891")
        account.przelew_przych(320)
        account.przelew_wych(200,"e")
        assert account.balance ==115.0