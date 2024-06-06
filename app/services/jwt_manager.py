from jwt import encode, decode



def create_token(data: dict) -> str:
    token : str = encode(payload=data, key="secrete_key", algorithm='HS256')
    return token

def verify_token(token: str) -> dict:
    data: dict = decode(token, key="secrete_key", algorithms=['HS256'])
    return data
    