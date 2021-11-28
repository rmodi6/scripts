# https://leetcode.com/problems/product-of-array-except-self/

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

# OR
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr, rtl = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            ltr[i] = ltr[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            rtl[i] = rtl[i+1] * nums[i+1]
        return [ltr[i] * rtl[i] for i in range(len(nums))]
    
