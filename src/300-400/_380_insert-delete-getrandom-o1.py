"""
https://leetcode.com/problems/insert-delete-getrandom-o1/

"""
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.item_idx = dict()
        self.idx_item = dict()
        self.n_items = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.item_idx:
            return False

        self.item_idx[val] = self.n_items
        self.idx_item[self.n_items] = val
        self.n_items += 1

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.item_idx:
            return False

        idx = self.item_idx.pop(val)
        self.idx_item.pop(idx)

        if idx != self.n_items - 1:
            self.idx_item[idx] = self.idx_item[self.n_items - 1]
            self.item_idx[self.idx_item[self.n_items - 1]] = idx
            self.idx_item.pop(self.n_items - 1)

        self.n_items -= 1

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        rand_idx = random.randint(0, self.n_items - 1)
        return self.idx_item[rand_idx]
