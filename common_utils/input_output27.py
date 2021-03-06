# -*- coding: utf-8 -*-
"""
General input/output helpers
"""

import pickle
import json

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class FileUtil:
    """
    Class of file manipulation utilities
    """

    @staticmethod
    def pickle_obj(obj, filename):
        """
        Pickles a python object as the provided filename
        :param obj: object
        :param filename: object
        :return: None
        """
        with open(filename, 'wb') as f:
            pickle.dump(obj, f)

    @staticmethod
    def unpickle_obj(filename):
        """
        Returns an unpickled object
        :param filename: str
        :return: object
        """
        with open(filename, 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def write_file(data, filename, mode='w'):
        """
        Writes string or bytes to a file, depending on the mode provided
        :param data: str or bytes
        :param filename: str
        :param mode: str
        :return: None
        """
        with open(filename, mode) as f:
            f.write(data)

    @staticmethod
    def read_file(filename, mode='r'):
        """
        Reads a filename as str or bytes based on mode specified
        :param filename: str
        :param mode: str
        :return: object
        """
        with open(filename, mode) as f:
            return f.read()

    @staticmethod
    def json_loads(str_val):
        """
        Loads str, bytes or bytearray instance containing a JSON document and returns a python object
        :param str_val: str, bytes, bytearray
        :return: object
        """
        return json.loads(str_val)

    @staticmethod
    def json_dumps(obj_val):
        """
        Dumps a python object to a json string
        :param obj_val:
        :return: str
        """
        return json.dumps(obj_val)



