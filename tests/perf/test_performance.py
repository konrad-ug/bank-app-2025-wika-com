import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/api"
max_time = 0.5

def test_performance_create_and_delete_account():
    for i in range(100):
        pesel = f"00000000{i:03d}"
        payload = {
            "first_name": "Jan",
            "last_name": "Kowalski",
            "pesel": pesel
        }
        response_create = requests.post(f"{BASE_URL}/accounts", json=payload, timeout=5)
        assert response_create.status_code == 201
        assert response_create.elapsed.total_seconds() < max_time
        response_delete = requests.delete(f"{BASE_URL}/accounts/{pesel}", timeout=5)
        assert response_delete.status_code == 200
        assert response_delete.elapsed.total_seconds() < max_time

def test_performance_multiple_transfers():
    requests.post(f"{BASE_URL}/accounts/clear")
    pesel = "11111111111"
    requests.post(f"{BASE_URL}/accounts", json={
        "first_name": "Jan", "last_name": "Kowalski", "pesel": pesel
    })
    for _ in range(100):
        payload = {"amount": 10, "type": "incoming"}
        response = requests.post(f"{BASE_URL}/accounts/{pesel}/transfer", json=payload, timeout=5)
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < max_time
    response_get = requests.get(f"{BASE_URL}/accounts/{pesel}")
    assert response_get.json()["balance"] == 1000