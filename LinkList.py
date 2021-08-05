
class Data():
    value: object = None

    def __new__(cls, *args):
        if args[0] is None:
            return None
        else:
            return super(Data, cls).__new__(cls)

    def __init__(self, value: object, defaultValue: object = None) -> None:
        if value is None:
            value = defaultValue
        self.value = value

    def __eq__(self, other: "Data") -> bool:
        return self.value == other.value


class Node():
    data: Data = None
    next: "Node" = None

    def __new__(cls, *args):
        if args[0] is None:
            return None
        else:
            return super(Node, cls).__new__(cls)

    def __init__(self, data: Data, next: "Node" = None):
        self.data = data
        self.next = next


class LinkedList():
    head: Node = None
    tail: Node = None
    size: int = 0

    def __len__(self) -> int:
        return self.size

    def insert_to_front(self, data: Data) -> Node:
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        self.size += 1
        if self.size == 1:
            self.tail = node
        return node

    def append(self, data: Data) -> Node:
        if data is None:
            return None
        node = Node(data, None)
        if self.size > 0:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.size += 1
        return node

    def find(self, data: Data) -> Node:
        if data is None:
            return None
        current = self.head
        while current and current.data != data and current != self.tail:
            current = current.next
        if current == self.tail:
            return None
        return current

    def delete(self, data: Data):
        current = self.head
        while current and current.next and current.next.data != data and current != self.tail:
            current = current.next
        if current != self.tail:
            current.next = current.next.next
            self.size -= 1

    def print(self):
        current = self.head
        while current != self.tail:
            print(current.data)
            current = current.next

    def values(self) -> list:
        values = []
        current = self.head
        while current:
            values.append(current.data.value)
            current = current.next
        return values
