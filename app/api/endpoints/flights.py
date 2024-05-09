from fastapi import APIRouter, HTTPException
import app.api.schemas.schemas_flights as schemas
from app.services.flights_services import FlightsService
from typing import Optional

flight_router = APIRouter()
service = FlightsService()

@flight_router.post("/api/flights" , tags=["flights"])
def create_flight(flight: schemas.FlightCreate):
    try:
        flight = service.create_flight(flight)
        return {"status": True, "data": flight, "message": "Flight created successfully", "code": 201}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}

@flight_router.get("/api/flights/{flight_id}" , tags=["flights"])
def get_flight(flight_id: int):
    try:
        flight = service.get_flight(flight_id)
        return {"status": True, "data": flight, "message": "Flight created successfully", "code": 201}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}


@flight_router.get("/api/flights" , tags=["flights"])
def get_flights(origin: Optional[int] = None):
    try:
        flights = service.get_flights(origin)
        return {"status": True, "data": flights, "message": "Flights retrieved successfully", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}

@flight_router.put("/api/flights/{flight_id}" , tags=["flights"])
def update_flight(flight_id: int, flight_capacity: int):
    try:
        flight = service.update_flight( flight_id, flight_capacity)
        return {"status": True, "data": flight, "message": "Flight updated successfully", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}

@flight_router.delete("/api/flights/{flight_id}" , tags=["flights"])
def delete_flight(flight_id: int):
    try:
        flight = service.delete_flight( flight_id)
        return {"status": True, "data": flight, "message": "Flight deleted successfully", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}