from fastapi import FastAPI
from app.db.database import engine
import app.db.models as db_models
from app.api.endpoints.flights import flight_router
from app.api.endpoints.passengers import passenger_router
from app.api.endpoints.reservations import reservation_router
from app.api.endpoints.cities import city_router
from app.api.endpoints.login import Login_router
from app.api.endpoints.airlines import airline_router
from app.api.endpoints.users import user_router

app = FastAPI()

db_models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(city_router)
app.include_router(flight_router)
app.include_router(passenger_router)
app.include_router(reservation_router)
app.include_router(Login_router)
app.include_router(airline_router)
app.include_router(user_router)







