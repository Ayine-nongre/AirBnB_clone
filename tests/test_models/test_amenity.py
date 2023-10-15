#!/usr/bin/python3
"""
Unittest for amenity class
"""
import unittest
from models.amenity import Amenity
import datetime


class AmenityCase(unittest.TestCase):
    """Tests instances and methods from amenity class"""

    amenity_model = Amenity()

    def test_amenity_model(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.amenity_model)),
                         "<class 'models.amenity.Amenity'>")

    def test_amenity_inheritance(self):
        """test if amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.amenity_model, Amenity)

    def test_amenity_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.amenity_model, 'id'))
        self.assertTrue(hasattr(self.amenity_model, 'created_at'))
        self.assertTrue(hasattr(self.amenity_model, 'updated_at'))
        self.assertTrue(hasattr(self.amenity_model, 'name'))

    def test_attributes_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.amenity_model.id, str)
        self.assertIsInstance(self.amenity_model.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity_model.updated_at, datetime.datetime)
        self.assertIsInstance(self.amenity_model.name, str)


if __name__ == '__main__':
    unittest.main()
