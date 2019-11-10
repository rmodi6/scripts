# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(), set()
        flag = 0
        row1 = False
        col1 = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        row1 = True
                    if j == 0:
                        col1 = True
                    matrix[i][0] = flag
                    matrix[0][j] = flag
                    
        for i in range(1, len(matrix)):
            if matrix[i][0] == flag:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
                    
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == flag:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
                    
        if row1 == True:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
                    
        if col1 == True:
            for i in range(len(matrix)):
                matrix[i][0] = 0
