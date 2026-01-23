from app.api import app, registry
from src.PersonalAccount import PersonalAccount
import pytest

@pytest.fixture
def client():
    app.config["TESTING"] = True
    registry.accounts = []
    with app.test_client() as client:
        yield client

@pytest.fixture
def account():
    return PersonalAccount("Jan", "Kowalski", "12345678901")

def test_create_account_ok(client):
    response = client.post("/api/accounts", json={
        "name": "Jan",
        "surname": "Kowalski",
        "pesel": "12345678901"
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "Konto stworzone"

def test_create_account_duplicate(client):
    payload={
        "name": "Jan",
        "surname": "Kowalski",
        "pesel": "12345678901"
    }
    response = client.post("/api/accounts", json=payload)
    assert response.status_code == 409
    assert response.json()["message"] == "Już istnieje konto o podanym PESELu"

def test_incoming_transfer_ok(client, account):
    # account.pesel = "12345678901"
    registry.add_account(account)
    response = client.post(
        f"/api/accounts/{account.pesel}/transfer",
        json={"amount": 500, "type": "incoming"}
    )
    assert response.status_code == 200
    assert response.get_json()["message"] == "Zlecenie przyjęto do realizacji"
    assert account.balance == 500

def test_outgoing_transfer_no_funds(client, account):
    account.balance = 1000
    registry.add_account(account)
    response = client.post(
        f"/api/accounts/{account.pesel}/transfer",
        json={"amount": 5000, "type": "outgoing"}
    )
    assert response.status_code == 422
    assert response.get_json()["detail"] == "Brak wystarczających środków"
    assert account.balance == 1000

def test_unknown_transfer_type(client, account):
    registry.accounts = []
    registry.add_account(account)

    payload = {
        "amount": 100, 
        "type": "magic"
    }

    response = client.post(
        f"/api/accounts/{account.pesel}/transfer",
        json=payload
    )
    assert response.status_code == 400
    assert response.get_json()["detail"] == "Nieznany typ przelewu"
