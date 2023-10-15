#!/usr/bin/python3
"""This is a model for a user object"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from the BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
