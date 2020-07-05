"""
https://leetcode.com/problems/minimum-index-sum-of-two-lists/

"""
from typing import List
import collections


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        rests = collections.defaultdict(list)

        answer = list()
        min_sum = 2000

        for idx, rest2 in enumerate(list2):
            rests[rest2].append(idx)

        for idx, rest1 in enumerate(list1):
            if rest1 in rests:
                if idx + rests[rest1][0] < min_sum:
                    answer = [rest1]
                    min_sum = idx + rests[rest1][0]
                elif idx + rests[rest1][0] == min_sum:
                    answer.append(rest1)

        return answer

