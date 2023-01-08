from puzzle import *
from node import *


def choose_heuristic() -> str:
    """
    Gets the user to select either the Manhattan or Hamming Distance heuristic.
    Returns:
        The type of heuristic to use for solving the 8-puzzle problem along with the stats of the heuristic chosen.
    """
    heuristic_input = ""
    while heuristic_input not in ("m", "h"):
        heuristic_input = input(
            "\nThe Manhattan Distance heuristic is based on number of squares "
            "between itself and the goal position, whereas the Hamming "
            "Distance heuristic is based on total number of misplaced tiles.\n"
            "Would you like to use the Manhattan Distance heuristic (m) or "
            "the Hamming Distance heuristic (h)?\n").lower()
        if heuristic_input not in ("m", "h"):
            print("Invalid input! Please enter 'm' for the Manhattan Distance "
                  "heuristic, or 'h' for the Hamming Distance heuristic.")
        elif heuristic_input == "m":
            puzzles = initiatepuzzles()
            stats = []
            for x in puzzles:
                stats.append(manhattanheuristic(x))
                print(puzzles.index(x), end=" ")
                if puzzles.index(x) == 99:
                    print()
                    printFinishedStats(stats)
            return "Manhattan"
        else:
            puzzles = initiatepuzzles()
            stats = []
            for x in puzzles:
                stats.append(hammingheuristic(x))
                print(puzzles.index(x), end=" ")
                if puzzles.index(x) == 99:
                    print()
                    printFinishedStats(stats)
            return "Hamming"


def printFinishedStats(stats):
    """
    This method is printFinishedStats that takes in one parameter called stats. The function
    calculates some statistics based on the data in stats and prints the results to the console.
    """
    expansions_sum = 0
    time_sum = 0
    for x in stats:
        expansions_sum += x.expansions
        time_sum += x.time
    print(f"Number of expanded nodes: {expansions_sum}")
    print(f"Computation Time: {round(time_sum, 3)}")


if __name__ == '__main__':
    choose_heuristic()
