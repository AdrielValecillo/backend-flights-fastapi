from fastapi import APIRouter
from app.db.database import SessionLocal
import app.db.schemas as schemas
import app.db.crud as crud


city_router = APIRouter()

@city_router.post("/cities/" , tags=["cities"])
def create_city(city: schemas.CityCreate):
    db = SessionLocal()
    city_create = crud.create_city(db, city)
    return city_create

@city_router.get("/city/{city_id}" , tags=["cities"])
def get_city(city_id: int):
    db = SessionLocal()
    city = crud.get_city(db, city_id)
    return city