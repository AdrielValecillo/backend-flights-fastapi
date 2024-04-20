from fastapi import FastAPI
from db.database import engine, SessionLocal
import db.models
app = FastAPI()

db.models.Base.metadata.create_all(bind=engine)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}
