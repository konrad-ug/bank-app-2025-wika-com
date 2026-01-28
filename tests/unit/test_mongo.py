import pytest
from src.MongoAccounts import MongoAccountsRepository
from src.PersonalAccount import PersonalAccount

def test_mongo_save_all_clears_collection(mocker):
    mock_collection = mocker.Mock()
    repo = MongoAccountsRepository()
    repo._collection = mock_collection
    
    acc = PersonalAccount("Jan", "Kowalski", "12345678901")
    repo.save_all([acc])
    mock_collection.delete_many.assert_called_once_with({})
    assert mock_collection.update_one.called

def test_mongo_load_all_returns_correct(mocker):
    mock_collection = mocker.Mock()
    mock_collection.find.return_value = [
        {
            "name": "Jan", "surname": "Kowalski", "pesel": "12345678901",
            "balance": 100, "historia": []
        }
    ]

    repo = MongoAccountsRepository()
    repo._collection = mock_collection    
    loaded_accounts = repo.load_all()
    assert len(loaded_accounts) == 1
    assert loaded_accounts[0].pesel == "12345678901"