"""
https://leetcode.com/problems/integer-to-english-words/

"""

import re


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        digits = {
            0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
            19: 'Nineteen'
        }

        tens = {
            20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
            60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
        }

        levels = {
            0: '',
            1: 'Thousand',
            2: 'Million',
            3: 'Billion'
        }

        def read_chunk_3(num):
            if num < 20: return digits[num]
            if num < 100: return tens[10 * (num // 10)] + ' ' + read_chunk_3(num % 10)
            if num < 1000: return digits[num // 100] + ' Hundred ' + read_chunk_3(num % 100)

        level = 0

        chunks = "{:,}".format(num).split(",")
        ans = ''
        for i, chunk_of_3 in enumerate(chunks[::-1]):
            number = int(chunk_of_3)
            comma_club = levels[i] + ' ' if number != 0 else ''
            ans = read_chunk_3(int(chunk_of_3)) + ' ' + comma_club + ans

        ans = re.sub(r'\s+', ' ', ans.strip())

        return ans
