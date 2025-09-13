from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

from src.routes import token
from src.controllers.token import verify_token

app = FastAPI()

app.include_router(token.router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
def root():
    return {"message": "Hello, this is auth service!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/need-auth")
def something_need_auth(payload: Annotated[dict, Depends(verify_token)]):
    return {"info": payload}