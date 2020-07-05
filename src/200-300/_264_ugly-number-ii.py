"""
https://leetcode.com/problems/ugly-number-ii/

"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        k = 3
        factors = (2, 3, 5)
        powers = [0] * k

        for i in range(n - 1):
            candidate_nums = [factors[i] * nums[powers[i]] for i in range(k)]
            next_num = min(candidate_nums)
            nums.append(next_num)
            powers = [powers[i] + (candidate_nums[i] == next_num) for i in range(k)]

        return nums[-1]
