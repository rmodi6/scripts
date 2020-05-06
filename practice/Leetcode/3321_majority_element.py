# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums)/2
        hmap = {}
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
            if hmap[n] > limit:
                return n
