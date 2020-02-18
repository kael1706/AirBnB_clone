#!/usr/bin/python3
"""FileStorage class unittests file"""
import os
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorageModel(unittest.TestCase):
    """FileStorage class unittests"""
    def test_is_an_instance(self):
        """check if my_class is an instance of BaseModel"""
        my_class = FileStorage()
        self.assertIsInstance(my_class, FileStorage)

    def test_insert_attr(self):
        """defining test suite"""
        FileStorage._FileStorage__file_path = 'file.json'
        FileStorage._FileStorage__objects = {}

    def test_file_path(self):
        """tests that file path exists"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    def test_file_obj(self):
        """test that file exists"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_file_path_value(self):
        """test that file has values"""
        self.assertEqual(FileStorage._FileStorage__file_path, 'file.json')

    def test_objects_value(self):
        """test that the objects had values"""
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_file_path_type(self):
        """test that the file path is a string"""
        self.assertTrue(isinstance(FileStorage._FileStorage__file_path, str))

    def test_objects_value(self):
        """test that the returned objects is a dictionary"""
        self.assertTrue(isinstance(FileStorage._FileStorage__objects, dict))

if __name__ == '__main__':
    unittest.main()
