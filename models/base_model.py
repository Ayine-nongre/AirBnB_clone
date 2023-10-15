#!/usr/bin/python3
"""This is a base model for the Airbnb project"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defining the base constructor"""
    def __init__(self, *args, **kwargs):
        """if kwargs is not empty, we handle it"""
        if len(kwargs) > 0:
            """Iterating over the items in the kwargs dictionary"""
            for key, value in kwargs.items():
                """Checks if the key attributes
                is either created_at or updated_at"""
                if key == 'created_at' or key == 'updated_at':
                    """Convert the value from a string to a datetime object"""
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            """Using uuid.uuid4 to generate the unique id"""
            self.id = str(uuid.uuid4())
            """Assign the current datetime to the instance created"""
            self.created_at = datetime.now()
            """This will be updated everytime you change your object"""
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates the public instance attribute
        'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """This method defines a custom string representation for this model"""
        dic = {}

        for key, data in self.__dict__.items():
            dic[key] = data

        return "[" + self.__class__.__name__ + "](" + self.id + ") " + str(dic)

    def to_dict(self):
        """This method converts a class to a dictionary"""
        dic = {}

        for key, data in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                dic[key] = data.strftime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                dic[key] = data
        dic['__class__'] = type(self).__name__
        return dic
