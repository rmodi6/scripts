# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3494/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solve(nums):
            dp = [(nums[0], 0)]
            for num in nums[1:]:
                curr = (num + dp[-1][1], max(dp[-1]))
                dp.append(curr)
            return max(dp[-1])
            
        if len(nums) == 0:
            return 0
        if len(nums) < 4:
            return max(nums)
        
        nums1, nums2 = nums[0:-1], nums[1:]
        return max(solve(nums1), solve(nums2))
