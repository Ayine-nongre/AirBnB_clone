#!/usr/bin/python3
"""This class saves a JSON object by serialiazation
and loads it back by deserialization"""

import json
import os


class FileStorage:
    """FileStorage is the class object"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns all objects"""
        return FileStorage.__objects

    def new(self, model):
        """This method creates a new object and saves"""
        tag = model.__class__.__name__ + "." + model.id
        FileStorage.__objects[tag] = model

    def save(self):
        """This method saves all the objects to a json file"""
        data = {}

        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """This method reads the data from a json file
        and makes it an object by deserialization"""
        from models.base_model import BaseModel
        from models.user import User

        models = {"BaseModel": BaseModel, "User": User}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    obj = key.split('.')
                    for tag, data in models:
                        if obj[0] == tag:
                            self.new(data(**value))
