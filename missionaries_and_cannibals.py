"""
Author: G Roques

Solves the missionaries and cannibals problem:

Three missionaries and three cannibals are on one side of a river,
along with a boat that can hold one or two people.

Find a way to get everyone to the other side,
without ever leaving a group of missionaries in one place,
outnumbered by the cannibals in that place.

Represents current state with a list [a, b, c].
This list represents the number of missionaries on the wrong side,
cannibals on the wrong side, and whether the boat is on the wrong side.
Initially all the missionaries, cannibals, and the boat are on the wrong side.
The list representing the initial state is [3, 3, 1]
"""

import operator

from node import Node


def main():
    initial_state = get_initial_state()


def get_initial_state():
    return 3, 3, 1


def add_tuples(a, b):
    return operate_on_tuples(a, b, operator.add)


def subtract_tuples(a, b):
    return operate_on_tuples(a, b, operator.sub)


def operate_on_tuples(a, b, operation):
    return tuple(map(operation, a, b))


def is_state_valid(state, previous_state=None):
    if contains_negative(state):
        return False
    elif has_more_than_one_boat(state):
        return False
    elif has_more_cannibals_than_missionaries(state):
        return False
    elif state > get_initial_state():
        return False
    elif state == previous_state:
        return False
    else:
        return True


def contains_negative(collection):
    return any(n < 0 for n in collection)


def has_more_than_one_boat(state):
    return state[2] > 1


def has_more_cannibals_than_missionaries(state):
    return state[1] > state[0]


def get_actions():
    return {
        (1, 0, 1),
        (2, 0, 1),
        (0, 1, 1),
        (0, 2, 1),
        (1, 1, 1)
    }


def get_successors(state, operation, previous_state=None):
    actions = get_actions()

    apply_action = get_apply_action(state, operation)

    possible_successors = map(apply_action, actions)

    prune = get_prune(previous_state)
    return set(filter(prune, possible_successors))


def get_prune(previous_state):
    return lambda possible_successor: is_state_valid(possible_successor, previous_state)


def get_apply_action(state, operation):
    return lambda action: operate_on_tuples(state, action, operation)


def search(max_depth):
    initial_state = get_initial_state()
    root = Node(initial_state)
    successors = get_successors(root.state, operator.sub)
    successor_nodes = map(lambda n: Node(n), successors)
    root.extend(successor_nodes)
    return {
        'success': False,
        'tree': root
    }


if __name__ == '__main__':
    main()
