from fastapi import APIRouter, HTTPException
import app.api.schemas.schemas_flights as schemas
from app.services.flights_services import FlightsService
from typing import Optional
from app.api.responses.responses import Responses

flight_router = APIRouter()
service = FlightsService()
messages = Responses()

@flight_router.post("/api/flights" , tags=["flights"])
def create_flight(flight: schemas.FlightCreate):
    try:
        flight = service.create_flight(flight)
        return messages.response_message(flight, "Flight created successfully", 201)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)

@flight_router.get("/api/flights/{flight_id}" , tags=["flights"])
def get_flight(flight_id: int):
    try:
        flight = service.get_flight(flight_id)
        return messages.response_message(flight, "Flight retrieved successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@flight_router.get("/api/flights" , tags=["flights"])
def get_flights(search: Optional[str] = None):
    try:
        flights = service.get_flights(search)
        return messages.response_message(flights, "Flights retrieved successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)

@flight_router.put("/api/flights/{flight_id}" , tags=["flights"])
def update_flight(flight_id: int, flight_capacity: int):
    try:
        flight = service.update_flight( flight_id, flight_capacity)
        return messages.response_message(flight, "Flight updated successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)

@flight_router.delete("/api/flights/{flight_id}" , tags=["flights"])
def delete_flight(flight_id: int):
    try:
        flight = service.delete_flight( flight_id)
        return messages.response_message(flight, "Flight deleted successfully", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)