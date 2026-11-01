import unittest

from main import BinarySearchTree


def make_tree(values):
    tree = BinarySearchTree()
    for value in values:
        tree.insert(value)
    return tree


class TestTreeTraversal(unittest.TestCase):
    def setUp(self):
        self.tree = make_tree([8, 3, 10, 1, 6, 14, 4, 7, 13])

    def test_preorder(self):
        self.assertEqual(self.tree.preorder(), [8, 3, 1, 6, 4, 7, 10, 14, 13])

    def test_inorder(self):
        self.assertEqual(self.tree.inorder(), [1, 3, 4, 6, 7, 8, 10, 13, 14])

    def test_postorder(self):
        self.assertEqual(self.tree.postorder(), [1, 4, 7, 6, 3, 13, 14, 10, 8])

    def test_reverse_preorder(self):
        self.assertEqual(self.tree.reverse_preorder(), [8, 10, 14, 13, 3, 6, 7, 4, 1])

    def test_reverse_inorder(self):
        self.assertEqual(self.tree.reverse_inorder(), [14, 13, 10, 8, 7, 6, 4, 3, 1])

    def test_reverse_postorder(self):
        self.assertEqual(self.tree.reverse_postorder(), [13, 14, 10, 7, 4, 6, 1, 3, 8])

    def test_empty_tree(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.preorder(), [])
        self.assertEqual(tree.inorder(), [])
        self.assertEqual(tree.postorder(), [])

    def test_one_node(self):
        tree = make_tree([5])
        self.assertEqual(tree.preorder(), [5])
        self.assertEqual(tree.reverse_postorder(), [5])

    def test_duplicate_is_not_inserted(self):
        tree = make_tree([5, 3, 5, 3])
        self.assertEqual(tree.inorder(), [3, 5])


if __name__ == "__main__":
    unittest.main()
