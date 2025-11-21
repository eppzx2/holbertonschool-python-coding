#!/usr/bin/python3
"""
this project is about writing if conditions and raise an exception inside of class
"""


class Square:
    """
    This class is square class and it has own exceptions
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
