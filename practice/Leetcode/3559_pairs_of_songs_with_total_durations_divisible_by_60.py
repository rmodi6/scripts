# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3559/

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = sorted(time)
        dp = {}
        ans = 0
        for t in time:
            i = 0
            while 60*i - t < 0:
                i += 1
            diff = 60*i - t
            while diff <= t:
                ans += dp.get(diff, 0)
                i += 1
                diff = 60*i - t
            dp[t] = dp.get(t, 0) + 1
        return ans
