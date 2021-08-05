class MinHeap:
    def __init__(self) -> None:
        self.array = []

    def __len__(self):
        return len(self.array)

    def extract_min(self):
        if not self.array:
            return None
        if len(self.array) == 1:
            return self.array.pop(0)
        min = self.array[0]
        self.array[0] = self.array.pop(-1)
        self.bubble_down(0)
        return min

    def peek_min(self):
        return self.array[0] if self.array else None

    def insert(self, key):
        self.array.append(key)
        self.bubble_up(len(self.array)-1)

    def bubble_up(self, index):
        if index == 0:
            return
        parent_index = (index-1)//2
        if self.array[parent_index] > self.array[index]:
            self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
            self.bubble_up(parent_index)

    def bubble_down(self, index):
        smallerChild = self.smaller_child(index)
        if smallerChild == -1:
            return
        if self.array[index] > self.array[smallerChild]:
            self.array[index], self.array[smallerChild] = self.array[smallerChild], self.array[index]
            self.bubble_down(smallerChild)

    def smaller_child(self, index):
        left_child_index = (2*index) + 1
        right_child_index = (2*index) + 2
        if right_child_index >= len(self.array):
            if left_child_index >= len(self.array):
                return -1
            else:
                return left_child_index
        else:
            return left_child_index if self.array[left_child_index] < self.array[right_child_index] else right_child_index
