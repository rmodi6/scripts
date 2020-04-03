# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for n in nums[1:]:
            ans ^= n
        return ans
