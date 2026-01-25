from src.company_account import CompanyAccount
import pytest

class TestPrzelew:
    @pytest.fixture
    # def accountt(self):
    #     accountt = CompanyAccount("Netflix","1234567891")
    #     return accountt
    
    def accountt(self, mocker):
        mock_response = {"result": {"subject": {"statusVat": "Czynny"}}}
        mocker.patch(
            "src.company_account.requests.get",
            return_value=mocker.Mock(json=lambda: mock_response)
        )
        return CompanyAccount("Netflix", "1234567891")
    
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

    def test_company_account_send_history(self,mocker):
        mocker.patch(
            "src.company_account.requests.get",
            return_value=mocker.Mock(
                json=lambda: {
                    "result": {
                        "subject": {"statusVat": "Czynny"}
                    }
                }
            )
        )

        acc = CompanyAccount("Firma", "8461627563")
        acc.historia = [5000, -1000, 500]

        mock_send = mocker.patch(
            "src.company_account.SMTPClient.send",
            return_value=True
        )

        result = acc.send_history_via_email("firma@email.com")
        assert result is True
        args, _ = mock_send.call_args
        assert args[1] == "Company account history:[5000, -1000, 500]"
        