from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
import app.api.schemas.schemas_passengers as schemas
from app.services.passengers_services import PassengersService
from app.api.responses.responses import Responses
from app.api.endpoints.login import JWTBearer

passenger_router = APIRouter()
crud = PassengersService()
messages = Responses()

@passenger_router.post("/api/passengers" , tags=["passengers"])
def create_passenger(passenger: schemas.PassengerCreate):
    try:
        passenger_create =  crud.create_passenger(passenger)
        return messages.response_message(passenger_create, "Passenger created successfully", 201)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@passenger_router.get("/api/passengers/{passenger_id}" , tags=["passengers"], dependencies=[Depends(JWTBearer())])
def get_passenger(passenger_id: int):
    try:
        passenger = crud.get_passenger(passenger_id)
        return messages.response_message(passenger, "Passenger retrieved successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@passenger_router.get("/api/passengers" , tags=["passengers"], dependencies=[Depends(JWTBearer())])
def get_passengers(search: Optional[str] = None):
    try:
        passengers = crud.get_passengers(search)
        return messages.response_message(passengers, "Passengers retrieved successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@passenger_router.put("/api/passengers/{passenger_id}" , tags=["passengers"])
def update_passenger(passenger_id: int, passenger: schemas.PassengerCreate):
    try:
        passenger_update = crud.update_passenger(passenger_id, passenger)
        return messages.response_message(passenger_update, "Passenger updated successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@passenger_router.delete("/api/passengers/{passenger_id}" , tags=["passengers"], dependencies=[Depends(JWTBearer())])
def delete_passenger(passenger_id: int):
    try:
        passenger = crud.delete_passenger(passenger_id)
        return messages.response_message(passenger, "Passenger deleted successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)
    
    
"""
@passenger_router.get("/api/passengers/email/{email}" , tags=["passengers"])
def get_passenger_email(email: str):
    try:
        passenger = crud.get_passenger_email(email)
        return messages.response_message(passenger, "Passenger retrieved successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)
"""