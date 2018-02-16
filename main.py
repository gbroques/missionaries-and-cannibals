from missionaries_and_cannibals import MissionariesAndCannibals


def main():
    initial_state = get_initial_state()
    goal_state = get_goal_state()
    problem = MissionariesAndCannibals(initial_state, goal_state)


def get_initial_state():
    return 3, 3, 1


def get_goal_state():
    return 0, 0, 0


if __name__ == '__main__':
    main()
