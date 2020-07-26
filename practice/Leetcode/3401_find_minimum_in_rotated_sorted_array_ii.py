# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3401/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            elif nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1

        return nums[low]
