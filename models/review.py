#!/usr/bin/python3
"""This is a class for the review model that inherits from base model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class for the review models"""

    place_id = ""
    user_id = ""
    text = ""
