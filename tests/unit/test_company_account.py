from src.company_account import CompanyAccount
import pytest

@pytest.fixture
def mock_mf_active(mocker):
    mock_response = {"result": {"subject": {"statusVat": "Czynny"}}}
    return mocker.patch(
        "src.company_account.requests.get",
        return_value=mocker.Mock(json=lambda: mock_response)
    )

class TestAccount:
    def test_account_creation(self, mock_mf_active):
        account = CompanyAccount("Netflix","1234567891")
        assert account.company_name == "Netflix"
        assert account.nip =="1234567891"

    def test_nip_too_short(self):
        # account = CompanyAccount("Netflix","1234567")
        # assert account.nip =="Invalid"
        with pytest.raises(ValueError, match="Niepoprawny format NIP!"):
            CompanyAccount("Netflix", "1234567")

    def test_nip_too_long(self):
        # account = CompanyAccount("Netflix","1234567891012")
        # assert account.nip =="Invalid"
        with pytest.raises(ValueError, match="Niepoprawny format NIP!"):
            CompanyAccount("Netflix", "1234567891012")
        
    def test_nip_non_digit(self):
        # account =CompanyAccount("Netflix",None)
        # assert account.nip =="Invalid"
        with pytest.raises(ValueError, match="Niepoprawny format NIP!"):
            CompanyAccount("Netflix", "ABC4567890")

    def test_company_account_valid_nip(self,mocker):
        mock_response = {
            "result": {
                "subject": {
                    "statusVat": "Czynny"
                }
            }
        }
        mocker.patch(
            "src.company_account.requests.get",
            return_value=mocker.Mock(json=lambda: mock_response)
        )
        acc = CompanyAccount("Firma", "8461627563")
        assert acc.nip == "8461627563"

def test_company_account_invalid_nip(mocker):
    mock_response = {
        "result": {
            "subject": {
                "statusVat": "Zwolniony"
            }
        }
    }

    mocker.patch(
        "src.company_account.requests.get",
        return_value=mocker.Mock(json=lambda: mock_response)
    )

    with pytest.raises(ValueError, match="Company not registered!!"):
        CompanyAccount("Firma", "8461627563")

def test_company_account_wrong_nip_length(mocker):
    spy = mocker.patch("src.company_account.requests.get")
    with pytest.raises(ValueError, match="Niepoprawny format NIP!"):
        CompanyAccount("Firma", "123")
    # acc = CompanyAccount("Firma", "123")
    # spy.assert_not_called()
    # assert acc.nip == "Invalid"

def test_company_to_dict(mock_mf_active):
    acc = CompanyAccount("Netflix", "1234567891")
    data = acc.to_dict()
    assert data["name"] == "Netflix"
    assert data["nip"] == "1234567891"
    assert "balance" in data
    assert "historia" in data
