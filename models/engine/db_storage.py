#!/usr/bin/python3

from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    __engine = None
    __session = None

    _classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


    def __init__(self):
        self._classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

        """Create the engine and configure the session for the MySQL database."""
        db_user = getenv('HBNB_MYSQL_USER')
        db_pwd = getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST', default='localhost')
        db_name = getenv('HBNB_MYSQL_DB')

        connection_str = f'mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db_name}'
        self.__engine = create_engine(connection_str, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        """
        Query all objects from the current database session.
        """
        from models import storage
        #classes = ['User', 'State', 'City', 'Amenity',
         #          'Place', 'Review']
        result = {}

        if cls is not None:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = f'{cls.__name__}.{obj.id}'
                result[key] = obj
        else:
            for cls_name in _classes:
                if cls_name in storage._classes:
                    query_result = self.__session.query(
                            storage._classes[cls_name]).all()
                    for obj in query_result:
                        key = f'{storage._classes[cls_name].__name__}.{obj.id}'
                        result[key] = obj

        return result

    def new(self, obj):
        """
        Add the object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from the current database session if not None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and the current database session.
        """
        from models.base_model import BaseModel
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
            expire_on_commit=False))
        self.__session = Session()
