# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3373/

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        y = int(math.sqrt(n))
        perfect_squares = [i**2 for i in range(y+1)]
        for i in range(1, n+1):
            for k in perfect_squares:
                if k > i:
                    break
                dp[i] = min(dp[i], dp[i-k]+1)
        return dp[-1]
