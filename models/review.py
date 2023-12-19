#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Review(BaseModel):
    """
    Initializing the class

    Parameters:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    __tablename__ = 'reviews'
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    text = Column(String(128))
