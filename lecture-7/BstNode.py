class BstNode:
    """Represents a node in a Binary Search Tree (BST)."""

    def __init__(self, value, left=None, right=None):
        """
        Initializes a BstNode with a value and optional
        left and right children.

        :param value: The value of the node.
        :param left: The left child of the node (default is None).
        :param right: The right child of the node (default is None).
        """
        self.value = value
        self.left = left
        self.right = right

    def add(self, val):
        """
        Adds a value to the BST.

        :param val: The value to add.
        """
        if val < self.value:
            if self.left is None:
                self.left = BstNode(val)
            else:
                self.left.add(val)
        elif val > self.value:
            if self.right is None:
                self.right = BstNode(val)
            else:
                self.right.add(val)

    def contains(self, val):
        """
        Checks if a value exists in the BST.

        :param val: The value to check.
        :return: True if the value exists, False otherwise.
        """
        if val == self.value:
            return True
        elif val < self.value:
            return False if self.left is None else self.left.contains(val)
        else:  # val > self.value
            return False if self.right is None else self.right.contains(val)

    def remove(self, val):
        """
        Removes a value from the BST.

        :param val: The value to remove.
        :return: The updated node.
        """
        if val < self.value:
            # Look in the left subtree
            if self.left is not None:
                self.left = self.left.remove(val)
            return self

        elif val > self.value:
            # Look in the right subtree
            if self.right is not None:
                self.right = self.right.remove(val)
            return self

        else:
            # Case 1: No left child
            if self.left is None:
                return self.right  # Could be None or a subtree
            # Case 2: No right child
            elif self.right is None:
                return self.left
            # Case 3: Has two children
            else:
                successor = self.right.find_min_node()
                self.value = successor.value
                self.right = self.right.remove(successor.value)
                return self

    def find_min_node(self):
        """
        Finds the node with the minimum value in the subtree.

        :return: The node with the minimum value.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def max_depth(self):
        """
        Calculates the maximum depth of the subtree.

        :return: The maximum depth.
        """
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return 1 + max(left_depth, right_depth)

    def to_string(self):
        """
        Generates a string representation of the subtree.

        :return: A string representation of the subtree.
        """
        result = []
        if self.left:
            result.append(self.left.to_string())
        result.append(str(self.value))
        if self.right:
            result.append(self.right.to_string())
        return ", ".join(result)

    def to_dot(self, lines):
        """
        Generates a DOT representation of the subtree.

        :param lines: A list of strings to append to.
        """
        if self.left is not None:
            lines.append(f'    "{self.value}" -> "{self.left.value}" ;')
            self.left.to_dot(lines)
        if self.right is not None:
            lines.append(f'    "{self.value}" -> "{self.right.value}" ;')
            self.right.to_dot(lines)
