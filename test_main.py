import unittest

from main import get_goal_state
from main import get_initial_state


class TestMain(unittest.TestCase):
    def test_initial_state(self):
        expected_initial_state = (3, 3, 1)

        initial_state = get_initial_state()

        self.assertEqual(expected_initial_state, initial_state)

    def test_goal_state(self):
        expected_goal_state = (0, 0, 0)

        goal_state = get_goal_state()

        self.assertEqual(expected_goal_state, goal_state)


if __name__ == '__main__':
    unittest.main()
