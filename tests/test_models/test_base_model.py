#!/usr/bin/python3
"""Tests"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class BaseModelTest(unittest.TestCase):
    test_model = BaseModel()

    def selfTest(self):
        self.test_model.name = "Eugene"
        self.test_model.my_number = 43
        self.test_model.save()
        test_modelJson = self.test_model.to_dict()

        self.assertEqual(self.test_model.name, test_modelJson['name'])
        self.assertEqual(self.test_model.my_number, test_modelJson['my_number'])
        self.assertEqual('BaseModel', test_modelJson['__class__'])
        self.assertEqual(self.test_model.id, test_modelJson['id'])

    def test_save(self):
        self.test_model.name = "Khal"
        self.test_model.save()
        self.assertIsInstance(self.test_model.id, str)
        self.assertIsInstance(self.test_model.created_at, datetime)
        self.assertIsInstance(self.test_model.updated_at, datetime)
        self.assertNotEqual(self.test_model.created_at, self.test_model.updated_at)

if __name__ == '__main__':
    unittest.main() 
