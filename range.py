import random

"""
A class to represent a range of numbers.
"""

import random

def get_5_range(beg):
    """
    Returns a Range object with the beginning of the range set to the input 'beg' and the end of the range set to 'beg + 5'.

    Args:
    beg (int): The beginning of the range.

    Returns:
    Range: A Range object with the specified beginning and end.
    """
    return Range(beg, beg + 5)

class Range:
    """
    A class to represent a range of numbers.

    Attributes:
    beg (int): The beginning of the range.
    end (int): The end of the range.

    Methods:
    get_rand(): Returns a random integer within the range.
    get_beg(): Returns the beginning of the range.
    """

    def __init__(self, beg, end):
        """
        Initializes a Range object with the specified beginning and end.

        Args:
        beg (int): The beginning of the range.
        end (int): The end of the range.
        """
        self.beg = beg
        self.end = end

    def get_rand(self):
        """
        Returns a random integer within the range.

        Returns:
        int: A random integer within the range.
        """
        return random.choice(range(self.beg, self.end))

    def get_beg(self):
        """
        Returns the beginning of the range.

        Returns:
        int: The beginning of the range.
        """
        return self.beg
