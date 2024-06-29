from typing import Optional
from app.services.base import Base
from app.db.models import Passenger
import app.api.schemas.schemas_passengers as schemas
from fastapi import HTTPException
from sqlalchemy import or_


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



    def get_passengers(self, search: Optional[str] = None):
        if search is not None:
            passengers = self.db.query(Passenger).filter(
                or_(Passenger.name.ilike(f"%{search}%"), 
                    Passenger.email == search, 
                    Passenger.last_name.ilike(f"%{search}%")
                )
            ).all()
        else:
            passengers = self.db.query(Passenger).all()
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