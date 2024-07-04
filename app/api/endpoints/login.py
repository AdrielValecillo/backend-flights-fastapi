from fastapi import APIRouter, Request, HTTPException
from app.api.schemas.schemas_login import UsuarioLogin
from app.services.jwt_manager import create_token, verify_token
from fastapi.security import HTTPBearer
from app.services.users_services import UserService

crud = UserService()

Login_router = APIRouter()
"""
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
            
"""


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request) 
        data = verify_token(auth.credentials)
        if not data:
            raise HTTPException(status_code=403, detail="Token inválido")
        user = crud.get_user_by_email(data['email'])
        if not user or data['email'] != user.email:
            raise HTTPException(status_code=403, detail="Credenciales no son validas")




@Login_router.post("/login", tags=["login"])
def login(usuario: UsuarioLogin):
    try:
        user = crud.verify_user(usuario.email, usuario.password)
        token = create_token({"email": user.email})
        return {"token": token}
    except HTTPException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        