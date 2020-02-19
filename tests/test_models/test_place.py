#!/usr/bin/python3
""" Place class unittests file"""
import os
import unittest
import models
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
import time


class TestPlace(unittest.TestCase):
    """test class Place"""

    def setUp(self):
        """know if i can create a instance"""
        self.p1 = Place()
        # time.sleep(0.2)
        self.p2 = Place()
        Place.city_id = ''
        Place.user_id = ''
        Place.name = ''
        Place.description = ''
        Place.number_rooms = 0
        Place.number_bathrooms = 0
        Place.max_guest = 0
        Place.price_by_night = 0
        Place.latitude = 0.0
        Place.longitude = 0.0
        Place.amenity_ids = []

    def test_create(self):
        """know egain if i can create a instance."""
        self.p3 = Place()
        self.assertTrue(hasattr(self.p3, 'id'))

    def test_uuid(self):
        """should have a id"""
        self.assertTrue(hasattr(self.p1, 'id'))

    def test_type_id(self):
        """should be a sttring"""
        self.assertTrue(isinstance(self.p1.id, str))

    def test_uniq_uuid(self):
        """should be a unique"""
        self.assertNotEqual(self.p1.id, self.p2.id)

    def test_uuid_str(self):
        """id should be a str"""
        self.assertIsInstance(self.p1.id, str)

    def test_user_model(self):
        """should be a instance of model"""
        self.assertIsInstance(self.p1, Place)

    def test_BaseModel(self):
        """should be a instance of BaseModel"""
        self.assertIsInstance(self.p1, BaseModel)

    def test_created_at_exists(self):
        """should have created_at"""
        self.assertTrue(hasattr(self.p1, 'created_at'))

    def test_created_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.p1.created_at, datetime))

    def test_create_update_equal(self):
        """should have the same date and time"""
        self.assertEqual(self.p1.created_at, self.p1.updated_at)

    def test_created_not_equal1(self):
        """should have diferent date and time"""
        self.assertNotEqual(self.p1.created_at, self.p2.created_at)

    def test_create_update_not_equal2(self):
        """should have diferent date and time"""
        self.p1.updated_at = datetime.now()
        self.assertNotEqual(self.p1.created_at, self.p1.updated_at)

    def test_updated_at_exists(self):
        """should have updated_at"""
        self.assertTrue(hasattr(self.p1, 'updated_at'))

    def test_updated_at_datetime(self):
        """should be a datatype"""
        self.assertTrue(isinstance(self.p1.updated_at, datetime))

    def test_class_value_attrs(self):
        """testing value attrs"""
        self.assertEqual(Place.city_id, '')
        self.assertEqual(Place.user_id, '')
        self.assertEqual(Place.name, '')
        self.assertEqual(Place.description, '')
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

    def test_value_attrs(self):
        """testing value of attr"""
        self.assertEqual(self.p1.city_id, '')
        self.assertEqual(self.p1.user_id, '')
        self.assertEqual(self.p1.name, '')
        self.assertEqual(self.p1.description, '')
        self.assertEqual(self.p1.number_rooms, 0)
        self.assertEqual(self.p1.number_bathrooms, 0)
        self.assertEqual(self.p1.max_guest, 0)
        self.assertEqual(self.p1.price_by_night, 0)
        self.assertEqual(self.p1.latitude, 0.0)
        self.assertEqual(self.p1.longitude, 0.0)
        self.assertEqual(self.p1.amenity_ids, [])

    def test_input_dict(self):
        """testing set attr as dict"""
        attrs = {"id": "1"}
        self.p1 = Place(**attrs)
        self.assertEqual(attrs['id'], self.p1.id)

    def test_many_attrs(self):
        """Testing state_id"""
        n = [
            'city_id', 'user_id', 'name',
            'description', 'number_rooms', 'number_bathrooms',
            'max_guest', 'price_by_night', 'latitude', 'longitude',
            'amenity_ids'
            ]
        t = {
            '0': str, '1': str, '2': str,
            '3': str, '4': int, '5': int,
            '6': int, '7': int, '8': float,
            '9': float, '10': list
            }
        for k, v in enumerate(n):
            tmp = t[str(k)]
            if k >= 0 and k <= 3:
                tmp2 = ''
            elif k >= 4 and k <= 7:
                tmp2 = 0
            elif k == 8 or k == 9:
                tmp2 = 0.0
            else:
                tmp2 = []
            self.assertTrue(hasattr(self.p1, v))
            self.assertTrue(isinstance(eval('self.p1.'+v), tmp))
            self.assertEqual(eval('self.p1.'+v), tmp2)

    def test_to_dict(self):
        """ testing create and update """
        date_frmt = "%Y-%m-%dT%H:%M:%S.%f"
        d = self.p1.to_dict()
        self.assertEqual(d["created_at"],
                         self.p1.created_at.strftime(date_frmt))
        self.assertEqual(d["updated_at"],
                         self.p1.updated_at.strftime(date_frmt))
        self.assertEqual(d["__class__"], 'Place')
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)

    def test_str(self):
        """Testing string  of obj"""
        output = "[{}] ({}) {}".format(
            self.p1.__class__.__name__, self.p1.id, self.p1.__dict__)
        self.assertEqual(str(self.p1), output)

if __name__ == '__main__':
    unittest.main()
