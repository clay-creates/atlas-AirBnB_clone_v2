#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
#ace do the thing
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

    id = Column('id', String(60), primary_key=True)
    created_at = Column('created_at', DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column('cupdated_at', DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        print("created new model")
        if not kwargs:
            print("Did not detect kwargs")
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key in kwargs:
                print("start of key loop")
                if key == "updated_at":
                    print("set 'updated at'")
                    kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                             '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "created_at":
                    print("set 'created at'")
                    kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                             '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    print("Set {0} to {1}".format(key, kwargs[key]))
                    setattr(self, key, kwargs[key])
                del kwargs['__class__']
                self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        if '_sa_instance state' in dictionary:
            del dictionary['_sa_instance_state']
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Deletes current instance from storage"""
        from models import storage
        storage.delete(self)
