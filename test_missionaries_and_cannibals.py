import unittest
import missionaries_and_cannibals


class TestMissionariesAndCannibals(unittest.TestCase):
    def test_initial_state(self):
        expected_initial_state = [3, 3, 1]
        initial_state = missionaries_and_cannibals.get_initial_state()
        self.assertEqual(expected_initial_state, initial_state)


if __name__ == '__main__':
    unittest.main()
