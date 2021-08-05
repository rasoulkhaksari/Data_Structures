import unittest
from BST import BinarySearchTree,Node


class TestBSTree(unittest.TestCase):

    def test_bsttree(self):
        """Test Binary Search Tree"""
        bst = BinarySearchTree(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        result = []
        bst.in_order(bst.root, result)
        self.assertEqual(result, [1, 2, 3, 5, 8])


