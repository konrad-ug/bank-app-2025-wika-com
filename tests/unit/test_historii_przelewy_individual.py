from src.PersonalAccount import PersonalAccount
import pytest

class TestPrzelew:
    @pytest.fixture
    def accountt(self):
        accountt = PersonalAccount("John", "Doe","12345678910")
        return accountt
    
    def test_hist_przych(self,accountt):
        accountt.przelew_przych(120)
        accountt.przelew_przych(200)
        assert accountt.historia == [120,200]

    def test_hist_wych(self,accountt):
        accountt.przelew_przych(400)
        accountt.przelew_wych(200,"n") 
        assert accountt.historia == [400,-200]

    def test_hist_wych_e(self,accountt):
        accountt.przelew_przych(400)
        accountt.przelew_wych(200,"e") 
        assert accountt.historia == [400,-200,-1]

    def test_send_history_ok(self,mocker, accountt):
        accountt.historia = [150.0, -50.0]

        mock_send = mocker.patch(
            "src.account.SMTPClient.send",
            return_value=True
        )

        result = accountt.send_history_via_email("test@email.com")

        assert result is True
        mock_send.assert_called_once()

        args, _ = mock_send.call_args
        assert args[0].startswith("Account Transfer History")
        assert args[1] == "Personal account history:[150.0, -50.0]"
        assert args[2] == "test@email.com"
    def test_send_history_fail(self,mocker, accountt):
        mocker.patch(
            "src.account.SMTPClient.send",
            return_value=False
        )

        result = accountt.send_history_via_email("test@email.com")
        assert result is False