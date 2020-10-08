# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3488/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            m = l + (h-l)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                h = m-1
        return -1
