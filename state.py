from state_constants import INITIAL_STATE
from util import contains_negative


class State:
    def __init__(self, missionaries, cannibals, boat):
        self.value = (missionaries, cannibals, boat)
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    @staticmethod
    def value_of(state):
        if not isinstance(state, tuple) or len(state) != 3:
            raise ValueError("State must be a tuple with 3 elements.")
        return State(state[0], state[1], state[2])

    def is_state_valid(self):
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
