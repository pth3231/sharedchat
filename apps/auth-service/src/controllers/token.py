import os
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from typing import Annotated
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        secret_key = os.getenv("SECRET_KEY")
        if secret_key is None:
            raise Exception("SECRET_KEY not set in environment variables")
        decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
        
        print("Decoded token:", decoded) 
        return decoded
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server configuration error",
        )

def create_token(payload: dict, expires_in: timedelta = timedelta(minutes=30)):
    try:
        secret_key = os.getenv("SECRET_KEY")
        expiration = datetime.now(timezone.utc) + expires_in
        payload.update({"exp": expiration})
        
        encoded = jwt.encode(payload, secret_key, algorithm="HS256")
        print("Encoded token:", encoded) 
        return encoded
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server configuration error",
        )