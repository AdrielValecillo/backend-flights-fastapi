from sqlalchemy.orm import Session
from db.models import Flight, Passenger, Reservation, City
import db.schemas as schemas
from fastapi import HTTPException
from datetime import datetime


def create_city(db: Session, city: schemas.CityCreate):
    db_city = City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def get_city(db: Session, city_id: int):
    db_city = db.query(City).filter(City.id == city_id).first()
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city

def create_flight(db: Session, flight: schemas.FlightCreate):
    db_flight = Flight(**flight.dict())
    db_flight.available_seats = flight.capacity
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
    db_reservation.status = "active"
    db_reservation.created_at = datetime.now()
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)

    # Obtener el vuelo asociado a la reserva
    db_flight = get_flight(db, db_reservation.flight_id)

    # Comprobar si hay suficientes asientos disponibles
    if db_flight.available_seats < db_reservation.reserved_seats:
        raise HTTPException(status_code=400, detail="Not enough seats available")

    # Disminuir la capacidad del vuelo
    db_flight.available_seats -= db_reservation.reserved_seats
    db.commit()

    return db_reservation


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
    db_flight.available_seats += db_reservation.reserved_seats
    db.commit()

    # Borrar la reserva
    db.delete(db_reservation)
    db.commit()

    return db_reservation


def update_reservation(db: Session, reservation_id: int, new_seats: int):
    # Obtener la reserva
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    if db_reservation.status == "cancelled":
        raise HTTPException(status_code=400, detail="Cannot update a cancelled reservation")

    # Obtener el vuelo asociado a la reserva
    db_flight = get_flight(db, db_reservation.flight_id)

    # Actualizar la capacidad del vuelo
    db_flight.available_seats = db_flight.available_seats + db_reservation.reserved_seats - new_seats
    db.commit()

    # Actualizar el número de asientos reservados
    db_reservation.reserved_seats = new_seats
    db_reservation.updated_at = datetime.now()
    db.commit()

    return db_reservation

def cancel_reservation(db: Session, reservation_id: int):
    # Obtener la reserva
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    if db_reservation.status == "cancelled":
        raise HTTPException(status_code=400, detail="Reservation already cancelled")
    # Obtener el vuelo asociado a la reserva
    db_flight = get_flight(db, db_reservation.flight_id)

    # Aumentar la capacidad del vuelo
    db_flight.available_seats += db_reservation.reserved_seats
    db.commit()

    # Cancelar la reserva
    db_reservation.status = "cancelled"
    db.commit()

    return db_reservation