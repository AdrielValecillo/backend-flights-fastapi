from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship



class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    country = Column(String)

    # Define the relationships
    origin_flights = relationship("Flight", back_populates="origin_city", foreign_keys="Flight.origin_id")
    destination_flights = relationship("Flight", back_populates="destination_city", foreign_keys="Flight.destination_id")


class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True, index=True)
    origin_id = Column(Integer , ForeignKey('cities.id'))
    destination_id = Column(Integer , ForeignKey('cities.id'))
    departure_date = Column(TIMESTAMP)
    capacity = Column(Integer)
    available_seats = Column(Integer)
    status = Column(String)
    
    # Define the relationships
    origin_city = relationship("City", back_populates="origin_flights", foreign_keys=[origin_id])
    destination_city = relationship("City", back_populates="destination_flights", foreign_keys=[destination_id])
    reservations = relationship("Reservation", back_populates="flight")






class Passenger(Base):
    __tablename__ = 'passengers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True,  index=True)
    phone_number = Column(String)  

    # Define the relationships
    reservations = relationship("Reservation", back_populates="passenger") 



# Define the Reservation model
class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(Integer, ForeignKey('flights.id'))
    passenger_id = Column(Integer, ForeignKey('passengers.id'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    reserved_seats = Column(Integer)
    status = Column(String)

    # Define the relationships
    flight = relationship("Flight", back_populates="reservations")
    passenger=  relationship("Passenger", back_populates="reservations")

