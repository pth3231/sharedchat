from pydantic import BaseModel

class CrendentialModel(BaseModel):
    user_id: int
    username: str
    password: str