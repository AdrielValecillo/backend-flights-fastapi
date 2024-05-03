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

