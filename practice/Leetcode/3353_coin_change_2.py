# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3353/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in sorted(coins):
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]
