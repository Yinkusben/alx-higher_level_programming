#!/usr/bin/python3
""" Write a function that writes an Object to a text file, using a JSON representation """

import json

def save_to_json_file(my_obj, filename):
    """ We convert the python object to Json object and write it to the file "filensme"
    Args:
        my_obj (obj): The object to write
        filename (str): The file to write to
    """

    my_obj_json = json.dumps(my_obj)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(my_obj_json)
