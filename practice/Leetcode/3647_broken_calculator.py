# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3647/

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X == Y:
            return 0
        if X > Y:
            return X-Y
        if X == 2:
            return self.brokenCalc(X*2, Y) + 1
        if X <= Y//2:
            return self.brokenCalc(X, math.ceil(Y/2)) + 1 + Y%2
        return X - math.ceil(Y/2) + 1 + Y%2
