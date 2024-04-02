import random
from range import Range

class Person:
    """
    A class representing a person with a bag of ranges.

    Attributes:
        name (str): The name of the person.
        bag (list): A list of Range objects representing the ranges in the person's bag.

    Methods:
        __init__(self, name, bag): Initializes a new Person object with the given name and bag.
        get_name(self): Returns the name of the person.
        print_person(self, file): Writes the name and the current contents of the bag to the given file.
        get_num(self): Returns a random number from the bag, removes the range from the bag, and returns its random number.
        bag_is_empt(self): Returns True if the bag is empty, False otherwise.
        reset_bag(self): Resets the bag to its initial state with four ranges.
    """

    def __init__(self, name, bag):
        """
        Initializes a new Person object with the given name and bag.

        Args:
            name (str): The name of the person.
            bag (list): A list of Range objects representing the ranges in the person's bag.

        Returns:
            None
        """
        self.name = name
        self.bag = bag

    def get_name(self):
        """
        Returns the name of the person.

        Args:
            None

        Returns:
            str: The name of the person.
        """
        return self.name

    def print_person(self, file):
        """
        Writes the name and the current contents of the bag to the given file.

        Args:
            file (file): The file to write the person's information to.

        Returns:
            None
        """
        file.write(f"{self.name}: ")
        begs = [str(rng.get_beg()) for rng in self.bag]
        sep = ", "
        file.write(sep.join(begs))
        file.write("\n")

    def get_num(self):
        """
        Returns a random number from the bag, removes the range from the bag, and returns its random number.

        Args:
            None

        Returns:
            int: A random number from the bag.
        """
        choice = random.choice(self.bag)
        self.bag.remove(choice)
        return choice.get_rand()

    def bag_is_empt(self):
        """
        Returns True if the bag is empty, False otherwise.

        Args:
            None

        Returns:
            bool: True if the bag is empty, False otherwise.
        """
        return not self.bag

    def reset_bag(self):
        """
        Resets the bag to its initial state with four ranges.

        Args:
            None

        Returns:
            None
        """
        self.bag = []
        self.bag.append(Range(0, 5))
        self.bag.append(Range(5, 10))
        self.bag.append(Range(10, 15))
        self.bag.append(Range(15, 20))
