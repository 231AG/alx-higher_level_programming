#!/usr/bin/python3
"""
101-add_attribute to an object 
"""


def add_attribute(obj, objname, value):
    """
    add_attribute to object
    args:
        obj: object class 
        objname: name of object
        value: attribute's value
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
