# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3383/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        r, c = len(grid), len(grid[0])
        perimeter = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    perimeter += int(i == 0 or grid[i-1][j] == 0) + int(i == r-1 or grid[i+1][j] == 0) + int(j == 0 or grid[i][j-1] == 0) + int(j == c-1 or grid[i][j+1] == 0)
        return perimeter
