import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

def create_sample_account(pesel="12345678901"):
    payload = {
        "name": "Test",
        "surname": "User",
        "pesel": pesel,
    }
    return requests.post(f"{BASE_URL}/api/accounts", json=payload)

def test_get_existing_account():
    pesel = "12345678910"
    create_sample_account(pesel)
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
    create_sample_account(pesel)
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
    create_sample_account(pesel)
    response = requests.delete(f"{BASE_URL}/api/accounts/{pesel}")
    assert response.status_code == 204
    check = requests.get(f"{BASE_URL}/api/accounts/{pesel}")
    assert check.status_code == 404
