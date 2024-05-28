
from app.db.database import SessionLocal
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import make_transient
from app.db.models import Flight, Reservation
import app.api.schemas.schemas_reservations as schemas
from fastapi import HTTPException
from datetime import datetime
from app.services.flights_services import FlightsService
from app.services.passengers_services import PassengersService

get_flight = FlightsService().get_flight
get_passenger = PassengersService().get_passenger

class ReservationService():
    def __init__(self):
        self.db = SessionLocal()
    
    def create_reservation(self, reservation: schemas.ReservationCreate):
        
        db_flight = get_flight( reservation.flight_id)
        get_passenger(reservation.passenger_id)
        
        make_transient(db_flight)

        if db_flight.available_seats < reservation.reserved_seats:
            raise HTTPException(status_code=400, detail="Not enough seats available")

        db_reservation = Reservation(**reservation.dict())
        db_flight = get_flight(db_reservation.flight_id)
        db_reservation.is_active = True
        db_reservation.created_at = datetime.now()
        self.db.add(db_reservation)
        self.db.commit()
        self.db.refresh(db_reservation)

        db_flight.available_seats -= db_reservation.reserved_seats
        self.db.add(db_flight)
        self.db.commit()
        self.db.refresh(db_flight)
        self.db.refresh(db_reservation)
        return db_reservation


    def get_reservation(self, reservation_id: int):
        reservation = self.db.query(Reservation).options(
            joinedload(Reservation.passenger),
            joinedload(Reservation.flight).joinedload(Flight.origin_city),
            joinedload(Reservation.flight).joinedload(Flight.destination_city)
        ).filter(Reservation.id == reservation_id).first()
        if reservation is None:
            raise HTTPException(status_code=404, detail="Reservation not found")
        return reservation


    def get_reservations(self):
        reservations = self.db.query(Reservation).options(
            joinedload(Reservation.passenger),
            joinedload(Reservation.flight).joinedload(Flight.origin_city),
            joinedload(Reservation.flight).joinedload(Flight.destination_city)
        ).filter(Reservation.is_active != False).all()
        if not reservations:
            raise HTTPException(status_code=404, detail="Reservations not found")
        return reservations
        

    def delete_reservation(self, reservation_id: int):
        # Obtener la reserva
        db_reservation = self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if db_reservation is None:
            raise HTTPException(status_code=404, detail="Reservation not found")

        # Obtener el vuelo asociado a la reserva
        db_flight = get_flight(db_reservation.flight_id)

        # Aumentar la capacidad del vuelo
        db_flight.available_seats += db_reservation.reserved_seats
        self.db.commit()

        # Borrar la reserva
        self.db.delete(db_reservation)
        self.db.commit()

        return db_reservation


    def update_reservation(self, reservation_id: int, new_seats: int):

        # Obtener la reserva
        db_reservation = self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if not db_reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        if db_reservation.is_active == False:
            raise HTTPException(status_code=400, detail="Cannot update a cancelled reservation")

        # Obtener el vuelo asociado a la reserva
        db_flight = get_flight(db_reservation.flight_id)
        if db_flight.available_seats + db_reservation.reserved_seats < new_seats:
            raise HTTPException(status_code=400, detail="Not enough seats available")
        
        
        # Actualizar la capacidad del vuelo
        db_flight.available_seats = db_flight.available_seats + db_reservation.reserved_seats - new_seats
        self.db.commit()

        # Actualizar el número de asientos reservados
        db_reservation.reserved_seats = new_seats
        db_reservation.updated_at = datetime.now()
        self.db.commit()
        return db_reservation

    def cancel_reservation(self, reservation_id: int):

        db_reservation = self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if db_reservation is None:
            raise HTTPException(status_code=404, detail="Reservation not found")
        if db_reservation.status == False:
            raise HTTPException(status_code=400, detail="Reservation already cancelled")
        
        db_flight = get_flight( db_reservation.flight_id)

        # Aumentar la capacidad del vuelo
        db_flight.available_seats += db_reservation.reserved_seats
        self.db.commit()

        # Cancelar la reserva
        db_reservation.is_active = False
        self.db.commit()
        self.db.refresh(db_reservation)
        return db_reservation





