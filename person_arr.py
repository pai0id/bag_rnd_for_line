from person import Person
from range import get_5_range

# Пример строки в файле сохранения:
# Поляков: 0, 5
# После двоеточия сохраняются начальные значения оставшихся в мешке диапазонов

def read_arr(file):
    """
    Reads a file containing a list of people and their initial bag contents.

    Args:
    file (file): The file object to read from.

    Returns:
    list: A list of Person objects, each with a name and a list of bag contents.

    Raises:
    Exception: If the file cannot be read or if the format of the file is incorrect.

    The format of the file is as follows:
    Each line contains a name and a bag content separated by a colon.
    The bag content is a comma-separated list of integers.
    If the bag content is not a valid list of integers, an empty list is used instead.
    """
    arr = []
    lst = file.readlines()
    for line in lst:
        name, bag = line.split(":")
        try:
            bag = [get_5_range(int(x)) for x in bag.split(",")]
        except Exception:
            bag = []
        arr.append(Person(name, bag))
    return arr

def write_arr(file, arr):
    for person in arr:
        person.print_person(file)

def reset_arr(arr):
    for p in arr:
        p.reset_bag()
    return arr
