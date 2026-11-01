import unittest

from main import TreeNode, is_valid_bst


class TestValidateBST(unittest.TestCase):
    def test_valid_tree(self):
        root = TreeNode(8, TreeNode(3), TreeNode(10))
        self.assertTrue(is_valid_bst(root))

    def test_invalid_direct_child(self):
        root = TreeNode(8, TreeNode(9), TreeNode(10))
        self.assertFalse(is_valid_bst(root))

    def test_invalid_value_deep_in_subtree(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15, TreeNode(6), TreeNode(20))
        self.assertFalse(is_valid_bst(root))

    def test_duplicate_value(self):
        root = TreeNode(5, TreeNode(5), None)
        self.assertFalse(is_valid_bst(root))

    def test_negative_values(self):
        root = TreeNode(-2, TreeNode(-5), TreeNode(-1))
        self.assertTrue(is_valid_bst(root))

    def test_empty_tree(self):
        self.assertTrue(is_valid_bst(None))

    def test_one_node(self):
        self.assertTrue(is_valid_bst(TreeNode(1)))


if __name__ == "__main__":
    unittest.main()
