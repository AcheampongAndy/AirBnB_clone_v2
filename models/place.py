#!/usr/bin/python3

from models.base_model import BaseModel, Base
from typing import List
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               nullable=False, primary_key=True),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
               nullable=False, primary_key=True))

class Place(BaseModel, Base):
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

    if  getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', passive_deletes=True, backref='place')
        amenities = relationship('Amenity', back_populates="place_amenities",
                                 secondary=place_amenity, viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []


    @property
    def reviews(self):
        """
        Getter attribute that returns the list of Review instances
        with place_id equals to the current Place.id.
        """
        from models import storage
        reviews_dict = storage.all('Review')
        reviews_list = []
        for review in reviews_dict.values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list

    @property
    def amenities(self):
        """getter attribute returns the list of Amenity instances"""
        from models import storage
        #from models.amenity import Amenity
        amenity_list = []
        all_amenities = storage.all('Amenity')
        for amenity in all_amenities.values():
            if amenity.place_id == self.id:
                amenity_list.append(amenity)
        return amenity_list

'''
    @property
    def amenities(self):
        """
        Getter attribute that returns the list of Amenity instances
        based on the attribute amenity_ids that contains all Amenity.id
        linked to the Place.
        """
        from models import storage
        amenity_dict = storage.all('Amenity')
        amenity_list = []
        for amenity in amenity_dict.values():
            if amenity.id in amenity_ids:
                amenity_list.append(amenity)
        return amenity_list


    @amenities.setter
    def amenities(self, amenity):
        """
        Setter attribute that handles append method for adding an Amenity.id
        to the attribute amenity_ids. This method should accept only Amenity
        object, otherwise, do nothing.
        """
        if isinstance(amenity, Amenity):
            if amenity.place_id == self.id:
                self.amenity_ids.append(amenity.id)'''
