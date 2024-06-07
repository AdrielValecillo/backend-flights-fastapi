from fastapi import APIRouter, HTTPException, Depends
import app.api.schemas.schemas_reservations as schemas
from app.services.reservations_services import ReservationService
from app.api.responses.responses import Responses
from app.api.endpoints.login import JWTBearer

crud = ReservationService()
reservation_router = APIRouter()
messages = Responses()

@reservation_router.post("/api/reservations" , tags=["reservations"])
def create_reservation(reservation: schemas.ReservationCreate):
    try:
        reservation_create = crud.create_reservation(reservation)
        return messages.response_message(reservation_create, "Reservation created", 201)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)

@reservation_router.get("/api/reservations" , tags=["reservations"])
def get_reservations():
    try:
        reservations = crud.get_reservations()
        return messages.response_message(reservations, "Reservations retrieved", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)




@reservation_router.get("/api/reservations/{reservation_id}" , tags=["reservations"])
def get_reservation(reservation_id: int):
    try:
        info = crud.get_reservation( reservation_id )
        return messages.response_message(info, "Reservation retrieved", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@reservation_router.put("/api/reservations/cancel" , tags=["reservations"])
def cancel_reservation(reservation_id: int):
    try:
        crud.cancel_reservation( reservation_id)
        return messages.response_message(None, "Reservation cancelled", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)


@reservation_router.put("/api/reservations/{reservation_id}" , tags=["reservations"])
def update_reservation(reservation_id: int, new_seats: int):
    try:
        crud.update_reservation( reservation_id, new_seats)
        return messages.response_message(None, "Reservation updated", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)
    
    
@reservation_router.delete("/api/reservarions/{reservation_id}" , tags=["reservations"], dependencies=[Depends(JWTBearer())])
def delete_reservation(reservation_id: int):
    try:
        crud.delete_reservation( reservation_id)
        return messages.response_message(None, "Reservation deleted", 200)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)
    
