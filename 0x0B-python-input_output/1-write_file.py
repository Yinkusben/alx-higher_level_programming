#!/usr/bin/python3
""" A function that writes a string to a text file (UTF8) and returns the number of characters written """

def write_file(filename="", text=""):
    """ Write text to filename and return the number of characters written
    Args:
        filename (str): The name of the file to write
        text (str): The text to write
    Returns:
        The no. of character written
    """

    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)
    return num
