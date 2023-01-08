import random


def createPuzzle():
    """
    This method is used to create the 8 puzzle and generate puzzles with numbers randomly. Inside the loop, the function
    uses the ramdom.sample function to choose numbers randomly and the numbers are appended into a list.
     """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    numbers_arrangement = []
    while numbers:
        temp_number = random.sample(numbers, 1)[0]
        numbers.remove(temp_number)
        numbers_arrangement.append(temp_number)
    return numbers_arrangement


def solvecheck(Puzzle):
    """
    This method is there to check the solvability of the puzzles
    before they are attempted to be solved by the heuristics.
    """
    inverse = sum([1 for i in range(9) for j in range(i + 1, 9)
                   if Puzzle[i] != 0 and Puzzle[j] != 0 and Puzzle[i] > Puzzle[j]])
    return inverse % 2 == 0


def initiatepuzzles():
    """
       This code defines a function called initiatepuzzles that generates a list of 100 random puzzle configurations and
       checks if the puzzle are solvable, before the puzzle is added to the list, to get solved. Once the list reaches
       the length of a 100, the loops breaks and the list with 100 random puzzles is generated.
    """
    openlist = []
    while True:
        temp_array = createPuzzle()
        if solvecheck(temp_array) and temp_array not in openlist:
            openlist.append(temp_array)
        if len(openlist) == 100:
            break
    return openlist
