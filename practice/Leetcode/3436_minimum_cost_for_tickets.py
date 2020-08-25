# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3436/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]
        days = set(days)
        for day in range(1, max(days) + 1):
            if day not in days:
                dp.append(dp[day-1])
            else:
                cost1 = dp[day-1] if day-1 > 0 else 0
                cost7 = dp[day-7] if day-7 > 0 else 0
                cost30 = dp[day-30] if day-30 > 0 else 0
                dp.append(min(cost1 + costs[0], cost7 + costs[1], cost30 + costs[2]))
        return dp[-1]
