# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3308/

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        num_shifts = 0
        while m < n:
            m = m >> 1
            n = n >> 1
            num_shifts += 1
        return m << num_shifts
