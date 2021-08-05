import sys


class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, node: Node):
        self.array.append(node)
        return self.array[-1]

    def extract_min(self)->Node:
        if not self.array:
            return None
        minimum = sys.maxsize
        for index, node in enumerate(self.array):
            if node.priority < minimum:
                minimum = node.priority
                minimum_index = index
        return self.array.pop(minimum_index)

    def decrease_priority(self, data, new_priority):
        for node in self.array:
            if node.data is data:
                node.priority = new_priority
                return node
        return None
