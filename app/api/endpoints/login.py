from fastapi import APIRouter, Request, HTTPException
from app.api.schemas.schemas_login import UsuarioLogin
from app.services.jwt_manager import create_token, verify_token
from fastapi.security import HTTPBearer

Login_router = APIRouter()

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = verify_token(auth.credentials)
        if data["email"]  != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Invalid authentication")
            



@Login_router.post("/login", tags=["login"])
def login(usuario: UsuarioLogin):
    if usuario.email == "admin@gmail.com" and usuario.password == "admin":
        token: str = create_token(usuario.dict())
    return {"token": token}
        