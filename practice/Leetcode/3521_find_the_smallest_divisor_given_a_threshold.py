# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3521/

import numpy as np

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums = np.array(nums)
        l, h = 1, np.max(nums)
        while l <= h:
            m = l + (h-l)//2
            if np.sum((nums + m - 1) // m) <= threshold:
                h = m - 1
            else:
                l = m + 1
        return l            
