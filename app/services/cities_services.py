from typing import Optional
from app.db.models import City
import app.api.schemas.schemas_cities as schemas
from fastapi import HTTPException
from app.services.base import Base
from sqlalchemy import or_


class CitiesService(Base):

    def create_city(self, city: schemas.CityCreate):
        db_city = City(**city.dict())
        if db_city.name is None:
            raise HTTPException(status_code=400, detail="Invalid city name")
        if db_city.country is None:
            raise HTTPException(status_code=400, detail="Invalid country name")
        self.db.add(db_city)
        self.db.commit()
        self.db.refresh(db_city)
        return db_city

    def get_city(self, city_id: int):
        db_city = self.db.query(City).filter(City.id == city_id).first()
        if db_city is None:
            raise HTTPException(status_code=404, detail="City not found")
        return db_city

    def get_cities(self, search: Optional[str] = None):
        if search is not None:
            db_cities = self.db.query(City).filter(
                or_(City.name.ilike(f"%{search}%"), City.country.ilike(f"%{search}%"))
            ).all()
        else:
            db_cities = self.db.query(City).all()

        if len(db_cities) == 0:
            raise HTTPException(status_code=404, detail="No cities found")
        return db_cities

    def update_city(self, city_id: int, city: schemas.CityCreate):
        db_city = self.db.query(City).filter(City.id == city_id).first()
        if db_city is None:
            raise HTTPException(status_code=404, detail="City not found")
        db_city.name = city.name
        db_city.country = city.country
        self.db.commit()
        self.db.refresh(db_city)
        return db_city

    def delete_city(self, city_id: int):
        db_city = self.db.query(City).filter(City.id == city_id).first()
        if db_city is None:
            raise HTTPException(status_code=404, detail="City not found")
        self.db.delete(db_city)
        self.db.commit()
        return db_city