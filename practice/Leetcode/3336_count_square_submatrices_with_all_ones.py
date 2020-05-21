# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3336/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        ans = 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    ans += dp[i][j]
        return ans
