from fastapi import APIRouter
import app.api.schemas.schemas_reservations as schemas
from fastapi import HTTPException
#import app.db.crud as crud
import app.services.reservations_services as crud

reservation_router = APIRouter()


@reservation_router.post("/api/reservations" , tags=["reservations"])
def create_reservation(reservation: schemas.ReservationCreate):
    try:
        reservation_create = crud.create_reservation( reservation)
        return {"status": True, "data": reservation_create, "message": "Reservation Created sussefully", "code": 201}
    except HTTPException as e:
        # todo: log error
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}

@reservation_router.get("/api/reservations/all" , tags=["reservations"])
def get_reservations():
    try:
        reservations = crud.get_reservations()
        return {"status": True, "data": reservations, "message": "Reservations retrieved", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}




@reservation_router.get("/api/reservations/{reservation_id}" , tags=["reservations"])
def get_reservations(reservation_id: int):
    try:
        info = crud.get_reservation_with_related_data( reservation_id )
        return {"status": True, "data": info, "message": "Reservations retrieved", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}


@reservation_router.put("/api/reservations/cancel" , tags=["reservations"])
def cancel_reservation(reservation_id: int):
    try:
        crud.cancel_reservation( reservation_id)
        return {"status": True, "data": None,"message": "Reservation cancelled", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}


@reservation_router.put("/api/reservations/{reservation_id}" , tags=["reservations"])
def update_reservation(reservation_id: int, new_seats: int):
    try:
        crud.update_reservation( reservation_id, new_seats)
        return {"status": True, "data": None, "message": "Reservation updated", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}
    
    
@reservation_router.delete("/api/reservarions/{reservation_id}" , tags=["reservations"])
def delete_reservation(reservation_id: int):
    try:
        crud.delete_reservation( reservation_id)
        return {"status": True, "data": None, "message": "Reservation deleted", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}
    except Exception as e:
        return {"status": False, "data": None, "message": str(e), "code": 500}
    
