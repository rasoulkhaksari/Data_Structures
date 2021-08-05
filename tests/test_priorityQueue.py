import unittest
from priorityQueue import Node,PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def test_priority_queue(self):
        priority_queue = PriorityQueue()
        self.assertEqual(priority_queue.extract_min(), None)
        priority_queue.insert(Node('a', 20))
        priority_queue.insert(Node('b', 5))
        priority_queue.insert(Node('c', 15))
        priority_queue.insert(Node('d', 22))
        priority_queue.insert(Node('e', 40))
        priority_queue.insert(Node('f', 3))
        priority_queue.decrease_priority('f', 2)
        priority_queue.decrease_priority('a', 19)
        mins = []
        while priority_queue.array:
            mins.append(priority_queue.extract_min().priority)
        self.assertEqual(mins, [2, 5, 15, 19, 22, 40])


