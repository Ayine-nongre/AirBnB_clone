#!/usr/bin/python3
"""
Unittest for the review model
"""
import unittest
from models.review import Review
import datetime


class ReviewCase(unittest.TestCase):
    """Tests instances and methods from review class"""

    review_model = Review()

    def test_review_model(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.review_model)),
                         "<class 'models.review.Review'>")

    def test_review_inheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.review_model, Review)

    def test_user_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.review_model, 'id'))
        self.assertTrue(hasattr(self.review_model, 'created_at'))
        self.assertTrue(hasattr(self.review_model, 'updated_at'))
        self.assertTrue(hasattr(self.review_model, 'place_id'))
        self.assertTrue(hasattr(self.review_model, 'user_id'))
        self.assertTrue(hasattr(self.review_model, 'text'))

    def test_attributes_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.review_model.id, str)
        self.assertIsInstance(self.review_model.created_at, datetime.datetime)
        self.assertIsInstance(self.review_model.updated_at, datetime.datetime)
        self.assertIsInstance(self.review_model.place_id, str)
        self.assertIsInstance(self.review_model.user_id, str)
        self.assertIsInstance(self.review_model.text, str)


if __name__ == '__main__':
    unittest.main()
