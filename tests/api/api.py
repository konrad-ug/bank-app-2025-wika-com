import json
from app.api import app
import pytest
from src.accountsRegistry import AccountRegistry
from src.PersonalAccount import PersonalAccount

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_create_account():
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
    data = response.get_json()["message"] == "Konto stworzone"

@pytest.fixture
def account():
    acc = PersonalAccount("Jan", "Kowalski", "123")
    acc.balance = 1000
    return acc