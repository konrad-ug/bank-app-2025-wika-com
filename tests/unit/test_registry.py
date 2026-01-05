from src.PersonalAccount import PersonalAccount
from src.accountsRegistry import AccountRegistry

def test_add_account_success():
    registry = AccountRegistry()
    acc = PersonalAccount("Jan", "Kowalski", "12345678901")
    registry.add_account(acc)

    assert registry.count_accounts() == 1
    assert registry.find_by_pesel("12345678901") is not None

def test_add_account_duplicate_pesel():
    registry = AccountRegistry()
    account1 = PersonalAccount("Jan", "Kowalski", "12345678902")
    registry.add_account(account1)

    account2 = PersonalAccount("Anna", "Nowak", "12345678902")
    existing = registry.get_account_by_pesel(account2.pesel)
    assert existing is not None
    assert existing.first_name == "Jan"
