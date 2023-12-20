#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String

class City(BaseModel):
    """
    Initializing a new City

    Paramets:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
