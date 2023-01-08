import math


def calcHamming(puzzle):
    """
    This code defines a function that calculates the Hamming distance between an initial list and the goal list
    The Hamming distance is the number of positions at which the two lists differ.
    The function does this by iterating through the elements of the two lists, comparing them position by position,
    and incrementing a count for each position at which the elements are not equal.
    The function then returns the final count, which is the Hamming distance.
    """
    return sum(x != y for x, y in zip(puzzle, range(9)))


def calcManhattan(puzzle):
    """
    This code defines a function that calculates the Manhattan distance between an initial state and goal state.
    The Manhattan distance is the sum of the absolute differences of the indices of the two lists. The
    function uses another function called calc_distance to calculate the distance between a single element and its
    corresponding element in the other list. This function calculates the indices of the elements and returns the sum of
    the absolute differences between these indices. The function then iterates through the elements of the two lists and
    calculates the distance between each element and its corresponding element in the other list. If an element in the
    given list is equal to 0, it is skipped. Finally, the function returns the sum of all the distances, which is the
    Manhattan distance between the two lists.
    """

    def calc_distance(x, y):
        row = math.floor(x / 3)
        column = x % 3
        actualRow = math.floor(y / 3)
        actualColumn = y % 3
        return abs(actualRow - row) + abs(actualColumn - column)

    return sum([calc_distance(i, puzzle[i]) for i in range(9) if puzzle[i] != 0])


class Manhattan:
    """
    This is the class called Manhattan. The class has four attributes: puzzle, manDis, generation, and fscore. These
    attributes are stored using the __slots__ mechanism, which is a way to optimize the memory usage of the class by
    using a fixed set of slots for the attributes instead of a dictionary. The class has an __init__ method,
    which is a special method in Python classes that is called when an object of the class is created. The __init__
    method takes four arguments: puzzle, manDis, generation, and fscore. These arguments are used to initialize the
    attributes of the object. These attributes are used later in other methods to solve 8-puzzle using Manhattan
    Heuristic.
    """
    __slots__ = ['puzzle', 'manDis', 'children', 'fscore']

    def __init__(self, puzzle, manDis, children, fscore):
        self.puzzle = puzzle
        self.manDis = manDis
        self.children = children
        self.fscore = fscore


class Hamming:
    """
    This is the class called Hamming. The __init__ method takes four arguments: puzzle, hamDis, generation,
    and fscore. These arguments are used to initialize the attributes of the object. These attributes are used later
    in other methods to solve the 8 puzzle using Hamming Heuristic.
    """
    __slots__ = ['puzzle', 'hamDis', 'children', 'fscore']

    def __init__(self, puzzle, hamDis, children, fscore):
        self.puzzle = puzzle
        self.hamDis = hamDis
        self.children = children
        self.fscore = fscore


class comparisionofheuristic:
    """
    This is the class called comparisionofheuristic.
    The class has two attributes: expansions and time. We used these attributes to compare the expanded nodes
    and computation time between the two heuristic.
    """
    __slots__ = ['expansions', 'time']

    def __init__(self, expansions, time):
        self.expansions = expansions
        self.time = time
