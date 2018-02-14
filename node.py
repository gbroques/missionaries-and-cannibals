class Node:
    def __init__(self, state, children=None):
        self.state = state
        self.children = []
        if children is not None:
            self.extend(children)

    def extend(self, children):
        for child in children:
            self.append(child)

    def append(self, state):
        assert isinstance(state, Node)
        self.children.append(state)

    def __repr__(self):
        return self.state.__str__()

    def __str__(self):
        return self.state.__str__()

    def __eq__(self, other):
        if self.state != other.state:
            return False
        elif self.children != other.children:
            return False
        else:
            return True
