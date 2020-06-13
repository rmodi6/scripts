# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3359/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        nums = sorted(nums)
        hmap = {}
        for n in nums:
            temp = []
            for k in hmap:
                if n % k == 0 and len(hmap[k]) > len(temp):
                    temp = hmap[k]
            hmap[n] = temp + [n]
        return max(hmap.values(), key=lambda k: len(k))
