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


def main():
    initial_state = get_initial_state()


def get_initial_state():
    return [3, 3, 1]


if __name__ == '__main__':
    main()
