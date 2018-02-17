import unittest

from missionaries_and_cannibals import GOAL_STATE
from missionaries_and_cannibals import INITIAL_STATE
from missionaries_and_cannibals import MissionariesAndCannibals
from missionaries_and_cannibals import State


class TestMissionariesAndCannibals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.problem = MissionariesAndCannibals()

    def test_initial_state(self):
        expected_initial_state = (3, 3, 1)

        self.assertEqual(expected_initial_state, INITIAL_STATE)

    def test_goal_state(self):
        expected_goal_state = (0, 0, 0)

        self.assertEqual(expected_goal_state, GOAL_STATE)

    def test_get_all_actions(self):
        expected_actions = {
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        }

        actions = self.problem.get_all_actions()
        self.assertEqual(expected_actions, actions)

    def test_actions_from_initial_state(self):
        expected_actions = {
            (0, 1, 1),
            (1, 1, 1),
            (0, 2, 1)
        }

        actions = self.problem.actions(State(3, 3, 1))

        self.assertEqual(expected_actions, actions)

    def test_actions_from_second_state(self):
        expected_actions = {
            (1, 0, 1),
            (0, 2, 1),
            (1, 1, 1)
        }

        actions = self.problem.actions(State(2, 2, 0))

        self.assertEqual(expected_actions, actions)

    def test_result_on_initial_transition(self):
        expected_result = State(2, 2, 0)
        state = State(3, 3, 1)
        action = (1, 1, 1)

        result = self.problem.result(state, action)

        self.assertEqual(expected_result, result)

    def test_result_on_second_transition(self):
        expected_result = State(3, 2, 1)
        state = State(2, 2, 0)
        action = (1, 0, 1)

        result = self.problem.result(state, action)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
