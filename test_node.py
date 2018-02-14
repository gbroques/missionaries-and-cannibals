import unittest

from node import Node


class TestNode(unittest.TestCase):
    def test_append(self):
        root = Node()
        root.append(Node((2, 2, 0)))

        self.assertEqual(root.children, [Node((2, 2, 0))])

    def test_equals(self):
        root1 = Node()
        child1 = Node((2, 3, 0))
        child1.append(Node((1, 2, 1)))
        child1.append(Node((1, 3, 1)))
        root1.append(child1)

        root2 = Node()
        child2 = Node((2, 3, 0))
        child2.append(Node((1, 2, 1)))
        child2.append(Node((1, 3, 1)))
        root2.append(child2)

        self.assertEqual(root1, root2)

if __name__ == '__main__':
    unittest.main()
