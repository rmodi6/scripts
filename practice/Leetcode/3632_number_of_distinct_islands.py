# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3632/

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = 0 if num_rows == 0 else len(grid[0])
        
        def markIsland(grid, i, j, x, y, island):
            if -1 < i < num_rows and -1 < j < num_cols and grid[i][j] == 1:
                island.append((x, y))
                grid[i][j] = 0
                markIsland(grid, i, j+1, x, y+1, island)
                markIsland(grid, i, j-1, x, y-1, island)
                markIsland(grid, i+1, j, x+1, y, island)
                markIsland(grid, i-1, j, x-1, y, island)
            return island
        
        islands = set()
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    island = markIsland(grid, i, j, 0, 0, [])
                    s = ''
                    for (x, y) in island:
                        s += str(x)+str(y)
                    islands.add(s)
        return len(islands)
