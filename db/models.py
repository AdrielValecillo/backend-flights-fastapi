from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import TIMESTAMP


class Passenger(Base):
    __tablename__ = 'passengers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True,  index=True)
    phone_number = Column(String)  

    # Define the relationships
    reservations = relationship("Reservation", back_populates="passenger") 

# Define the Flight model
class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String)
    destination = Column(String)
    deaperature_date = Column(TIMESTAMP)
    capacity = Column(Integer)
    
    # Define the relationships
    reservations = relationship("Reservation", back_populates="flight")

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

