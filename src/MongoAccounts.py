from pymongo import MongoClient
from src.PersonalAccount import PersonalAccount

class MongoAccountsRepository:
    def __init__(self):
        self._client = MongoClient("mongodb://localhost:27017/")
        self._db = self._client["bank_database"]
        self._collection = self._db["accounts"]

    def save_all(self, accounts):
        self._collection.delete_many({})
        for account in accounts:
            self._collection.update_one(
                {"pesel": account.pesel},
                {"$set": {
                    "name": account.first_name,
                    "surname": account.last_name,
                    "pesel": account.pesel,
                    "balance": account.balance,
                    "historia": account.historia
                }},
                upsert=True,
            )

    def load_all(self):
        db_accounts = list(self._collection.find({}))
        accounts_list = []
        for acc_data in db_accounts:
            acc = PersonalAccount(acc_data["name"], acc_data["surname"], acc_data["pesel"])
            acc.balance = float(acc_data["balance"])
            acc.historia = acc_data.get("historia", [])
            accounts_list.append(acc)
        return accounts_list