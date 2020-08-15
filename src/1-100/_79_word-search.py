"""
https://leetcode.com/problems/word-search/

"""
from typing import List


class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode('*')

    def insert(self, word):
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
    def dfs(self, board, i, j, N, M, node):
        if node.is_word:
            return True

        if i < 0 or i >= N or j < 0 or j >= M or board[i][j] not in node.children:
            return False

        fc = board[i][j]

        board[i][j] = '#'
        for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if self.dfs(board, ni, nj, N, M, node.children[fc]):
                return True

        board[i][j] = fc

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        N, M = len(board), len(board[0])

        trie = Trie()
        trie.insert(word)

        for i in range(N):
            for j in range(M):
                if self.dfs(board, i, j, N, M, trie.root):
                    return True

        return False
