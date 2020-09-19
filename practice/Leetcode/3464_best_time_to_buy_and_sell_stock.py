# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3464/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        ans = 0
        minPrice = prices[0]
        for price in prices[1:]:
            minPrice = min(minPrice, price)
            ans = max(ans, price - minPrice)
        return ans
