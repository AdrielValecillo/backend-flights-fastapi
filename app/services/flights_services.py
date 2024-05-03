
from app.db.database import SessionLocal
from sqlalchemy.orm import Session, joinedload
from app.db.models import Flight, Passenger, Reservation, City
import app.api.schemas.schemas_flights as schemas
from fastapi import HTTPException
from datetime import datetime
from sqlalchemy.orm import joinedload
from fastapi import HTTPException



def create_flight(flight: schemas.FlightCreate):
    db = SessionLocal()
    if flight.capacity <= 0:
        raise HTTPException(status_code=400, detail="Invalid number of seats")
    db_flight = Flight(**flight.dict())
    db_flight.available_seats = flight.capacity
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight

def get_flight(flight_id: int):
    db = SessionLocal()
    db_flight = db.query(Flight).options(joinedload(Flight.origin_city), joinedload(Flight.destination_city)).filter(Flight.id == flight_id).first()
    if db_flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return db_flight

def get_flights( skip: int = 0, limit: int = 100):
    db = SessionLocal()
    flights = db.query(Flight).options(joinedload(Flight.origin_city), joinedload(Flight.destination_city)).offset(skip).limit(limit).all()
    if flights is None:
        raise HTTPException(status_code=404, detail="No flights found")
    return flights


def update_flight(flight_id: int, flight_capacity: int):
    db = SessionLocal()
    db_flight = db.query(Flight).filter(Flight.id == flight_id).first()
    if db_flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    db_flight.capacity = flight_capacity
    db_flight.available_seats = flight_capacity
    db.commit()
    db.refresh(db_flight)
    return db_flight

def delete_flight(flight_id: int):
    db = SessionLocal()
    db_flight = db.query(Flight).filter(Flight.id == flight_id).first()
    if db_flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    db.delete(db_flight)
    db.commit()
    return db_flight