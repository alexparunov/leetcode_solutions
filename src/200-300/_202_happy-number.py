"""
https://leetcode.com/problems/happy-number/

"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n: int):
            x, s = n, 0
            while x:
                x, d = divmod(x, 10)
                s += d ** 2
            return s

        slow = sum_of_squares(n)
        fast = sum_of_squares(sum_of_squares(n))

        if slow == 1 or fast == 1:
            return True

        while slow != fast:
            if slow == 1 or fast == 1:
                return True

            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))

        return False
