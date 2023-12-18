#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """"
        This defines common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
            Initialize BaseModel instance.
        """
        if kwargs:
            """
                if kwargs is not empty set attributes from kwargs
            """
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                    if key in ["created_at", "updated_at"]:
                        """
                            convert created_at and updated_at to datetime
                        """
                        val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, val)
        else:
            """
               if kwargs is empty generate the foll
            """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            """
                Set update_at with the value of created_at
            """
            self.updated_at = datetime.now()
            """
            if it’s a new instance (not from a dictionary representation)
            add a call to the method new(self) on storage
            """
            storage.new(self)

    def __str__(self):
        """
            Print [<class name>] (<self.id>) <self.__dict__> to the screen
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at to the current datetime
        """
        self.updated_at = datetime.now()
        """ call save(self) method of storage """
        storage.save()

    def to_dict(self):
        """
        Return dictionary representation of BaseModel class.
        """
        sel_dict = dict(self.__dict__)
        sel_dict["__class__"] = type(self).__name__
        sel_dict["created_at"] = sel_dict["created_at"].isoformat()
        sel_dict["updated_at"] = sel_dict["updated_at"].isoformat()

        return sel_dict
