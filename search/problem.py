class Problem:
    """Abstract class for a formal search problem.

    The problem must be fully-observable, deterministic, and discrete.

    Adapted From: https://github.com/aimacode/aima-python/blob/master/search.py
    """

    def __init__(self, initial_state, goal=None):
        """Specify the initial state, and possibly a goal state."""
        self.initial_state = initial_state
        self.goal_state = goal

    def actions(self, state):
        """Return the actions that can be executed on the given state.

        The result would typically be a list, but if there a many actions,
        consider yielding them one at a time in an iterator.
        """
        raise NotImplementedError

    def result(self, state, action):
        """Return the node that results from executing the given action on the given state.

        The action must be one of self.get_actions(state).
        """
        raise NotImplementedError

    def is_goal_state(self, state):
        """Return True if the state is a a goal state."""
        return state == self.goal_state
