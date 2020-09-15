# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3459/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [(nums[0], 0)]
        for num in nums[1:]:
            curr = (num + dp[-1][1], max(dp[-1]))
            dp.append(curr)
        return max(dp[-1])
