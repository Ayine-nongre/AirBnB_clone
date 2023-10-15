#!/usr/bin/python3
"""
Unittest for state class
"""
import unittest
from models.state import State
import datetime


class StateCase(unittest.TestCase):
    """Tests instances and methods from state class"""

    state_model = State()

    def test_state_model(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.state_model)),
                         "<class 'models.state.State'>")

    def test_state_inheritance(self):
        """test if state is a subclass of BaseModel"""
        self.assertIsInstance(self.state_model, State)

    def test_state_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.state_model, 'id'))
        self.assertTrue(hasattr(self.state_model, 'created_at'))
        self.assertTrue(hasattr(self.state_model, 'updated_at'))
        self.assertTrue(hasattr(self.state_model, 'name'))

    def test_attributes_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.state_model.id, str)
        self.assertIsInstance(self.state_model.created_at, datetime.datetime)
        self.assertIsInstance(self.state_model.updated_at, datetime.datetime)
        self.assertIsInstance(self.state_model.name, str)


if __name__ == '__main__':
    unittest.main()
