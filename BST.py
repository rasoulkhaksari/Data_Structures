class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root: Node) -> None:
        self.root = root

    def insert(self, data, parent: Node = None):
        if data is None:
            return
        if self.root is None:
            self.root = Node(data)
            return
        if parent is None:
            parent = self.root
        if data <= parent.data:
            if parent.left:
                self.insert(data, parent.left)
            else:
                parent.left = Node(data)
        else:
            if parent.right:
                self.insert(data, parent.right)
            else:
                parent.right = Node(data)

    def in_order(self, node: Node, result: list):
        if node is None:
            return
        self.in_order(node.left, result)
        result.append(node.data)
        self.in_order(node.right, result)
