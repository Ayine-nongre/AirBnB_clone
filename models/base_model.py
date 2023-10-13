#!/usr/bin/python3
"""This is a base model for the Airbnb project"""

from datetime import datetime

class BaseModel:
    """This is a base model for the Airbnb project"""

    def __str__(self):
        """This method defines a custom string representation for this model"""
        dic = {}

        for key, data in self.__dict__.items():
            dic[key] = data

        return "[" + self.__class__.__name__ + "] (" + self.id + ") " + str(dic)

    def to_dict(self):
        """This method converts a class to a dictionary"""
        dic = {}

        for key, data in self.__dict__.items():
            dic[key] = data
        
        return dic