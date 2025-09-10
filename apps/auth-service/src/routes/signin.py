from fastapi import APIRouter, Form, status
from pydantic import BaseModel
from typing import Annotated
from ..controllers.auth import verify_user

router = APIRouter(
    prefix="/signin",
    tags=["signin"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

class SigninRequest(BaseModel):
    username: Annotated[str, Form()]
    password: Annotated[str, Form()]

@router.get("/")
def signin_greeting():
    return "This is the signin API"

@router.post("/")
def check_user(credentials: SigninRequest):
    print(f"Received credentials: {credentials}")
    
    result = verify_user(credentials.username, credentials.password)
    if not result.status:
        return {"status": "error", "message": result.error}
    return {"status": "success", "message": "User verified"}