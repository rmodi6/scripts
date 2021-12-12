# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, visited = 0, set()

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0 or (x, y) in visited:
                return 0
            visited.add((x, y))
            area = 1 + dfs(x, y-1) + dfs(x-1, y) + dfs(x, y+1) + dfs(x+1, y)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = dfs(i, j)
                    ans = max(ans, area)
        return ans
