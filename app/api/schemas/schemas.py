from pydantic import BaseModel, EmailStr
from datetime import datetime, date

# Define Pydantic model for Flight
class FlightBase(BaseModel):
    origin_id: int
    destination_id: int
    deaperature_date: date
    capacity: int

class FlightCreate(FlightBase):
    pass

class FlightUpdate(FlightBase):
    pass

class FlightResponse(FlightBase):
    id: int
    
    class Config:
        orm_mode = True


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


# Define Pydantic model for Reservation
class ReservationBase(BaseModel):
    flight_id: int
    passenger_id: int
    reserved_seats: int

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(ReservationBase):
    updated_at: date

class ReservationResponse(ReservationBase):
    id: int
    
    class Config:
        orm_mode = True


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