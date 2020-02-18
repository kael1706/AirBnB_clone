#!/usr/bin/python3
""" State class unittests file"""
import os
import unittest
import models
from models.state import State

class TestState(unittest.TestCase):
    """pending"""

    def test_create(self):
        """pending"""
        self.s1 = State()

    def test_uuid(self):
        """know if id exist"""
        self.assertTrue(hasattr(self.s1, 'id'))

