from src.company_account import CompanyAccount
import pytest

class TestPrzelew:
    @pytest.fixture
    # def accountt(self):
    #     accountt = CompanyAccount("Netflix","1234567891")
    #     return accountt
    def accountt(self, mocker):
        mock_response = {
            "result": {
                "subject": {"statusVat": "Czynny"}
            }
        }
        mocker.patch(
            "src.company_account.requests.get",
            return_value=mocker.Mock(json=lambda: mock_response)
        )
        return CompanyAccount("Netflix", "1234567891")
    
    def test_przelew_przy(self,accountt):
        accountt.przelew_przych(120)
        assert accountt.balance == 120.0
        accountt.przelew_przych(200)
        assert accountt.balance == 320.0

    def test_przelew_wy(self,accountt):
        accountt.przelew_przych(320)
        accountt.przelew_wych(200,"n")
        assert accountt.balance ==120.0

    def test_przelew_wy_ekspres(self,accountt):
        accountt.przelew_przych(320)
        accountt.przelew_wych(200,"e")
        assert accountt.balance ==119.0 