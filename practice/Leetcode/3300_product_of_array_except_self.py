# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                output[i] = 1
            else:
                output[i] = output[i-1] * nums[i-1]
        rightRunningProduct = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                rightRunningProduct = 1
            else:
                rightRunningProduct *= nums[i+1]
                output[i] *= rightRunningProduct
        return output
