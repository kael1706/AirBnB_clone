#!/usr/bin/python3
""" City class unittests file"""
import os
import unittest
import models
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
import time


class TestCity(unittest.TestCase):
    """test class City"""

    def setUp(self):
        """know if i can create a instance"""
        self.c1 = City()
        time.sleep(1)
        self.c2 = City()
        City.state_id = ''
        City.name = ''
    
    def test_create(self):
        """know egain if i can create a instance."""
        self.c3 = City()
        self.assertTrue(hasattr(self.c3, 'id'))

    def test_uuid(self):
        """should have a id"""
        self.assertTrue(hasattr(self.c1, 'id'))

    def test_type_id(self):
        """should be a sttring"""
        self.assertTrue(isinstance(self.c1.id, str))

    def test_uniq_uuid(self):
        """should be a unique"""
        self.assertNotEqual(self.c1.id, self.c2.id)

    def test_uuid_str(self):
        """id should be a str"""
        self.assertIsInstance(self.c1.id, str)

    def test_user_model(self):
        """should be a instance of model"""
        self.assertIsInstance(self.c1, City)

    def test_BaseModel(self):
        """should be a instance of BaseModel"""
        self.assertIsInstance(self.c1, BaseModel)

    def test_created_at_exists(self):
        """should have created_at"""
        self.assertTrue(hasattr(self.c1, 'created_at'))

    def test_created_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.c1.created_at, datetime))

    def test_create_update_equal(self):
        """should have the same date and time"""
        self.assertEqual(self.c1.created_at, self.c1.updated_at)

    def test_created_not_equal1(self):
        """should have diferent date and time"""
        self.assertNotEqual(self.c1.created_at, self.c2.created_at)

    def test_create_update_not_equal2(self):
        """should have diferent date and time"""
        self.c1.updated_at = datetime.now()
        self.assertNotEqual(self.c1.created_at, self.c1.updated_at)

    def test_updated_at_exists(self):
        """should have updated_at"""
        self.assertTrue(hasattr(self.c1, 'updated_at'))

    def test_updated_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.c1.updated_at, datetime))

    def test_class_value_attrs(self):
        """testing value attrs"""
        self.assertEqual(City.state_id, '')
        self.assertEqual(City.name, '')

    def test_value_attrs(self):
        """testing value of attr"""
        self.assertEqual(self.c1.state_id, '')
        self.assertEqual(self.c1.name, '')

    def test_input_dict(self):
        """testing set attr as dict"""
        attrs = {"id": "1"}
        self.c1 = City(**attrs)
        self.assertEqual(attrs['id'], self.c1.id)

    def test_state_id(self):
        """Testing state_id"""
        self.assertTrue(hasattr(self.c1, 'state_id'))
        self.assertTrue(isinstance(self.c1.state_id, str))
        self.assertEqual(self.c1.state_id, '')

    def test_name(self):
        """Testing name"""
        self.assertTrue(hasattr(self.c1, 'name'))
        self.assertTrue(isinstance(self.c1.name, str))
        self.assertEqual(self.c1.name, '')

    def test_to_dict(self):
        """ testing create and update """
        date_frmt = "%Y-%m-%dT%H:%M:%S.%f"
        d = self.c1.to_dict()
        self.assertEqual(d["created_at"],
                         self.c1.created_at.strftime(date_frmt))
        self.assertEqual(d["updated_at"],
                         self.c1.updated_at.strftime(date_frmt))
        self.assertEqual(d["__class__"], 'City')
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)

    def test_str(self):
        """Testing string  of obj"""
        output = "[{}] ({}) {}".format(
            self.c1.__class__.__name__, self.c1.id, self.c1.__dict__)
        self.assertEqual(str(self.c1), output)

if __name__ == '__main__':
    unittest.main()
