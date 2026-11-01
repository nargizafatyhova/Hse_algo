import unittest

from main import TreeNode, is_balanced


class TestBalancedBinaryTree(unittest.TestCase):
    def test_balanced_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3))
        self.assertTrue(is_balanced(root))

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertFalse(is_balanced(root))

    def test_unbalanced_subtree(self):
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3, TreeNode(4), None), None)
        root.right = TreeNode(5, None, TreeNode(6))
        self.assertFalse(is_balanced(root))

    def test_perfect_tree(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        self.assertTrue(is_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(is_balanced(None))

    def test_one_node(self):
        self.assertTrue(is_balanced(TreeNode(1)))


if __name__ == "__main__":
    unittest.main()
