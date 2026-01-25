import json
from app.api import app

def test_create_account():
    client = app.test_client()

    payload = {
        "first_name": "Jan",
        "last_name": "Kowalski",
        "pesel": "89092909825"
    }

    response = client.post(
        "/api/accounts",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 201
    assert response.get_json()["message"] == "Konto stworzone"

    response_get = client.get(f"/api/accounts/{payload['pesel']}")
    assert response_get.status_code == 200

    assert response.status_code == 201
    assert response.get_json()["message"] == "Konto stworzone"

    # data = response.get_json()
    # assert data["name"] == "Jan"
    # assert data["surname"] == "Kowalski"
    # assert data["pesel"] == "89092909825"
    # assert data["balance"] == 0
