# -*- coding: utf-8 -*-
"""
General encoding utilities
"""

from base64 import b64encode, b64decode

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class Base64Util:
    @staticmethod
    def base64_encode_str(str_val: str) -> str:
        """
        Base 64 encode an input str
        :param str_val: str
        :return: str
        """
        return b64encode(str_val.encode('utf-8')).decode('utf-8')

    @staticmethod
    def base64_decode_str(str_val: str) -> str:
        """
        Base 64 decode and input str
        :param str_val: str
        :return: str
        """
        return b64decode(str_val.encode('utf-8')).decode('utf-8')
