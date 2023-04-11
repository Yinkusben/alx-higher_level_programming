#!/usr/bin/python3
""" A function that returns the list of available attributes and methods of an object """

def lookup(obj):
    """ We use the dir() funcrion to return the list of built in and user defines attributes and methods of the objecrs

    Args:
        obj: The object whose attr and method is to be returned
    Returns:
        a list of returned attributes and methods
    """

    return dir(obj)
