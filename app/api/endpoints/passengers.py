from fastapi import APIRouter
from app.db.database import SessionLocal
import app.db.schemas as schemas
import app.db.crud as crud

passenger_router = APIRouter()

@passenger_router.post("/passengers/" , tags=["passengers"])
def create_passenger(passenger: schemas.PassengerCreate):
    db = SessionLocal()
    passenger_create =  crud.create_passenger(db, passenger)
    return passenger_create

@passenger_router.get("/passenger/{passenger_id}" , tags=["passengers"])
def get_passenger(passenger_id: int):
    db = SessionLocal()
    passenger = crud.get_passenger(db, passenger_id)
    return passenger