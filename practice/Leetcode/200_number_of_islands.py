# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = 0 if num_rows == 0 else len(grid[0])
        
        def convert_to_zero(grid, i, j):
            if i > -1 and i < num_rows and j > -1 and j < num_cols and grid[i][j] == '1':
                grid[i][j] = '0'
                convert_to_zero(grid, i, j+1)
                convert_to_zero(grid, i, j-1)
                convert_to_zero(grid, i+1, j)
                convert_to_zero(grid, i-1, j)
        
        
        count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                v = grid[i][j]
                if v == '1':
                    convert_to_zero(grid, i, j+1)
                    convert_to_zero(grid, i, j-1)
                    convert_to_zero(grid, i+1, j)
                    convert_to_zero(grid, i-1, j)
                    count += 1
        return count
