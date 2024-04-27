from fastapi import APIRouter
from fastapi import FastAPI
from db.database import SessionLocal
import db.schemas as schemas
import db.crud as crud

reservation_router = APIRouter()


@reservation_router.post("/reservations/" , tags=["reservations"])
def create_reservation(reservation: schemas.ReservationCreate):
    db = SessionLocal()
    return crud.create_reservation(db, reservation)

@reservation_router.get("/reservation/{reservation_id}" , tags=["reservations"])
def get_reservation(reservation_id: int):
    db = SessionLocal()
    return crud.get_reservation(db, reservation_id)

@reservation_router.get("/info_reservation/{reservation_id}" , tags=["reservations"])
def get_info(reservation_id: int):
    db = SessionLocal()
    info = crud.get_reservation(db, reservation_id)
    passenger_id = info.passenger_id
    flight_id = info.flight_id
    passenger = crud.get_passenger(db, passenger_id)
    flight = crud.get_flight(db, flight_id)
    origin_id = flight.origin_id
    destination_id = flight.destination_id
    origin = crud.get_city(db, origin_id)
    destination = crud.get_city(db, destination_id)
    return info, passenger, flight, origin, destination


@reservation_router.put("/cancel_reservation/" , tags=["reservations"])
def cancel_reservation(reservation_id: int):
    db = SessionLocal()
    crud.cancel_reservation(db, reservation_id)
    return {"message": "Reservation cancelled"}


@reservation_router.delete("/delete_reservation/{reservation_id}" , tags=["reservations"])
def delete_reservation(reservation_id: int):
    db = SessionLocal()
    crud.delete_reservation(db, reservation_id)
    return {"message": "Reservation deleted"}

@reservation_router.put("/update_reservation/{reservation_id}" , tags=["reservations"])
def update_reservation(reservation_id: int, new_seats: int):
    db = SessionLocal()
    crud.update_reservation(db, reservation_id, new_seats)
    return {"message": "Reservation updated"}