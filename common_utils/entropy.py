# -*- coding: utf-8 -*-
"""
Utilities that use entropy as an input
"""

import random
from time import sleep

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class SleepUtil:
    @staticmethod
    def random_int(max_int: int=12) -> int:
        """
        Returns a random int between zero and max_int
        :param max_int: int
        :return: int
        """
        return random.choice(range(1, max_int))

    @classmethod
    def random_sleep(cls, max_int: int=15) -> None:
        """
        Sleeps for a random duration between zero and max_int
        :param max_int: int
        :return: None
        """
        sleep(cls.random_int(max_int))

    @staticmethod
    def sleep(seconds: int):
        """
        Sleeps for input duration
        :param seconds: int
        :return: None
        """
        sleep(seconds)
