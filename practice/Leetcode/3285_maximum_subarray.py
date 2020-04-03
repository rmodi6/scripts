# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cumulative = 0
        for n in nums:
            cumulative += n
            if n > cumulative:
                cumulative = n
            if cumulative > max_sum:
                max_sum = cumulative
        return max_sum
