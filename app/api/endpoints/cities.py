from fastapi import HTTPException
from fastapi import APIRouter
import app.api.schemas.schemas_cities as schemas
from app.services.cities_services import CitiesService
from app.api.responses.responses import Responses

city_router = APIRouter()
crud = CitiesService()
messages = Responses()

@city_router.post("/api/cities" , tags=["cities"])
def create_city(city: schemas.CityCreate):
    try:
        city_create = crud.create_city(city)
        return {"status": True, "data": city_create, "message": "City created successfully", "code": 201}
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@city_router.get("/api/cities/{city_id}" , tags=["cities"])
def get_city(city_id: int):
    try:
        city = crud.get_city(city_id)
        return {"status": True, "data": city, "message": "City retrieved successfully", "code": 200}
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@city_router.get("/api/cities" , tags=["cities"])
def get_cities(skip: int = 0, limit: int = 100):
    try:
        cities = crud.get_cities( skip, limit)
        return {"status": True, "data": cities, "message": "Cities retrieved successfully", "code": 200}
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@city_router.put("/api/cities/{city_id}" , tags=["cities"])
def update_city(city_id: int, city: schemas.CityCreate):
    try:
        city_update = crud.update_city(city_id, city)
        return {"status": True, "data": city_update, "message": "City updated successfully", "code": 200}
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@city_router.delete("/api/cities/{city_id}" , tags=["cities"])
def delete_city(city_id: int):
    try:
        city = crud.delete_city(city_id)
        return {"status": True, "data": city, "message": "City deleted successfully", "code": 200}
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)