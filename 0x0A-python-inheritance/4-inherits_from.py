#!/usr/bin/python3
""" A function that checks is an object is an instance if a class that inherited directly or indirectly from the specified class """

def inherits_from(obj, a_class):
    """ Returns true if object is an instance of a class that inherited (directly or indirectly) fron a_class
    Args:
        obj: The object
        a_class: The specified class
    Retutns:
        True or false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
