#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

#From Clay: class State(BaseModel, Base):
class State(BaseModel):
    """ State class """
    #temporarily commenting out stuff to get JSON checks
    #__tablename__ = 'states'
    name = "" #Column('name', String(128), nullable=False)
    #cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
