from fastapi import APIRouter
from fastapi import FastAPI
from db.database import SessionLocal
import db.schemas as schemas
import db.crud as crud




app = FastAPI()

flight_router = APIRouter()


@flight_router.post("/flights/" , tags=["flights"])
def create_flight(flight: schemas.FlightCreate):
    db = SessionLocal()
    flight_create = crud.create_flight(db, flight)
    return flight_create

@flight_router.get("/flight/{flight_id}" , tags=["flights"])
def get_flight(flight_id: int):
    db = SessionLocal()
    flight = crud.get_flight(db, flight_id)
    return flight

@flight_router.get("/info_flight/{flight_id}" , tags=["flights"])
def get_info(flight_id: int):
    db = SessionLocal()
    info = crud.get_flight(db, flight_id)
    city_origin_id = info.origin_id
    city_destination_id = info.destination_id
    city_origin = crud.get_city(db, city_origin_id)
    city_destination = crud.get_city(db, city_destination_id)
    return info, city_origin, city_destination