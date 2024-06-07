import os
from dotenv import load_dotenv
from jwt import encode, decode
from fastapi import HTTPException

load_dotenv("./.env")

def create_token(data: dict) -> str:
    secret_key: str = os.getenv("SECRET_KEY")
    token : str = encode(payload=data, key=secret_key, algorithm='HS256')
    return token

def verify_token(token: str) -> dict:
    secret_key: str = os.getenv("SECRET_KEY")
    data: dict = decode(token, key=secret_key, algorithms=['HS256'])
    if data is None:
        raise HTTPException(status_code=403, detail="Invalid token")
    return data