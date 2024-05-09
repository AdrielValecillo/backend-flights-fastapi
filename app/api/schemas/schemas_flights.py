from pydantic import BaseModel, conint, validator
from datetime import datetime, date

# Define Pydantic model for Flight
class FlightBase(BaseModel):
    origin_id: conint(gt=0)
    destination_id: conint(gt=0)
    departure_date: date
    capacity: conint(gt=0)


class FlightCreate(FlightBase):
    pass

class FlightUpdate(FlightBase):
    pass

class FlightResponse(FlightBase):
    id: int
    
    class Config:
        orm_mode = True