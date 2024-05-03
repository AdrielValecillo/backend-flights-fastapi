from fastapi import HTTPException
from fastapi import APIRouter
from app.db.database import SessionLocal
import app.api.schemas.schemas_cities as schemas
#import app.db.crud as crud
import app.services.cities_services as crud


city_router = APIRouter()

@city_router.post("/api/cities" , tags=["cities"])
def create_city(city: schemas.CityCreate):
    try:
        city_create = crud.create_city(city)
        return {"status": True, "data": city_create, "message": "City created successfully", "code": 201}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}

@city_router.get("/api/cities/{city_id}" , tags=["cities"])
def get_city(city_id: int):
    try:
        city = crud.get_city(city_id)
        return {"status": True, "data": city, "message": "City retrieved successfully", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}


@city_router.get("/api/cities/" , tags=["cities"])
def get_cities(skip: int = 0, limit: int = 100):
    try:
        cities = crud.get_cities( skip, limit)
        return {"status": True, "data": cities, "message": "Cities retrieved successfully", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}