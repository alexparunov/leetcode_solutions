"""
https://leetcode.com/problems/add-to-array-form-of-integer/

"""
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        total_sum = 0
        n = len(A)

        for i in range(n):
            total_sum += A[i] * (10 ** (n - i - 1))

        final_num = total_sum + K

        if final_num == 0:
            return [0]

        answer = list()
        while final_num > 0:
            answer.insert(0, final_num % 10)
            final_num //= 10

        return answer
