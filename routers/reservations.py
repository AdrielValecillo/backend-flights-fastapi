from fastapi import APIRouter
from fastapi import FastAPI
from db.database import SessionLocal
import db.schemas as schemas
import db.crud as crud

reservation_router = APIRouter()


@reservation_router.post("/reservations/" , tags=["reservations"])
def create_reservation(reservation: schemas.ReservationCreate):
    db = SessionLocal()
    reservation_create =  crud.create_reservation(db, reservation)
    return reservation_create

@reservation_router.get("/reservation/{reservation_id}" , tags=["reservations"])
def get_reservation(reservation_id: int):
    db = SessionLocal()
    reservation = crud.get_reservation(db, reservation_id)
    return reservation

@reservation_router.get("/info_reservation/{reservation_id}" , tags=["reservations"])
def get_info(reservation_id: int):
    db = SessionLocal()
    info = crud.get_reservation(db, reservation_id)
    passenger_id = info.passenger_id
    flight_id = info.flight_id
    passenger = crud.get_passenger(db, passenger_id)
    flight = crud.get_flight(db, flight_id)
    return info, passenger, flight

@reservation_router.delete("/delete_reservation/{reservation_id}" , tags=["reservations"])
def delete_reservation(reservation_id: int):
    db = SessionLocal()
    crud.delete_reservation(db, reservation_id)
    return {"message": "Reservation deleted"}