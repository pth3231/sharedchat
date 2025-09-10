from pydantic import BaseModel
from bcrypt import hashpw, gensalt

class Result(BaseModel):
    status: bool
    error: str | None = None    

def verify_user(username: str, password: str) -> Result:
    return Result(status = True)

def create_user(username: str, password: str) -> Result:
    password_as_bytes = password.encode('utf-8')
    salt = gensalt()
    hashed_password = hashpw(password_as_bytes, salt)
    
    return Result(status=True)