#!/usr/bin/python3
""" Amenity class unittests file"""
import os
import unittest
import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test class Amenity"""

    def test_create(self):
        """know if i can create a instance"""
        self.a1 = Amenity()

    def test_uuid(self):
        """know if id exist"""
        self.assertTrue(hasattr(self.a1, 'id'))
