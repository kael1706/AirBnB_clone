#!/usr/bin/python3
""" BaseModel class unittests file"""
import os
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """test class BaseModel"""

    def setUp(self):
        """know if i can create a instance"""
        self.bm1 = BaseModel()
        time.sleep(0.2)
        self.bm2 = BaseModel()

    def test_uuid(self):
        """should have a id"""
        self.assertTrue(hasattr(self.bm1, 'id'))

    def test_type_id(self):
        """should be a sttring"""
        self.assertTrue(isinstance(self.bm1.id, str))

    def test_uniq_uuid(self):
        """should be a unique"""
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_uuid_str(self):
        """id should be a str"""
        self.assertIsInstance(self.bm1.id, str)

    def test_BaseModel(self):
        """should be a instance of BaseModel"""
        self.assertIsInstance(self.bm1, BaseModel)

    def test_created_at_exists(self):
        """should have created_at"""
        self.assertTrue(hasattr(self.bm1, 'created_at'))

    def test_created_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.bm1.created_at, datetime))

    def test_create_update_equal(self):
        """should have the same date and time"""
        self.assertEqual(self.bm1.created_at, self.bm1.updated_at)

    def test_created_not_equal1(self):
        """should have diferent date and time"""
        self.assertNotEqual(self.bm1.created_at, self.bm2.created_at)

    def test_create_update_not_equal2(self):
        """should have diferent date and time"""
        self.bm1.updated_at = datetime.now()
        self.assertNotEqual(self.bm1.created_at, self.bm1.updated_at)

    def test_updated_at_exists(self):
        """should have updated_at"""
        self.assertTrue(hasattr(self.bm1, 'updated_at'))

    def test_updated_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.bm1.updated_at, datetime))

    def test_input_dict(self):
        """testing set attr as dict"""
        attrs = {"id": "1"}
        self.bm1 = BaseModel(**attrs)
        self.assertEqual(attrs['id'], self.bm1.id)

    def test_to_dict(self):
        """ testing create and update """
        date_frmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.bm1.name = "Holberton"
        self.bm1.my_number = 89
        d = self.bm1.to_dict()
        self.assertEqual(d["created_at"],
                         self.bm1.created_at.strftime(date_frmt))
        self.assertEqual(d["updated_at"],
                         self.bm1.updated_at.strftime(date_frmt))
        self.assertEqual(d["__class__"], 'BaseModel')
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)
        self.assertEqual(d["id"], self.bm1.id)
        self.assertEqual(d["name"], "Holberton")
        self.assertEqual(d["my_number"], 89)

    def test_str(self):
        """Testing string  of obj"""
        output = "[{}] ({}) {}".format(
            self.bm1.__class__.__name__, self.bm1.id, self.bm1.__dict__)
        self.assertEqual(str(self.bm1), output)

if __name__ == '__main__':
    unittest.main()
