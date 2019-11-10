# https://leetcode.com/contest/weekly-contest-162/problems/cells-with-odd-values-in-a-matrix/

import numpy as np

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = np.zeros((n, m), dtype='int32')
        for i in indices:
            row_vector = np.zeros((n, 1), dtype='int32')
            row_vector[i[0]][0] = 1
            col_vector = np.zeros((1, m), dtype='int32')
            col_vector[0][i[1]] = 1
            mat = np.add(mat, row_vector)
            mat = np.add(mat, col_vector)
        return len(np.where(mat % 2 == 1)[0])
