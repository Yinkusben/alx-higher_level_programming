#!/usr/bin/python3
""" A function that checks if an object is an instance of, or an instance of a class that inherited from the specified class """

def is_kind_of_class(obj, a_class):
    """ Returns True if obj is an instance of "a_class" or it sub class
    Args:
        obj: The object
        a_class: The class

    Returns:
        True or False
    """
    return isinstance(obj, a_class)
