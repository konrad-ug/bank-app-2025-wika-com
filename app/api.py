from flask import Flask, request, jsonify
from src.PersonalAccount import PersonalAccount
from src.accountsRegistry import AccountRegistry
from src.account import Account
from src.MongoAccounts import MongoAccountsRepository
from src.accountsRegistry import AccountRegistry

app = Flask(__name__)
registry = AccountRegistry()

@app.post("/api/accounts/<pesel>/transfer")
def transfer(pesel):
    data = request.get_json()
    amount = data.get("amount")
    transfer_type = data.get("type")
    is_express = data.get("express", False)
    account = registry.find_by_pesel(pesel)
    if not account:
        return jsonify({"detail": "Konto nie znalezione"}), 404
    if transfer_type not in ["incoming", "outgoing"]:
        return jsonify({"detail": "Nieznany typ przelewu"}), 400
    try:
        if transfer_type == "incoming":
            account.przelew_przych(amount)
        elif transfer_type == "outgoing":
            if is_express:
                mode="e"
            else:
                mode="n"
            account.przelew_wych(amount,mode)
        elif transfer_type == "express":
            account.przelew_wych(amount,"e")
        return jsonify({"message": "Zlecenie przyjęto"}), 200
    except ValueError:
        return jsonify({"detail": "Brak wystarczających środków"}), 422
    
@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    if registry.find_by_pesel(data["pesel"]):
        return jsonify({"message": "Już istnieje konto o podanym PESELu"}), 409
    account = PersonalAccount(data["first_name"], data["last_name"], data["pesel"])
    registry.add_account(account)
    return jsonify({"message": "Konto stworzone"}), 201

@app.route("/api/accounts", methods=['GET'])
def get_all_accounts():
    accounts = registry.get_all_accounts()
    # accounts_data = [{"name": acc.first_name, "surname": acc.last_name, "pesel":acc.pesel, "balance": acc.balance} for acc in accounts]
    return jsonify([acc.to_dict() for acc in accounts]), 200

@app.route("/api/accounts/count", methods=['GET'])
def get_account_count():
    count = len(registry.get_all_accounts())
    return jsonify({"count": count}), 200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    account = registry.find_by_pesel(pesel)
    if account:
        return jsonify({
            "name": account.first_name, 
            "surname": account.last_name, 
            "pesel": account.pesel, 
            "balance": account.balance}), 200
    return jsonify({"message": "Konto nie znalezione"}),404
    
@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    data = request.get_json()
    account = registry.find_by_pesel(pesel)
    if account:
        if "name" in data:
            account.first_name = data["name"]
        if "surname" in data:
            account.last_name = data["surname"]
        return jsonify({"message": "Konto zaktualizowane"}), 200
    else:
        return jsonify({"message": "Konto nie znalezione"}), 404

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    account = registry.find_by_pesel(pesel)
    if account:
        registry.remove(account)
        return jsonify({"message": "Konto usunięte"}), 200
    else:
        return ({"message": "Nie znaleziono konta do usunięcia"}),404
    
repo = MongoAccountsRepository()

@app.route("/api/accounts/save", methods=['POST'])
def save_accounts():
    accounts = registry.get_all_accounts()
    repo.save_all(accounts)
    return jsonify({"message": "Pomyślnie zapisano konta do bazy"}), 200

@app.route("/api/accounts/load", methods=['POST'])
def load_accounts():
    accounts_from_db = repo.load_all()
    registry.accounts = [] 
    for acc in accounts_from_db:
        registry.add_account(acc)
    return jsonify({"message": f"Pomyślnie załadowano {len(accounts_from_db)}kont"}), 200

@app.route("/api/accounts/clear", methods=['POST'])
def clear_accounts():
    registry.accounts=[]
    return jsonify({"message": "Rejestr wyczyszczony"}), 200