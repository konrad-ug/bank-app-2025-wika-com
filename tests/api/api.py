import json
from app.api import app, registry
import pytest
from src.accountsRegistry import AccountRegistry
from src.PersonalAccount import PersonalAccount

@pytest.fixture
def client():
    app.config["TESTING"] = True
    registry.accounts = []
    with app.test_client() as client:
        yield client

def test_create_account(client):
    payload = {
        "name": "james",
        "surname": "hetfield",
        "pesel": "89092909825"
    }

    response = client.post(
        "/api/accounts",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 201
    assert response.get_json()["message"] == "Konto stworzone"

def test_get_all_accounts(client):
    # Dodajemy konto bezpośrednio do rejestru, żeby sprawdzić GET
    from src.PersonalAccount import PersonalAccount
    registry.add_account(PersonalAccount("Jan", "Kowalski", "12345678901"))
    
    response = client.get("/api/accounts")
    assert response.status_code == 200
    assert len(response.get_json()) == 1
