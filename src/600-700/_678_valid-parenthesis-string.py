"""
https://leetcode.com/problems/valid-parenthesis-string/

"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        left_p, right_p = 0, 0

        for c in s:
            if c == '(' or c == '*':
                left_p += 1
            else:
                left_p -= 1

            # On iteration we have more right parentheses than left, thus we have inbalanced string
            if left_p < 0:
                return False

        # Means we have perfect balance of left and right parantheses
        if left_p == 0:
            return True

        for c in reversed(s):
            if c == ')' or c == '*':
                right_p += 1
            else:
                right_p -= 1

            # On iteration we have more right parantheses than left, thus we have inbalanced string
            if right_p < 0:
                return False

        # the case when we checked all cases of, i.e. first loop took * as left parenthesis and second loop took all * as right parenthesis.
        # In all cases we have balanced string
        return True
