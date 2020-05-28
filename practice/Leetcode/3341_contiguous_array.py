# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3341/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hmap = {0: -1}
        sum = 0
        ans = 0
        for i, n in enumerate(nums):
            sum += -1 if n == 0 else 1
            if sum not in hmap:
                hmap[sum] = i
            else:
                ans = max(ans, i - hmap[sum])
        return ans
