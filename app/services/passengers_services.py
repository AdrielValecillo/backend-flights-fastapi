from app.services.base import Base
from app.db.models import Passenger
import app.api.schemas.schemas_passengers as schemas
from fastapi import HTTPException


class PassengersService(Base):

    def create_passenger(self, passenger: schemas.PassengerCreate):
        
        db_passenger = self.db.query(Passenger).filter(Passenger.email == passenger.email).first()
        if db_passenger:
            raise HTTPException(status_code=400, detail="Email already exists")
        
        db_passenger = Passenger(**passenger.dict())
        
        self.db.add(db_passenger)
        self.db.commit()
        self.db.refresh(db_passenger)
        return db_passenger

    def get_passenger(self, passenger_id: int):
        db_passenger = self.db.query(Passenger).filter(Passenger.id == passenger_id).first()
        if db_passenger is None:
            raise HTTPException(status_code=404, detail="Passenger not found")
        return db_passenger

    def get_passengers(self, skip: int = 0, limit: int = 100):
        passengers = self.db.query(Passenger).all()
        if passengers is None:
            raise HTTPException(status_code=404, detail="No passengers found")
        return passengers

    def update_passenger(self, passenger_id: int, passenger: schemas.PassengerCreate):
        db_passenger = self.db.query(Passenger).filter(Passenger.id == passenger_id).first()
        if db_passenger is None:
            raise HTTPException(status_code=404, detail="Passenger not found")
        db_passenger.name = passenger.name
        db_passenger.last_name = passenger.last_name
        db_passenger.email = passenger.email
        db_passenger.phone_number = passenger.phone_number
        self.db.commit()
        self.db.refresh(db_passenger)
        return db_passenger

    def delete_passenger(self, passenger_id: int):
        db_passenger = self.db.query(Passenger).filter(Passenger.id == passenger_id).first()
        if db_passenger is None:
            raise HTTPException(status_code=404, detail="Passenger not found")
        self.db.delete(db_passenger)
        self.db.commit()
        return db_passenger

    def get_passenger_email(self, email: str):
        db_passenger = self.db.query(Passenger).filter(Passenger.email == email).first()
        if db_passenger is None:
            raise HTTPException(status_code=404, detail="Passenger not found")
        return db_passenger