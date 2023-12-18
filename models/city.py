#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """
    Initializing a new City

    Paramets:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    state_id: str = ""
    name: str = ""
