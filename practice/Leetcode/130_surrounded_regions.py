# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                board[x][y] = 'Z'
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)
        
        for i in [0, m-1]:
            for j in range(n):
                dfs(i, j)
        
        for i in range(m):
            for j in [0, n-1]:
                dfs(i, j)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Z':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
