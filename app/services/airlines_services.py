
import app.api.schemas.schemas_airlines as schemas
from fastapi import HTTPException
from app.db.models import Airline
from app.services.base import Base




class AirlinesServices(Base):

    def create_airline(self, airline: schemas.Airline):
        db_airline = Airline(**airline.dict())
        if db_airline.name is None:
            raise HTTPException(status_code=400, detail="Invalid airline name")
        self.db.add(db_airline)
        self.db.commit()
        self.db.refresh(db_airline)
        return db_airline
    
    def get_airlines(self):
        airlines = self.db.query(Airline).all()
        return airlines
    
    def get_logo(self, airline_id: int):
        airline = self.db.query(Airline).filter(Airline.id == airline_id).first()
        if airline is None:
            raise HTTPException(status_code=404, detail="Airline not found")
        return airline.logo_path