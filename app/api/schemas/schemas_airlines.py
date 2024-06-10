from pydantic import BaseModel, constr
from typing import Optional

class AirlineBase(BaseModel):
    name: constr(min_length=1, max_length=30)
    logo_path: Optional[str] = None

class AirlineCreate(AirlineBase):
    pass

class Airline(AirlineBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True