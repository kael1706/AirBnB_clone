#!/usr/bin/python3
""" User class unittests file"""
import os
import unittest
import models
from models.user import User


class TestUser(unittest.TestCase):
    """class User"""

    def test_create_user(self):
        """pending"""
        self.u1 = User()
        User.email = ''
        User.password = ''
        User.first_name = ''
        User.last_name = ''

    def test_uuid(self):
        """pending"""
        self.assertTrue(hasattr(self.u1, 'id'))
