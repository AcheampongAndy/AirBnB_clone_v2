#!/usr/bin/python3

from models.base_model import BaseModel, Base
from typing import List
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table


placeAmenity = Table(
        'placeaAmenity',
        Base.metadata,
        Column(
            'place_id', String(50), ForeignKey('places.id'),
            nullable=False, primary_key=True),
        Column(
            'amenity_id', String(50), ForeignKey('amenities.id'),
            nullable=False, primary_key=True)
        )

class Place(BaseModel):
    """
    Initializing the class

    Parameters:
    city_id: string - empty string: it will be the City.id
    user_id: string - empty string: it will be the User.id
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    """
    __tablename__ = 'places'

    city_id = Column(String(50), ForeignKey('cities.id'), nullable = False)
    user_id = Column(String(50), ForeignKey('users.id'), nullable = False)
    name = Column(String(128), nullable = False)
    description = Column(String(1028))
    number_rooms = Column(Integer, nullable = False, default = 0)
    number_bathrooms = Column(Integer, nullable = False, default = 0)
    max_guest = Column(Integer, nullable = False, default = 0)
    price_by_night = Column(Integer, nullable = False, default = 0)
    latitude = Column(Float)
    logitude = Column(Float)
