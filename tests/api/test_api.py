from app.api import app

client = app.test_client()

def test_create_account_ok():
    response = client.post("/api/accounts", json={
        "name": "Jan",
        "surname": "Kowalski",
        "pesel": "999"
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "Konto stworzone"

def test_create_account_duplicate():
    client.post("/api/accounts", json={
        "name": "Jan",
        "surname": "Kowalski",
        "pesel": "555"
    })
    response = client.post("/api/accounts", json={
        "name": "Anna",
        "surname": "Nowak",
        "pesel": "555"
    })
    assert response.status_code == 500
    assert response.json()["message"] == "Już istnieje konto o podanym PESELu"
