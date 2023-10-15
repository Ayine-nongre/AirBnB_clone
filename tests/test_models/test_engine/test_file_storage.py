#!/usr/bin/python3
""" Unittests for file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """ Suite of File Storage Tests """

    test_model = BaseModel()

    def testClassInstance(self):
        """ Check instance """
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """ Test save and reload functions """
        self.test_model.full_name = "BaseModel Instance"
        self.test_model.save()
        data = self.test_model.to_dict()
        obj = storage.all()

        key = data['__class__'] + "." + data['id']
        self.assertEqual(key in obj, True)

    def testStoreBaseModel2(self):
        """ Test save, reload and update functions """
        self.test_model.my_name = "First name"
        self.test_model.save()
        data = self.test_model.to_dict()
        obj = storage.all()

        key = data['__class__'] + "." + data['id']

        self.assertEqual(key in obj, True)
        self.assertEqual(data['my_name'], "First name")

        time_created = data['created_at']
        time_updated = data['updated_at']

        self.test_model.my_name = "Second name"
        self.test_model.save()
        data = self.test_model.to_dict()
        obj = storage.all()

        self.assertEqual(key in obj, True)

        time_created2 = data['created_at']
        time_updated2 = data['updated_at']

        self.assertEqual(time_created, time_created2)
        self.assertNotEqual(time_updated, time_updated2)
        self.assertEqual(data['my_name'], "Second name")

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testsave(self):
        """verify if JSON exists"""
        self.test_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testreload(self):
        """test if reload """
        self.test_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        obj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(obj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(obj[key].to_dict(), value.to_dict())

    def testSaveSelf(self):
        """ Check save self """
        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)

    def test_save_FileStorage(self):
        """ Test if 'new' method is working good """
        data = self.test_model.to_dict()
        new_key = data['__class__'] + "." + data['id']
        storage.save()
        with open("file.json", 'r') as fd:
            read_data = json.load(fd)
        new = read_data[new_key]
        for key in new:
            self.assertEqual(data[key], new[key])


if __name__ == '__main__':
    unittest.main()
