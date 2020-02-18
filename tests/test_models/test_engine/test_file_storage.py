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
        fs1 = FileStorage()
        self.assertIsInstance(fs1, FileStorage)

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

     def test_all(self):
        """Test the all() method in class FileStorage"""
        fs2 = FileStorage()
        FileStorage._FileStorage__objects = {'k': 'j'}
        self.assertEqual(FileStorage._FileStorage__objects, fs2.all())

if __name__ == '__main__':
    unittest.main()
