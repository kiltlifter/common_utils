# -*- coding: utf-8 -*-
"""
Storage Format Conversion Class
"""

import math
import re

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class UnitConversion:
    """
    Class to convert between byte and human readable storage formats
    """
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    def __init__(self, binary: bool=True):
        self.nn = 1024 if binary else 1000

    @staticmethod
    def _separate(val: str) -> tuple:
        """
        Extract a float and unit type from a string
        :param val: str
        :return: tuple([float, str])
        """
        if not val:
            return tuple([0.00, 'b'])
        elif not len(val.split()) > 1:
            _ = re.search('([\d.]+)(.*)', val)
            if _:
                m = _.groups()
                return tuple([float(m[0]), m[1] if m[1] else 'b'])
        else:
            s = val.split()
            return tuple([float(s[0]), s[1]])

    def _convert_bytes(self, x_bytes: int) -> tuple:
        """
        Converts bytes to a tuple that is easier to read
        :param x_bytes: int
        :return: tuple([float, str])
        """
        if x_bytes:
            u = int(math.floor(math.log(x_bytes) / math.log(self.nn)))
            return tuple([x_bytes / math.pow(self.nn, u), self.units[u].lower()])
        else:
            return tuple([None, None])

    def _convert_string(self, value: float, unit: str) -> int:
        """
        Convert a tuple containing a human readable string representation to bytes
        :param value: float
        :param unit: str
        :return: int
        """
        try:
            x = self.units.index(unit.upper())
            return int(value * math.pow(self.nn, x))
        except ValueError as v:
            print('Unit not supported, {}: {}'.format(v.args[-1], ', '.join(self.units)))

    @classmethod
    def bytes_to_str(cls, x_bytes: int, binary: bool=True, precision: int=2) -> str:
        """
        Convert bytes integer to a human readable string.
        :param x_bytes: int
        :param binary: bool, True uses decimal representation (1024) False used base 10 (1000)
        :param precision: int, decimal precision
        :return: str
        """
        res = cls(binary)._convert_bytes(x_bytes)
        return '{}{}'.format(round(res[0], precision), res[1])

    @classmethod
    def str_to_bytes(cls, value: str, binary: bool=True) -> int:
        """
        Convert human readable string into an bytes integer
        :param value: str
        :param binary: bool, True uses decimal representation (1024) False used base 10 (1000)
        :return: int
        """
        s = cls._separate(value)
        return cls(binary)._convert_string(s[0], s[1])
