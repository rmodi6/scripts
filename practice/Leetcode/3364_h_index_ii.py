# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3364/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, h = 0, n-1
        ans = 0
        while l <= h:
            m = (l+h) // 2
            r = n - m
            if citations[m] >= r:
                ans = r
                h = m - 1
            else:
                l = m + 1
        return ans
