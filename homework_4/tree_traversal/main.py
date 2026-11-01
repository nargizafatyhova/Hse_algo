class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return

        node = self.root

        while True:
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                    return
                node = node.left
            elif value > node.value:
                if node.right is None:
                    node.right = TreeNode(value)
                    return
                node = node.right
            else:
                return

    def preorder(self):
        result = []

        def walk(node):
            if node is None:
                return
            result.append(node.value)
            walk(node.left)
            walk(node.right)

        walk(self.root)
        return result

    def inorder(self):
        result = []

        def walk(node):
            if node is None:
                return
            walk(node.left)
            result.append(node.value)
            walk(node.right)

        walk(self.root)
        return result

    def postorder(self):
        result = []

        def walk(node):
            if node is None:
                return
            walk(node.left)
            walk(node.right)
            result.append(node.value)

        walk(self.root)
        return result

    def reverse_preorder(self):
        result = []

        def walk(node):
            if node is None:
                return
            result.append(node.value)
            walk(node.right)
            walk(node.left)

        walk(self.root)
        return result

    def reverse_inorder(self):
        result = []

        def walk(node):
            if node is None:
                return
            walk(node.right)
            result.append(node.value)
            walk(node.left)

        walk(self.root)
        return result

    def reverse_postorder(self):
        result = []

        def walk(node):
            if node is None:
                return
            walk(node.right)
            walk(node.left)
            result.append(node.value)

        walk(self.root)
        return result
