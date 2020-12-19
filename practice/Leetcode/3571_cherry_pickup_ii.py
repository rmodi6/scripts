# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3571/

from collections import defaultdict

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = defaultdict(lambda : defaultdict(int))
        m, n = len(grid), len(grid[0])        
        for i in range(m):
            for j in range(i + 1):
                for k in range(n-1, n-i-2, -1):
                    for d1 in [-1,0,1]:
                        for d2 in [-1,0,1]:
                            if 0 <= j + d1 < n and 0 <= k + d2 < n:
                                dp[i][(j, k)] = max(dp[i][(j, k)], dp[i - 1][(j + d1, k + d2)])
                    dp[i][(j, k)] += grid[i][j] if j < n else 0
                    if j != k:
                        dp[i][(j, k)] += grid[i][k] if k < n else 0
        return max([v for _, v in dp[m -1].items()])
