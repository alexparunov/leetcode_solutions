"""
https://leetcode.com/problems/design-a-stack-with-increment-operation/

"""


class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = [-1] * self.maxSize
        self.pos = 0

    def push(self, x: int) -> None:
        if self.pos < self.maxSize:
            self.stack[self.pos] = x
            self.pos += 1

    def pop(self) -> int:
        val = -1
        if self.pos > 0:
            self.pos -= 1
            val = self.stack[self.pos]

        return val

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val
