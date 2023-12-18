#!/usr/bin/python3

import json
import models
from collections import OrderedDict


class FileStorage:
    """
    a class taht serializes and deserializes instances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
         Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        serializes_objects = {}
        for key, obj in self.__objects.items():
            serializes_objects[key] = obj.to_dict()
        json_str = json.dumps(serializes_objects)

        with open(self.__file_path, "w", encoding='utf-8') as file:
            file.write(json_str)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        from models.review import Review
        from models.place import Place
        from models.amenity import Amenity
        from models.city import City
        from models.state import State
        from models.user import User
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_objects = json.load(file)
                for obj in loaded_objects.values():
                    class_name = obj["__class__"]
                    self.new(eval("{}({})".format(class_name, "**obj")))
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    main()
