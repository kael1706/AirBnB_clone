#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage():
    """
    pending
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        pending
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        pending
        """
        k = obj.__class__.__name__ + '.' + str(obj.id)
        self.__objects[k] = obj

    def save(self):
        """
        pending
        """
        d = {}
        for k, v in self.__objects.items():
            d[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """
        pending
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                for k, v in (json.load(f)).items():
                    v = eval(v['__class__'])(**(v))
                    self.__objects[k] = v
        except Exception:
            pass
