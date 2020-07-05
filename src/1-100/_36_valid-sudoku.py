"""
https://leetcode.com/problems/valid-sudoku/

"""
from typing import List
import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        sub_box = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    sub_row = i // 3
                    sub_col = j // 3

                    if board[i][j] not in row[i] and board[i][j] not in col[j] and board[i][j] not in sub_box[(sub_row, sub_col)]:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        sub_box[(sub_row, sub_col)].add(board[i][j])
                    else:
                        return False
        return True
