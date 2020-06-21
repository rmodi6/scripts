# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3367/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r, c = len(dungeon), len(dungeon[0])
        dp = [[float('inf') for _ in range(c)] for _ in range(r)]
        ans = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = ans[0][0] + dungeon[0][0]
        for i in range(1, r):
            dp[i][0] = ans[i][0] + dungeon[i][0]           
        for j in range(1, c):
            dp[0][j] = ans[0][j] + dungeon[0][j]
        for i in reversed(range(r)):
            for j in reversed(range(c)):
                if i+1 >= r and j+1 >=c:
                    dp[i][j] = float('inf')
                elif i+1 >= r:
                    dp[i][j] = max(1, dp[i][j+1] - dungeon[i][j])
                elif j+1 >=c:
                    dp[i][j] = max(1, dp[i+1][j] - dungeon[i][j])
                else:
                    dp[i][j] = min(max(1, dp[i+1][j] - dungeon[i][j]), max(1, dp[i][j+1] - dungeon[i][j]))
                if dp[i][j] == float('inf'):
                    dp[i][j] = max(1, 1-dungeon[i][j])
        return dp[0][0]
