from app.db.database import SessionLocal
from sqlalchemy.orm import Session, joinedload
from app.db.models import Flight, Passenger, Reservation, City
import app.api.schemas.schemas_passengers as schemas
from fastapi import HTTPException
from datetime import datetime
from sqlalchemy.orm import joinedload
from fastapi import HTTPException



def create_passenger(passenger: schemas.PassengerCreate):
    db = SessionLocal()
    db_passenger = db.query(Passenger).filter(Passenger.email == passenger.email).first()
    if db_passenger:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    db_passenger = Passenger(**passenger.dict())

    if db_passenger.name is None:
        raise HTTPException(status_code=400, detail="Invalid first name")
    if db_passenger.last_name is None:
        raise HTTPException(status_code=400, detail="Invalid last name")
    if db_passenger.email is None:
        raise HTTPException(status_code=400, detail="Invalid email")
    if db_passenger.phone_number is None:
        raise HTTPException(status_code=400, detail="Invalid phone number")
    
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger

def get_passenger(passenger_id: int):
    db = SessionLocal()
    db_passenger = db.query(Passenger).filter(Passenger.id == passenger_id).first()
    if db_passenger is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return db_passenger

def get_passengers(skip: int = 0, limit: int = 100):
    db = SessionLocal()
    passengers = db.query(Passenger).offset(skip).limit(limit).all()
    if passengers is None:
        raise HTTPException(status_code=404, detail="No passengers found")
    return passengers

def update_passenger(  passenger_id: int, passenger: schemas.PassengerCreate):
    db = SessionLocal()
    db_passenger = db.query(Passenger).filter(Passenger.id == passenger_id).first()
    if db_passenger is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    db_passenger.name = passenger.name
    db_passenger.last_name = passenger.last_name
    db_passenger.email = passenger.email
    db_passenger.phone_number = passenger.phone_number
    db.commit()
    db.refresh(db_passenger)
    return db_passenger

def delete_passenger( passenger_id: int):
    db = SessionLocal()
    db_passenger = db.query(Passenger).filter(Passenger.id == passenger_id).first()
    if db_passenger is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    db.delete(db_passenger)
    db.commit()
    return db_passenger

def get_passenger_email(email: str):
    db = SessionLocal()
    db_passenger = db.query(Passenger).filter(Passenger.email == email).first()
    if db_passenger is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return db_passenger