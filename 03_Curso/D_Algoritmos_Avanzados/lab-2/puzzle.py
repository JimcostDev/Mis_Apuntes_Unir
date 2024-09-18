"""
This module solves the tile puzzle using the A* algorithm.
The tile puzzle is a game where you have n numbered tiles
and an empty space on an nxn grid. The goal is to rearrange
the tiles from an initial configuration to a goal configuration.
"""
import time
from heapq import heappop, heappush

class Puzzle:
    """Class representing the tile puzzle."""

    def __init__(self, state, goal, steps=None, cost=0, size=4):
        """
        Initializes an instance of the Puzzle class.

        Parameters:
        - state (list): The current puzzle configuration.
        - goal (list): The goal puzzle configuration.
        - steps (list, optional): List of states reached so far. Default is None.
        - cost (int, optional): The accumulated cost to reach the current state. Default is 0.
        - size (int): Side length of the puzzle (n x n).
        """
        self.state = state
        self.goal = goal
        self.steps = steps if steps is not None else [state]
        self.cost = cost
        self.size = size

    def is_goal(self):
        """
        Checks if the current state is the goal.

        Returns:
        bool: True if the current state is the goal, False otherwise.
        """
        return self.state == self.goal

    def generate_children(self):
        """
        Generates child states resulting from each action.

        Returns:
        list: List of Puzzle instances representing the child states.
        """
        empty_pos = self.state.index(0)
        size = self.size
        actions = [
            ('up', empty_pos - size),
            ('down', empty_pos + size),
            ('left', empty_pos - 1 if empty_pos % size != 0 else -1),
            ('right', empty_pos + 1 if empty_pos % size != size - 1 else -1)
        ]
        children = []
        for _, new_pos in actions:
            if 0 <= new_pos < len(self.state) and abs(new_pos % size - empty_pos % size) <= 1:
                new_state = self.state.copy()
                new_state[empty_pos], new_state[new_pos] = new_state[new_pos], new_state[empty_pos]
                new_steps = self.steps + [new_state]
                new_cost = self.cost + 1
                children.append(Puzzle(new_state, self.goal, new_steps, new_cost, size))
        return children

    def heuristic(self):
        """
        Calculates the heuristic using the Manhattan distance.

        Returns:
        int: The heuristic value.
        """
        size = self.size
        return sum(
            abs(i // size - self.state.index(i) // size) +
            abs(i % size - self.state.index(i) % size)
            for i in range(1, size * size)
        )

    def total_cost(self):
        """
        Calculates the total cost as the sum of the heuristic and the accumulated cost.

        Returns:
        int: The total cost.
        """
        return self.heuristic() + self.cost

    def __lt__(self, other):
        """
        Defines the less than (<) comparison between Puzzle instances.

        Parameters:
        - other (Puzzle): Another instance of Puzzle to compare.

        Returns:
        bool: True if the total cost of self is less than that of other, False otherwise.
        """
        return self.total_cost() < other.total_cost()


def count_inversions(lst):
    """
    Counts the number of inversions in the list.

    Parameters:
    - lst (list): List of numbers to count inversions.

    Returns:
    int: The number of inversions.
    """
    inversions = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j] and lst[i] != 0 and lst[j] != 0:
                inversions += 1
    return inversions

def is_solvable(initial_state, goal_state, size):
    """
    Checks if the goal configuration is reachable.

    Parameters:
    - initial_state (list): The initial puzzle configuration.
    - goal_state (list): The goal puzzle configuration.
    - size (int): Side length of the puzzle (n x n).

    Returns:
    bool: True if the goal configuration is reachable, False otherwise.
    str: Detailed reason if the configuration is not reachable.
    """
    initial_inversions = count_inversions(initial_state)
    goal_inversions = count_inversions(goal_state)
    empty_pos_initial = initial_state.index(0) // size
    empty_pos_goal = goal_state.index(0) // size

    if size % 2 == 1:
        solvable = initial_inversions % 2 == goal_inversions % 2
    else:
        solvable = (initial_inversions + empty_pos_initial) % 2 == (goal_inversions + empty_pos_goal) % 2

    if solvable:
        reason = "Both have the same parity in the sum of inversions and empty space position."
    else:
        if size % 2 == 1:
            reason = "Both have different parity in the sum of inversions."
        else:
            reason = "The sum of inversions and the empty space position have different parity."
    return solvable, reason


def solve_puzzle(initial_state, goal_state, size):
    """
    Solves the tile puzzle using the A* algorithm.

    Parameters:
    - initial_state (list): The initial puzzle configuration.
    - goal_state (list): The goal puzzle configuration.
    - size (int): Side length of the puzzle (n x n).

    Returns:
    str: Message indicating whether a solution was found or not.
    """
    solvable, reason = is_solvable(initial_state, goal_state, size)
    if not solvable:
        return f"The goal configuration is not reachable. Reason: {reason}"

    initial_puzzle = Puzzle(initial_state, goal_state, size=size)
    visited_states = set()
    nodes_to_explore = [initial_puzzle]
    start_time = time.time()

    while nodes_to_explore:
        current_node = heappop(nodes_to_explore)
        if current_node.is_goal():
            end_time = time.time()
            execution_time = end_time - start_time
            for step, arrangement in enumerate(current_node.steps):
                print(f"Step {step + 1}: {arrangement}")
            return f"Execution time: {execution_time} seconds"

        visited_states.add(tuple(current_node.state))
        children = current_node.generate_children()
        unvisited_children = [child for child in children if tuple(child.state) not in visited_states]

        for child in unvisited_children:
            heappush(nodes_to_explore, child)

    return "No solution found"


def get_user_input():
    """
    Gets the puzzle size and the initial and goal states from the user.

    Returns:
    tuple: Puzzle size, initial state, and goal state.
    """
    size = int(input("Enter the side length of the puzzle (e.g., 3 for a 3x3 puzzle): "))
    print(f"Enter the initial state of the puzzle ({size * size} numbers, separated by spaces, with 0 representing the empty space):")
    initial_state = list(map(int, input().split()))
    print(f"Enter the goal state of the puzzle ({size * size} numbers, separated by spaces, with 0 representing the empty space):")
    goal_state = list(map(int, input().split()))
    return size, initial_state, goal_state


if __name__ == "__main__":
    SIZE, INITIAL_STATE, GOAL_STATE = get_user_input()
    RESULT = solve_puzzle(INITIAL_STATE, GOAL_STATE, SIZE)
    print(RESULT)
