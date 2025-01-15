import bcrypt
from app.services.base import Base
from app.db.models import User
from fastapi import HTTPException
import app.api.schemas.schemas_users as schemas
from sqlalchemy.exc import SQLAlchemyError





class UserService(Base):
    
    def create_user(self, user: schemas.UserCreate) -> User:
        try:
            user_exist = self.get_user_by_email(user.email)
            if user_exist:
                raise HTTPException(status_code=403, detail="User already exists")
            hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user = User(name=user.name ,email=user.email, password=hashed_password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Internal server error")
    
    def get_users(self) -> list[User]:
        users = self.db.query(User).all()
        return users
    
    def verify_user(self, email: str, password: str) -> User:
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            raise HTTPException(status_code=403, detail="Invalid password")
        return user
    
    def user_admin(self, email: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if user.is_admin == True:
            user.is_admin = False
            return user
        user.is_admin = True
        return user

    def get_user_by_email(self, email: str) -> User:
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user