from src.company_account import CompanyAccount
import pytest

@pytest.fixture
def mock_mf_active(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": {"subject": {"statusVat": "Czynny"}}}
    mock_response.text = '{"statusVat": "Czynny"}'
    return mocker.patch(
        "src.company_account.requests.get",
        return_value=mock_response
    )

class TestAccount:
    def test_is_nip_valid_true(self, mock_mf_active):
        acc = CompanyAccount("Netflix", "1234567891")
        wynik = acc.is_NIP_valid("8461627563")
        
        assert wynik is True
    def test_account_creation(self, mock_mf_active):
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
    
    def test_is_nip_valid_false(self):
        with pytest.raises(ValueError, match="Company not registered!!"):
            CompanyAccount("Firma", "1234567890")

    def test_is_nip_valid_direct_false(self, mock_mf_active):
        acc = CompanyAccount("Netflix", "1234567891")
        assert acc.is_NIP_valid("123") is False

    def test_company_account_invalid_nip(self, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": {
                "subject": {
                    "statusVat": "Zwolniony"
                }
            }
        }
        mock_response.text = "Zwolniony"
        mocker.patch(
            "src.company_account.requests.get",
            return_value=mock_response
        )
        with pytest.raises(ValueError, match="Company not registered!!"):
            CompanyAccount("Firma", "8461627563")
    
    def test_validate_nip_api_problems(self, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": {}}
        mocker.patch("requests.get", return_value=mock_response)
        from src.company_account import CompanyAccount
        assert CompanyAccount.validate_nip("1234567890") is False
        mock_404 = mocker.Mock(status_code=404)
        mocker.patch("src.company_account.requests.get", return_value=mock_404)
        assert CompanyAccount.validate_nip("1234567890") is False

    def test_company_to_dict(self, mock_mf_active):
        acc = CompanyAccount("Netflix", "1234567891")
        data = acc.to_dict()
        assert data["name"] == "Netflix"
        assert data["nip"] == "1234567891"
        assert "balance" in data
        assert "historia" in data
    
    def test_smtp_send_fails_by_default(self):
        from src.smtp.smtp import SMTPClient
        assert SMTPClient.send("test", "test", "test@pl") is False