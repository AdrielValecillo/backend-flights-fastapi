from app.db.database import SessionLocal
from sqlalchemy.orm import Session, joinedload
from app.db.models import Flight, Passenger, Reservation, City
import app.api.schemas.schemas_reservations as schemas
from fastapi import HTTPException
from datetime import datetime
from sqlalchemy.orm import joinedload
from fastapi import HTTPException
from app.services.flights_services import get_flight
from app.services.passengers_services import get_passenger



def create_reservation( reservation: schemas.ReservationCreate):
    db = SessionLocal()
    db_flight = get_flight( reservation.flight_id)
    get_passenger(reservation.passenger_id)
    if reservation.reserved_seats <= 0:
        raise HTTPException(status_code=400, detail="Invalid number of seats")
    if db_flight.available_seats < reservation.reserved_seats:
        raise HTTPException(status_code=400, detail="Not enough seats available")

    db_reservation = Reservation(**reservation.dict())
    db_flight = get_flight(db_reservation.flight_id)
    db_reservation.status = "active"
    db_reservation.created_at = datetime.now()
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)

    db_flight.available_seats -= db_reservation.reserved_seats
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    db.refresh(db_reservation)
    return db_reservation


def get_reservation( reservation_id: schemas.ReservationCreate):
    db = SessionLocal()
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation
    

def delete_reservation( reservation_id: int):
    db = SessionLocal()
    # Obtener la reserva
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")

    # Obtener el vuelo asociado a la reserva
    db_flight = get_flight(db, db_reservation.flight_id)

    # Aumentar la capacidad del vuelo
    db_flight.available_seats += db_reservation.reserved_seats
    db.commit()

    # Borrar la reserva
    db.delete(db_reservation)
    db.commit()

    return db_reservation


def update_reservation(reservation_id: int, new_seats: int):
    db = SessionLocal()
    # Obtener la reserva
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    if db_reservation.status == "cancelled":
        raise HTTPException(status_code=400, detail="Cannot update a cancelled reservation")

    # Obtener el vuelo asociado a la reserva
    db_flight = get_flight(db, db_reservation.flight_id)
    if db_flight.available_seats + db_reservation.reserved_seats < new_seats:
        raise HTTPException(status_code=400, detail="Not enough seats available")
    
    
    # Actualizar la capacidad del vuelo
    db_flight.available_seats = db_flight.available_seats + db_reservation.reserved_seats - new_seats
    db.commit()

    # Actualizar el número de asientos reservados
    db_reservation.reserved_seats = new_seats
    db_reservation.updated_at = datetime.now()
    db.commit()
    return db_reservation

def cancel_reservation( reservation_id: int):
    db = SessionLocal()
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    if db_reservation.status == "cancelled":
        raise HTTPException(status_code=400, detail="Reservation already cancelled")
    
    db_flight = get_flight(db, db_reservation.flight_id)

    # Aumentar la capacidad del vuelo
    db_flight.available_seats += db_reservation.reserved_seats
    db.commit()

    # Cancelar la reserva
    db_reservation.status = "cancelled"
    db.commit()

    return db_reservation



def get_reservation_with_related_data( reservation_id: int):
    db = SessionLocal()
    reservation = db.query(Reservation).options(
        joinedload(Reservation.passenger),
        joinedload(Reservation.flight).joinedload(Flight.origin_city),
        joinedload(Reservation.flight).joinedload(Flight.destination_city)
    ).filter(Reservation.id == reservation_id).first()
    if reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

def get_reservations():
    db = SessionLocal()
    reservations = db.query(Reservation).options(
        joinedload(Reservation.passenger),
        joinedload(Reservation.flight).joinedload(Flight.origin_city),
        joinedload(Reservation.flight).joinedload(Flight.destination_city)
    ).filter(Reservation.status != "cancelled").all()
    if not reservations:
        raise HTTPException(status_code=404, detail="Reservations not found")
    return reservations

