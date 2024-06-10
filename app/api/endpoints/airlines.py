import os
import shutil
from typing import Optional, List
from fastapi import HTTPException, APIRouter, Depends, UploadFile, File, Form
from fastapi.responses import FileResponse
import app.api.schemas.schemas_airlines as schemas
from app.services.airlines_services import AirlinesServices
from app.api.responses.responses import Responses
from app.api.endpoints.login import JWTBearer

airline_router = APIRouter()
crud = AirlinesServices()
messages = Responses()

@airline_router.post("/api/airlines", tags=["airlines"]) #, dependencies=[Depends(JWTBearer())])
async def create_airline(name: str = Form(...), logo: UploadFile = File(...)):
    try:
        # Ensure the images directory exists
        os.makedirs('images', exist_ok=True)
        # Save the logo file
        with open(f"images/{logo.filename}", "wb") as buffer:
            shutil.copyfileobj(logo.file, buffer)

        # Create the airline object
        airline = schemas.Airline(name=name, logo_path=f"images/{logo.filename}")

        airline_create = crud.create_airline(airline)
        return messages.response_message(airline_create, "Airline created successfully", 201)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)
    
@airline_router.get("/api/airlines", tags=["airlines"], response_model=List[schemas.Airline])
async def get_all_airlines(service: AirlinesServices = Depends()):
    return service.get_airlines()

@airline_router.get("/api/airlines/{airline_id}/logo", tags=["airlines"])
async def get_airline_logo(airline_id: int):
    try:
        logo_path = crud.get_logo(airline_id)
        return FileResponse(logo_path)
    except HTTPException as e:
        return messages.message_HTTPException(e)
    except Exception as e:
        return messages.message_exception(e)