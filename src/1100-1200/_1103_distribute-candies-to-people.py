"""
https://leetcode.com/problems/distribute-candies-to-people/

"""
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        answer = [0] * num_people

        i = 0
        dist = 0
        while candies > 0:
            answer[i % num_people] += min(dist + 1, candies)
            dist += 1
            candies -= dist
            i += 1

        return answer
