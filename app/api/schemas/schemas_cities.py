from pydantic import BaseModel, EmailStr
from datetime import datetime, date

# Define Pydantic model for City
class CityBase(BaseModel):
    name: str
    country: str
    
class CityCreate(CityBase):
    pass

class CityUpdate(CityBase):
    pass

class CityResponse(CityBase):
    id: int
    
    class Config:
        orm_mode = True