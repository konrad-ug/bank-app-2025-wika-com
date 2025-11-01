from src.company_account import CompanyAccount

class TestAccount:
    def test_account_creation(self):
        account = CompanyAccount("Netflix","1234567891")
        assert account.company_name == "Netflix"
        assert account.NIP =="1234567891"
    def test_nip_too_short(self):
        account = CompanyAccount("Netflix","1234567")
        assert account.NIP =="Invalid"
    def test_nip_too_long(self):
        account = CompanyAccount("Netflix","1234567891012")
        assert account.NIP =="Invalid"
    def test_nip_non_digit(self):
        account =CompanyAccount("Netflix",None)
        assert account.NIP =="Invalid"
