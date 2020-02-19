#!/usr/bin/python3
""" User class unittests file"""
import os
import unittest
import models
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """class User"""

    def setUp(self):
        """should can"""
        self.u1 = User()
        self.u2 = User()
        User.email = ''
        User.password = ''
        User.first_name = ''
        User.last_name = ''

    def test_uuid(self):
        """should have a id"""
        self.assertTrue(hasattr(self.u1, 'id'))

    def test_type_id(self):
        """should be a sttring"""
        self.assertTrue(isinstance(self.u1.id, str))

    def test_uniq_uuid(self):
        """should be a unique"""
        self.assertNotEqual(self.u1.id, self.u2.id)

    def test_uuid_str(self):
        """id should be a str"""
        self.assertIsInstance(self.u1.id, str)

    def test_user_model(self):
        """should be a instance of model"""
        self.assertIsInstance(self.u1, User)

    def test_BaseModel(self):
        """should be a instance of BaseModel"""
        self.assertIsInstance(self.u1, BaseModel)

    def test_created_at_exists(self):
        """should have created_at"""
        self.assertTrue(hasattr(self.u1, 'created_at'))

    def test_created_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.u1.created_at, datetime))

    def test_create_update_equal(self):
        """should have the same date and time"""
        self.assertEqual(self.u1.created_at, self.u1.updated_at)
    
    def test_created_not_equal1(self):
        """should have diferent date and time"""
        self.assertNotEqual(self.u1.created_at, self.u2.created_at)

    def test_create_update_not_equal2(self):
        """should have diferent date and time"""
        self.u1.updated_at = datetime.now()
        self.assertNotEqual(self.u1.created_at, self.u1.updated_at)

    def test_updated_at_exists(self):
        """should have updated_at"""
        self.assertTrue(hasattr(self.u1, 'updated_at'))

    def test_updated_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.u1.updated_at, datetime))

    def test_class_value_attrs(self):
        """testing value attrs"""
        self.assertEqual(User.first_name, '')
        self.assertEqual(User.last_name, '')
        self.assertEqual(User.email, '')
        self.assertEqual(User.password, '')

    def test_value_attrs(self):
        """testing value of attr"""
        self.assertEqual(self.u1.first_name, '')
        self.assertEqual(self.u1.last_name, '')
        self.assertEqual(self.u1.email, '')
        self.assertEqual(self.u1.password, '')

    def test_input_dict(self):
        """testing set attr as dict"""
        attrs = {"id": "1"}
        self.u1 = User(**attrs)
        self.assertEqual(attrs['id'], self.u1.id)

    def test_name(self):
        """Testing first name"""
        self.assertTrue(hasattr(self.u1, 'first_name'))
        self.assertTrue(isinstance(self.u1.first_name, str))
        self.assertEqual(self.u1.first_name, '')

    def test_last_name(self):
        """Testing last name"""
        self.assertTrue(hasattr(self.u1, 'last_name'))
        self.assertTrue(isinstance(self.u1.last_name, str))
        self.assertEqual(self.u1.last_name, '')

    def test_email(self):
        """Testing  email"""
        self.assertTrue(hasattr(self.u1, 'email'))
        self.assertTrue(isinstance(self.u1.email, str))
        self.assertEqual(self.u1.email, '')

    def test_password(self):
        """Testing class attribute password"""
        self.assertTrue(hasattr(self.u1, 'password'))
        self.assertTrue(isinstance(self.u1.password, str))
        self.assertEqual(self.u1.password, '')

    def test_to_dict(self):
        """ testing create and update """
        date_frmt = "%Y-%m-%dT%H:%M:%S.%f"
        d = self.u1.to_dict()
        self.assertEqual(d["created_at"],
                         self.u1.created_at.strftime(date_frmt))
        self.assertEqual(d["updated_at"],
                         self.u1.updated_at.strftime(date_frmt))
        self.assertEqual(d["__class__"], 'User')
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)

    def test_str(self):
        """Testing string  of obj"""
        output = "[{}] ({}) {}".format(
            self.u1.__class__.__name__, self.u1.id, self.u1.__dict__)
        self.assertEqual(str(self.u1), output)

if __name__ == '__main__':
    unittest.main()
