import os
from fastapi import status
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

HOST = "db"
USER = os.getenv("POSTGRES_USER")
PASS = os.getenv("POSTGRES_PASSWORD")


connection_string = f"postgresql+psycopg2://{USER}:{PASS}@{HOST}/auth_db"

async def verify_credentials(username: str, password: str) -> bool:
    try:
        engine = create_engine(connection_string)
        
        with engine.connect() as conn:
            query = text("SELECT user_id, username FROM credentials WHERE username = :username AND password = :password")
            params = {
                "username": username, 
                "password": password
            }
            
            result = conn.execute(query, params)
            return result.rowcount > 0
    except Exception as e:
        print(f"Error verifying credentials: {e}")
        return False