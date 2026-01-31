from src.PersonalAccount import PersonalAccount
import pytest

class TestKredyt:
    @pytest.fixture
    def accountt(self):
        accountt = PersonalAccount("John", "Doe","12345678910")
        return accountt
    def test_kredyt_przyznany(self,accountt):
        accountt.przelew_przych(120)
        accountt.przelew_wych(50,"n")
        accountt.przelew_przych(120)
        accountt.przelew_przych(200)
        accountt.przelew_przych(50)
        assert accountt.submit_for_loan(100) == True
        assert accountt.balance == 540
    def test_kredyt_przyznany2(self,accountt):
        accountt.przelew_przych(120)
        accountt.przelew_wych(50,"e")
        accountt.przelew_przych(120)
        accountt.przelew_wych(100,"n")
        accountt.przelew_przych(200)
        accountt.przelew_przych(50)
        assert accountt.submit_for_loan(100) == True
        assert accountt.balance == 439
    def test_kredyt_nieprzyznany(self,accountt):
        accountt.przelew_przych(200)
        accountt.przelew_wych(100,"n")
        accountt.przelew_przych(50)
        assert accountt.submit_for_loan(100) == False
        assert accountt.balance == 150
    def test_kredyt_nieprzyznany2(self,accountt):
        accountt.przelew_przych(200)
        accountt.przelew_przych(50)
        accountt.przelew_wych(200,"e")
        accountt.przelew_przych(150)
        accountt.przelew_wych(100,"n")
        assert accountt.submit_for_loan(1000) == False
        assert accountt.balance == 99
    def test_kredyt_nieprzyznany3(self,accountt):
        accountt.przelew_przych(200)
        accountt.przelew_przych(50)
        accountt.przelew_wych(200,"n")
        accountt.przelew_przych(150)
        accountt.przelew_wych(100,"n")
        assert accountt.submit_for_loan(100) == False
        assert accountt.balance == 100
    def test_historia_kredytu_za_krotka(self,accountt):
        accountt.historia = [100, 200]
        result = accountt.submit_for_loan(500)
        assert result is False