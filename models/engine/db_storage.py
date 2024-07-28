#!/usr/bin/python3
"""create a mysql engine"""

import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """creating an engine for a mysql database storage system"""

    all_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
    __engine = None
    __session = None

    def __init__(self):
        """Instatiate the engine and drop if test database"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.environ['HBNB_MYSQL_USER'],
            os.environ['HBNB_MYSQL_PWD'],
            os.environ['HBNB_MYSQL_HOST'],
            os.environ['HBNB_MYSQL_DB']), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects for curent session based on class name"""
        obj_dict = {}
        cls = self.all_classes[cls]
        if cls is not None:
            objects = self.__session.query(cls).all()
        else:
            objects = self.__session.query(
                State, City, User, Amenity, Place, Review)
        for obj in objects:
            key = obj.__class__.__name__ + '.' + obj.id
            value = obj
            obj_dict[key] = value
        return obj_dict
