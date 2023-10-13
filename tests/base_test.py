#!/usr/bin/python3
"""Tests"""

import unittest
from models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
    test_model = BaseModel()

    def test_to_dict(self):
        self.test_model.name = "Eugene"
        self.test_model.my_number = 89
        self.test_model.save()
        test_modelJson = self.my_model.to_dict()

        self.assertEqual(self.test_model.name, test_modelJson['name'])
        self.assertEqual(self.test_model.my_number, test_modelJson['my_number'])
        self.assertEqual('BaseModel', test_modelJson['__class__'])
        self.assertEqual(self.test_model.id, test_modelJson['id'])

    
    def test_save(self):
        self.test_model.name = "Khal"
        self.test_model.save()
        self.assertIsInstance(self.test_model.id, str)
        self.assertIsInstance(self.test_model.created_at, str)
        self.assertIsInstance(self.test_model.updated_at, str)
        self.assertNotEqual(self.test_model.created_at, self.test_model.updated_at)

if __name__ == '__main__':
    unittest.main() 