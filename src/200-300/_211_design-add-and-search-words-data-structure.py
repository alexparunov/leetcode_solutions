"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/

"""


class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.is_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('*')

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)

            current = current.children[letter]

        current.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_recursive(self.root, word, 0)

    def search_recursive(self, node, word, index):
        if index == len(word):
            return node.is_word

        letter = word[index]
        if letter in node.children:
            return self.search_recursive(node.children[letter], word, index + 1)
        elif letter == '.':
            for child_letter, child_node in node.children.items():
                if self.search_recursive(child_node, word, index + 1):
                    return True

        return False
