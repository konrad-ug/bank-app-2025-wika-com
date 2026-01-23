from flask import Flask, request, jsonify
from src.PersonalAccount import PersonalAccount
from src.accountsRegistry import AccountRegistry
from src.account import Account

app = Flask(__name__)
registry = AccountRegistry()

@app.post("/api/accounts/<pesel>/transfer")
def transfer(pesel):
    data = request.get_json()

    amount = data.get("amount")
    transfer_type = data.get("type")

    account = registry.find_by_pesel(pesel)
    if not account:
        return jsonify({"detail": "Konto nie znalezione"}), 404
    if transfer_type not in ["incoming", "outgoing", "express"]:
        return jsonify({"detail": "Nieznany typ przelewu"}), 400
    try:
        if transfer_type == "incoming":
            account.przelew_przych(amount)
        elif transfer_type == "outgoing":
            account.przelew_wych(amount,"n")
        elif transfer_type == "express":
            account.przelew_wych(amount,"e")
        return jsonify({"message": "Zlecenie przyjęto do realizacji"}), 200
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
    accounts_data = [{"first_name": acc.first_name, "last_name": acc.last_name, "pesel":acc.pesel, "balance": acc.balance} for acc in accounts]
    return jsonify(accounts_data), 200

@app.route("/api/accounts/count", methods=['GET'])
def get_account_count():
    count = len(registry.get_all_accounts())
    return jsonify({"count": count}), 200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    account = registry.find_by_pesel(pesel)
    if account:
        return jsonify({
            "first_name": account.first_name, 
            "last_name": account.last_name, 
            "pesel": account.pesel, 
            "balance": account.balance}), 200
    return 404
    
@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    data = request.get_json()
    account = registry.find_by_pesel(pesel)

    if account:
        account.first_name = data["first_name"]
        account.last_name = data["last_name"]
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
        return 404
    
