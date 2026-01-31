from src.company_account import CompanyAccount
import pytest

class TestPrzelew:
    # @pytest.fixture
    # def accountt(self):
    #     accountt = CompanyAccount("Netflix","1234567891")
    #     return accountt
    def accountt(self, mocker):
        mock_data = {
            "result": {
                "subject": {"statusVat": "Czynny"}
            }
        }
        mock_response = mocker.Mock()
        mock_response.json.return_value = mock_data
        mock_response.status_code = 200
        mock_response.text = '{"statusVat": "Czynny"}'
        mocker.patch(
            "src.company_account.requests.get",
            return_value=mock_response
        )
        return CompanyAccount("Netflix", "1234567891")
    
    def test_przelew_przy(self,accountt):
        accountt.przelew_przych(120)
        assert accountt.balance == 120.0
        accountt.przelew_przych(200)
        assert accountt.balance == 320.0

    def test_przelew_przych_nieudany(self, accountt):
        res = accountt.przelew_przych(-100)
        assert res =="Przelew nieudany"

    def test_przelew_wy(self,accountt):
        accountt.przelew_przych(320)
        accountt.przelew_wych(200,"n")
        assert accountt.balance ==120.0

    def test_przelew_wy_ekspres(self,accountt):
        accountt.przelew_przych(320)
        accountt.przelew_wych(200,"e")
        assert accountt.balance ==119.0 