from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from src.controllers.db import verify_credentials
from src.controllers.token import create_token

router = APIRouter(
    prefix="/token",
    tags=["token"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)

@router.post("/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    validity: bool = await verify_credentials(form_data.username, form_data.password)
    if validity:
        return {
            "access_token": create_token({
                "username": form_data.username
            }), 
            "token_type": "bearer"
        }
    
    return {"error": "Invalid credentials"}