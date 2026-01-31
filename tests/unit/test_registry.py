from src.PersonalAccount import PersonalAccount
from src.accountsRegistry import AccountRegistry
import pytest

def test_add_account_success():
    registry = AccountRegistry()
    acc = PersonalAccount("Jan", "Kowalski", "12345678901")
    registry.add_account(acc)
    found = registry.find_by_pesel("12345678901")

    assert registry.count_accounts() == 1
    assert registry.find_by_pesel("12345678901") is not None
    assert found == acc
    assert found.first_name == "Jan"

def test_add_account_duplicate_pesel():
    registry = AccountRegistry()
    account1 = PersonalAccount("Jan", "Kowalski", "12345678902")
    registry.add_account(account1)

    account2 = PersonalAccount("Anna", "Nowak", "12345678902")
    existing = registry.find_by_pesel(account2.pesel)
    assert existing is not None
    assert existing.first_name == "Jan"

def test_add_duplicate_pesel_raises_error():
    registry = AccountRegistry()
    acc = PersonalAccount("Jan", "Kowalski", "80010112345")
    registry.add_account(acc)
    
    with pytest.raises(ValueError, match="Już istnieje konto z takim peselem"):
        registry.add_account(acc)

def test_find_by_pesel_not_found():
    registry = AccountRegistry()
    assert registry.find_by_pesel("00000000000") is None

def test_remove_account():
    registry = AccountRegistry()
    acc = PersonalAccount("Jan", "Kowalski", "12345678901")
    registry.add_account(acc)
    registry.remove(acc)
    assert registry.count_accounts() == 0