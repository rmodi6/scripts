# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3371/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p, q = nums[0], nums[0]
        while True:
            p, q = nums[p], nums[nums[q]]
            if p == q:
                break
        p = nums[0]
        while p != q:
            p, q = nums[p], nums[q]
        return p
