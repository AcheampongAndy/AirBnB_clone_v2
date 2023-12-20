#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel):
    """
    Initializing the class

    Parameters:
    name: string - empty string
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable = False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """
            Getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id
            """
            from models import storage
            cities_list = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
