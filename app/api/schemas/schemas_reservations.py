from pydantic import BaseModel, conint
from datetime import date



# Define Pydantic model for Reservation
class ReservationBase(BaseModel):
    flight_id: conint(ge=1)
    passenger_id: conint(ge=1)
    reserved_seats: conint(gt=0)

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(ReservationBase):
    updated_at: date

class ReservationResponse(ReservationBase):
    id: int
    
    class Config:
        from_attributes = True


