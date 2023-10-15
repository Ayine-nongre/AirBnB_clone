#!/usr/bin/python3
"""
Unittest for city class
"""
import unittest
from models.city import City
import datetime


class CityCase(unittest.TestCase):
    """Tests instances and methods from state class"""

    city_model = City()

    def test_city_model(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.city_model)),
                         "<class 'models.city.City'>")

    def test_city_inheritance(self):
        """test if city is a subclass of BaseModel"""
        self.assertIsInstance(self.city_model, City)

    def test_city_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.city_model, 'id'))
        self.assertTrue(hasattr(self.city_model, 'created_at'))
        self.assertTrue(hasattr(self.city_model, 'updated_at'))
        self.assertTrue(hasattr(self.city_model, 'state_id'))
        self.assertTrue(hasattr(self.city_model, 'name'))

    def test_attributes_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.city_model.id, str)
        self.assertIsInstance(self.city_model.created_at, datetime.datetime)
        self.assertIsInstance(self.city_model.updated_at, datetime.datetime)
        self.assertIsInstance(self.city_model.state_id, str)
        self.assertIsInstance(self.city_model.name, str)


if __name__ == '__main__':
    unittest.main()
