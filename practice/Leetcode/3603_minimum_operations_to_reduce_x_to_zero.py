# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3603/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        k = sum(nums) - x
        if k < 0:
            return -1
        p = cumsum = 0
        ans = -1
        for q in range(0, len(nums)):
            cumsum += nums[q]
            while p <= q and cumsum > k:
                cumsum -= nums[p]
                p += 1
            if cumsum == k:
                ans = max(ans, q-p+1)
        return -1 if ans == -1 else len(nums)-ans
