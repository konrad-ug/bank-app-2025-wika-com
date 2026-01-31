from src.PersonalAccount import PersonalAccount
import pytest

class TestPrzelew:
    @pytest.fixture
    def accountt(self):
        accountt = PersonalAccount("John", "Doe","12345678910")
        return accountt
    
    def test_przelew_przy(self,accountt):
        accountt.przelew_przych(120)
        assert accountt.balance == 120.0
        accountt.przelew_przych(200) 
        assert accountt.balance == 320.0

    def test_przelew_wy(self,accountt):
        accountt.przelew_przych(320)
        accountt.przelew_wych(200,"n") 
        assert accountt.balance == 120.0

    def test_przelew_wy_ekspres(self,accountt):
        accountt.przelew_przych(320)
        accountt.przelew_wych(200,"e") 
        assert accountt.balance == 119.0
        assert accountt.historia == [320, -200, -1]
    
    def test_przelew_ekspresowy_osobisty(self,accountt):
        accountt.przelew_przych(100)
        accountt.przelew_wych(50, "e")
        assert accountt.balance == 49
        assert -1 in accountt.historia
    
    def test_przelew_wych_brak_srodkow(self, accountt):
        accountt.przelew_przych(100)
        with pytest.raises(ValueError, match="Brak wystarczających środków"):
            accountt.przelew_wych(200, "n")

    def test_przelew_wych_nieznany_typ(self, accountt):
        accountt.przelew_przych(100)
        with pytest.raises(ValueError, match="Nieznany typ przelewu"):
            accountt.przelew_wych(50, "x")
    
    def test_przelew_wych_ujemna_kwota(self, accountt):
        with pytest.raises(ValueError, match="Brak wystarczających środków"):
            accountt.przelew_wych(-50, "n")