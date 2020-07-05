"""
https://leetcode.com/problems/prison-cells-after-n-days/

"""
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        repeats_dicts = dict()

        for n in range(N):
            t_cells = tuple(cells)
            if t_cells in repeats_dicts:
                loop_len = n - repeats_dicts[t_cells]
                return self.prisonAfterNDays(cells, (N - n) % loop_len)
            else:
                repeats_dicts[t_cells] = n
                cells_day_n = [0] * 8
                for i in range(1, len(cells) - 1):
                    if cells[i - 1] == cells[i + 1]:
                        cells_day_n[i] = 1

                cells = cells_day_n
        return cells
