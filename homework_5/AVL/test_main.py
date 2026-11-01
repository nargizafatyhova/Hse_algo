import unittest

from main import AVLTree


def make_tree(values):
    tree = AVLTree()
    for value in values:
        tree.insert(value)
    return tree


def check_avl(test_case, node):
    if node is None:
        return 0

    left_height = check_avl(test_case, node.left)
    right_height = check_avl(test_case, node.right)
    test_case.assertLessEqual(abs(left_height - right_height), 1)
    test_case.assertEqual(node.height, max(left_height, right_height) + 1)
    return node.height


class TestAVLTree(unittest.TestCase):
    def test_insert_and_search(self):
        tree = make_tree([10, 5, 15, 3, 7])
        self.assertTrue(tree.search(7))
        self.assertFalse(tree.search(20))
        self.assertIn(5, tree)

    def test_right_rotation(self):
        tree = make_tree([30, 20, 10])
        self.assertEqual(tree.root.key, 20)
        self.assertEqual(tree.inorder(), [10, 20, 30])
        check_avl(self, tree.root)

    def test_left_rotation(self):
        tree = make_tree([10, 20, 30])
        self.assertEqual(tree.root.key, 20)
        check_avl(self, tree.root)

    def test_left_right_rotation(self):
        tree = make_tree([30, 10, 20])
        self.assertEqual(tree.root.key, 20)
        check_avl(self, tree.root)

    def test_right_left_rotation(self):
        tree = make_tree([10, 30, 20])
        self.assertEqual(tree.root.key, 20)
        check_avl(self, tree.root)

    def test_delete_leaf(self):
        tree = make_tree([20, 10, 30, 5])
        tree.delete(5)
        self.assertEqual(tree.inorder(), [10, 20, 30])
        check_avl(self, tree.root)

    def test_delete_node_with_one_child(self):
        tree = make_tree([20, 10, 30, 25])
        tree.delete(30)
        self.assertEqual(tree.inorder(), [10, 20, 25])
        check_avl(self, tree.root)

    def test_delete_node_with_two_children(self):
        tree = make_tree([20, 10, 30, 25, 40, 22])
        tree.delete(30)
        self.assertEqual(tree.inorder(), [10, 20, 22, 25, 40])
        check_avl(self, tree.root)

    def test_delete_causes_rebalancing(self):
        tree = make_tree([9, 5, 10, 0, 6, 11, -1, 1, 2])
        tree.delete(10)
        self.assertEqual(tree.inorder(), [-1, 0, 1, 2, 5, 6, 9, 11])
        check_avl(self, tree.root)

    def test_duplicate_is_not_inserted(self):
        tree = make_tree([2, 1, 2, 1])
        self.assertEqual(tree.inorder(), [1, 2])

    def test_delete_missing_key(self):
        tree = make_tree([2, 1, 3])
        tree.delete(100)
        self.assertEqual(tree.inorder(), [1, 2, 3])
        check_avl(self, tree.root)

    def test_empty_tree(self):
        tree = AVLTree()
        tree.delete(1)
        self.assertFalse(tree.search(1))
        self.assertEqual(tree.inorder(), [])


if __name__ == "__main__":
    unittest.main()
