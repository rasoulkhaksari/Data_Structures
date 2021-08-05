
class Node:
    def __init__(self, key, parent=None, terminates=False):
        self.key = key
        self.parent = parent
        self.terminates = terminates
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node('')

    def find(self,word):
        if word is None:
            raise ValueError('word cannot be None')
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            else:
                node=node.children[char]
        return node if node.terminates else None

    def insert(self,word):
        if word is None:
            raise ValueError('word cannot be None')
        node=self.root
        # parent=None
        for char in word:
            # if char in node.children:
            #     node = node.children[char]
            # else:
            #     node.children[char]=Node(char,node)
            #     node = node.children[char]

            if char not in node.children:
                node.children[char]=Node(char,node)
            node = node.children[char]
        node.terminates=True

    def remove(self,word):
        if word is None:
            raise ValueError('word cannot be None')
        node =self.find(word)
        if node is None:
            raise KeyError('word does not exist')
        node.terminates=False
        parent = node.parent
        while parent is not None:
            if node.children or node.terminates:
                return
            del parent.children[node.key]
            node = parent
            parent = parent.parent

    def list_words(self):
        result = []
        curr_word = ''
        self._list_words(self.root, curr_word, result)
        return result

    def _list_words(self, node, curr_word, result):
        if node is None:
            return
        for key, child in node.children.items():
            if child.terminates:
                result.append(curr_word + key)
            self._list_words(child, curr_word + key, result)

