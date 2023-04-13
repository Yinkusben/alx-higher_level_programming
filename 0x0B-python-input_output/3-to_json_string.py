#!/usr/bin/python3
""" Write a function that returns the JSON representation of an object (string)"""

import json

def to_json_string(my_obj):
    """ We use the json.dump() to serialize the python objext
    Args:
        my_obj (obj): The python object to serialize
    Returns:
        The json object
    """
    return json.dumps(my_obj)
