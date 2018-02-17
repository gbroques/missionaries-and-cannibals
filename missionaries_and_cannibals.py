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

from search import Problem
from tuple_util import operate_on_tuples


class MissionariesAndCannibals(Problem):

    def actions(self, state):
        all_actions = self.get_all_actions()
        return self.get_valid_actions(state, all_actions)

    @staticmethod
    def get_all_actions():
        return {
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        }

    def get_valid_actions(self, state, all_actions):
        is_action_valid_lambda = self.get_is_action_valid_lambda(state)
        return set(filter(is_action_valid_lambda, all_actions))

    def get_is_action_valid_lambda(self, state):
        return lambda action: self.is_action_valid(state, action)

    def is_action_valid(self, state, action):
        operation = self.get_operation(state[2])
        apply_action = self.get_apply_action(state, operation)

        result = apply_action(action)

        return self.is_state_valid(result)

    @classmethod
    def get_apply_action(cls, state, operation):
        return lambda action: operate_on_tuples(state, action, operation)

    def is_state_valid(self, state):
        if self.contains_negative(state):
            return False
        elif self.has_more_than_one_boat(state):
            return False
        elif self.has_more_cannibals_than_missionaries(state):
            return False
        elif state > self.initial_state:
            return False
        else:
            return True

    @staticmethod
    def contains_negative(collection):
        """Return True if any negative value exists in the collection."""
        return any(n < 0 for n in collection)

    @staticmethod
    def has_more_than_one_boat(state):
        return state[2] > 1

    @classmethod
    def has_more_cannibals_than_missionaries(cls, state):
        return cls.more_cannibals_on_wrong_side(state) or cls.more_cannibals_on_right_side(state)

    @staticmethod
    def more_cannibals_on_wrong_side(state):
        """Return True when more cannibals than missionaries exist on the wrong side of the river."""
        return ((state[0] == 1 and state[1] == 3) or
                (state[0] == 2 and state[1] == 3) or
                (state[0] == 1 and state[1] == 2))

    @staticmethod
    def more_cannibals_on_right_side(state):
        """Return True when more cannibals than missionaries exist on the right side of the river.

        The "right" side of the river is the side opposite of the starting side.
        """
        return (state[0] == 2 and state[1] == 1) or (state[0] == 1 and state[1] == 0)

    def result(self, state, action):
        operation = self.get_operation(state[2])
        return operate_on_tuples(state, action, operation)

    @staticmethod
    def get_operation(boat):
        """Subtract action from state if boat is on initial side of river."""
        return operator.sub if boat == 1 else operator.add
