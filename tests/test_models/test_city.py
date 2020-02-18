#!/usr/bin/python3
""" City class unittests file"""
import os
import unittest
import models
from models.city import City


class TestCity(unittest.TestCase):
    """test class City"""

    def test_create(self):
        """know if i can create a instance"""
        self.c1 = City()

    def test_uuid(self):
        """know if id exist"""
        self.assertTrue(hasattr(self.c1, 'id'))
