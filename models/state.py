#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class State(BaseModel):
    """
    Initializing the class

    Parameters:
    name: string - empty string
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable = False)
