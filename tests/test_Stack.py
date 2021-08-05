import unittest
from Stack import Stack,Node

class TestStack(unittest.TestCase):
    def test_end_to_end(self):
        print('\nTest: Empty stack')
        stack=Stack()
        self.assertEqual(stack.peek(),None)
        self.assertEqual(stack.pop(),None)

        print('Test: one element')
        top=Node(5)
        stack=Stack(top)
        self.assertEqual(stack.pop(),5)
        self.assertEqual(stack.peek(),None)

        print('Test: more than one element')
        stack=Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(),3)
        self.assertEqual(stack.peek(),2)
        self.assertEqual(stack.pop(),2)
        self.assertEqual(stack.peek(),1)
        self.assertEqual(stack.isEmpty(),False)
        self.assertEqual(stack.pop(),1)
        self.assertEqual(stack.peek(),None)
        self.assertEqual(stack.isEmpty(),True)
