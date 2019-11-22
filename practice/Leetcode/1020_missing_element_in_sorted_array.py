# https://leetcode.com/problems/missing-element-in-sorted-array/

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        low, high = 0, len(nums) - 1
        mid = (low + high) // 2
        k_ = k
        while high - low > 1:
            if nums[mid] - (mid + nums[0]) >= k:
                high = mid
            else:
                k_ = k - (nums[mid] - (mid + nums[0]))
                low = mid
            mid = (low + high) // 2
        if nums[mid] + k_ < nums[high]:
            return nums[mid] + k_
        return nums[high] + k - (nums[high] - (high + nums[0]))
