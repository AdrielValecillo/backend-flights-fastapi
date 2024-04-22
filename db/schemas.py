from pydantic import BaseModel, EmailStr
from datetime import datetime, date

# Define Pydantic model for Flight
class FlightBase(BaseModel):
    origin: str
    destination: str
    deaperature_date: date
    capacity: int

# Pydantic model for Flight creation
class FlightCreate(FlightBase):
    pass

# Pydantic model for Flight update
class FlightUpdate(FlightBase):
    pass

# Pydantic model for Flight response
class FlightResponse(FlightBase):
    id: int
    
    class Config:
        orm_mode = True
        
        
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
        
        
        
class ReservationBase(BaseModel):
    flight_id: int
    passenger_id: int
    created_at: date
    reserved_seats: int
    status: str

class ReservationCreate(ReservationBase):
    created_at: date

class ReservationUpdate(ReservationBase):
    updated_at: date

class ReservationResponse(ReservationBase):
    id: int
    
    class Config:
        orm_mode = True