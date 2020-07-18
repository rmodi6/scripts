# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/543/week-5-june-29th-june-30th/3375/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        dp[1][1] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i][j]
        return dp[-1][-1]
