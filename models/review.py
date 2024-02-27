#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

storage_type = os.getenv('HBNB_TYPE_STORAGE', 'file')



class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'

    if storage_type == 'db':
        place_id = Column('place_id', String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column('user_id', String(60), ForeignKey('users.id'), nullable=False)
        text = Column('text', String(1024), nullable=False)

        place = relationship('Place', back_populates='reviews')
        user = relationship('User', back_populates='reviews')
    else:
        place_id = ""
        user_id = ""
        text = ""
    