#!/usr/bin/python3
"""
101-add_attribute Module
"""


def add_attribute(obj, objname, value):
    """
    add_attribute to an object
    args:
        obj: class object
        objname: object name
        value: value of attribute
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
