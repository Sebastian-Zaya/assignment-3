class BstNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add(self, val):
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
        if val == self.value:
            return True
        elif val < self.value:
            return False if (self.left is None) else self.left.contains(val)
        else:  # val > self.value
            return False if (self.right is None) else self.right.contains(val)

    def remove(self, val):
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
        Returns the node with the minimum value in the subtree.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def max_depth(self):
        """
        Returns the number of nodes in the longest root-to-leaf path
        in this subtree (consistent with the assignment's definition).
        """
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return 1 + max(left_depth, right_depth)

    def to_string(self):
        """
        Return a string representing the in-order traversal of this subtree.
        Example: "2, 3, 5, 7"
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
        Recursively append DOT representation lines for this subtree.
        'lines' is a list of strings.
        """
        if self.left is not None:
            lines.append(f'    "{self.value}" -> "{self.left.value}" ;')
            self.left.to_dot(lines)
        else:
            pass

        if self.right is not None:
            lines.append(f'    "{self.value}" -> "{self.right.value}" ;')
            self.right.to_dot(lines)
        else:
            pass
