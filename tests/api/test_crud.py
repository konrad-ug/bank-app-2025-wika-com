import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

def create_account(pesel="12345678901"):
    payload = {
        "name": "Test",
        "surname": "User",
        "pesel": pesel,
    }
    return requests.post(f"{BASE_URL}/api/accounts", json=payload)

def test_get_existing_account():
    pesel = "12345678910"
    create_account(pesel)
    response = requests.get(f"{BASE_URL}/api/accounts/{pesel}")
    assert response.status_code == 200
    data = response.json()
    assert data["pesel"] == pesel
    assert data["name"] == "Test"
    assert data["surname"] == "User"
    assert data["balance"] == 0

def test_get_account_not_found():
    response = requests.get(f"{BASE_URL}/api/accounts/00000000000")
    assert response.status_code == 404

def test_update_account():
    pesel = "12345678911"
    create_account(pesel)
    update_payload = {
        "name": "Updated",
        "surname": "UserUpdated"
    }
    response = requests.put(f"{BASE_URL}/api/accounts/{pesel}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated"
    assert data["surname"] == "UserUpdated"

def test_delete_account():
    pesel = "12345678911"
    create_account(pesel)
    response = requests.delete(f"{BASE_URL}/api/accounts/{pesel}")
    assert response.status_code == 204
    check = requests.get(f"{BASE_URL}/api/accounts/{pesel}")
    assert check.status_code == 404

def test_przelew_przych_ok():
    pesel = "111"
    create_account(pesel)

    r = requests.post(
        f"{BASE_URL}/accounts/{pesel}/transfer",
        json={"amount": 500, "type": "incoming"}
    )
    assert r.status_code == 200
    assert r.json()["message"] == "Zlecenie przyjęto"

def test_nieistniejace_konto_transfer():
    r = requests.post(
        f"{BASE_URL}/accounts/999/transfer",
        json={"amount": 100, "type": "incoming"}
    )
    assert r.status_code == 404

def test_nieznany_typ_przelewu():
    pesel = "222"
    create_account(pesel)

    r = requests.post(
        f"{BASE_URL}/accounts/{pesel}/transfer",
        json={"amount": 100, "type": "magic"}
    )
    assert r.status_code == 400

def test_brak_srodkow():
    pesel = "333"
    create_account(pesel)

    r = requests.post(
        f"{BASE_URL}/accounts/{pesel}/transfer",
        json={"amount": 200, "type": "outgoing"}
    )
    assert r.status_code == 422

def test_wych_ok():
    pesel = "444"
    create_account(pesel)

    requests.post(
        f"{BASE_URL}/accounts/{pesel}/transfer",
        json={"amount": 300, "type": "incoming"}
    )
    r = requests.post(
        f"{BASE_URL}/accounts/{pesel}/transfer",
        json={"amount": 200, "type": "outgoing"}
    )
    assert r.status_code == 200