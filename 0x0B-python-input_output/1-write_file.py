#!/usr/bin/python3
"""
contain function that writes text and 
returns number chars written
"""

def write_file(filename="", text=""):
    """
    Writes text given into a file `filename`.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        if text and type(text) is str:
            return f.write(text)
