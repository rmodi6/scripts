# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda k: k[0] - k[1])
        ans = 0
        for i, cost in enumerate(costs):
            ans += cost[int(i >= len(costs)//2)]
        return ans
