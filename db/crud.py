from sqlalchemy.orm import Session
from db.models import Flight, Passenger, Reservation
import db.schemas as schemas
from fastapi import HTTPException

def create_flight(db: Session, flight: schemas.FlightCreate):
    db_flight = Flight(**flight.dict())
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight


def get_flight(db: Session, flight_id: int):
    db_flight = db.query(Flight).filter(Flight.id == flight_id).first()
    if db_flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return db_flight

def create_passenger(db: Session, passenger: schemas.PassengerCreate):
    db_passenger = Passenger(**passenger.dict())
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger

def get_passenger(db: Session, passenger_id: int):
    db_passenger = db.query(Passenger).filter(Passenger.id == passenger_id).first()
    if db_passenger is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return db_passenger


def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    # Crear la reserva
    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)

    # Obtener el vuelo asociado a la reserva
    db_flight = get_flight(db, db_reservation.flight_id)

    # Comprobar si hay suficientes asientos disponibles
    if db_flight.capacity < db_reservation.reserved_seats:
        raise HTTPException(status_code=400, detail="Not enough seats available")

    # Disminuir la capacidad del vuelo
    db_flight.capacity -= db_reservation.reserved_seats
    db.commit()

    return db_reservation


""""
def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation
"""
def get_reservation(db: Session, reservation_id: schemas.ReservationCreate):
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    return db_reservation
    

def delete_reservation(db: Session, reservation_id: int):
    # Obtener la reserva
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")

    # Obtener el vuelo asociado a la reserva
    db_flight = get_flight(db, db_reservation.flight_id)

    # Aumentar la capacidad del vuelo
    db_flight.capacity += db_reservation.reserved_seats
    db.commit()

    # Borrar la reserva
    db.delete(db_reservation)
    db.commit()

    return db_reservation