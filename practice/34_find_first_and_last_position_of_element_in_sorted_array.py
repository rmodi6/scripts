# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if index == -1:
            return [-1, -1]
        else:
            start, end = index, index
            while start > low and nums[start-1] == target:
                start -= 1
            while end < high and nums[end+1] == target:
                end += 1
        return [start, end]
        