from BstNode import BstNode

class BstSet:
    def __init__(self):
        self.root = None

    def add(self, val):
        """
        Insert 'val' into the BST if it's not already present.
        """
        if self.root is None:
            self.root = BstNode(val)
        else:
            self.root.add(val)

    def search(self, val):
        """
        Return True if 'val' is found in this BST, else False.
        """
        if self.root is None:
            return False
        else:
            return self.root.contains(val)

    def remove(self, val):
        """
        Remove 'val' from the BST if present.
        """
        if self.root is not None:
            self.root = self.root.remove(val)

    def max_depth(self):
        """
        Return the max depth (longest root-to-leaf path in terms of node count).
        """
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    def __str__(self):
        """
        Return a string representation of the BST values in sorted (in-order) order.
        """
        txt = "{ "
        if self.root is not None:
            txt += self.root.to_string()
        return txt + " }"

    def to_dot_string(self):
        """
        Return a string that describes this BST in the DOT graph language.
        """
        lines = ["digraph BST {"]
        if self.root is not None:
            # Add a label for the root
            lines.append(f'    "{self.root.value}" [label="{self.root.value}"];')
            self.root.to_dot(lines)
        lines.append("}")
        return "\n".join(lines)
