from fastapi import HTTPException, APIRouter
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
        return messages.response_message(city_create, "City created successfully", 201)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@city_router.get("/api/cities/{city_id}" , tags=["cities"])
def get_city(city_id: int):
    try:
        city = crud.get_city(city_id)
        return messages.response_message(city, "City retrieved successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@city_router.get("/api/cities" , tags=["cities"])
def get_cities():
    try:
        cities = crud.get_cities()
        return messages.response_message(cities, "Cities retrieved successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@city_router.put("/api/cities/{city_id}" , tags=["cities"])
def update_city(city_id: int, city: schemas.CityCreate):
    try:
        city_update = crud.update_city(city_id, city)
        return messages.response_message(city_update, "City updated successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@city_router.delete("/api/cities/{city_id}" , tags=["cities"])
def delete_city(city_id: int):
    try:
        city = crud.delete_city(city_id)
        return messages.response_message(city, "City deleted successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)