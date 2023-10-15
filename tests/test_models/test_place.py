#!/usr/bin/python3
"""
Unittest for place class
"""
import unittest
from models.place import Place
import datetime


class PlaceCase(unittest.TestCase):
    """Tests instances and methods from place class"""

    place_model = Place()

    def test_place_model(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.place_model)),
                         "<class 'models.place.Place'>")

    def test_place_inheritance(self):
        """test if place is a subclass of BaseModel"""
        self.assertIsInstance(self.place_model, Place)

    def test_place_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.place_model, 'id'))
        self.assertTrue(hasattr(self.place_model, 'created_at'))
        self.assertTrue(hasattr(self.place_model, 'updated_at'))
        self.assertTrue(hasattr(self.place_model, 'city_id'))
        self.assertTrue(hasattr(self.place_model, 'user_id'))
        self.assertTrue(hasattr(self.place_model, 'name'))
        self.assertTrue(hasattr(self.place_model, 'description'))
        self.assertTrue(hasattr(self.place_model, 'number_rooms'))
        self.assertTrue(hasattr(self.place_model, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place_model, 'max_guest'))
        self.assertTrue(hasattr(self.place_model, 'price_by_night'))
        self.assertTrue(hasattr(self.place_model, 'latitude'))
        self.assertTrue(hasattr(self.place_model, 'longitude'))
        self.assertTrue(hasattr(self.place_model, 'amenity_ids'))

    def test_attributes_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.place_model.id, str)
        self.assertIsInstance(self.place_model.created_at, datetime.datetime)
        self.assertIsInstance(self.place_model.updated_at, datetime.datetime)
        self.assertIsInstance(self.place_model.city_id, str)
        self.assertIsInstance(self.place_model.user_id, str)
        self.assertIsInstance(self.place_model.name, str)
        self.assertIsInstance(self.place_model.description, str)
        self.assertIsInstance(self.place_model.number_rooms, int)
        self.assertIsInstance(self.place_model.number_bathrooms, int)
        self.assertIsInstance(self.place_model.max_guest, int)
        self.assertIsInstance(self.place_model.price_by_night, int)
        self.assertIsInstance(self.place_model.latitude, float)
        self.assertIsInstance(self.place_model.longitude, float)
        self.assertIsInstance(self.place_model.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
