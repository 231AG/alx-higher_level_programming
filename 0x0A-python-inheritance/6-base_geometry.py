#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """ class with public attribute area"""
    def area(self):
        """raise exception when called"""
        raise Exception("area() is not implemented")
