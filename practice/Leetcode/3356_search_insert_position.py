# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3356/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        l, h = 0, len(nums)-1
        while l <= h:
            m = (l+h) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m-1
            else:
                l = m+1
        return l
