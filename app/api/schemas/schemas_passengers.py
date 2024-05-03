from pydantic import BaseModel, EmailStr
from datetime import datetime, date



# Define Pydantic model for Passenger
class PassengerBase(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    phone_number: str

class PassengerCreate(PassengerBase):
    pass

class PassengerUpdate(PassengerBase):
    pass

class PassengerResponse(PassengerBase):
    id: int
    
    class Config:
        orm_mode = True

