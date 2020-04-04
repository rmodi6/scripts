# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        empty_indexes = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                empty_indexes.append(i)
            elif len(empty_indexes) != 0:
                nums[empty_indexes.pop(0)] = nums[i]
                empty_indexes.append(i)
            else:
                pass
            i += 1
        for index in empty_indexes:
            nums[index] = 0
