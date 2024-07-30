from pydantic import BaseModel, EmailStr, validator, constr
from datetime import datetime, date



# Define Pydantic model for Passenger
class PassengerBase(BaseModel):
    name: constr(min_length=1, max_length=50)
    last_name: constr(min_length=1, max_length=50)
    email: EmailStr
    phone_number: constr(min_length=10, max_length=10)
    
    @validator('phone_number')
    def validate_phone_number(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must only contain digits')
        return v

class PassengerCreate(PassengerBase):
    pass

class PassengerUpdate(PassengerBase):
    pass

class PassengerResponse(PassengerBase):
    id: int
    
    class Config:
        from_attributes = True

