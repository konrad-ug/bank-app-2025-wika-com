from flask import Flask, request, jsonify
from src.accountsRegistry import AccountRegistry
from src.PersonalAccount import PersonalAccount
app = Flask(__name__)
registry = AccountRegistry()

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    account = PersonalAccount(data["name"], data["surname"], data["pesel"])
    registry.add_account(account)
    return jsonify({"message": "Account created"}), 201

@app.route("/api/accounts", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.get_all_accounts()
    accounts_data = [{"name": acc.first_name, "surname": acc.last_name, "pesel":acc.pesel, "balance": acc.balance} for acc in accounts]
    return jsonify(accounts_data), 200

@app.route("/api/accounts/count", methods=['GET'])
def get_account_count():
    print("Get account count request received")
    count = len(registry.get_all_accounts())
    return jsonify({"count": count}), 200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    for account in registry:
        if account.pesel == pesel:
            return jsonify({"name": "imie"}), 200
    return 404
    
@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    data = request.get_json()
    for account in registry:
        if account.pesel == pesel:
            account.first_name = data["first_name"]
            account.last_name = data["last_name"]
            return jsonify({"message": "Account updated"}), 200
    return 404

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    for account in registry:
        if account.pesel == pesel:
            registry.remove(account)
            return jsonify({"message": "Account deleted"}), 200
    return 404