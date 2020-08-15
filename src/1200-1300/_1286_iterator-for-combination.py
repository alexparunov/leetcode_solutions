"""
https://leetcode.com/problems/iterator-for-combination/

"""


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        N = len(characters)
        all_bits = [bin(n)[2:] for n in range(2 ** N) if sum(1 for c in bin(n)[2:] if c == '1') == combinationLength]
        all_bits = ['0' * (N - len(b)) + b for b in all_bits]

        self.all_strings = [''.join([c for c, bi in zip(characters, bits) if bi == '1']) for bits in all_bits]

        self.all_strings.sort()
        self.pos = 0

    def next(self) -> str:
        if self.hasNext():
            s = self.all_strings[self.pos]
            self.pos += 1
            return s

        return ''

    def hasNext(self) -> bool:
        return self.pos < len(self.all_strings)
