#!/usr/bin/python3
""" A function that returns an object (Python data structure) represented by a JSON string """

import json

def from_json_string(my_str):
    """ W use the loads() function and  return the deserialized python object of my_str
    Args:
        my_str (str): The json object to deserialize
    Returns:
         python objext
    """

    return json.loads(my_str)
