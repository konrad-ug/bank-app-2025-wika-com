from src.company_account import CompanyAccount
import pytest

class TestKredyt:
    @pytest.fixture
    def accountt(self):
        accountt = CompanyAccount("Netflix","1234567891")
        return accountt
    def test_kredyt_przyznany(self,accountt):
        accountt.przelew_przych(3750)
        accountt.przelew_wych(50,"n")
        accountt.przelew_wych(120,"n")
        accountt.przelew_przych(100)
        accountt.przelew_wych(1775,"n")
        accountt.przelew_wych(50,"n")
        assert accountt.take_loan(850) == True
        assert accountt.balance == 2705
    def test_kredyt_nieprzyznany(self,accountt):
        accountt.przelew_przych(200)
        accountt.przelew_wych(100,"n")
        accountt.przelew_przych(50)
        accountt.przelew_przych(50)
        accountt.przelew_przych(100)
        assert accountt.take_loan(100) == False
        assert accountt.balance == 300
    def test_kredyt_nieprzyznany2(self,accountt):
        accountt.przelew_przych(2000)
        accountt.przelew_wych(1775,"n")
        accountt.przelew_wych(200,"e")
        accountt.przelew_przych(150)
        accountt.przelew_wych(100,"n")
        assert accountt.take_loan(1000) == False
        assert accountt.balance == 74