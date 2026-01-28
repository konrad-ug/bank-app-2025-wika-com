from src.company_account import CompanyAccount
from unittest.mock import patch, Mock

class TestCompanyEmailHistory:
    @patch("src.company_account.requests.get")
    def test_send_history_company(self, mock_get):
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = {
            "result": {"subject": {"statusVat": "Czynny"}}
        }
        acc = CompanyAccount("Netflix", "1234567891")
        acc.historia = [5000, -1000, 500]
        email = "biuro@netflix.com"
        with patch("src.smtp.smtp.SMTPClient.send") as mock_send:
            mock_send.return_value = True
            result = acc.send_history_via_email(email)
            assert result is True
            args, _ = mock_send.call_args
            assert "Company account history: [5000, -1000, 500]" in args[1]
            assert email == args[2]