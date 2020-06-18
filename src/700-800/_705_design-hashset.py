"""
https://leetcode.com/problems/design-hashset/

"""


class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 1000001
        self.table = [None] * self.N

    def add(self, key: int) -> None:
        self.table[key % self.N] = key

    def remove(self, key: int) -> None:
        self.table[key % self.N] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.table[key % self.N] is not None
