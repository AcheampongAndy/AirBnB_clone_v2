#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Initializing the class

    Parameters:
    name: string - empty string
    """
    name: str = ""
