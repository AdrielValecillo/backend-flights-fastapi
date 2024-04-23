from fastapi import FastAPI
from db.database import engine, SessionLocal
import db.schemas as schemas
import db.crud as crud
import db.models
from routers.flights import flight_router
from routers.passengers import passenger_router
from routers.reservations import reservation_router


app = FastAPI()

db.models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(flight_router)
app.include_router(passenger_router)
app.include_router(reservation_router)







