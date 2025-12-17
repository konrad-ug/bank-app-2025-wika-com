from src.PersonalAccount import PersonalAccount
from src.accountsRegistry import AccountRegistry

def test_add_account_with_duplicate_pesel():
    registry = AccountRegistry()
    account1 = PersonalAccount("Jan", "Kowalski", "1234567890")
    registry.add_account(account1)

    account2 = PersonalAccount("Anna", "Nowak", "1234567890")
    existing = registry.get_account_by_pesel(account2.pesel)
    assert existing is not None
    assert existing.first_name == "Jan"
