# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3473/

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        prev_until = -1
        for time in timeSeries:
            until = time + duration - 1
            ans += until - max(prev_until, time-1)
            prev_until = until
        return ans
