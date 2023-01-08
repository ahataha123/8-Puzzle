import copy
import time

from heuristic import *


def hammingheuristic(puzzle):
    """
    This code defines a function called hammingheuristic that takes in one parameter called puzzle. The function uses
    the Hamming heuristic to try to solve the puzzle represented by the puzzle list. The function also starts a timer
    using the time module.The function calculates the elapsed time using the timer and passes this time and the
    number of expansions to another function called comparisonofheuristic, which calculates some statistics based on
    these values. The hammingheuristic function then returns the output of the comparisonofheuristic function.
    """
    start_state = Hamming(puzzle, calcHamming(puzzle), 0, calcHamming(puzzle))
    expansions = [start_state]
    open_nodes = [start_state]
    start = time.time()
    flag = True
    while flag:
        if expandNode(expansions, open_nodes, "hamming"):
            flag = False
    end = time.time()
    finished_time = end - start
    return comparisionofheuristic(len(expansions), finished_time)

def manhattanheuristic(puzzle):
    """
    This code defines a function called manhattanheuristic that takes in one parameter called puzzle. The function uses
    the Manhattan heuristic to try to solve the puzzle represented by the puzzle list. The function also starts a timer
    using the time module.The function calculates the elapsed time using the timer and passes this time and the
    number of expansions to another function called comparisonofheuristic, which calculates some statistics based on
    these values. The manhattanheuristic function then returns the output of the comparisonofheuristic function.
    """

    start_state = Manhattan(puzzle, calcManhattan(puzzle), 0, calcManhattan(puzzle))
    expansions = [start_state]
    open = [start_state]
    start = time.time()
    while True:
        if expandNode(expansions, open, "manhattan"):
            break
    end = time.time()
    finished_time = end - start
    return comparisionofheuristic(len(expansions), finished_time)

def addNewNode(expansions, open, children, puzzle, algorithm):
    """
    This code defines a function called addNewNode that takes five arguments: expansions, open, children, puzzle,
    and algorithm. The function appears to be used to add a new element to a list of expansions and a list of open
    nodes in some sort of search algorithm.The function starts by using an if statement to determine which of two
    possible classes (Manhattan or Hamming) to create an instance of. It does this based on the value of the
    algorithm argument. The function then initializes a variable called new_state to an instance of the chosen class,
    passing it the values of puzzle, man_dis or ham_dis, children + 1, and man_dis + children or ham_dis +
    children as arguments. The function then calls the Repeat function and passes it the expansions and puzzle
    arguments. If Repeat returns True, the function returns False. Otherwise, it appends new_state to both the
    expansions and open lists and returns True if the manDis attribute of new_state is equal to 0 (if algorithm is
    "manhattan") or the hamDis attribute of new_state is equal
    """
    if algorithm == "manhattan":
        man_dis = calcManhattan(puzzle)
        new_state = Manhattan(puzzle, man_dis, children + 1, man_dis + children)
    else:
        ham_dis = calcHamming(puzzle)
        new_state = Hamming(puzzle, ham_dis, children + 1, ham_dis + children)

    if Repeat(expansions, puzzle):
        return False
    expansions.append(new_state)
    open.append(new_state)
    return new_state.manDis == 0 \
        if algorithm == "manhattan" \
        else new_state.hamDis == 0

def Repeat(expansions, puzzle):
    """
    This function is to check if there are any repetitons of puzzles and takes them out of the list.
    """
    return any(x.puzzle == puzzle for x in expansions)

def expandNode(expansions, open, algorithm):
    """
    This code defines a function called expand that takes three arguments: expansions, open, and algorithm. The
    function appears to be implementing some sort of search algorithm, possibly related to finding a solution to the
    8-puzzle game. The function starts by initializing the variables fscore, index, puzzle, blank_index, row,
    and column to certain values. It then enters a loop that iterates over the elements in the open list. Within the
    loop, the function checks if the fscore is greater than the fscore attribute of the current element, and if so,
    it updates the value of fscore and index. After the loop, the function sets the value of puzzle to the puzzle
    attribute of the element at index. index in the open list. It also calculates the values of blank_index, row,
    and column based on the value of puzzle.The function then enters a series of if statements that check the values
    of row and column and perform certain actions based on those values. These actions involve creating a deep copy
    of puzzle, modifying the copy in some way, and then passing the copy to a function called addNewNode along with
    the other arguments. If addNewNode returns True, the function immediately returns True. The function then removes
    the element at index. index from the open list and enters another loop that iterates over the elements in open. If
    the element has a children attribute equal to children - 1, it is removed from the open list.Finally,
    the function returns None.
    """
    fscore = 9999999
    index = 0
    for x in open:
        if fscore > x.fscore:
            fscore = x.fscore
            index = open.index(x)

    puzzle = open[index].puzzle
    blank_index = puzzle.index(0)
    row = math.floor(blank_index / 3)
    column = blank_index % 3
    children = open[index].children

    if row == 0 or row == 1:
        puzzle_down = copy.deepcopy(puzzle)
        puzzle_down[blank_index] = puzzle_down[blank_index + 3]
        puzzle_down[blank_index + 3] = 0
        if addNewNode(expansions, open, children, puzzle_down, algorithm):
            return True

    if row == 2 or row == 1:
        puzzle_down = copy.deepcopy(puzzle)
        puzzle_down[blank_index] = puzzle_down[blank_index - 3]
        puzzle_down[blank_index - 3] = 0
        if addNewNode(expansions, open, children, puzzle_down, algorithm):
            return True

    if column == 2 or column == 1:
        puzzle_down = copy.deepcopy(puzzle)
        puzzle_down[blank_index] = puzzle_down[blank_index - 1]
        puzzle_down[blank_index - 1] = 0
        if addNewNode(expansions, open, children, puzzle_down, algorithm):
            return True

    if column == 0 or column == 1:
        puzzle_down = copy.deepcopy(puzzle)
        puzzle_down[blank_index] = puzzle_down[blank_index + 1]
        puzzle_down[blank_index + 1] = 0
        if addNewNode(expansions, open, children, puzzle_down, algorithm):
            return True

    open.remove(open[index])

    for x in open:
        if x.children == children - 1:
            open.remove(x)
