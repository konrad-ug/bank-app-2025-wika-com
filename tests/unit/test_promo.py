import pytest
from src.PersonalAccount import PersonalAccount

@pytest.mark.parametrize("pesel, promo_code, additional_balance", [
    ("80010112345", "PROM_XYZ", 50),
    ("50010112345", "PROM_XYZ", 0),
    ("80010112345", "RABAT_10", 0),
    ("80010112345", None, 0), 
])
def test_promo_code_logic(pesel, promo_code, additional_balance):
    account = PersonalAccount("Jan", "Kowalski", pesel, promo_code)
    assert account.balance == additional_balance