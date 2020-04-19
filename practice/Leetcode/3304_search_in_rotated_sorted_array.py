# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3304/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[low] > nums[mid]:
                    high = mid - 1
                elif nums[mid] > nums[high]:
                    if target > nums[high]:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[high] < nums[mid]:
                    low = mid + 1
                elif nums[mid] < nums[low]:
                    if target < nums[low]:
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    low = mid + 1
        return -1
