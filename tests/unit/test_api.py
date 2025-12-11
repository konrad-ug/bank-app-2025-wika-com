from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_create_account_ok():
    response = client.post("/accounts", json={
        "name": "Jan",
        "pesel": "999"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Account created"

def test_create_account_duplicate():
    client.post("/accounts", json={
        "name": "Jan",
        "pesel": "555"
    })
    response = client.post("/accounts", json={
        "name": "Anna",
        "pesel": "555"
    })
    assert response.status_code == 409
    assert response.json()["detail"] == "PESEL already used"
