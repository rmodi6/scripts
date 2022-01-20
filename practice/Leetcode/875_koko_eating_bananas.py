# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            m = lo + (hi-lo)//2
            t = sum([(pile//m + int(pile%m!=0)) for pile in piles])
            if t <= h:
                hi = m
            else:
                lo = m + 1
        return lo
