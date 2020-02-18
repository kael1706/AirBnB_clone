#!/usr/bin/python3
""" Place class unittests file"""
import os
import unittest
import models
from models.place import Place


class TestPlace(unittest.TestCase):
    """test class Place"""

    def test_create(self):
        """know if i can create a instance"""
        self.p1 = Place()

    def test_uuid(self):
        """know if id exist"""
        self.assertTrue(hasattr(self.p1, 'id'))
