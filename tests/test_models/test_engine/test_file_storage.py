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
        """testing all()"""
        fs2 = FileStorage()
        FileStorage._FileStorage__objects = {'k': 'j'}
        self.assertEqual(FileStorage._FileStorage__objects, fs2.all())

    def test_new(self):
        """testing new()"""
        bm1 = BaseModel()
        cn = bm1.__class__.__name__
        k = cn + '.' + str(bm1.id)
        s = FileStorage()
        s.new(bm1)
        self.assertIn(k, FileStorage._FileStorage__objects)

    def test_save(self):
        """testing save()"""
        bm1 = BaseModel()
        cn = bm1.__class__.__name__
        k = cn + '.' + str(bm1.id)
        s = FileStorage()
        s.new(bm1)
        s.save()
        with open('file.json') as file:
            self.assertTrue(isinstance(file.read(), str))

    def test_save2(self):
        """testing save() part 2"""
        bm1 = BaseModel()
        cn = bm1.__class__.__name__
        k = cn + '.' + str(bm1.id)
        s = FileStorage()
        s.new(bm1)
        s.save()
        with open('file.json') as file:
            self.assertIn(k, file.read())

    def test_reload(self):
        """testing reload"""
        bm1 = BaseModel()
        cn = bm1.__class__.__name__
        k = cn + '.' + str(bm1.id)
        s = FileStorage()
        s.new(bm1)
        s.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload2(self):
        """testing reald part 2"""
        FileStorage._FileStorage__objects = {}
        bm1 = BaseModel()
        cn = bm1.__class__.__name__
        k = cn + '.' + str(bm1.id)
        s = FileStorage()
        s.new(bm1)
        s.save()
        s.reload()
        self.assertIn(k, FileStorage._FileStorage__objects)

    def test_permissions_file(self):
        """Test File test_file_storage.py permissions"""

        test_file = os.access("models/engine/file_storage.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/engine/file_storage.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/engine/file_storage.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

if __name__ == '__main__':
    unittest.main()
