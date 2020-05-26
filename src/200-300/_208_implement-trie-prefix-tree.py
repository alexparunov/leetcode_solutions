"""
https://leetcode.com/problems/implement-trie-prefix-tree/

"""


class TrieNode:
    def __init__(self, val: str, children=dict(), is_word=False):
        self.val = val
        self.children = children
        self.is_word = is_word


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('*')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root

        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = TrieNode(letter)
                node.children[letter] = new_node
                node = new_node

        node.is_word = True

    def searchPrefix(self, prefix: str) -> TrieNode:
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return None

            node = node.children[letter]

        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.searchPrefix(word)

        return node != None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.searchPrefix(prefix)

        return node != None
