import pytest
from src.accountsRegistry import AccountsRegistry, PersonalAccount

def test_add_account_success():
    reg = AccountsRegistry()
    acc = PersonalAccount("Jan", "123")
    reg.add_account(acc)

    assert reg.count_accounts() == 1
    assert reg.find_by_pesel("123") is not None


def test_add_account_duplicate_pesel():
    reg = AccountsRegistry()
    reg.add_account(PersonalAccount("Jan", "123"))

    with pytest.raises(ValueError):
        reg.add_account(PersonalAccount("Anna", "123"))
