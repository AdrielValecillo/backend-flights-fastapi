from fastapi import APIRouter, HTTPException, Depends
import app.api.schemas.schemas_users as schemas
from app.services.users_services import UserService
from app.api.responses.responses import Responses
from app.api.endpoints.login import JWTBearer


crud= UserService()
user_router = APIRouter()
messages = Responses()


@user_router.post("/api/users" , tags=["users"])
def create_user(user: schemas.UserCreate):
    try:
        user_create = crud.create_user(user)
        return messages.response_message(user_create, "User created", 201)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)
    
@user_router.get("/api/users" , tags=["users"])
def get_users():
    try:
        users = crud.get_users()
        return messages.response_message(users, "Users retrieved", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)
    
@user_router.post("/api/users/login" , tags=["users"])
def login_user(user: schemas.UserBase):
    try:
        user_login = crud.verify_user(user.email, user.password)
        return messages.response_message(user_login, "User logged in", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)
    
@user_router.put("/api/users/admin" , tags=["users"])
def user_admin(email: str):
    try:
        user_admin = crud.user_admin(email)
        return messages.response_message(user_admin, "User admin updated", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)