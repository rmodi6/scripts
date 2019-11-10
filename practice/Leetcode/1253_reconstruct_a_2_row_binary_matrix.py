# https://leetcode.com/contest/weekly-contest-162/problems/reconstruct-a-2-row-binary-matrix/

import numpy as np

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        ans = np.zeros((2, len(colsum)), dtype='int32')
        for i, n in enumerate(colsum):
            if n == 2:
                if upper > 0 and lower > 0:
                    ans[0][i], ans[1][i] = 1, 1
                    upper -= 1
                    lower -= 1
                else:
                    return []
                
        for i, n in enumerate(colsum):   
            if n == 1:
                if upper > 0:
                    ans[0][i] = 1
                    upper -= 1
                elif lower > 0:
                    ans[1][i] = 1
                    lower -= 1
                else:
                    return []
        
        return ans.tolist()
