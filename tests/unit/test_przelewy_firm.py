from src.account import CompanyAccount

class TestPrzelew:
    def przelew_przy(self):
        account = CompanyAccount("Netflix","1234567891")
        account.przelew_przych(120)
        assert account.przelew_przych(200) == 320
    def przelew_wy(self):
        account = CompanyAccount("Netflix","1234567891")
        assert account.przelew_wych(200) == 120