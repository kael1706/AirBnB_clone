#!/usr/bin/python3
""" Amenity class unittests file"""
import os
import unittest
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
import time


class TestAmenity(unittest.TestCase):
    """test class Amenity"""

    def setUp(self):
        """know if i can create a instance"""
        self.a1 = Amenity()
        time.sleep(0.2)
        self.a2 = Amenity()
        Amenity.state_id = ''
        Amenity.name = ''

    def test_uuid(self):
        """should have a id"""
        self.assertTrue(hasattr(self.a1, 'id'))

    def test_type_id(self):
        """should be a sttring"""
        self.assertTrue(isinstance(self.a1.id, str))

    def test_uniq_uuid(self):
        """should be a unique"""
        self.assertNotEqual(self.a1.id, self.a2.id)

    def test_uuid_str(self):
        """id should be a str"""
        self.assertIsInstance(self.a1.id, str)

    def test_user_model(self):
        """should be a instance of model"""
        self.assertIsInstance(self.a1, Amenity)

    def test_BaseModel(self):
        """should be a instance of BaseModel"""
        self.assertIsInstance(self.a1, BaseModel)

    def test_created_at_exists(self):
        """should have created_at"""
        self.assertTrue(hasattr(self.a1, 'created_at'))

    def test_created_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.a1.created_at, datetime))

    def test_create_update_equal(self):
        """should have the same date and time"""
        self.assertEqual(self.a1.created_at, self.a1.updated_at)
    
    def test_created_not_equal1(self):
        """should have diferent date and time"""
        self.assertNotEqual(self.a1.created_at, self.a2.created_at)

    def test_create_update_not_equal2(self):
        """should have diferent date and time"""
        self.a1.updated_at = datetime.now()
        self.assertNotEqual(self.a1.created_at, self.a1.updated_at)

    def test_updated_at_exists(self):
        """should have updated_at"""
        self.assertTrue(hasattr(self.a1, 'updated_at'))

    def test_updated_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.a1.updated_at, datetime))

    def test_class_value_attrs(self):
        """testing value attrs"""
        self.assertEqual(Amenity.name, '')

    def test_value_attrs(self):
        """testing value of attr"""
        self.assertEqual(self.a1.name, '')

    def test_input_dict(self):
        """testing set attr as dict"""
        attrs = {"id": "1"}
        self.a1 = Amenity(**attrs)
        self.assertEqual(attrs['id'], self.a1.id)

    def test_name(self):
        """Testing name"""
        self.assertTrue(hasattr(self.a1, 'name'))
        self.assertTrue(isinstance(self.a1.name, str))
        self.assertEqual(self.a1.name, '')

    def test_to_dict(self):
        """ testing create and update """
        date_frmt = "%Y-%m-%dT%H:%M:%S.%f"
        d = self.a1.to_dict()
        self.assertEqual(d["created_at"],
                         self.a1.created_at.strftime(date_frmt))
        self.assertEqual(d["updated_at"],
                         self.a1.updated_at.strftime(date_frmt))
        self.assertEqual(d["__class__"], 'Amenity')
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)

    def test_str(self):
        """Testing string  of obj"""
        output = "[{}] ({}) {}".format(
            self.a1.__class__.__name__, self.a1.id, self.a1.__dict__)
        self.assertEqual(str(self.a1), output)

if __name__ == '__main__':
    unittest.main()
