# tests/api/test_create_account.py
import json
from app.api import app

def test_create_account():
    client = app.test_client()

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

    data = response.get_json()

    assert data["name"] == "james"
    assert data["surname"] == "hetfield"
    assert data["pesel"] == "89092909825"
    assert data["balance"] == 0
