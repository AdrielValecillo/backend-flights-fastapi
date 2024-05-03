from app.db.database import SessionLocal
from sqlalchemy.orm import Session, joinedload
from app.db.models import Flight, Passenger, Reservation, City
import app.api.schemas.schemas_cities as schemas
from fastapi import HTTPException
from datetime import datetime
from sqlalchemy.orm import joinedload
from fastapi import HTTPException

def create_city( city: schemas.CityCreate):
    db = SessionLocal()
    db_city = City(**city.dict())
    if db_city.name is None:
        raise HTTPException(status_code=400, detail="Invalid city name")
    if db_city.country is None:
        raise HTTPException(status_code=400, detail="Invalid country name")
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def get_city( city_id: int):
    db = SessionLocal()
    db_city = db.query(City).filter(City.id == city_id).first()
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city

def get_cities( skip: int = 0, limit: int = 100):
    db = SessionLocal()
    cities = db.query(City).offset(skip).limit(limit).all()
    if cities is None:
        raise HTTPException(status_code=404, detail="No cities found")
    return cities

def update_city( city_id: int, city: schemas.CityCreate):
    db = SessionLocal()
    db_city = db.query(City).filter(City.id == city_id).first()
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    db_city.name = city.name
    db_city.country = city.country
    db.commit()
    db.refresh(db_city)
    return db_city

def delete_city( city_id: int):
    db = SessionLocal()
    db_city = db.query(City).filter(City.id == city_id).first()
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    db.delete(db_city)
    db.commit()
    return db_city