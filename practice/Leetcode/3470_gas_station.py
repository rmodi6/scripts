# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3470/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        surplus = 0
        ans = -1
        for i, (g, c) in enumerate(zip(gas, cost)):
            if ans == -1:
                surplus = g-c
                if surplus >= 0:
                    ans = i
            else:
                surplus += (g-c)
                if surplus < 0:
                    ans = -1
        return ans
