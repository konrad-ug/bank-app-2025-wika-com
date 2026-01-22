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
    assert response.status_code == 409
    assert response.json()["message"] == "Już istnieje konto o podanym PESELu"

def test_incoming_transfer_ok(client, account):
    from app.api import registry
    registry.add_account(account)

    response = client.post(
        "/api/accounts/123/transfer",
        json={"amount": 500, "type": "incoming"}
    )

    assert response.status_code == 200
    assert response.get_json()["message"] == "Zlecenie przyjęto do realizacji"
    assert account.balance == 1500

def test_outgoing_transfer_no_funds(client, account):
    from app.api import registry
    registry.add_account(account)

    response = client.post(
        "/api/accounts/123/transfer",
        json={"amount": 5000, "type": "outgoing"}
    )

    assert response.status_code == 422
    assert response.get_json()["detail"] == "Brak wystarczających środków"
    assert account.balance == 1000

def test_unknown_transfer_type(client, account):
    from app.api import registry
    registry.add_account(account)

    response = client.post(
        "/api/accounts/123/transfer",
        json={"amount": 100, "type": "magic"}
    )

    assert response.status_code == 400
    assert response.get_json()["detail"] == "Nieznany typ przelewu"
