from src.PersonalAccount import PersonalAccount

class TestAccount:
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe","12345678910")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.pesel =="12345678910"
        assert account.balance == 0

    def test_pesel_too_short(self):
        account = PersonalAccount("John", "Doe","1234567")
        assert account.pesel =="Invalid"

    def test_pesel_too_long(self):
        account = PersonalAccount("John", "Doe","1234567891012")
        assert account.pesel =="Invalid"
        
    def test_pesel_non_digit(self):
        account = PersonalAccount("John", "Doe", "")
        assert account.pesel =="Invalid"
    
    def test_to_dict_conversion(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        data = account.to_dict()
        assert data["name"] == "John"
        assert data["surname"] == "Doe"
        assert data["pesel"] == "12345678910"
        assert "balance" in data
        assert "historia" in data
