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

def test_api_save_and_load(client, mocker):
    mock_repo = mocker.patch("app.api.repo")
    client.post("/api/accounts", json={
        "first_name": "Adam",
        "last_name": "Nowak",
        "pesel": "11111111111"
    })

    save_resp = client.post("/api/accounts/save")
    assert save_resp.status_code == 200
    mock_repo.save_all.assert_called_once()
    mock_repo.load_all.return_value = []
    load_resp = client.post("/api/accounts/load")
    assert load_resp.status_code == 200