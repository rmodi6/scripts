# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628/

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        prev, ans = None, 0
        for n in sorted(counts.keys()):
            if prev is not None and n - prev == 1:
                ans = max(ans, counts[prev] + counts[n])
            prev = n
        return ans
