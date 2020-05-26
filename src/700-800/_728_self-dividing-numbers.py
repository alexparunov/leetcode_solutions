"""
https://leetcode.com/problems/self-dividing-numbers/

"""
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num):
            x = num
            while x:
                x, d = divmod(x, 10)
                if d == 0 or num % d > 0:
                    return False

            return True

        return [i for i in range(left, right + 1) if isSelfDividing(i)]
