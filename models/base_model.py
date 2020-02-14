#!/usr/bin/python3
import uuid
from datetime import datetime

"""
this is the module base_module.py
"""
class BaseModel():
    """Base Model class"""

    def __init__(self, *args, **kwargs):
        """
        pending
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
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Instance method that returns an “informal”
        and nicely printable string representation
        of an instance.
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        pending
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        pending
        """
        d = {}
        d['__class__'] = self.__class__.__name__
        if self.__dict__:
            for k, v in self.__dict__.items():
                if isinstance(v, datetime) is True:
                    v = v.isoformat()
                d[k] = v
        return d
