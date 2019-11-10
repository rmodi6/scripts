# https://leetcode.com/contest/weekly-contest-162/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        visited = set()
        def is_island(i, j):
            if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                return False
            grid[i][j] = 1
            x = (grid[i-1][j] == 1 or is_island(i-1, j)) 
            y = (grid[i][j-1] == 1 or is_island(i, j-1))
            z = (grid[i+1][j] == 1 or is_island(i+1, j)) 
            w = (grid[i][j+1] == 1 or is_island(i, j+1))
            return x and y and z and w
        
        ans = 0
        for l in range(1, r-1):
            for m in range(1, c-1):
                if grid[l][m] == 0 and is_island(l, m):
                    ans += 1
                    
        return ans
