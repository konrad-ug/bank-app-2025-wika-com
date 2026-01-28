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
        "first_name": "Jan",
        "last_name": "Kowalski",
        "pesel": "12345678901"
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "Konto stworzone"

def test_get_account_by_pesel_success(client):
    payload = {
        "first_name": "Alicja",
        "last_name": "Nowak",
        "pesel": "93210112345"
    }
    client.post("/api/accounts", json=payload)
    response = client.get("/api/accounts/93210112345")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Alicja"
    assert data["surname"] == "Nowak"
    assert data["pesel"] == "90010112345"

def test_create_account_duplicate(client):
    payload={
        "first_name": "Jan",
        "last_name": "Kowalski",
        "pesel": "12345678901"
    }
    response = client.post("/api/accounts", json=payload)
    assert response.status_code == 201
    second_response = client.post("/api/accounts", json=payload)
    assert second_response.status_code == 409
    assert second_response.get_json()["message"] == "Już istnieje konto o podanym PESELu"

def test_update_account_success(client):
    client.post("/api/accounts", json={
        "first_name": "Tom",
        "last_name": "Morawski",
        "pesel": "12345678901"
    })
    response = client.patch("/api/accounts/12345678901", json={
        "name": "Tom",
        "surname": "Morawski"
    })

    assert response.status_code == 200
    assert response.get_json()["message"] == "Konto zaktualizowane"

def test_incoming_transfer_ok(client, account):
    # account.pesel = "12345678901"
    registry.add_account(account)
    response = client.post(
        f"/api/accounts/{account.pesel}/transfer",
        json={"amount": 500, "type": "incoming"}
    )
    assert response.status_code == 200
    assert response.get_json()["message"] == "Zlecenie przyjęto"
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

def test_transfer_account_not_found(client):
    response = client.post(
        "/api/accounts/99999999999/transfer",
        json={"amount": 100, "type": "incoming"}
    )
    assert response.status_code == 404
    assert response.get_json()["detail"] == "Konto nie znalezione"

def test_express_transfer_api(client, account):
    account.balance = 100
    registry.add_account(account)
    client.post(f"/api/accounts/{account.pesel}/transfer", 
        json={"amount": 50, "type": "outgoing", "express": True})
    assert account.balance == 49

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
