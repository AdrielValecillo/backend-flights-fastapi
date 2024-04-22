from fastapi import FastAPI
from db.database import engine, SessionLocal
import db.schemas as schemas
import db.crud as crud
import db.models
app = FastAPI()

db.models.Base.metadata.create_all(bind=engine)



@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/flights/" , tags=["Create flights"])
def create_flight(flight: schemas.FlightCreate):
    db = SessionLocal()
    flight_create = crud.create_flight(db, flight)
    return flight_create

@app.get("/flight/{flight_id}" , tags=["Get flight"])
def get_flight(flight_id: int):
    db = SessionLocal()
    flight = crud.get_flight(db, flight_id)
    return flight

@app.post("/passengers/" , tags=["Create passengers"])
def create_passenger(passenger: schemas.PassengerCreate):
    db = SessionLocal()
    passenger_create =  crud.create_passenger(db, passenger)
    return passenger_create

@app.get("/passenger/{passenger_id}" , tags=["Get passenger"])
def get_passenger(passenger_id: int):
    db = SessionLocal()
    passenger = crud.get_passenger(db, passenger_id)
    return passenger

@app.post("/reservations/" , tags=["Create reservations"])
def create_reservation(reservation: schemas.ReservationCreate):
    db = SessionLocal()
    reservation_create =  crud.create_reservation(db, reservation)
    return reservation_create

@app.get("/reservation/{reservation_id}" , tags=["Get reservation"])
def get_reservation(reservation_id: int):
    db = SessionLocal()
    reservation = crud.get_reservation(db, reservation_id)
    return reservation

@app.get("/info_reservation/{reservation_id}" , tags=["Get info reservation"])
def get_info(reservation_id: int):
    db = SessionLocal()
    info = crud.get_reservation(db, reservation_id)
    passenger_id = info.passenger_id
    flight_id = info.flight_id
    passenger = crud.get_passenger(db, passenger_id)
    flight = crud.get_flight(db, flight_id)
    return info, passenger, flight

@app.delete("/delete_reservation/{reservation_id}" , tags=["Delete reservation"])
def delete_reservation(reservation_id: int):
    db = SessionLocal()
    crud.delete_reservation(db, reservation_id)
    return {"message": "Reservation deleted"}