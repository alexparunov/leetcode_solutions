"""
https://leetcode.com/problems/first-bad-version/

"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low < high:
            m = (low + high) // 2
            if isBadVersion(m):
                high = m
            else:
                low = m + 1

        return low
