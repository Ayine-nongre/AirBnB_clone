#!/usr/bin/python3
"""This is a base model for the Airbnb project"""

import uuid
from datetime import datetime


class BaseModel:
    """Defining the base constructor"""
    def __init__(self):
        """Using uuid.uuid4 to generate the unique id"""
        self.id = str(uuid.uuid4())
        """Assign the current datetime to the instance created"""
        self.created_at = datetime.now()
        """This will be updated everytime you change your object"""
        self.updated_at = datetime.now()

    def save(self):
        """Updates the public instance attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()

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
            dic[key] = data

        return dic
