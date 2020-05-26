"""
https://leetcode.com/problems/unique-morse-code-words/

"""

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
                 '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
                 '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

        eng_morse_map = {chr(97 + i): morse[i] for i in range(26)}

        morse_words = set()

        for word in words:
            morse_word = ''
            for letter in word:
                morse_word += eng_morse_map[letter]

            morse_words.add(morse_word)

        return len(morse_words)
