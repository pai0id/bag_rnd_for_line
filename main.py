"""
Module for reading, writing, and resetting a list of Person objects.

This module provides functions for reading, writing, and resetting a list of Person objects.

Functions:
read_arr(file) - Reads a list of Person objects from a file.
write_arr(file, arr) - Writes a list of Person objects to a file.
reset_arr(arr) - Resets a list of Person objects to its original state.
"""

from random import shuffle
import subprocess

def read_arr(file):
    """
    Reads a list of Person objects from a file.

    Args:
        file (file): The file object to read from.

    Returns:
        list: A list of Person objects.

    Raises:
        ValueError: If the file does not contain valid Person objects.
    """
    # Open the file and read the data
    try:
        f = open(file, "r")
    except Exception as e:
        raise ValueError("Error opening file: " + str(e))

    data = f.read()

    # Close the file
    f.close()

    # Convert the data to a list of Person objects
    try:
        arr = eval(data)
    except Exception as e:
        raise ValueError("Error reading data: " + str(e))

    # Check that the data is valid
    if not isinstance(arr, list) or not all(isinstance(x, Person) for x in arr):
        raise ValueError("Invalid data in file")

    return arr

def write_arr(file, arr):
    """
    Writes a list of Person objects to a file.

    Args:
        file (file): The file object to write to.
        arr (list): The list of Person objects to write.

    Raises:
        ValueError: If the file cannot be written.
    """
    # Convert the list to a string
    data = str(arr)

    # Open the file for writing and write the data
    try:
        f = open(file, "w")
    except Exception as e:
        raise ValueError("Error opening file for writing: " + str(e))

    try:
        f.write(data)
    except Exception as e:
        raise ValueError("Error writing to file: " + str(e))

    # Close the file
    f.close()

def reset_arr(arr):
    """
    Resets a list of Person objects to its original state.

    Args:
        arr (list): The list of Person objects to reset.

    Returns:
        list: The reset list of Person objects.
    """
    # Shuffle the list and return it
    shuffle(arr)
    return arr