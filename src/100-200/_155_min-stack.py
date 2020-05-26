"""
https://leetcode.com/problems/min-stack/

"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = list()
        self.s2 = list()

    def push(self, x: int) -> None:
        self.s1.append(x)

        popped = list()
        while self.s2 and x > self.s2[-1]:
            popped.append(self.s2.pop())

        self.s2.append(x)
        for p in popped[::-1]:
            self.s2.append(p)

    def pop(self) -> None:
        if self.s1:
            popped = self.s1.pop()
            self.s2.remove(popped)

    def top(self) -> int:
        return self.s1[-1] if self.s1 else -1

    def getMin(self) -> int:
        return self.s2[-1] if self.s2 else -1
