from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.accountsRegistry import AccountsRegistry, PersonalAccount

app = FastAPI()
registry = AccountsRegistry()

class AccountRequest(BaseModel):
    name: str
    pesel: str

@app.post("/accounts")
def create_account(req: AccountRequest):
    try:
        account = PersonalAccount(req.name, req.pesel)
        registry.add_account(account)
        return {"message": "Account created"}
    except ValueError:
        raise HTTPException(status_code=409, detail="PESEL already used")
