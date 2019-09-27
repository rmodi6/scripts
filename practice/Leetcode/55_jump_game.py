# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachableIndex = 0
        destIndex = len(nums) - 1
        i = 0
        while i <= reachableIndex and reachableIndex < destIndex:
            reachableIndex = max(reachableIndex, i + nums[i])
            i += 1
        if reachableIndex >= destIndex:
            return True
        return False
