import operator

from util import contains_negative
from util import operate_on_tuples
from .state_constants import INITIAL_STATE


class State:
    """Represents the state in the Missionaries and Cannibals problem."""

    def __init__(self, missionaries, cannibals, boat):
        self.value = (missionaries, cannibals, boat)
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    @classmethod
    def value_of(cls, state):
        if not cls.__is_valid_tuple(state):
            raise ValueError(str(state) + " must be a tuple with 3 elements.")
        return State(state[0], state[1], state[2])

    def is_valid(self):
        if contains_negative(self.value):
            return False
        elif self.__has_more_than_one_boat():
            return False
        elif self.__has_more_cannibals_than_missionaries():
            return False
        elif self.value > INITIAL_STATE:
            return False
        else:
            return True

    def __has_more_than_one_boat(self):
        return self.boat > 1

    def __has_more_cannibals_than_missionaries(self):
        return self.__more_cannibals_on_wrong_side() or self.__more_cannibals_on_right_side()

    def __more_cannibals_on_wrong_side(self):
        """Return True when more cannibals than missionaries exist on the wrong side of the river."""
        return ((self.missionaries == 1 and self.cannibals == 3) or
                (self.missionaries == 2 and self.cannibals == 3) or
                (self.missionaries == 1 and self.cannibals == 2))

    def __more_cannibals_on_right_side(self):
        """Return True when more cannibals than missionaries exist on the right side of the river.

        The "right" side of the river is the side opposite of the starting side.
        """
        return ((self.missionaries == 2 and self.cannibals == 1) or
                (self.missionaries == 1 and self.cannibals == 0))

    def __add__(self, other):
        result = self.__operate(other, operator.add)
        return self.value_of(result)

    def __sub__(self, other):
        result = self.__operate(other, operator.sub)
        return self.value_of(result)

    def __operate(self, other, operation):
        if self.__is_valid_tuple(other):
            return operate_on_tuples(self.value, other, operation)
        elif isinstance(other, State):
            return operate_on_tuples(self.value, other.value, operation)
        else:
            raise ValueError(self.__get_invalid_operand_error(other))

    @staticmethod
    def __is_valid_tuple(other):
        return isinstance(other, tuple) and len(other) == 3

    @staticmethod
    def __get_invalid_operand_error(other):
        return str(other) + " must be an instance of State or a tuple of length 3."

    def __repr__(self):
        return '<State {}>'.format(self.value)

    def __str__(self):
        return '<State {}>'.format(self.value)

    def __lt__(self, other):
        self.__ensure_instance_of_state(other)
        return self.value < other.value

    def __eq__(self, other):
        return isinstance(other, State) and self.value == other.value

    def __hash__(self):
        return hash(self.value)

    @staticmethod
    def __ensure_instance_of_state(other):
        if not isinstance(other, State):
            raise ValueError(str(other) + " must be an instance of State")
