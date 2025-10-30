from src.account import CompanyAccount

class TestAccount:
    def test_account_creation(self):
        account = CompanyAccount("Netflix","1234567891")
        assert account.company_name == "Netflix"
        assert account.nip =="1234567891"
    def test_nip_too_short(self):
        account = CompanyAccount("Netflix","1234567")
        assert account.nip =="Invalid"
    def test_nip_too_long(self):
        account = CompanyAccount("Netflix","1234567891012")
        assert account.nip =="Invalid"
    def test_nip_non_digit(self):
        account =CompanyAccount("Netflix",None)
        assert account.nip =="Invalid"
