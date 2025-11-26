from src.company_account import CompanyAccount
import pytest

class TestPrzelew:
    @pytest.fixture
    def accountt(self):
        accountt = CompanyAccount("Netflix","1234567891")
        return accountt
    
    def test_hist_przych(self,accountt):
        accountt.przelew_przych(120)
        accountt.przelew_przych(200)
        assert accountt.historia == [120,200]

    def test_hist_wych(self,accountt):
        accountt.przelew_przych(200)
        accountt.przelew_przych(120)
        accountt.przelew_wych(200,"n") 
        assert accountt.historia == [200,120,-200]

    def test_hist_wych_e(self,accountt):
        accountt.przelew_przych(200)
        accountt.przelew_przych(120)
        accountt.przelew_wych(200,"e") 
        assert accountt.historia == [200,120,-200,-1]