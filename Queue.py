class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self, head=None):
        self.head: Node = None
        self.tail: Node = None

    def enqueue(self, data):
        if not self.head:
            node = Node(data)
            self.head = node
            self.tail = node
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            return data
        else:
            data = self.head.data
            self.head = self.head.next
            return data
