import unittest
from Queue import Queue

class TestQueue(unittest.TestCase):
    def test_end_to_end(self):
        print('\nTest: Dequeue an empty queue')
        queue = Queue()
        self.assertEqual(queue.dequeue(), None)

        print('Test: Enqueue to an empty queue')
        queue.enqueue(1)

        print('Test: Dequeue a queue with one element')
        self.assertEqual(queue.dequeue(), 1)

        print('Test: Enqueue to a non-empty queue')
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        print('Test: Dequeue a queue with more than one element')
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)

