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
from .state import State
from .state_constants import GOAL_STATE
from .state_constants import INITIAL_STATE


class MissionariesAndCannibals(Problem):

    def __init__(self):
        initial_state = State.value_of(INITIAL_STATE)
        goal_state = State.value_of(GOAL_STATE)
        super().__init__(initial_state, goal_state)

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
        operate = self.get_operation(state.boat)
        result = operate(state, action)

        return result.is_valid()

    def result(self, state, action):
        operate = self.get_operation(state.boat)
        return operate(state, action)

    @staticmethod
    def get_operation(boat):
        """Subtract action from state if boat is on initial side of river."""
        return operator.sub if boat == 1 else operator.add
