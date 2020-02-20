#!/usr/bin/python3
"""
FileStorage class module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage():
    """
    FileStorage class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        show all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        create a new object
        """
        k = obj.__class__.__name__ + '.' + str(obj.id)
        self.__objects[k] = obj

    def save(self):
        """
        save the new object in to json file
        """
        d = {}
        for k, v in self.__objects.items():
            d[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """
        reload objects from json file
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                for k, v in (json.load(f)).items():
                    v = eval(v['__class__'])(**(v))
                    self.__objects[k] = v
        except Exception:
            pass
