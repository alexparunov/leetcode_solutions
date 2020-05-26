"""
https://leetcode.com/problems/maximum-69-number/

"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        max_num = num
        addon = 0
        i = 0

        while num:
            num, d = divmod(num, 10)
            if d == 6:
                addon = 3 * 10 ** i

            i += 1

        max_num += addon
        return max_num
