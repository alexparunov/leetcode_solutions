"""
https://leetcode.com/problems/queue-reconstruction-by-height/

"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda el: (-el[0], el[1]))

        queue = []
        for h, k in people:
            queue.insert(k, (h, k))

        return queue
