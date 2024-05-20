from fastapi import APIRouter, HTTPException
import app.api.schemas.schemas_passengers as schemas
from app.services.passengers_services import PassengersService
from app.api.responses.responses import Responses

passenger_router = APIRouter()
crud = PassengersService()
messages = Responses()

@passenger_router.post("/api/passengers" , tags=["passengers"])
def create_passenger(passenger: schemas.PassengerCreate):
    try:
        passenger_create =  crud.create_passenger(passenger)
        return {"status": True, "data": passenger_create, "message": "Passenger created successfully", "code": 201}
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@passenger_router.get("/api/passengers/{passenger_id}" , tags=["passengers"])
def get_passenger(passenger_id: int):
    try:
        passenger = crud.get_passenger(passenger_id)
        return {"status": True, "data": passenger, "message": "Passenger retrieved successfully", "code": 200}
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@passenger_router.get("/api/passengers" , tags=["passengers"])
def get_passengers(skip: int = 0, limit: int = 100):
    try:
        passengers = crud.get_passengers( skip, limit)
        return {"status": True, "data": passengers, "message": "Passengers retrieved successfully", "code": 200}
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@passenger_router.put("/api/passengers/{passenger_id}" , tags=["passengers"])
def update_passenger(passenger_id: int, passenger: schemas.PassengerCreate):
    try:
        passenger_update = crud.update_passenger(passenger_id, passenger)
        return {"status": True, "data": passenger_update, "message": "Passenger updated successfully", "code": 200}
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@passenger_router.delete("/api/passengers/{passenger_id}" , tags=["passengers"])
def delete_passenger(passenger_id: int):
    try:
        passenger = crud.delete_passenger(passenger_id)
        return {"status": True, "data": passenger, "message": "Passenger deleted successfully", "code": 200}
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)

@passenger_router.get("/api/passengers/email/{email}" , tags=["passengers"])
def get_passenger_email(email: str):
    try:
        passenger = crud.get_passenger_email(email)
        return {"status": True, "data": passenger, "message": "Passenger retrieved successfully", "code": 200}
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)