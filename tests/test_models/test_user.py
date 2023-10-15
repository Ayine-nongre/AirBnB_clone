#!/usr/bin/python3
"""
Test for the user model
"""
import unittest
from models.user import User
import datetime


class UserCase(unittest.TestCase):
    """Tests for the user class"""

    user_model = User()

    def test_user_model(self):
        """tests to check if class was created"""
        self.assertEqual(str(type(self.user_model)),
                         "<class 'models.user.User'>")

    def test_user_attributes(self):
        """Test to check if attributes were created"""
        self.assertTrue(hasattr(self.user_model, 'id'))
        self.assertTrue(hasattr(self.user_model, 'created_at'))
        self.assertTrue(hasattr(self.user_model, 'updated_at'))
        self.assertTrue(hasattr(self.user_model, 'email'))
        self.assertTrue(hasattr(self.user_model, 'password'))
        self.assertTrue(hasattr(self.user_model, 'first_name'))
        self.assertTrue(hasattr(self.user_model, 'last_name'))

    def test_attributes_types(self):
        """tests to check if attribute type is correct"""
        self.assertIsInstance(self.user_model.id, str)
        self.assertIsInstance(self.user_model.created_at, datetime.datetime)
        self.assertIsInstance(self.user_model.updated_at, datetime.datetime)
        self.assertIsInstance(self.user_model.first_name, str)
        self.assertIsInstance(self.user_model.last_name, str)
        self.assertIsInstance(self.user_model.email, str)
        self.assertIsInstance(self.user_model.password, str)


if __name__ == '__main__':
    unittest.main()
