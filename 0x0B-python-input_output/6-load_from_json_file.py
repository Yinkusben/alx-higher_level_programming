#!/usr/bin/python3
""" A function that creates an Object from a “JSON file """

import json

def load_from_json_file(filename):
    """ Open the filw and deserialize using load() funcrion
    """
    with open(filename, 'r' encoding='utf-8') as f:
        return json.load(filename)
