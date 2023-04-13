#!/usr/bin/python3
""" A Write a function that reads a text file (UTF8) and prints it to stdout """

def read_file(filename=""):
    """ We read the file filename and prints its content
    Args:
        filename (str): The name of the file to open
    Returns:
        Nothing
    """

    with open(filename, "r", encoding="utf-8") as myfile:
        print(myfile.read())
