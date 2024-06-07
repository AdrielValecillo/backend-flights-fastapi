from fastapi import APIRouter, Request, HTTPException
from app.api.schemas.schemas_login import UsuarioLogin
from app.services.jwt_manager import create_token, verify_token
from fastapi.security import HTTPBearer

Login_router = APIRouter()

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        try:
            data = verify_token(auth.credentials)
            email = data.get("email")
            if email is None:
                raise HTTPException(status_code=403, detail="Invalid token")
            # En una aplicación real, reemplazarías esto con la lógica para verificar el correo electrónico contra tu base de datos de usuarios
            if email != "admin@gmail.com":
                raise HTTPException(status_code=403, detail="Invalid authentication")
        except Exception as e:
            raise HTTPException(status_code=403, detail=str(e))
            





@Login_router.post("/login", tags=["login"])
def login(usuario: UsuarioLogin):
    try:
        if usuario.email != "admin@gmail.com" or usuario.password != "admin":
            raise HTTPException(status_code=401, detail="Invalid email or password")
        token: str = create_token(usuario.dict())
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        