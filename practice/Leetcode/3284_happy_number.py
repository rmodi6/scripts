# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/

class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        d[n] = True
        while True:
            new_n = 0
            for digit in str(n):
                new_n += int(digit)**2
            if new_n == 1:
                return True
            if new_n in d:
                return False
            n = new_n
            d[n] = True
