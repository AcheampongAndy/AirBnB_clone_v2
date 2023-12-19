#!/usr/bin/python3

from models.base_model import BaseModel
from sqlalchemy import Column, String 

class Amenity(BaseModel):
    """
    Initializing the class

    Parameters:
    name: string - empty string
    """
    __tablename__ = 'amenities'
    name = Column(String(128))
