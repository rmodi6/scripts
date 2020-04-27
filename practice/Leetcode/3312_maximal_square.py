# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3312/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        r = len(matrix)
        c = len(matrix[0]) if r > 0 else 0
        dp = [[0 for j in range(c+1)] for i in range(r+1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    ans = max(ans, dp[i][j])
        return ans ** 2
