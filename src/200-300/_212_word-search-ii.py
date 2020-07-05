"""
https://leetcode.com/problems/word-search-ii/

"""
from typing import List


class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.is_word = False
        self.children = dict()


class Trie(object):
    def __init__(self):
        self.root = TrieNode('*')

    def insert(self, word: str):
        current = self.root

        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                new_child = TrieNode(char)
                current.children[char] = new_child
                current = new_child

        current.is_word = True


class Solution:
    def dfs(self, board, i, j, node, word_path, result_words, num_words):
        if len(result_words) == num_words:
            return

        if node.is_word:
            result_words.append(word_path)
            node.is_word = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        fc = board[i][j]

        if fc not in node.children:
            return

        # mark as visited
        board[i][j] = '#'

        child = node.children[fc]
        for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            self.dfs(board, ni, nj, child, word_path + fc, result_words, num_words)

        board[i][j] = fc

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return False

        trie = Trie()
        for word in words:
            trie.insert(word)

        result_words = list()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie.root, '', result_words, len(words))

        return result_words
