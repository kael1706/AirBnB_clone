#!/usr/bin/python3
""" Review class unittests file"""
import os
import unittest
import models
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
import time


class TestReview(unittest.TestCase):
    """test class Review"""

    def setUp(self):
        """create a instance"""
        self.r1 = Review()
        time.sleep(0.2)
        self.r2 = Review()
        Review.place_id = ''
        Review.user_id = ''
        Review.text = ''

    def test_create(self):
        """know egain if i can create a instance."""
        self.r3 = Review()
        self.assertTrue(hasattr(self.r3, 'id'))

    def test_uuid(self):
        """know if id exist"""
        self.assertTrue(hasattr(self.r1, 'id'))

    def test_type_id(self):
        """should be a sttring"""
        self.assertTrue(isinstance(self.r1.id, str))

    def test_uniq_uuid(self):
        """should be a unique"""
        self.assertNotEqual(self.r1.id, self.r2.id)

    def test_uuid_str(self):
        """id should be a str"""
        self.assertIsInstance(self.r1.id, str)

    def test_user_model(self):
        """should be a instance of model"""
        self.assertIsInstance(self.r1, Review)

    def test_BaseModel(self):
        """should be a instance of BaseModel"""
        self.assertIsInstance(self.r1, BaseModel)

    def test_created_at_exists(self):
        """should have created_at"""
        self.assertTrue(hasattr(self.r1, 'created_at'))

    def test_created_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.r1.created_at, datetime))

    def test_create_update_equal(self):
        """should have the same date and time"""
        self.assertEqual(self.r1.created_at, self.r1.updated_at)

    def test_created_not_equal1(self):
        """should have diferent date and time"""
        self.assertNotEqual(self.r1.created_at, self.r2.created_at)

    def test_create_update_not_equal2(self):
        """should have diferent date and time"""
        self.r1.updated_at = datetime.now()
        self.assertNotEqual(self.r1.created_at, self.r1.updated_at)

    def test_updated_at_exists(self):
        """should have updated_at"""
        self.assertTrue(hasattr(self.r1, 'updated_at'))

    def test_updated_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.r1.updated_at, datetime))

    def test_class_value_attrs(self):
        """testing value attrs"""
        self.assertEqual(Review.place_id, '')
        self.assertEqual(Review.user_id, '')
        self.assertEqual(Review.text, '')

    def test_value_attrs(self):
        """testing value of attr"""
        self.assertEqual(self.r1.place_id, '')
        self.assertEqual(self.r1.user_id, '')
        self.assertEqual(self.r1.text, '')

    def test_input_dict(self):
        """testing set attr as dict"""
        attrs = {"id": "1"}
        self.r1 = Review(**attrs)
        self.assertEqual(attrs['id'], self.r1.id)

    def test_place_id(self):
        """Testing place_id"""
        self.assertTrue(hasattr(self.r1, 'place_id'))
        self.assertTrue(isinstance(self.r1.place_id, str))
        self.assertEqual(self.r1.place_id, '')

    def test_user_id(self):
        """Testing user_id"""
        self.assertTrue(hasattr(self.r1, 'user_id'))
        self.assertTrue(isinstance(self.r1.user_id, str))
        self.assertEqual(self.r1.user_id, '')

    def test_text(self):
        """Testing text"""
        self.assertTrue(hasattr(self.r1, 'text'))
        self.assertTrue(isinstance(self.r1.text, str))
        self.assertEqual(self.r1.text, '')

    def test_to_dict(self):
        """ testing create and update """
        date_frmt = "%Y-%m-%dT%H:%M:%S.%f"
        d = self.r1.to_dict()
        self.assertEqual(d["created_at"],
                         self.r1.created_at.strftime(date_frmt))
        self.assertEqual(d["updated_at"],
                         self.r1.updated_at.strftime(date_frmt))
        self.assertEqual(d["__class__"], 'Review')
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)

    def test_str(self):
        """Testing string  of obj"""
        output = "[{}] ({}) {}".format(
            self.r1.__class__.__name__, self.r1.id, self.r1.__dict__)
        self.assertEqual(str(self.r1), output)

if __name__ == '__main__':
    unittest.main()
