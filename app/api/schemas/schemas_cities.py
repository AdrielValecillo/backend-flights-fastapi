from pydantic import BaseModel, constr


# Define Pydantic model for City
class CityBase(BaseModel):
    name: constr(min_length=1, max_length=20)
    country: constr(min_length=1, max_length=20)
    
class CityCreate(CityBase):
    pass

class CityUpdate(CityBase):
    pass

class CityResponse(CityBase):
    id: int
    
    class Config:
        from_attributes = True