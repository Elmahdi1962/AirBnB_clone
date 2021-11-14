#!/usr/bin/python3
''' module for FileStorage class '''
import json
from os.path import isfile
import models


class FileStorage:
    ''' class for persistent storage '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' gets all objects '''
        return self.__class__.__objects

    def new(self, obj):
        ''' registers a new object '''
        self.__class__.__objects['{}.{}'.format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        ''' saves all objects to a file '''
        with open(self.__class__.__file_path, 'w') as file:
            r_objs = self.__class__.__objects
            objs = {k: r_objs[k].to_dict() for k in r_objs}
            json.dump(objs, file)

    def reload(self):
        ''' load objects from a file '''
        clss = models.models
        if isfile(self.__class__.__file_path):
            with open(self.__class__.__file_path, 'r') as file:
                js_objs = json.load(file)
                type(self).__objects = {k: clss[v['__class__']](**v)
                                        for k, v in js_objs.items()}
