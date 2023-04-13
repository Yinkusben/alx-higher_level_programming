#!/usr/bin/python3
""" A function that appends a string at the end of a text file (UTF8) and returns the number of characters added"""
def append_write(filename="", text=""):
    """ Opens a file in append mode and append text to it
    Args:
        filename (str): The name of the file to write to
        text (str): The string to write to the file
    Returns:
        The number of characters appended
    """

    with open(filename, 'a', encoding='utf-8') as f:
        num = f.write(text)
    return num
