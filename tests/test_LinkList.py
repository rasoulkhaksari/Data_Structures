import unittest
from LinkList import LinkedList,Data

class TestLinkedList(unittest.TestCase):
    def test_insert_to_front(self):
        print('Test: insert_to_front on an empty list')
        linked_list = LinkedList()
        linked_list.insert_to_front(Data(10))
        self.assertEqual(linked_list.values(), [10])

        print('Test: insert_to_front on a None')
        linked_list.insert_to_front(Data(None))
        self.assertEqual(linked_list.values(), [10])

        print('Test: insert_to_front general case')
        linked_list.insert_to_front(Data('a'))
        linked_list.insert_to_front(Data('bc'))
        self.assertEqual(linked_list.values(), ['bc', 'a', 10])


    def test_append(self):
        print('Test: append on an empty list')
        linked_list = LinkedList()
        linked_list.append(Data(10))
        self.assertEqual(linked_list.values(), [10])

        print('Test: append a None')
        linked_list.append(None)
        self.assertEqual(linked_list.values(), [10])

        print('Test: append general case')
        linked_list.append(Data('a'))
        linked_list.append(Data('bc'))
        self.assertEqual(linked_list.values(), [10, 'a', 'bc'])


    def test_find(self):
        print('Test: find on an empty list')
        linked_list = LinkedList()
        node = linked_list.find(Data('a'))
        self.assertEqual(node, None)

        print('Test: find a None')
        linked_list = LinkedList()
        linked_list.append(Data(10))
        node = linked_list.find(None)
        self.assertEqual(node, None)

        print('Test: find general case with matches')
        linked_list = LinkedList()
        linked_list.append(Data(10))
        linked_list.insert_to_front(Data('a'))
        linked_list.insert_to_front(Data('bc'))
        node = linked_list.find(Data('a'))
        self.assertEqual(node.data.value, 'a')

        print('Test: find general case with no matches')
        node = linked_list.find(Data('aaa'))
        self.assertEqual(node, None)


    def test_delete(self):
        print('Test: delete on an empty list')
        linked_list = LinkedList()
        linked_list.delete(Data('a'))
        self.assertEqual(linked_list.values(), [])

        print('Test: delete a None')
        linked_list = LinkedList()
        linked_list.append(Data(10))
        linked_list.delete(None)
        self.assertEqual(linked_list.values(), [10])

        print('Test: delete general case with matches')
        linked_list = LinkedList()
        linked_list.append(Data(10))
        linked_list.insert_to_front(Data('a'))
        linked_list.insert_to_front(Data('bc'))
        linked_list.delete(Data('a'))
        self.assertEqual(linked_list.values(), ['bc', 10])

        print('Test: delete general case with no matches')
        linked_list.delete(Data('aa'))
        self.assertEqual(linked_list.values(), ['bc', 10])


    def test_len(self):
        print('Test: len on an empty list')
        linked_list = LinkedList()
        self.assertEqual(len(linked_list), 0)

        print('Test: len general case')
        linked_list = LinkedList()
        linked_list.append(Data(10))
        linked_list.insert_to_front(Data('a'))
        linked_list.insert_to_front(Data('bc'))
        self.assertEqual(len(linked_list), 3)

