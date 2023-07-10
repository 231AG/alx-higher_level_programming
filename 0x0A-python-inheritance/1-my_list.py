#!/usr/bin/python3
"""
contains MyList class
"""


class MyList(list):
    """A subclass of Mylist"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
