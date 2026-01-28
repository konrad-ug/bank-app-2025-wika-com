import pytest
import requests
from app.api import app, registry

BASE_URL = "http://localhost:5000/api"
@pytest.fixture
def client():
    app.config["TESTING"] = True
    registry.accounts = []
    with app.test_client() as client:
        yield client

def test_api_save_and_load(client):
    client.post("/api/accounts", json={
        "first_name": "Adam", "last_name": "Nowak", "pesel": "11111111111"
    })

    save_resp = client.post("/api/accounts/save")
    assert save_resp.status_code == 200
    load_resp = client.post("/api/accounts/load")
    assert load_resp.status_code == 200
    assert "Pomyślnie załadowano" in load_resp.get_json()["message"]
    get_resp = client.get("/api/accounts/11111111111")
    assert get_resp.status_code == 200
    assert get_resp.get_json()["first_name"] == "Adam"