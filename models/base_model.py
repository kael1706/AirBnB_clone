#!/usr/bin/python3
"""
this is the module base_module.py
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """Base Model class"""

    def __init__(self, *args, **kwargs):
        """
        initialize class BaseModel
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != '__class__':
                    setattr(self, k, v)

        try:
            self.id
        except Exception:
            self.id = str(uuid.uuid4())
        try:
            self.created_at
        except Exception:
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        method that returns printable string representation
        of an instance.
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        save in FileStorage
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        object to dictionary
        """
        d = {}
        d['__class__'] = self.__class__.__name__
        if self.__dict__:
            for k, v in self.__dict__.items():
                if isinstance(v, datetime) is True:
                    v = v.isoformat()
                d[k] = v
        return d
