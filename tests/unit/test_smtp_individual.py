import pytest
from unittest.mock import patch
from src.PersonalAccount import PersonalAccount
from datetime import date

class TestPersonalEmailHistory:
    def test_send_history_success_personal(self):
        acc = PersonalAccount("Jan", "Kowalski", "80010112345")
        acc.historia = [100, -1, 500]
        today = date.today().isoformat()
        email = "test@mail.com"
        with patch("src.smtp.smtp.SMTPClient.send") as mock_send:
            mock_send.return_value = True
            result = acc.send_history_via_email(email)
            assert result is True
            mock_send.assert_called_once_with(
                f"Account Transfer History {today}",
                f"Personal account history: [100, -1, 500]",
                email
            )

    def test_send_history_failure_personal(self):
        acc = PersonalAccount("Jan", "Kowalski", "80010112345")
        with patch("src.smtp.smtp.SMTPClient.send") as mock_send:
            mock_send.return_value = False
            result = acc.send_history_via_email("test@mail.com")
            assert result is False