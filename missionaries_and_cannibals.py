"""
Author: G Roques

Solves the missionaries and cannibals problem:

Three missionaries and three cannibals are on one side of a river,
along with a boat that can hold one or two people.

Find a way to get everyone to the other side,
without ever leaving a group of missionaries on one side outnumbered by the cannibals.

The current state is represented with a list [a, b, c].
This list represents the number of missionaries on the wrong side,
cannibals on the wrong side, and whether the boat is on the wrong side.
Initially all the missionaries, cannibals, and the boat are on the wrong side of the river.
The list representing the initial state is [3, 3, 1].
"""

import operator

from search import Problem
from state import State
from state_constants import GOAL_STATE
from state_constants import INITIAL_STATE
from util import operate_on_tuples


class MissionariesAndCannibals(Problem):

    def __init__(self):
        super().__init__(INITIAL_STATE, GOAL_STATE)

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

        return State.value_of(result).is_state_valid()

    @classmethod
    def get_apply_action(cls, state, operation):
        return lambda action: operate_on_tuples(state, action, operation)

    def result(self, state, action):
        operation = self.get_operation(state[2])
        return operate_on_tuples(state, action, operation)

    @staticmethod
    def get_operation(boat):
        """Subtract action from state if boat is on initial side of river."""
        return operator.sub if boat == 1 else operator.add
