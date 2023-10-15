#!/usr/bin/python3
"""This is a class for city model it inherits from base model"""

from models.base_model import BaseModel


class City(BaseModel):
    """This is a model for the city object"""

    state_id = ""
    name = ""
