from pydantic import BaseModel, EmailStr
from datetime import datetime, date



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


