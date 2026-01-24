from src.company_account import CompanyAccount
import pytest

class TestKredyt:
    @pytest.fixture
    def accountt(self):
        accountt = CompanyAccount("Netflix","1234567891")
        return accountt
    # @pytest.fixture
    # def accountt(self, mocker):
    #     mock_response = {"result": {"subject": {"statusVat": "Czynny"}}}
    #     mocker.patch(
    #         "src.company_account.requests.get",
    #         return_value=mocker.Mock(json=lambda: mock_response)
    #     )
    #     return CompanyAccount("Netflix", "1234567891")

    def test_kredyt_przyznany(self,accountt):
        accountt.przelew_przych(3750)
        accountt.przelew_wych(50,"n")
        accountt.przelew_wych(120,"n")
        accountt.przelew_przych(100)
        accountt.przelew_wych(1775,"n")
        accountt.przelew_wych(50,"n")
        assert accountt.take_loan(850) == True
        assert accountt.balance == 2705

    def test_kredyt_nieprzyznany_brak_zus(self, accountt):
        accountt.przelew_przych(5000)
        assert accountt.take_loan(1000) is False
        assert accountt.balance == 5000

    def test_kredyt_nieprzyznany_za_male_saldo(self, accountt):
        accountt.przelew_przych(2000)
        accountt.przelew_wych(1775, "n")
        assert accountt.take_loan(200) is False
        assert accountt.balance == 225

    def test_kredyt_nieprzyznany_za_male_saldo(self,accountt):
        accountt.przelew_przych(2000)
        accountt.przelew_wych(1775,"n")
        accountt.przelew_wych(200,"e")
        accountt.przelew_przych(150)
        accountt.przelew_wych(100,"n")
        assert accountt.take_loan(1000) == False
        assert accountt.balance == 74