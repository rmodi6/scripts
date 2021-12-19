# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @cache
        def dp(i):
            if i >= len(nums):
                return float('inf')
            if i == len(nums)-1:
                return 0
            if nums[i] == 0:
                return float('inf')
            return 1 + min(dp(i+j) for j in range(1, nums[i]+1) if i+j < len(nums))
        
        return dp(0)
