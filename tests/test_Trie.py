import unittest
from Trie import Trie

class TestTrie(unittest.TestCase):       

    def test_trie(self):
        trie = Trie()

        print('\nTest: Insert')
        words = ['a', 'at', 'has', 'hat', 'he',
                 'me', 'men', 'mens', 'met']
        for word in words:
            trie.insert(word)
        for word in trie.list_words():
            self.assertTrue(trie.find(word) is not None)
            
        print('Test: Remove me')
        trie.remove('me')
        words_removed = ['me']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'mens', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)

        print('Test: Remove mens')
        trie.remove('mens')
        words_removed = ['me', 'mens']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)

        print('Test: Remove a')
        trie.remove('a')
        words_removed = ['a', 'me', 'mens']
        words = ['at', 'has', 'hat', 'he',
                 'men', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)

        print('Test: Remove has')
        trie.remove('has')
        words_removed = ['a', 'has', 'me', 'mens']
        words = ['at', 'hat', 'he',
                 'men', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)


    def test_trie_remove_invalid(self):
        print('Test: Remove from empty trie')
        trie = Trie()
        with self.assertRaises(KeyError):
            trie.remove('foo')


