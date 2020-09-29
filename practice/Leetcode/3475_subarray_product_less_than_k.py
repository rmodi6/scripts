# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3475/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        ans = 0
        i = j = 0
        prod = 1
        for j in range(len(nums)):
            prod *= nums[j]
            if prod < k:
                ans += j-i+1
            else:
                while i < j:
                    prod /= nums[i]
                    i += 1
                    if prod < k:
                        ans += j-i+1
                        break
        return ans
