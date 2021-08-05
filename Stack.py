class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self,top:Node=None):
        self.top = top

    def push(self, data):
        node = Node(data, self.top)
        self.top = node

    def pop(self):
        if not self.top:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if not self.top:
            return None
        return self.top.data

    def isEmpty(self):
        if self.top:
            return False
        return True
