from pydantic import BaseModel, conint, constr, EmailStr


class UserBase(BaseModel):
    
    email: EmailStr
    password: constr(min_length=4, max_length=30)
    
class UserCreate(UserBase):
    name : constr(min_length=3, max_length=50)

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True