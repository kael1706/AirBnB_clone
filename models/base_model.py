#!/usr/bin/python3
import uuid
from datetime import datetime

"""
this is the module base_module.py
"""
class BaseModel():
    """Base Model class"""

    def __init__(self):
        """
        pending
        """
        self.id = str(uuid.uuid4());
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

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
        self.updated_at = datetime.today()

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

my_model = BaseModel()
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
