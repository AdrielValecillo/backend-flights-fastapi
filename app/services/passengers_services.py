from sqlalchemy.orm import Session, joinedload
from app.db.models import Flight, Passenger, Reservation, City
import app.api.schemas.schemas_passengers as schemas
from fastapi import HTTPException
from datetime import datetime
from sqlalchemy.orm import joinedload
from fastapi import HTTPException


def create_passenger(db: Session, passenger: schemas.PassengerCreate):
    db_passenger = Passenger(**passenger.dict())
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger

def get_passenger(db: Session, passenger_id: int):
    db_passenger = db.query(Passenger).filter(Passenger.id == passenger_id).first()
    if db_passenger is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return db_passenger


