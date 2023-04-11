#!/usr/bin/python3
""" A function that checks if an object is exactly an instance of the specified class """

def is_same_class(obj, a_class):
    """ It returns True is obj is of type 'a_class'

    Args:
        obj: The object
        a_class: The class name

    Return: True or False
    """
    
    return type(obj) == a_class
