from src.account_individual import IndividualAccount
import pytest

class TestPrzelew:
    @pytest.fixture
    def accountt(self):
        accountt = IndividualAccount("John", "Doe","12345678910")
        return accountt
    
    def test_przelew_przy(self,accountt):
        accountt.przelew_przych(120)
        assert accountt.balance == 120.0
        accountt.przelew_przych(200) 
        assert accountt.balance == 320.0

    def test_przelew_wy(self,accountt):
        accountt.przelew_przych(320)
        accountt.przelew_wych(200,"n") 
        assert accountt.balance == 120.0

    def test_przelew_wy_ekspres(self,accountt):
        accountt.przelew_przych(320)
        accountt.przelew_wych(200,"e") 
        assert accountt.balance == 119.0
