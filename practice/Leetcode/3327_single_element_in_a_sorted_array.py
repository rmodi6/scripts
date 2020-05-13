# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1)
    
    def binarySearch(self, nums, l, h):
        if l == h:
            return nums[l]
        mid = int((l+h)/2)
        if nums[mid] == nums[mid-1]:
            if mid % 2 == 0:
                return self.binarySearch(nums, l, mid-1)
            else:
                return self.binarySearch(nums, mid+1, h)
        if nums[mid] == nums[mid+1]:
            if mid % 2 == 0:
                return self.binarySearch(nums, mid+1, h)
            else:
                return self.binarySearch(nums, l, mid-1)
        return nums[mid]
