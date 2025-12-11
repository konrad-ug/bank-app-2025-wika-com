from src.PersonalAccount import PersonalAccount

class AccountRegistry:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: PersonalAccount):
        if self.find_by_pesel(account.pesel) is not None:
            raise ValueError("Już istnieje konto z takim peselem")
        self.accounts.append(account)

    def find_by_pesel(self, pesel):
        for account in self.accounts:
            if account.pesel == pesel:
                return account
        return None

    def get_all_accounts(self):
        return self.accounts

    def count_accounts(self):
        return len(self.accounts)