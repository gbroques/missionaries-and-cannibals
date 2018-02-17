"""
Iterative deepening and depth limited search.

Source:
https://github.com/aimacode/aima-python/blob/master/search.py
"""

import sys

from search import Node


def iterative_deepening_search(problem):
    """Iteratively search greater depths of the search tree to find the goal state."""
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result


def depth_limited_search(problem, limit=50):
    """Depth-first search with a limit.

    Depth-first search always expands the deepest node
    in the current frontier of the search tree.

    We apply a limit to prevent the algorithm from failing on
    problems with infinitely deep paths.

    Limit defaults to 50.
    """
    root = Node(problem.initial_state)
    return __recursive_dls(root, problem, limit)


def __recursive_dls(node, problem, limit):
    """Recursive helper function for depth limited search.

    Returns 'cutoff' if no solution was found within the specified limit.
    Otherwise returns the node containing the goal state.
    """
    if problem.is_goal_state(node.state):
        return node
    elif limit == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        for child in node.expand(problem):
            result = __recursive_dls(child, problem, limit - 1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result is not None:
                return result
        return 'cutoff' if cutoff_occurred else None
