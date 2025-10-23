from src.account import CompanyAccount

class TestPrzelew:
    def przelew_przy(self):
        account = CompanyAccount("John", "Doe","12345678910")
        account.przelew_przych(120)
        assert account.przelew_przych(200) == 320
    def przelew_wy(self):
        account = CompanyAccount("John", "Doe","12345678910")
        assert account.przelew_wych(200) == 120