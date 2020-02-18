#!/usr/bin/python3
""" State class unittests file"""
import os
import unittest
import models
from models.state import State


class TestState(unittest.TestCase):
    """test class state"""

    def test_create(self):
        """know if i can create a instance"""
        self.s1 = State()

    def test_uuid(self):
        """know if id exist"""
        self.assertTrue(hasattr(self.s1, 'id'))
