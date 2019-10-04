# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = -float('inf')
        propagate_sum = -float('inf')
        for num in nums:
            propagate_sum = max(propagate_sum + num, num)
            if propagate_sum > largest_sum:
                largest_sum = propagate_sum
        return largest_sum