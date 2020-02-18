#!/usr/bin/python3
"""FileStorage class unittests file"""
import os
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorageModel(unittest.TestCase):
    """pending"""
    def test_is_an_instance(self):
        """check if my_class is an instance of BaseModel"""
        my_class = FileStorage()
        self.assertIsInstance(my_class, FileStorage)

    def test_insert_attr(self):
        """pending"""
        FileStorage._FileStorage__file_path = 'file.json'
        FileStorage._FileStorage__objects = {}

    def test_file_path(self):
        """pending"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    def test_file_obj(self):
        """pending"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

if __name__ == '__main__':
    unittest.main()
