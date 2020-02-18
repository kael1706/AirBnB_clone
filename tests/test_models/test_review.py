#!/usr/bin/python3
""" Review class unittests file"""
import os
import unittest
import models
from models.review import Review


class TestReview(unittest.TestCase):
    """test class Review"""

    def test_create(self):
        """know if i can create a instance"""
        self.r1 = Review()

    def test_uuid(self):
        """know if id exist"""
        self.assertTrue(hasattr(self.r1, 'id'))
