import unittest
from HashMap import HashTable


class TestHashMap(unittest.TestCase):
    def test_end_to_end(self):
        """Test Hash Table"""
        hash_table = HashTable(10)

        print("\nTest: get on an empty hash table index")
        self.assertRaises(KeyError, hash_table.get, 0)

        print("Test: set on an empty hash table index")
        hash_table.set(0, 'foo')
        self.assertEqual(hash_table.get(0), 'foo')
        hash_table.set(1, 'bar')
        self.assertEqual(hash_table.get(1), 'bar')

        print("Test: set on a non empty hash table index")
        hash_table.set(10, 'foo2')
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertEqual(hash_table.get(10), 'foo2')

        print("Test: set on a key that already exists")
        hash_table.set(10, 'foo3')
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertEqual(hash_table.get(10), 'foo3')

        print("Test: remove on a key that already exists")
        hash_table.remove(10)
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertRaises(KeyError, hash_table.get, 10)

        print("Test: remove on a key that doesn't exist")
        self.assertRaises(KeyError, hash_table.remove, -1)

