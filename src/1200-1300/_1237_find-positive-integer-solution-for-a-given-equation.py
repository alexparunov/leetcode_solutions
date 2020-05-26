"""
https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

"""

from typing import List


class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
           pass


class Solution:
    def findSolution(self, customfunction: CustomFunction, z: int) -> List[List[int]]:
        answer = list()

        for x in range(1, 1001):
            y_left, y_right = 1, 1000

            while y_left <= y_right:
                mid = (y_left + y_right) // 2

                val = customfunction.f(x, mid)

                if val < z:
                    y_left = mid + 1
                elif val > z:
                    y_right = mid - 1
                else:
                    answer.append([x, mid])
                    break

        return answer
