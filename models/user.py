#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, String

class User(BaseModel):
    """
    User class inherits from BaseModel
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
