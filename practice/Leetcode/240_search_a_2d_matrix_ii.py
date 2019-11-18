# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        def search(matrix, i, j, target):
            if i < 0 or j >= len(matrix[0]):
                return False
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                return search(matrix, i-1, j, target)
            return search(matrix, i, j+1, target)
            
        return search(matrix, len(matrix) - 1, 0, target)
