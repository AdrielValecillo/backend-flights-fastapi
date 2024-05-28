from typing import Optional
from app.services.base import Base
from sqlalchemy.orm import joinedload
from app.db.models import Flight
import app.api.schemas.schemas_flights as schemas
from fastapi import HTTPException
from app.services.cities_services import CitiesService
from sqlalchemy import or_

get_city = CitiesService().get_city


class FlightsService(Base):


    def create_flight(self, flight: schemas.FlightCreate):
        get_city(flight.origin_id)
        get_city(flight.destination_id)
        if flight.origin_id == flight.destination_id:
            raise HTTPException(status_code=400, detail="Origin and destination cannot be the same")
        db_flight = Flight(**flight.dict())
        db_flight.available_seats = flight.capacity
        self.db.add(db_flight)
        self.db.commit()
        self.db.refresh(db_flight)
        return db_flight

    def get_flight(self, flight_id: int):
        db_flight = self.db.query(Flight).options(
            joinedload(Flight.origin_city), joinedload(Flight.destination_city)
            ).filter(Flight.id == flight_id).first()
        if db_flight is None:
            raise HTTPException(status_code=404, detail="Flight not found")
        return db_flight



    def get_flights(self, search: Optional[str] = None):
        if search is not None:
            flights = self.db.query(Flight).options(
                joinedload(Flight.origin_city), 
                joinedload(Flight.destination_city)
            ).filter(Flight.is_active == True).filter(
                or_(Flight.origin_city.has(name=search), Flight.destination_city.has(name=search))
            ).all()
        else:
            flights = self.db.query(Flight).options(
                joinedload(Flight.origin_city), 
                joinedload(Flight.destination_city)
            ).filter(Flight.is_active == True).all()
            
        if len(flights) == 0:
            raise HTTPException(status_code=404, detail="Flights not found")
        return flights

    def update_flight(self, flight_id: int, flight_capacity: int):
        db_flight = self.db.query(Flight).filter(Flight.id == flight_id).first()
        if db_flight is None:
            raise HTTPException(status_code=404, detail="Flight not found")
        db_flight.capacity = flight_capacity
        db_flight.available_seats = flight_capacity
        self.db.commit()
        self.db.refresh(db_flight)
        return db_flight

    def delete_flight(self, flight_id: int):
        db_flight = self.db.query(Flight).filter(Flight.id == flight_id).first()
        if db_flight is None:
            raise HTTPException(status_code=404, detail="Flight not found")
        self.db.delete(db_flight)
        self.db.commit()
        return db_flight
    
    def cancel_flight(self, flight_id: int):
        db_flight = self.db.query(Flight).filter(Flight.id == flight_id).first()
        if db_flight is None:
            raise HTTPException(status_code=404, detail="Flight not found")
        if db_flight.is_available == False:
            raise HTTPException(status_code=400, detail="Flight already cancelled")
        db_flight.is_available = False
        self.db.commit()
        self.db.refresh(db_flight)
        return db_flight